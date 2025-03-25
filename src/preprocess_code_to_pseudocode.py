# src/preprocess_code_to_pseudocode.py

import csv
import argparse
from collections import defaultdict

def parse_tsv(file_path):
    rows = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            rows.append(row)
    return rows

def preprocess_line(row):
    # For converting code to pseudocode, we use:
    # - Source: the C++ code (from 'code')
    # - Target: the pseudocode (from 'text')
    # If the pseudocode is empty, you might decide to skip this example.
    code_line = row['code'].strip()
    pseudocode_line = row['text'].strip()
    return code_line, pseudocode_line

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_tsv', type=str, required=True,
                        help='Path to the input TSV (e.g., spoc-train-train.tsv)')
    parser.add_argument('--output_txt', type=str, required=True,
                        help='Output file to store paired code and pseudocode')
    args = parser.parse_args()

    rows = parse_tsv(args.input_tsv)
    
    with open(args.output_txt, 'w', encoding='utf-8') as out_f:
        for row in rows:
            code_line, pseudocode_line = preprocess_line(row)
            # Only include examples with non-empty pseudocode.
            if pseudocode_line:
                out_f.write(f"{code_line}\t{pseudocode_line}\n")

if __name__ == "__main__":
    main()
