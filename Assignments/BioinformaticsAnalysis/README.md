# Bioinformatics Analysis Projects

## Course: AS.410.635.81 - Bioinformatics: Tools for Genome Analysis
**Instructors**: Sajung Yun and Sijung Yun  
**Institution**: Johns Hopkins University

## Overview
This collection contains advanced bioinformatics analysis projects demonstrating practical application of genomic tools, NGS data processing, and computational biology techniques.

## Project Categories

### 📊 NGS Analysis (`NGS_analysis/`)
Next-Generation Sequencing data processing and variant analysis
- **Variant Calling**: VCF file processing and analysis
- **Annotation**: Variant Effect Predictor (VEP) analysis
- **Quality Control**: NGS data validation and filtering
- **Reporting**: Automated analysis report generation

### 🧬 Gene Analysis (`gene_analysis/`)
Gene-focused research and analysis projects
- **Huntington's Disease**: HTT gene analysis and research
- **BioMart Integration**: Automated gene data retrieval
- **Comparative Analysis**: Gene expression and function studies
- **Disease Genetics**: Neurological disorder gene research

### 🔬 Genomics Tools (`genomics_tools/`)
Computational tools and utilities for genomic analysis
- **Sequence Analysis**: DNA sequence processing utilities
- **Gene Lookup**: Automated gene information retrieval
- **Data Processing**: BED file manipulation and analysis
- **Automation Scripts**: Workflow enhancement tools

## Key Technologies and Methods

### Bioinformatics Tools
- **Variant Effect Predictor (VEP)**: Functional annotation of genetic variants
- **BioMart**: Biological database federation system
- **BEDTools**: Genome arithmetic and interval operations
- **UCSC Genome Tools**: Genomic data visualization and analysis

### Programming Languages
- **Python**: Primary analysis and tool development
- **R**: Statistical analysis and BioMart queries
- **Shell Scripting**: Workflow automation
- **SQL**: Database queries and data management

### Data Formats
- **VCF**: Variant Call Format for genetic variations
- **BED**: Browser Extensible Data format
- **FASTA**: Sequence data format
- **GFF/GTF**: Gene annotation formats

## Learning Outcomes
- Practical NGS data analysis workflows
- Variant calling and annotation pipelines
- Gene expression and function analysis
- Database integration and automation
- Reproducible research methodologies
- Computational biology best practices

## Skills Demonstrated
- **Data Analysis**: Large-scale genomic data processing
- **Tool Integration**: Combining multiple bioinformatics tools
- **Automation**: Scripting and pipeline development
- **Quality Control**: Data validation and error handling
- **Visualization**: Results presentation and interpretation
- **Documentation**: Technical writing and reporting

## Project Structure
```
BioinformaticsAnalysis/
├── NGS_analysis/
│   ├── NGS_Report_huD3FFCB.md
│   ├── huD3FFCB_variant.vcf
│   ├── huD3FFCB_variant_clean.vcf
│   ├── huD3FFCB_vep_output.txt
│   ├── huD3FFCB_vep_output.txt_summary.html
│   └── parse_vep.py
├── gene_analysis/
│   ├── biomart_htt_query.R
│   └── huntington_analysis/
└── genomics_tools/
    ├── gene_lookup.py
    ├── DNASequence.py
    └── *.bed files
```

Each subdirectory contains specific project documentation and implementation details.