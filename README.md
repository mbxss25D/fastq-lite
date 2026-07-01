Markdown
# fastq-lite
**A Constant-Memory Python Adapter Trimmer for Resource-Limited NGS Analysis**

* **Author:** Sahil Shelote
* **Affiliation:** Independent Researcher, London, UK
* **License:** MIT
* **Repository:** https://github.com/mbxss25D/fastq-lite

---

## Overview
`fastq-lite` is a lightweight, pure-Python tool for removing Illumina adapter sequences from FASTQ files. It is designed for environments where memory is constrained, achieving strictly constant *O(1)* RAM usage regardless of dataset size.

## Key Findings
Benchmarked against `cutadapt` v4.4 on synthetic data with 1 adapter per read:

| Dataset | Tool | Peak RAM | Time | Bases Trimmed |
| :--- | :--- | :--- | :--- | :--- |
| 100k reads | fastq-lite | 12.75 MB | 6.15 s | 3,300,000 |
| 100k reads | cutadapt | 22.00 MB | 1.32 s | 3,300,000 |
| 1M reads | fastq-lite | 12.75 MB | 43.15 s | 33,000,000 |
| 1M reads | cutadapt | 21.88 MB | 12.92 s | 33,000,000 |

**Result:** 1.7x less peak RAM with identical trimming accuracy. Memory remained flat from 100k to 1M reads, confirming constant-space execution.

## Installation
No dependencies required. Uses only the Python standard library.

```bash
git clone [https://github.com/mbxss25D/fastq-lite](https://github.com/mbxss25D/fastq-lite)
cd fastq-lite

## Usage
Bash
python fastq-lite.py -i input.fastq.gz -a AGATCGGAAGAGC -o trimmed.fastq.gz

Arguments:

-i: Input FASTQ or FASTQ.gz

-a: Adapter sequence to remove, exact match only

-o: Output FASTQ.gz

Repository Structure
Plaintext
├── fastq-lite.py   # Source code
├── benchmark/      # Benchmark data and plots
├── paper.md        # JOSS manuscript
├── paper.bib       # References
└── LICENSE         # MIT License

Citation
If you use fastq-lite in your work, please cite:

Shelote S. fastq-lite: A Constant-Memory Python Adapter Trimmer. bioRxiv. 2026. doi:10.1101/XXXXXX [Pending]

The full manuscript is available in paper.md.

Limitations
The current version supports single exact-match adapters only. No paired-end or quality-based trimming. Future work will include Cython for speed while keeping O(1) memory.

Acknowledgements
Benchmarking methods follow cutadapt [Martin 2011].
