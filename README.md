# fastq-lite

`fastq-lite` is a lightweight, constant-memory $O(1)$ Python tool for trimming Illumina adapters from FASTQ files.

**Author:** Sahil Shelote, Bioinformatician  
**Affiliation:** Independent Researcher, London, UK

## Key Result
- **1.7x Less RAM** vs cutadapt v4.4: `12.75 MB` vs `22.00 MB`
- **Constant Scaling**: `12.75 MB` at 100k reads and 1M reads
- **Identical Output**: `33,000,000` bases trimmed on 1M dataset

## Installation
```bash
git clone https://github.com/mbxss25D/fastq-lite
cd fastq-lite
