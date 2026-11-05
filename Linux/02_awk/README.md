# AWK – Text Processing and Data Analysis

## Overview

AWK is a Linux command-line utility used for processing and analysing structured text files. It is particularly useful for extracting columns, filtering records, performing calculations, and summarising tabular data.

In bioinformatics, AWK can be used to process TSV files, variant annotation tables, sequencing results, and other structured datasets.

## 1. Basic AWK Syntax

```bash
awk 'pattern { action }' filename
```

- `pattern`: Defines which records to process.
- `action`: Defines what operation to perform.
- `filename`: Input file.

## 2. Field Variables

AWK automatically separates input records into fields.

| Variable | Description |
|---|---|
| `$0` | Entire line |
| `$1` | First field |
| `$2` | Second field |
| `$NF` | Last field |
| `NF` | Number of fields |
| `NR` | Current record number |

### Examples

```bash
awk '{print $0}' sample.txt
awk '{print $1}' sample.txt
awk '{print $2}' sample.txt
awk '{print $1, $2}' sample.txt
awk '{print $NF}' sample.txt
awk '{print NR, $0}' sample.txt
awk '{print NF}' sample.txt
```

## 3. Custom Field Separators

The `-F` option specifies the input field separator.

For tab-separated files:

```bash
awk -F '\t' '{print $2}' variants.tsv
awk -F '\t' '{print $1, $2}' variants.tsv
```

Skip the header:

```bash
awk -F '\t' 'NR > 1 {print $2}' variants.tsv
```

## 4. Conditional Filtering

AWK supports comparison operators such as:

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `&&` | Logical AND |
| `||` | Logical OR |

### Filter HIGH-impact variants

```bash
awk -F '\t' '$4 == "HIGH" {print $0}' variants.tsv
```

### Filter MODERATE-impact variants

```bash
awk -F '\t' '$4 == "MODERATE" {print $0}' variants.tsv
```

### Extract gene names

```bash
awk -F '\t' '$4 == "HIGH" {print $2}' variants.tsv
```

## 5. BEGIN and END Blocks

- `BEGIN`: Executes before processing input records.
- `END`: Executes after processing all input records.

```bash
awk 'BEGIN {print "WES Variant Summary"} {print $0}' variants.tsv
```

Count total variants:

```bash
awk -F '\t' 'NR > 1 {count++} END {print "Total variants:", count}' variants.tsv
```

## 6. Associative Arrays

AWK supports associative arrays for grouping and counting values.

Count variants by impact:

```bash
awk -F '\t' 'NR > 1 {impact[$4]++} END {for (i in impact) print i, impact[i]}' variants.tsv
```

Example output:

```text
HIGH 2
MODERATE 2
LOW 1
```

## 7. Conditional Counting and Percentages

Count HIGH-impact variants and calculate their percentage:

```bash
awk -F '\t' 'NR > 1 {total++; if ($4 == "HIGH") high++} END {printf "HIGH impact: %.2f%%\n", (high/total)*100}' variants.tsv
```

## 8. Practical WES Variant Filtering

Example input: `wes_variants.tsv`

Columns:

```text
Sample_ID  Chromosome  Position  Gene  Consequence  Impact  AF  Depth
```

### Filter HIGH-impact variants

```bash
awk -F '\t' 'NR > 1 && $6 == "HIGH" {print $0}' wes_variants.tsv
```

### Extract HIGH-impact gene names

```bash
awk -F '\t' 'NR > 1 && $6 == "HIGH" {print $4}' wes_variants.tsv
```

### Filter variants with allele frequency below 5%

```bash
awk -F '\t' 'NR > 1 && $7 < 0.05 {print $4, $7}' wes_variants.tsv
```

### Filter variants with sequencing depth greater than 100

```bash
awk -F '\t' 'NR > 1 && $8 > 100 {print $1, $4, $8}' wes_variants.tsv
```

### Combine multiple filtering conditions

Select HIGH-impact variants with allele frequency below 5%:

```bash
awk -F '\t' 'NR > 1 && $6 == "HIGH" && $7 < 0.05 {print $1, $4, $5, $6, $7}' wes_variants.tsv
```

Expected matching genes:

```text
BRCA1
PIK3CA
RB1
```

## 9. Important AWK Concepts

- Field extraction using `$1`, `$2`, and `$NF`.
- Record and field counting using `NR` and `NF`.
- Custom delimiters using `-F`.
- Header exclusion using `NR > 1`.
- Conditional filtering using `if`, `&&`, and comparison operators.
- Summary calculations using `BEGIN`, `END`, and `printf`.
- Grouping and counting using associative arrays.

## 10. Applications in Bioinformatics

AWK is useful for:

- Extracting specific columns from TSV files.
- Filtering annotated genetic variants.
- Identifying HIGH-impact variants.
- Filtering by allele frequency and sequencing depth.
- Counting variants by annotation category.
- Generating simple summaries from sequencing datasets.

**Note:** These exercises use simplified educational data. Production WES analysis requires additional QC, annotation, filtering, and clinical interpretation steps.

---

**Lesson status:** Completed  
**Next topic:** SED – Stream Editor
