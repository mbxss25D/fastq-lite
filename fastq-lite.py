#!/usr/bin/env python3
"""
fastq-lite: Constant-memory adapter trimmer for gzipped FASTQ files.
Usage: python fastq-lite.py -i input.fq.gz -a AGATCGGAAGAGC -o output.fq.gz
"""
import argparse
import gzip
import sys

ADAPTER_DEFAULT = "AGATCGGAAGAGC"

def trim_read(seq: bytes, qual: bytes, adapter: bytes):
    """Trim adapter if found. Returns trimmed seq, qual."""
    idx = seq.find(adapter)
    if idx != -1:
        return seq[:idx], qual[:idx]
    return seq, qual

def main():
    parser = argparse.ArgumentParser(
        description="fastq-lite: O(1) memory adapter trimmer for gzipped FASTQ"
    )
    parser.add_argument("-i", "--input", required=True, help="Input FASTQ.gz file")
    parser.add_argument("-a", "--adapter", required=True, help="Adapter sequence")
    parser.add_argument("-o", "--output", required=True, help="Output FASTQ.gz file")
    args = parser.parse_args()

    adapter_bytes = args.adapter.encode()

    try:
        with gzip.open(args.input, "rb") as fin, gzip.open(args.output, "wb") as fout:
            while True:
                header = fin.readline()
                if not header:
                    break
                seq = fin.readline().strip()
                plus = fin.readline()
                qual = fin.readline().strip()

                seq_trim, qual_trim = trim_read(seq, qual, adapter_bytes)
                
                fout.write(header)
                fout.write(seq_trim + b"\n")
                fout.write(plus)
                fout.write(qual_trim + b"\n")
    except Exception as e:
        sys.exit(f"Error: {e}")

if __name__ == "__main__":
    main()
