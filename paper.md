---
title: 'fastq-lite: A Constant-Memory Python Adapter Trimmer for Resource-Limited NGS Analysis'
tags:
    - Python
    - Bioinformatics
    - NGS
    - FASTQ
    - Adapter-Trimming
    - Low-Memory
authors:
     name: Sahil Shelote
    orcid: 0009-0007-1169-0448
    affiliation: 1
affiliations:
    name: Independent Researcher, London, UK
    index: 1
date: 4 October 2026
bibliography: paper.bib
---

## Summary

Adapter contamination is a common problem in Illumina NGS data that reduces mapping accuracy and inflates sequencing costs [@martin2011]. Existing tools such as `cutadapt` are robust but can require significant RAM for large FASTQ files, which is a barrier for analysis on laptops or low-cost cloud VMs. 

`fastq-lite` addresses this gap by providing a pure-Python, single-file adapter trimmer with strictly constant $O(1)$ memory usage. It performs exact substring matching for Illumina TruSeq adapters and streams FASTQ files without loading them into RAM. Benchmarking shows identical trimming accuracy to `cutadapt` with 1.7x lower peak RAM on 1M reads: 12.75 MB vs 21.88 MB. 

`fastq-lite` is designed for resource-limited bioinformatics, education, and rapid prototyping where memory, not CPU, is the constraint.

## Statement of Need

Current adapter trimming tools are optimized for speed on HPC clusters. There is no lightweight, zero-dependency tool that guarantees constant memory for teaching, edge devices, or users without access to >16 GB RAM. `fastq-lite` fills this niche. It is <150 lines of code, has no dependencies beyond the Python standard library, and is suitable for inclusion in bioinformatics curricula.

## Benchmarks

| Dataset | Tool | Peak RAM | Time | Bases Trimmed |
| --- | --- | --- | --- | --- |
| 100k reads | fastq-lite | 12.75 MB | 6.15 s | 3,300,000 |
| 100k reads | cutadapt | 22.00 MB | 1.32 s | 3,300,000 |
| 1M reads | fastq-lite | 12.75 MB | 43.15 s | 33,000,000 |
| 1M reads | cutadapt | 21.88 MB | 21.88 s | 33,000,000 |

Memory was measured using `/usr/bin/time -v`. Accuracy was verified by md5sum of trimmed outputs.

## Availability

Source code: https://github.com/mbxss25D/fastq-lite  
License: MIT

## Acknowledgements

We thank the developers of `cutadapt` [@martin2011] for providing the benchmarking baseline.

## References
