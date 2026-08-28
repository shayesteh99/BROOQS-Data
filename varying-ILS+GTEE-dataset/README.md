# Varying-ILS+GTEE Dataset

This dataset is organized as:

```text
varying-ILS+GTEE-dataset/[n]/[ils]/[nbp]/[rep]/
```

where:

* `[n]` is the number of taxa and is one of `{25, 50, 100, 200}`.
* `[ils]` is the ILS level and is either `low` or `high`.
* `[nbp]` is the number of base pairs and is one of `{100, 1000}`.
* `[rep]` is the replicate number and ranges from `1` to `10`.
* `[gt]` indicates the source of gene trees and is either `true` or `est`.

## Input and True Files

| File           | Description                          |
| -------------- | ------------------------------------ |
| `true.net`     | True simulated phylogenetic network. |
| `true_tob.nwk` | True tree of blobs (ToB).            |
| `truegts.tre`  | True gene trees.                     |
| `estgts.tre`   | Estimated gene trees.                |

## Estimated Species Trees and Trees of Blobs

| File                   | Description                            |
| ---------------------- | -------------------------------------- |
| `TOB_QMC_${gt}gts.tre` | Tree of blobs estimated using TOB-QMC. |
| `astral4_${gt}gts.tre` | Species tree estimated using ASTRAL.   |

## Estimated Phylogenetic Networks

| File                               | Description                                                 |
| ---------------------------------- | ----------------------------------------------------------- |
| `${gt}gts_network.enewick`         | Network inferred by BROOQS using true tree of blobs.                                 |
| `TOB_QMC_${gt}gts_network.enewick` | Network inferred by BROOQS using TOB-QMC tree of blobs. |
| `${gt}gts_nanuq.enewick`           | Network inferred by NANUQ+ using true tree of blobs.                                 |
| `${gt}gts_nanuq_complete.enewick`  | Network inferred by NANUQ+ using TINNIK tree of blobs.                        |
| `netcs_${gt}gts.enewick`           | Network inferred by NetCS using true tree of blobs.                                  |
| `netcs_complete_${gt}gts.enewick`  | Network inferred by NetCS using TOB-QMC tree of blobs.                         |
| `${gt}gts_camus.enewick`           | Network inferred by CAMUS using ASTRAL tree.                                  |
| `msa_squirrel.enewick`             | Network inferred by SQUIRREL from the MSA.                  |
