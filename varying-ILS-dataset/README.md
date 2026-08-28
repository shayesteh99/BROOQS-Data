# Varying-ILS Dataset

This dataset is organized as:

```text
varying-ILS-dataset/TAXA_[n]/[net]/
```

where:

* `[n]` is the number of taxa and is one of `{50, 100, 200}`.
* `[net]` is the network ID.
* `[ils]` is the ILS level and is one of `{0.25, 0.5, 1.0, 2.0}`.
* `[gt]` indicates the source of gene trees and is either `true` or `est`.

## Input and True Files

| File                                     | Description                          |
| ---------------------------------------- | ------------------------------------ |
| `${net}_ils_${ils}.newick`               | True simulated phylogenetic network. |
| `${net}_ils_${ils}.true_tob`             | True tree of blobs (ToB).            |
| `${net}_ils_${ils}.true_gene_trees`      | True gene trees.                     |
| `${net}_ils_${ils}.estimated_gene_trees` | Estimated gene trees.                |

## Estimated Species Trees and Trees of Blobs

| File                              | Description                            |
| --------------------------------- | -------------------------------------- |
| `${net}_ils_${ils}.${gt}_TOB_QMC` | Tree of blobs estimated using TOB-QMC. |
| `${net}_ils_${ils}.${gt}_astral4` | Species tree estimated using ASTRAL.   |

## Estimated Phylogenetic Networks

| File                                              | Description                                 |
| ------------------------------------------------- | ------------------------------------------- |
| `${net}_ils_${ils}.${gt}.brooqs.enewick`          | Network inferred by BROOQS on true tree of blobs.                 |
| `${net}_ils_${ils}.${gt}.brooqs_complete.enewick` | Network inferred by BROOQS on TOB-QMC tree of blobs.        |
| `${net}_ils_${ils}.${gt}.nanuq.enewick`           | Network inferred by NANUQ+ on true tree of blobs.                 |
| `${net}_ils_${ils}.${gt}.nanuq_complete.enewick`  | Network inferred by NANUQ+ on TINNIK tree of blobs.        |
| `${net}_ils_${ils}.${gt}.netcs.enewick`           | Network inferred by NetCS on true tree of blobs..                  |
| `${net}_ils_${ils}.${gt}.netcs_complete.enewick`  | Network inferred by NetCS on TOB-QMC tree of blobs.         |
| `${net}_ils_${ils}.${gt}.camus.enewick`           | Network inferred by CAMUS on ASTRAL tree.                  |
| `${net}_ils_${ils}.msa.squirrel.enewick`          | Network inferred by SQUIRREL from the MSAs. |
