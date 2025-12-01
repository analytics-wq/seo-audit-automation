# Ahrefs Schema 

This document defines the structure of Ahrefs exports used in the SEO Audit Proposal. This schema definition is just a reference & data inside is only an example how to read. **DO NOT use any data from this file** for the actual audit.**ONLY extract data from the user-uploaded CSV/XLSX files**.
---

## Export Overview

| Sheet | Purpose | Used In |
|-------|---------|---------|
| `Organic Benchmarking` | Monthly traffic, pages, position, referring domains by competitor | Slide 8, Slide 20 |
| `Organic Position Rank` | Monthly keyword counts by position bucket by competitor | Slide 7, Slide 8 |

**Note:** Ahrefs exports use a **transposed matrix structure** — competitors and metrics are in columns, time periods in rows.

---

## Sheet 1: Organic Benchmarking

**Purpose:** Time-series competitive data for traffic, pages, avg position, and referring domains

**Used In:** Slide 8 (Referring Domains), Slide 20 (Domain Authority Trend)

### Structure Overview

```
Row 0: Domain URLs (repeated 4× per competitor for each metric)
Row 1: Metric names
Row 2+: Monthly data (one row per month, oldest to newest)
```

### Column Layout

Each competitor has 4 columns (one per metric), repeated across the sheet:

| Columns | Competitor | Metrics |
|---------|------------|---------|
| 1-4 | constructdigital.com | Avg. organic traffic, Avg. Organic pages, Organic position, Referring domains |
| 5-8 | impossible.sg | Avg. organic traffic, Avg. Organic pages, Organic position, Referring domains |
| 9-12 | oom.com.sg | Avg. organic traffic, Avg. Organic pages, Organic position, Referring domains |
| 13-16 | firstpagedigital.sg | Avg. organic traffic, Avg. Organic pages, Organic position, Referring domains |
| 17-20 | brewinteractive.com | Avg. organic traffic, Avg. Organic pages, Organic position, Referring domains |
| 21-24 | mediaonemarketing.com.sg | Avg. organic traffic, Avg. Organic pages, Organic position, Referring domains |
| 25-28 | hashmeta.com | Avg. organic traffic, Avg. Organic pages, Organic position, Referring domains |

### Row Structure

| Row | Content | Example |
|-----|---------|---------|
| 0 | Domain (header) | `https://constructdigital.com/` |
| 1 | Metric (header) | `Avg. organic traffic` |
| 2 | June 2025 | `2025-06-01 00:00:00` |
| 3 | July 2025 | `2025-07-01 00:00:00` |
| 4 | August 2025 | `2025-08-01 00:00:00` |
| 5 | September 2025 | `2025-09-01 00:00:00` |
| 6 | October 2025 | `2025-10-01 00:00:00` |
| 7 | November 2025 | `2025-11-01 00:00:00` |

### Metric Definitions

| Metric | Data Type | Description | Column Position |
|--------|-----------|-------------|-----------------|
| `Avg. organic traffic` | Integer | Estimated monthly organic visits | 1st column per competitor |
| `Avg. Organic pages` | Integer | Pages receiving organic traffic | 2nd column per competitor |
| `Organic position` | Integer | Average ranking position | 3rd column per competitor |
| `Referring domains` | Integer | Unique linking domains | 4th column per competitor |

### Data Extraction for Slide 8

**Referring Domains (use latest month = last row):**

```python
# Get last row (most recent month)
latest = df.iloc[-1]

# Referring domains is 4th metric (column index 4, 8, 12, etc.)
referring_domains = {
    'constructdigital.com': latest[4],   # Column index for RD
    'impossible.sg': latest[8],
    'oom.com.sg': latest[12],
    'firstpagedigital.sg': latest[16],
    'brewinteractive.com': latest[20],
    'mediaonemarketing.com.sg': latest[24],
    'hashmeta.com': latest[28]
}
```

**Sample Output (Nov 2025):**

