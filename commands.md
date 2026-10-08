## Inferring a tree of blob

### TOB-QMC

```
tree-qmc --blob -i [GENETREE_FILE] -o [OUTPUT_FILE] --override 2> [LOG_FILE]
```

## Resolving a tree of blobs into a level-1 network

### BROOQS
```
brooqs -i [GENETREE_FILE] -t [TOB_FILE] -o [OUTPUT_FILE] > [LOG_FILE]
```

### NANUQ+
We wrote the following R script for NANUQ+ (see [run_nanuq.r](Scripts/run_nanuq.r)). We then run the following command to run this script:
```
Rscript run_nanuq.R [GENETREE_FILE] [TOB_FILE] [OUTPUT_FILE] 2> [LOG_FILE]
```

Use an empty string instead of `[TOB_FILE]` to use the tree of blobs inferred by TINNIK as input.


### NetCS
We used the following command to run NetCS:
```
tree-qmc --network -i [GENETREE_FILE] --at [TOB_FILE] -o [OUTPUT_FILE] > [LOG_FILE]
```

## Estimating species tree

### ASTRAL-IV

```
astral4 -i [GENETREE_FILE] -o [OUTPUT_FILE] > [LOG_FILE]
```

## Inferring a network given a guide tree:

### CAMUS 
```
camus -n 1 -o [OUTPUT_DIR] [ASTRAL_TREE_FILE] [GENE_TREE_FILE] &> [LOG_FILE]
```

## Inferring a network using MSA:

### SQUIRREL

We wrote a python script to run SQUIRREL (see ). We then run the script using the following command:

```
python run_squirrel.py -i [MSA_DIR] -f [MSA_FILE] -o [OUTPUT_FILE] &> [LOG_FILE]
```

The input is a directory with the MSA for each gene tree (`[MSA_DIR]`). The script will create a single MSA file by concatenating all gene MSAs, and write it to `[MSA_FILE]`.
It will then run SQUIRREL using the concatenated MSA as input and infer a network.




