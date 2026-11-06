# Linux Lesson 03: SED

## Overview

`sed` (Stream Editor) is a Linux command-line utility used to search, filter, replace, insert, and delete text in files.

It is useful for automating repetitive text-processing tasks, including preparing and cleaning tabular data.

## 1. Basic Syntax

```bash
sed 'command' filename
```

## 2. Print Specific Lines

Print the first three lines:

```bash
sed -n '1,3p' sample.txt
```

- `-n`: Suppresses automatic printing.
- `1,3`: Selects lines 1 through 3.
- `p`: Prints the selected lines.

## 3. Search and Replace

Replace the first occurrence on each line:

```bash
sed 's/Rachel/Emma/' sample.txt
```

Replace all occurrences on each line:

```bash
sed 's/BRCA1/TP53/g' test.txt
```

- `s`: Substitution command.
- `g`: Replaces all occurrences on each line.

## 4. Modify Files In Place

Modify the original file directly:

```bash
sed -i 's/BRCA1/TP53/g' test.txt
```

Create a backup before modifying:

```bash
sed -i.bak 's/tp53/TP53/g' test.txt
```

This creates `test.txt.bak` as a backup.

## 5. Delete Lines

Delete line 2:

```bash
sed '2d' sample.txt
```

Delete lines containing `LOW`:

```bash
sed '/LOW/d' sample.txt
```

Case-insensitive deletion:

```bash
sed '/LOW/Id' sample.txt
```

Delete lines 2 through 4:

```bash
sed '2,4d' sample.txt
```

Keep only the first line:

```bash
sed '1!d' sample.txt
```

## 6. Pattern Matching

Print lines containing `HIGH`:

```bash
sed -n '/HIGH/p' wes_variants.tsv
```

Print lines beginning with `S00`:

```bash
sed -n '/^S00/p' wes_variants.tsv
```

- `^`: Matches the beginning of a line.
- `$`: Matches the end of a line.

## 7. WES Variant Data Examples

Remove the header row:

```bash
sed '1d' wes_variants.tsv
```

Replace a gene name:

```bash
sed 's/BRCA1/BRCA1_modified/g' wes_variants.tsv
```

Convert tab-separated data into comma-separated data:

```bash
sed 's/\t/,/g' wes_variants.tsv > wes_variants.csv
```

Here, `\t` represents a tab character.

## 8. Important Concepts

| Symbol / Option | Meaning |
|---|---|
| `s` | Substitute text |
| `g` | Replace all matches on each line |
| `d` | Delete selected lines |
| `p` | Print selected lines |
| `-n` | Suppress automatic printing |
| `-i` | Modify the original file |
| `^` | Beginning of a line |
| `$` | End of a line |
| `I` | Case-insensitive matching |

## 9. Bioinformatics Applications

SED can help with:

- Removing unwanted header or data lines.
- Replacing text in variant annotation files.
- Filtering records based on text patterns.
- Converting simple tab-delimited text into comma-delimited text.
- Performing repetitive text-cleaning operations.

**Note:** SED is a text-processing utility, not a biological data parser. For production WES pipelines, use structured tools such as Python's `csv` module or pandas when data integrity, column validation, and data types matter.

## 10. Key Takeaway

SED is a useful stream editor for automating basic text manipulation in Linux. Understanding substitution, deletion, printing, pattern matching, and in-place editing provides a foundation for working with text-based bioinformatics files.
