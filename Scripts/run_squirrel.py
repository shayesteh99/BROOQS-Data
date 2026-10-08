import sys
import os
import argparse
import tarfile
import tempfile
import time
import numpy as np
from pathlib import Path
import physquirrel as psq

FORMAT_EXTENSIONS = {
    "phy": ["phy"],
    "fasta": ["fasta", "fa"],
}


def is_tarball(path):
    return path.is_file() and (path.name.endswith(".tar.gz") or path.name.endswith(".tgz"))


def extract_tarball(archive_path, dest_dir):
    with tarfile.open(archive_path, "r:gz") as tar:
        for member in tar.getmembers():
            member_path = (dest_dir / member.name).resolve()

            if dest_dir.resolve() not in member_path.parents and member_path != dest_dir.resolve():
                raise RuntimeError(f"Unsafe path in archive: {member.name}")

        try:
            tar.extractall(dest_dir, filter="data")
        except TypeError:
            tar.extractall(dest_dir)

    return dest_dir


def parse_phy(path):
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]

    ntaxa, length = map(int, lines[0].split())

    current = {}

    for line in lines[1:]:
        parts = line.split()

        if len(parts) < 2:
            continue

        taxon = parts[0]
        seq = "".join(parts[1:])

        if len(seq) != length:
            raise ValueError(
                f"{path.name}: {taxon} has length {len(seq)} instead of {length}"
            )

        current[taxon] = seq

    if len(current) != ntaxa:
        raise ValueError(f"{path.name}: expected {ntaxa} taxa.")

    return current


def parse_fasta(path):
    current = {}
    taxon = None
    seq_parts = []

    with open(path) as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            if line.startswith(">"):
                if taxon is not None:
                    current[taxon] = "".join(seq_parts)

                taxon = line[1:].split()[0]
                seq_parts = []
            else:
                seq_parts.append(line)

        if taxon is not None:
            current[taxon] = "".join(seq_parts)

    lengths = {len(seq) for seq in current.values()}

    if len(lengths) > 1:
        raise ValueError(f"{path.name}: sequences have inconsistent lengths.")

    return current


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-i', '--input', required=True,
                         help="Input sequence dir, or a .tar.gz/.tgz archive containing the MSA files")
    # parser.add_argument('-g', '--gene_trees', required=True, help="Gene tree file")
    # parser.add_argument('-a', '--annot', required=False, help="Annotation file")
    # parser.add_argument('-n', '--num_genes', required=False, default=1000, help="Number of gene trees")
    parser.add_argument('-t', '--format', choices=['phy', 'fasta'], default='phy',
                         help="Format of the individual per-gene MSA files (fasta matches .fasta and .fa)")
    parser.add_argument('-p', '--prefix', required=False, default=None,
                         help="Only read MSA files whose name starts with this prefix (default: read all files in the given format)")
    parser.add_argument('-f', '--fasta', required=True, help="Fasta file")
    parser.add_argument('-o', '--output', required=True, help="Output file")
    args = parser.parse_args()

    input_path = Path(args.input)

    # Output FASTA
    output_file = args.fasta

    parse_msa = parse_phy if args.format == 'phy' else parse_fasta

    with tempfile.TemporaryDirectory() as tmp_dir:

        if is_tarball(input_path):
            input_dir = extract_tarball(input_path, Path(tmp_dir))
            recursive = True
        else:
            input_dir = input_path
            recursive = False

        # Read files in a consistent order
        msa_files = set()

        for ext in FORMAT_EXTENSIONS[args.format]:
            pattern = f"{args.prefix}*.{ext}" if args.prefix else f"*.{ext}"
            msa_files.update(input_dir.rglob(pattern) if recursive else input_dir.glob(pattern))

        msa_files = sorted(msa_files)

        if len(msa_files) == 0:
            if args.prefix:
                raise RuntimeError(f"No {'/'.join(FORMAT_EXTENSIONS[args.format])} files found matching prefix '{args.prefix}'.")
            else:
                raise RuntimeError(f"No {'/'.join(FORMAT_EXTENSIONS[args.format])} files found.")

        concatenated = {}

        for msa_file in msa_files:

            current = parse_msa(msa_file)
            if len(set(current)) == 0:
                continue 

            # First gene
            if not concatenated:
                for taxon in current:
                    concatenated[taxon] = current[taxon]

            # Remaining genes
            else:
                if set(current) != set(concatenated):
                    raise ValueError(f"Taxa differ in {msa_file.name}")

                for taxon in concatenated:
                    concatenated[taxon] += current[taxon]

    # Write FASTA
    with open(output_file, "w") as out:
        for taxon, seq in concatenated.items():
            out.write(f">{taxon}\n")
            out.write(seq + "\n")

    print(f"Wrote {output_file}")
    print(f"{len(concatenated)} taxa")
    print(f"Alignment length = {len(next(iter(concatenated.values())))} bp")

    msa = psq.MSA.load(output_file)
    network = psq.squirrel_from_msa(msa)
    print(network.to_string())
    network.save(args.output, overwrite=True)



if __name__ == "__main__":
	main()  