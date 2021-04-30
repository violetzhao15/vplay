#
# how to run:
# $ Rscript analyse_pt5.R
#

library(dplyr)
library(Seurat)
library(ggplot2)
library(SCORPIUS)

# setwd("C:/Users/jorda/Desktop")
data.dir <- "~/00_code/human_sgRNA_seq_data_from_NASH/pt5/"
ecs <- Read10X(data.dir)

TC <- CreateSeuratObject(counts = ecs, project = "TC_ECs", min.cells = 3, min.features = 200)
TC[["percent.mt"]] <- PercentageFeatureSet(TC, pattern = "^mt-")
TC <- subset(TC, subset = nFeature_RNA > 200 & nFeature_RNA < 4000 & percent.mt < 5)
TC <- NormalizeData(TC, normalization.method = "LogNormalize", scale.factor = 10000)
TC <- FindVariableFeatures(TC, selection.method = "vst", nfeatures = 2000)
all.genes <- rownames(TC)
TC <- ScaleData(TC, features = all.genes)

TC <- RunPCA(TC, features = VariableFeatures(object = TC))
