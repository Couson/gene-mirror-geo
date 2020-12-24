
## Genes Reveal Geographical Relationships Worldwide: a replication of the main results in “Genes Mirror Geography within Europe”, using the data from 1000 Genomes Project
- Yifei Ning
- y3ning@ucsd.edu
- UC San Diego

### Introduction

In the article called Genes Mirror Geography within Europe, interested in revealing how genetic and geographic distances correspond to one another, John et al conduct the study on a sample of 3192 European individuals and collected millions of variable DNA sites in the human genome. They found a close association exists between the geographical map of Europe and a two-dimensional representation of genetic variations in Europeans. Most importantly, their research suggests that by using genotyping technologies, one could discover how population structures are associated with one’s genetic information. In this project, I will replicate the results from Genes Mirror Geography within Europe while using the data from “The 1000 Genomes Project”. Instead of studying European individuals based on their genetic variation sites, I am interested in how accurately we could associate the sample’s origins from “The 1000 Genomes Project” with their genetic information. My project will be stored in a GitHub repository so that any client could run this repository to replicate the main results in “Genes Mirror Geography within Europe” from end-to-end.

### Usage Instructions

* Description of targets and using `run.py`

### Description of Contents

The project consists of these portions:
```
PROJECT
├── .env
├── .gitignore
├── README.md
├── config
│   ├── data-params.json
│   └── test-params.json
├── data
│   ├── log
│   ├── out
│   ├── raw
│   └── temp
├── lib
├── notebooks
│   └── .gitkeep
├── references
│   └── .gitkeep
├── requirements.txt
├── run.py
└── src
    └── etl.py
```

#### `src`

* `etl.py`: Library code that executes tasks useful for getting data.

#### `config`

* `data-params.json`: Common parameters for getting data, serving as
  inputs to library code.
  
* `test-params.json`: parameters for running small process on small
  test data.

#### `references`

* Data Dictionaries, references to external sources
- [1] A global reference for human genetic variation https://www.nature.com/articles/nature15393.
- [2] Genes mirror geography within Europe https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2735096/.
- [3] DNA Sequencing Technologies Key to the Human Genome Project https://www.nature.com/scitable/topicpage/dna-sequencing-technologies-key-to-the-human-828/.
- [4] Figure 6: 1000 Genomes https://www.internationalgenome.org.
- [5] Population structure: PCA, https://speciationgenomics.github.io/pca/.
- [6] Whole genome association analysis toolset http://zzz.bwh.harvard.edu/plink/dataman.shtml#mergelist.


#### `notebooks`

* Jupyter notebooks for *analyses*
  - notebooks are not for data processing; they should import code
    from `src`.
