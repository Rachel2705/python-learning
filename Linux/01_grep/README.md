# Linux Command 01 - GREP

## 1. Introduction
GREP stands for Global Regular Expression Print.

It is used to search for specific words, patterns,
and regular expressions inside files.

## 2. Syntax

grep "pattern" filename

## 3. Commands Practised

| Command | Purpose |
|---|---|
| grep "BRCA1" sample.txt | Search for BRCA1 |
| grep -i "brca1" sample.txt | Ignore case |
| grep -n "TP53" sample.txt | Display line numbers |
| grep -c "mutation" sample.txt | Count matching lines |
| grep -v "BRCA1" sample.txt | Exclude matching lines |
| grep -E "BRCA1|TP53" sample.txt | Search multiple patterns |
| grep -r "BRCA1" . | Search recursively |

## 4. Bioinformatics Applications

- Search gene names in VCF files.
- Search patient IDs in TSV files.
- Identify errors in pipeline logs.
- Search sequence identifiers in FASTA files.
- Identify warnings in NGS pipeline outputs.

## 5. Practice Dataset

sample.txt contains six example patient records.

## 6. Key Learning

GREP is useful for text searching, filtering,
and identifying patterns in biological datasets.
