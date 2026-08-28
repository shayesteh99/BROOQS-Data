# Fixed-ILS Dataset

This dataset is organized as:

```text
fixed-ILS-dataset/n[n]/[rep]/
```

where:

* `[n]` is the number of taxa and is one of `{15, 25, 50, 100, 150, 200}`.
* `[rep]` is the replicate number, ranging from `00` to `49`.
* `[gt]` indicates the source of gene trees used by a method (e.g., true or estimated gene trees).

## Input and True Files

| File             | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| `true_net.nwk`   | True simulated phylogenetic network.                          |
| `true_tob.nwk`   | True tree of blobs (ToB).                                     |
| `g_true.nwk`     | True gene trees.                                              |

## Estimated Gene Trees

| File             | Description                          |
| ---------------- | ------------------------------------ |
| `iqtree_500.nwk` | Gene trees estimated using IQ-TREE.  |
| `g_500.nwk`      | Gene trees estimated using FastTree. |

## Estimated Species Trees and Trees of Blobs

| File               | Description                            |
| ------------------ | -------------------------------------- |
| `TOB_QMC_[gt].tre` | Tree of blobs estimated using TOB-QMC. |
| `astral4_[gt].tre` | Species tree estimated using ASTRAL.   |

## Estimated Phylogenetic Networks

| File                           | Description                                                          |
| ------------------------------ | -------------------------------------------------------------------- |
| `[gt]_network.enewick`         | Network estimated by BROOQS using true tree of blobs.                                         |
| `TOB_QMC_[gt]_network.enewick` | Network estimated by BROOQS using a TOB-QMC estimated tree of blobs. |
| `nanuq_[gt].nwk`               | Network estimated by NANUQ+ using true tree of blobs.                                         |
| `nanuq_complete_[gt].nwk`      | Network estimated by NANUQ+ using TINNIK estimated tree of blobs.                                |
| `netcs_[gt].nwk`               | Network estimated by NetCS using true tree of blobs.                                          |
| `netcs_complete_[gt].nwk`      | Network estimated by NetCS using a TOB-QMC estimated tree of blobs.                                 |
| `seqs_500_squirrel.enewick`    | Network estimated by SQUIRREL from the MSAs.                         |
| `[gt]_camus.enewick`           | Network estimated by CAMUS from ASTRAL tree and gene trees.                                          |
