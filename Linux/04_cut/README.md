# Linux Lesson 04: CUT

## Overview

`cut` is a Linux command-line utility used to extract specific fields, columns, or character ranges from text files.

It is particularly useful for extracting selected columns from TSV and CSV files in bioinformatics workflows.

## 1. Basic Syntax

```bash
cut [OPTION] filename
```

## 2. Extract Columns from TSV

Extract the first column:

```bash
cut -f1 variants.tsv
```

Extract the fourth column:

```bash
cut -f4 variants.tsv
```

Extract multiple columns:

```bash
cut -f1,4,5 variants.tsv
```

Extract a range of columns:

```bash
cut -f2-5 variants.tsv
```

## 3. Exclude Columns

Extract all columns except column 6:

```bash
cut --complement -f6 variants.tsv
```

## 4. Extract Characters

Extract the first 10 characters from each line:

```bash
cut -c1-10 selected_variants.csv
```

## 5. Working with CSV Files

Specify a comma as the delimiter:

```bash
cut -d',' -f1 selected_variants.csv
```

Extract the first and third fields:

```bash
cut -d',' -f1,3 selected_variants.csv
```

Exclude the second field:

```bash
cut -d',' --complement -f2 selected_variants.csv
```

## 6. Convert TSV to CSV

Select specific columns and convert tabs into commas:

```bash
cut -f1,4,5 variants.tsv | tr '\t' ',' > selected_variants.csv
```

## 7. Important Options

| Option | Description |
|---|---|
| `-f` | Extract fields |
| `-c` | Extract character positions |
| `-d` | Specify field delimiter |
| `--complement` | Extract all fields except selected ones |
| `-s` | Suppress lines without the delimiter |

## 8. Bioinformatics Applications

- Extract Sample IDs from WES variant files.
- Retrieve gene names and variant impact columns.
- Extract chromosome and genomic position information.
- Select relevant columns for downstream analysis.
- Prepare simplified tabular files for further processing.

## 9. Important Note

`cut` works with simple delimiters. It does not correctly parse complex CSV files containing quoted fields with embedded commas. For production bioinformatics workflows, use Python's `csv` module or pandas when structured parsing and data integrity are important.

## 10. Key Takeaway

`cut` is useful for quickly extracting selected columns and fields from structured text files. Understanding `-f`, `-c`, and `-d` is essential for effective Linux text processing.