| Competitor | Referring Domains |
|------------|-------------------|
| constructdigital.com | 397 |
| impossible.sg | 979 |
| oom.com.sg | 2,589 |
| firstpagedigital.sg | 1,425 |
| brewinteractive.com | 965 |
| mediaonemarketing.com.sg | 3,304 |
| hashmeta.com | 582 |

### Data Extraction for Slide 20

**Referring Domains Trend (time series for {Brand}):**

```python
# Column 4 = Referring domains for constructdigital.com
brand_rd_trend = df.iloc[2:, 4].tolist()  # Skip header rows

# Calculate growth
first_month = brand_rd_trend[0]   # 305 (Jun)
last_month = brand_rd_trend[-1]   # 397 (Nov)
growth = last_month - first_month  # +92
growth_pct = ((last_month - first_month) / first_month) * 100  # +30.2%
```

### Slide Mapping

| Slide | Placeholder | Data Source |
|-------|-------------|-------------|
| 8 | Referring Domains row | Latest month, column 4 per competitor |
| 20 | RD trend chart | All months, column 4 for {Brand} |
| 20 | RD growth % | `(last - first) / first × 100` |

---

## Sheet 2: Organic Position Rank

**Purpose:** Keyword count by position bucket over time for competitive analysis

**Used In:** Slide 7 (Position Distribution), Slide 8 (Total Keywords, Page 1 Keywords)

### Structure Overview

```
Row 0: Domain URLs (repeated 4× per competitor for each position bucket)
Row 1: Position bucket names
Row 2+: Monthly data (one row per month)
```

### Column Layout

Each competitor has 4 columns (one per position bucket):

| Columns | Competitor | Position Buckets |
|---------|------------|------------------|
| 1-4 | constructdigital.com | Rank 1-3, Rank 4-10, Rank 11-20, Rank 21-50 |
| 5-8 | impossible.sg | Rank 1-3, Rank 4-10, Rank 11-20, Rank 21-50 |
| 9-12 | oom.com.sg | Rank 1-3, Rank 4-10, Rank 11-20, Rank 21-50 |
| ... | ... | ... |

### Position Bucket Definitions

| Bucket | Description | SERP Location |
|--------|-------------|---------------|
| `Rank 1-3` | Top 3 positions | Above fold, highest CTR |
| `Rank 4-10` | Positions 4-10 | Page 1, below fold |
| `Rank 11-20` | Positions 11-20 | Page 2 |
| `Rank 21-50` | Positions 21-50 | Pages 3-5 |

### Calculated Metrics

**Total Keywords (for Slide 8):**

```python
# Sum all 4 position buckets for latest month
latest = df.iloc[-1]

# For constructdigital.com (columns 1-4):
total_keywords = {
    'constructdigital.com': latest[1] + latest[2] + latest[3] + latest[4],
    # = Rank 1-3 + Rank 4-10 + Rank 11-20 + Rank 21-50
    'impossible.sg': latest[5] + latest[6] + latest[7] + latest[8],
    # ... etc
}
```

**Sample Calculation (Nov 2025 for constructdigital.com):**
- Rank 1-3: 12
- Rank 4-10: 9
- Rank 11-20: 1
- Rank 21-50: 7
- **Total Keywords: 29**

**Page 1 Keywords (for Slide 8):**

```python
# Sum Rank 1-3 + Rank 4-10 only
page1_keywords = {
    'constructdigital.com': latest[1] + latest[2],  # 12 + 9 = 21
    'impossible.sg': latest[5] + latest[6],
    # ... etc
}
```

**Page 1 Ratio:**

```python
# What percentage of total keywords are on Page 1?
page1_ratio = page1_keywords / total_keywords * 100
# constructdigital.com: 21 / 29 = 72.4%
```

### Slide 7: Position Distribution

**Bar Chart Data (latest month for {Brand}):**

