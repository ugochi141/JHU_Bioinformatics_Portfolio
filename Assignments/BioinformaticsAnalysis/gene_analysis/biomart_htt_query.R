# Load required library
library(biomaRt)

# Connect to Ensembl
ensembl <- useMart("ensembl", dataset = "hsapiens_gene_ensembl")

# Query HTT gene
htt_info <- getBM(
  attributes = c(
    'hgnc_symbol',
    'ensembl_gene_id',
    'chromosome_name',
    'start_position',
    'end_position',
    'strand',
    'description',
    'gene_biotype'
  ),
  filters = 'hgnc_symbol',
  values = 'HTT',
  mart = ensembl
)

# Display results
print(htt_info)
