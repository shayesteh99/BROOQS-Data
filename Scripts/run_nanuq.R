#!/usr/bin/env Rscript

# install.packages("MSCquartets")

args <- commandArgs(trailingOnly = TRUE)

if (length(args) < 3) {
  stop(
    paste(
      "Usage:",
      "Rscript run_nanuq.R <gene_tree_file> <tob_file> <output_enewick>"
    )
  )
}

gene_tree_file <- args[1]
tob_file       <- args[2]
output_file    <- args[3]

# print(tob_file)
# dput(tob_file)

# gene_tree_file <- "00/g_true.nwk"
# tob_file <- "network_1552/network_1552_ils_2.0.true_tob"

library(MSCquartets)
library(ape)

# Read gene tree(s)
tgt <- read.tree(gene_tree_file)

# Compute quartet table
testTable <- quartetTable(tgt)

# Run TINNIK
output <- TINNIK(testTable, alpha=1e-7, beta=0.99)

output$ToB
# Extract pTable
pT <- output$pTable

if (tob_file == "") {
  # print("is empty")
  tob = output$ToB
} else {
  # Read Tree of Blobs
  ToB <- read.tree(tob_file)
  
  # Ensure unrooted
  tob <- unroot(ToB)
  if (is.rooted(tob)) {
    tob <- unroot(tob)
  }
}


# Resolve network
resN <- resolveLevel1(
  ToB = tob,
  pTable = pT,
  alpha = 1e-7,
  beta = 0.99,
  distance = "NANUQ"
)
?resolveLevel1

if (length(resN) == 0) {
  write.tree(tob, output_file)
} else {
  # Write all inferred networks to output file
  if (length(resN) == 1) {
    write.tree(resN[[1]][[1]], output_file)
  } else {
    nets <- sapply(resN[[2]]$cycleRes, function(x) x$cycleNet)
    writeLines(nets, output_file)
    # if (is.null(resN[[1]][[1]])) {
    #   nets <- sapply(resN[[2]]$cycleRes, function(x) x$cycleNet)
    #   writeLines(nets, "temp")
    # } else {
    #   writeLines(resN[[1]][[1]], output_file)
    # }
  }
}


cat("Saved network(s) to:", output_file, "\n")