```python
position_dist = {
    'Rank 1-3': latest[1],     # 12
    'Rank 4-10': latest[2],    # 9
    'Rank 11-20': latest[3],   # 1
    'Rank 21-50': latest[4]    # 7
}
```

### Trend Analysis

**Position Improvement Tracking:**

```python
# Compare first and last month for {Brand}
first = df.iloc[2]   # June 2025
last = df.iloc[-1]   # November 2025

# Top 3 change
top3_change = last[1] - first[1]  # 12 - 11 = +1

# Page 1 change
page1_first = first[1] + first[2]  # 11 + 9 = 20
page1_last = last[1] + last[2]     # 12 + 9 = 21
page1_change = page1_last - page1_first  # +1
```

### Slide Mapping

| Slide | Placeholder | Calculation |
|-------|-------------|-------------|
| 7 | Position Distribution chart | Latest month: Rank 1-3, 4-10, 11-20, 21-50 |
| 8 | Total Keywords row | Sum all 4 buckets per competitor |
| 8 | Page 1 Keywords row | Sum Rank 1-3 + Rank 4-10 per competitor |

---

## Competitor Alignment

Ensure competitor order is consistent across sheets and with SEMrush:

| Position | Domain |
|----------|--------|
| 1 | constructdigital.com (Brand) |
| 2 | impossible.sg |
| 3 | oom.com.sg |
| 4 | firstpagedigital.sg |
| 5 | brewinteractive.com |
| 6 | mediaonemarketing.com.sg |
| 7 | hashmeta.com |

---

## Priority Rules

### Page 1 Keywords Priority (Slide 8)

| Condition | Priority | Rationale |
|-----------|----------|-----------|
| {Brand} Page 1 < 50% of leader | **H** | Significant visibility gap |
| {Brand} Page 1 50-75% of leader | **M** | Competitive gap |
| {Brand} Page 1 > 75% of leader | **L** | Competitive position |

### Position Trend Priority

| Condition | Priority |
|-----------|----------|
| Top 3 declining over 3+ months | **H** |
| Page 1 flat or declining | **M** |
| Page 1 growing | **L** |

---
## Extraction Logic (Reference)

**System Note:** Use the logic below to extract ALL required metrics. Do not rely on static sample numbers.

```python
import pandas as pd

def extract_benchmark_metrics(df):
    """
    LOGIC for Slide 8 & 20:
    1. Scan Row 1 (header row) to find column indices for:
       - "Avg. organic traffic"
       - "Avg. Organic pages"
       - "Organic position"
       - "Referring domains"
       
    2. Jump to the LAST row of the file (df.iloc[-1]) to get the latest month's data.
    
    3. Return a dictionary with all 4 metrics for the brand and competitors.
    """
    # Pseudocode logic for the AI:
    latest_row = df.iloc[-1] 
    
    return {
        "traffic": latest_row["Avg. organic traffic"],
        "pages": latest_row["Avg. Organic pages"],
        "position": latest_row["Organic position"],
        "referring_domains": latest_row["Referring domains"]
    }

def extract_position_buckets(df):
    """
    LOGIC for Slide 7:
    1. Identify columns in Row 1 labeled "Rank 1-3", "Rank 4-10", etc.
    2. Sum these columns for the LAST row to get 'Total Keywords'.
    """
    pass
```

---

## Data Quality Checks

| Check | Validation |
|-------|------------|
| Time series | At least 6 months for trend analysis |
| All competitors | Same number in both sheets |
| Non-zero values | Flag if any competitor has 0 keywords |
| Date alignment | Both sheets should cover same months |

---

## Common Issues

| Issue | Resolution |
|-------|------------|
| Domain URL format varies | Normalize by extracting domain name |
| `.1`, `.2`, `.3` suffix in headers | Indicates repeated metric columns — use Row 1 for metric name |
| Missing Authority/DR | Not in Ahrefs export — use SEMrush `Authority Score` |
| Competitor order mismatch | Manually align to SEMrush Domain Overview order |
