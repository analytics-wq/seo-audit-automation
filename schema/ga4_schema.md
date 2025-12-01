# GA4 Schema

This document defines the structure of Google Analytics 4 exports used for traffic source analysis in the SEO Audit Proposal. This schema definition is just a reference & data inside is only an example how to read. **DO NOT use any data from this file** for the actual audit.**ONLY extract data from the user-uploaded CSV/XLSX files**.

---

## Overview

GA4 data answers the fundamental question: **Where is traffic coming from?**

| Report | File | Purpose | Answers |
|--------|------|---------|---------|
| Channel Report | `ga4_schema.xlsx` | Traffic by acquisition channel | Which channels drive traffic? |
| Countries Report | `GA4_Countries_report.xlsx` | Traffic by geography | Where are visitors located? |

**Key Insight:** The Countries Report shows **Organic Search traffic only** (5,238 sessions), while the Channel Report shows **all traffic sources** (23,994 sessions).

---

## Slide Support

| Slide | Element | Data Source |
|-------|---------|-------------|
| **7** | Traffic Sources Pie Chart | Channel Report → Totals by channel |
| **7** | Top Countries Bar Chart | Countries Report → Grand Total by country |
| **7** | Keyword Position Distribution | *Ahrefs (see ahrefs_schema.md)* |
| **9** | Engagement Metrics | Channel Report → Organic Search row |
| **24** | Organic Sessions KPI | Channel Report → Organic Search Totals |

---

# REPORT 1: Channel Report

**File:** `ga4_schema.xlsx`  
**Sheet:** `Session Default Channel Group`  
**Purpose:** Breakdown of ALL website traffic by acquisition channel

---

## File Structure

```
Rows 0-4:   Metadata (comments starting with #)
Row 5:      Empty
Row 6:      Month numbers (repeated 5× per month)
Row 7:      Metric column headers
Row 8:      Grand Total row (all channels combined)
Rows 9-19:  Individual channel data
```

**Dimensions:** 20 rows × 57 columns

---

## Metadata (Rows 0-4)

| Row | Content | Example |
|-----|---------|---------|
| 0 | Separator | `# ----------------------------------------` |
| 1 | Property URL | `# https://www.constructdigital.com/ - GA4` |
| 2 | Report name | `# 6 Months-Session Default Channel Group` |
| 3 | Date range | `# 20250101-20251031` |
| 4 | Separator | `# ----------------------------------------` |

### Extract Date Range

```python
date_row = df.iloc[3, 0]  # "# 20250101-20251031"
date_part = date_row.replace("# ", "")
start, end = date_part.split("-")
# Format: "01/01/2025 - 31/10/2025"
```

---

## Column Structure

### Row 6: Month Headers

Months repeat 5 times each (one per metric). **Months are NOT chronological.**

| Columns | Month # | Calendar |
|---------|---------|----------|
| 1-5 | 6 | June |
| 6-10 | 10 | October |
| 11-15 | 4 | April |
| 16-20 | 3 | March |
| 21-25 | 5 | May |
| 26-30 | 7 | July |
| 31-35 | 1 | January |
| 36-40 | 8 | August |
| 41-45 | 9 | September |
| 46-50 | 2 | February |
| 51-55 | **Totals** | Aggregated |
| 56 | — | Empty |

### Month-to-Column Mapping

```python
MONTH_COLUMNS = {
    1: 31,   # January
    2: 46,   # February
    3: 16,   # March
    4: 11,   # April
    5: 21,   # May
    6: 1,    # June
    7: 26,   # July
    8: 36,   # August
    9: 41,   # September
    10: 6,   # October
}
TOTALS_COL = 51
```

### Row 7: Metric Headers

Each month block has 5 metrics in fixed order:

| Offset | Metric | Data Type | Description |
|--------|--------|-----------|-------------|
| +0 | `Sessions` | Integer | Total visits |
| +1 | `Active users` | Integer | Unique users |
| +2 | `Engagement rate` | Float (0-1) | Engaged sessions ÷ Sessions |
| +3 | `Engaged sessions` | Integer | Sessions with interaction |
| +4 | `Average session duration` | Float | Duration in seconds |

**Example:** Month 6 (June) Sessions = Column 1, Engagement rate = Column 3

---

## Data Rows

### Row 8: Grand Total

All channels combined. Use for calculating percentages.

| Column | Value | Description |
|--------|-------|-------------|
| 51 | 23,994 | Total Sessions |
| 52 | 20,717 | Total Active Users |
| 53 | 0.3157 | Overall Engagement Rate |
| 54 | 7,574 | Total Engaged Sessions |
| 55 | 94.09 | Avg Session Duration (seconds) |

### Rows 9-19: Channel Data

| Row | Channel | Description | Sessions | % |
|-----|---------|-------------|----------|---|
| 9 | `Direct` | Direct URL, bookmarks | 16,630 | 69.3% |
| 10 | `Organic Search` | **PRIMARY** — SEO traffic | 5,238 | 21.8% |
| 11 | `Referral` | External website links | 1,124 | 4.7% |
| 12 | `Organic Social` | Unpaid social media | 545 | 2.3% |
| 13 | `Unassigned` | Unclassified | 374 | 1.6% |
| 14 | `Email` | Email campaigns | 38 | 0.2% |
| 15 | `Paid Search` | Google Ads | 17 | 0.1% |
| 16 | `Paid Social` | Paid social ads | 12 | 0.0% |
| 17 | `Organic Shopping` | Google Shopping | 4 | 0.0% |
| 18 | `Organic Video` | YouTube | 3 | 0.0% |
| 19 | `Paid Other` | Other paid | 3 | 0.0% |

---

## Slide 7: Traffic Sources Pie Chart

### Data Extraction

```python
# Get Totals Sessions (column 51) for each channel
def get_channel_sessions(df, channel_name):
    return df.loc[df[0] == channel_name, 51].values[0]

# Build pie chart data
pie_data = {
    'Direct': get_channel_sessions(df, 'Direct'),
    'Organic Search': get_channel_sessions(df, 'Organic Search'),
    'Referral': get_channel_sessions(df, 'Referral'),
    'Organic Social': get_channel_sessions(df, 'Organic Social'),
    'Paid': (
        get_channel_sessions(df, 'Paid Search') +
        get_channel_sessions(df, 'Paid Social') +
        get_channel_sessions(df, 'Paid Other')
    ),
    'Other': (
        get_channel_sessions(df, 'Unassigned') +
        get_channel_sessions(df, 'Email') +
        get_channel_sessions(df, 'Organic Shopping') +
        get_channel_sessions(df, 'Organic Video')
    )
}

# Calculate percentages
grand_total = df.iloc[8, 51]  # 23,994
for channel, sessions in pie_data.items():
    pct = (sessions / grand_total) * 100
```

### Output Format

| Channel | Sessions | Percentage |
|---------|----------|------------|
| Direct | 16,630 | 69.3% |
| Organic Search | 5,238 | 21.8% |
| Referral | 1,124 | 4.7% |
| Organic Social | 545 | 2.3% |
| Paid | 32 | 0.1% |
| Other | 425 | 1.8% |

### Key Message Generation

```python
organic_pct = (organic_sessions / grand_total) * 100

if organic_pct > 50:
    message = "Organic search dominates acquisition"
    priority = "L"
elif organic_pct > 30:
    message = "Organic search is a major traffic driver"
    priority = "L"
elif organic_pct > 15:
    message = "Organic search contributes significant traffic"
    priority = "M"
else:
    message = "Organic search is underutilized — growth opportunity"
    priority = "H"
```

---

## Slide 9: Engagement Metrics

### Period Comparison

Split data into Previous (Jan-May) vs Current (Jun-Oct) periods:

```python
# Get Organic Search row
organic = df[df[0] == 'Organic Search'].iloc[0]

# Previous period (months 1-5)
prev_months = [1, 2, 3, 4, 5]
prev_engagement = [organic[MONTH_COLUMNS[m] + 2] for m in prev_months]
prev_avg_engagement = sum(prev_engagement) / len(prev_engagement)

prev_engaged_sessions = sum(organic[MONTH_COLUMNS[m] + 3] for m in prev_months)

# Current period (months 6-10)
curr_months = [6, 7, 8, 9, 10]
curr_engagement = [organic[MONTH_COLUMNS[m] + 2] for m in curr_months]
curr_avg_engagement = sum(curr_engagement) / len(curr_engagement)

curr_engaged_sessions = sum(organic[MONTH_COLUMNS[m] + 3] for m in curr_months)
```

### Average Session Duration

```python
# From Totals column 55 (in seconds)
avg_seconds = organic[55]  # 226.19

# Convert to display format
minutes = int(avg_seconds // 60)   # 3
seconds = int(avg_seconds % 60)    # 46
formatted = f"{minutes}m {seconds:02d}s"  # "3m 46s"
```

### Placeholder Mapping

| Placeholder | Source | Sample |
|-------------|--------|--------|
| `{Previous Engagement Rate}` | Months 1-5 avg | 65.42% |
| `{Current Engagement Rate}` | Months 6-10 avg | 66.90% |
| `{Previous Engaged Sessions}` | Months 1-5 sum | 1,837 |
| `{Current Engaged Sessions}` | Months 6-10 sum | 1,659 |
| `{Avg Session Duration}` | Totals col 55 | 3m 46s |

---

## Slide 24: KPI Baseline

| KPI | Source | Value |
|-----|--------|-------|
| Organic Sessions | `organic[51]` | 5,238 |
| Organic Engagement Rate | `organic[53]` | 66.88% |
| Organic Avg Duration | `organic[55]` | 226.19s |

---

# REPORT 2: Countries Report

**File:** `GA4_Countries_report.xlsx`  
**Sheet:** `Session Default Channel Group`  
**Purpose:** Geographic breakdown of **Organic Search traffic only**

---

## File Structure

```
Rows 0-4:   Metadata (comments starting with #)
Row 5:      Empty
Row 6:      Country names (repeated 5× per country)
Row 7:      "Month" label + Metric headers
Row 8:      Grand Total row (all months per country)
Rows 9-18:  Monthly breakdown (months 1-10)
```

**Dimensions:** 19 rows × 82 columns

**Important:** Total sessions = 5,238 (matches Organic Search from Channel Report)

---

## Column Structure

### Row 6: Country Headers

Each country has 5 columns (one per metric):

| Columns | Country |
|---------|---------|
| 0 | `Country` (label) |
| 1-5 | Singapore |
| 6-10 | United States |
| 11-15 | India |
| 16-20 | Philippines |
| 21-25 | Malaysia |
| 26-30 | Vietnam |
| 31-35 | United Kingdom |
| 36-40 | Indonesia |
| 41-45 | Canada |
| 46-50 | Australia |
| 51-55 | Thailand |
| 56-60 | Pakistan |
| 61-65 | Germany |
| 66-70 | China |
| 71-75 | Japan |
| 76-80 | **Totals** |

### Country-to-Column Mapping

```python
COUNTRY_COLUMNS = {
    'Singapore': 1,
    'United States': 6,
    'India': 11,
    'Philippines': 16,
    'Malaysia': 21,
    'Vietnam': 26,
    'United Kingdom': 31,
    'Indonesia': 36,
    'Canada': 41,
    'Australia': 46,
    'Thailand': 51,
    'Pakistan': 56,
    'Germany': 61,
    'China': 66,
    'Japan': 71,
    'Totals': 76
}
```

### Row 7: Metric Headers

Same 5 metrics per country block:

| Offset | Metric |
|--------|--------|
| +0 | Sessions |
| +1 | Active users |
| +2 | Engagement rate |
| +3 | Engaged sessions |
| +4 | Average session duration |

---

## Data Rows

### Row 8: Grand Total (Per Country)

Aggregated across all months for each country.

| Country | Sessions | Active Users | Engagement Rate | Engaged Sessions |
|---------|----------|--------------|-----------------|------------------|
| Singapore | 2,049 | 1,248 | 71.60% | 1,467 |
| United States | 534 | 430 | 53.56% | 286 |
| India | 531 | 359 | 75.14% | 399 |
| Philippines | 398 | 252 | 66.83% | 266 |
| Malaysia | 194 | 126 | 60.82% | 118 |
| Vietnam | 178 | 104 | 71.35% | 127 |
| United Kingdom | 167 | 134 | 68.26% | 114 |
| Indonesia | 137 | 91 | 69.34% | 95 |
| Canada | 115 | 81 | 60.87% | 70 |
| Australia | 108 | 74 | 55.56% | 60 |
| Thailand | 95 | 41 | 51.58% | 49 |
| Pakistan | 60 | 50 | 78.33% | 47 |
| Germany | 49 | 38 | 65.31% | 32 |
| China | 43 | 40 | 58.14% | 25 |
| Japan | 39 | 26 | 64.10% | 25 |
| **TOTAL** | **5,238** | **3,531** | **66.88%** | **3,503** |

### Rows 9-18: Monthly Data

| Row | Month |
|-----|-------|
| 9 | January (1) |
| 10 | February (2) |
| 11 | March (3) |
| 12 | April (4) |
| 13 | May (5) |
| 14 | June (6) |
| 15 | July (7) |
| 16 | August (8) |
| 17 | September (9) |
| 18 | October (10) |

---

## Slide 7: Top Countries Bar Chart

### Data Extraction

```python
# Get Grand Total row (Row 8)
totals_row = df.iloc[8]

# Extract Sessions for each country
country_sessions = {}
for country, start_col in COUNTRY_COLUMNS.items():
    if country != 'Totals':
        country_sessions[country] = totals_row[start_col]

# Sort by sessions descending
sorted_countries = sorted(country_sessions.items(), key=lambda x: x[1], reverse=True)

# Get top 5
top_5 = sorted_countries[:5]

# Calculate percentages
grand_total = totals_row[COUNTRY_COLUMNS['Totals']]  # 5,238
for country, sessions in top_5:
    pct = (sessions / grand_total) * 100
```

### Output Format

| Rank | Country | Sessions | % of Organic |
|------|---------|----------|--------------|
| 1 | Singapore | 2,049 | 39.1% |
| 2 | United States | 534 | 10.2% |
| 3 | India | 531 | 10.1% |
| 4 | Philippines | 398 | 7.6% |
| 5 | Malaysia | 194 | 3.7% |

### Key Message Generation

```python
top_country = sorted_countries[0]
top_pct = (top_country[1] / grand_total) * 100

if top_pct > 50:
    message = f"{top_country[0]} dominates organic traffic at {top_pct:.0f}%"
elif top_pct > 30:
    message = f"{top_country[0]} leads organic traffic ({top_pct:.0f}%), with diversified global reach"
else:
    message = "Organic traffic is well-distributed across multiple markets"
```

---

## Geographic Analysis

### Regional Grouping

```python
REGIONS = {
    'Southeast Asia': ['Singapore', 'Malaysia', 'Vietnam', 'Indonesia', 'Philippines', 'Thailand'],
    'South Asia': ['India', 'Pakistan'],
    'East Asia': ['China', 'Japan'],
    'North America': ['United States', 'Canada'],
    'Europe': ['United Kingdom', 'Germany'],
    'Oceania': ['Australia']
}

# Calculate regional totals
regional_sessions = {}
for region, countries in REGIONS.items():
    regional_sessions[region] = sum(
        country_sessions.get(c, 0) for c in countries
    )
```

### Sample Regional Output

| Region | Sessions | % |
|--------|----------|---|
| Southeast Asia | 3,051 | 58.3% |
| South Asia | 591 | 11.3% |
| North America | 649 | 12.4% |
| East Asia | 82 | 1.6% |
| Europe | 216 | 4.1% |
| Oceania | 108 | 2.1% |

---

## Engagement by Geography

### High-Engagement Markets

Markets with engagement rate > 70%:

| Country | Engagement Rate | Implication |
|---------|-----------------|-------------|
| Pakistan | 78.33% | High-quality traffic |
| India | 75.14% | Strong content relevance |
| Singapore | 71.60% | Core market, engaged audience |
| Vietnam | 71.35% | Emerging opportunity |

### Low-Engagement Markets

Markets with engagement rate < 55%:

| Country | Engagement Rate | Implication |
|---------|-----------------|-------------|
| Thailand | 51.58% | Content/intent mismatch |
| United States | 53.56% | Review targeting strategy |
| Australia | 55.56% | Optimize for local relevance |

---

# Combined Analysis Framework

## Traffic Source Story (Slide 7)

The data tells a two-part story:

### Part 1: Channel Mix

```
"Of {total_sessions:,} total sessions, {organic_pct:.1f}% came from organic search,
indicating {channel_insight}."
```

| Organic % | Insight |
|-----------|---------|
| > 50% | strong SEO foundation driving majority of traffic |
| 30-50% | healthy organic presence with room for growth |
| 15-30% | significant SEO opportunity to capture more demand |
| < 15% | critical need for organic visibility investment |

### Part 2: Geographic Distribution

```
"Organic traffic is concentrated in {top_country} ({top_pct:.0f}%), with
{geographic_insight}."
```

| Concentration | Insight |
|---------------|---------|
| Top country > 50% | opportunity to diversify into secondary markets |
| Top country 30-50% | strong primary market with growing international presence |
| Top country < 30% | well-distributed global footprint |

---

## Data Quality Checks

| Check | Channel Report | Countries Report |
|-------|----------------|------------------|
| Date range | Row 3 metadata | Row 3 metadata |
| Organic Search exists | Row 10 | N/A (entire report is organic) |
| Sessions > 0 | Column 51 | Column 76 |
| Totals match | 5,238 organic | 5,238 total |
| Engagement ≤ 1 | All values | All values |

---

## Common Issues

| Issue | Cause | Resolution |
|-------|-------|------------|
| Months out of order | GA4 export format | Use MONTH_COLUMNS mapping |
| Countries Totals ≠ Channel Organic | Filter mismatch | Countries report is organic-only |
| Engagement > 100% | Decimal vs percent | Value is decimal (0.66 = 66%) |
| Missing countries | Low traffic | Normal — report shows top 15 |

---

## Extraction Logic (Reference)

**System Note:** Use the logic below to dynamically identify columns based on the client file provided. Do not rely on static row numbers or specific country names.

```python
import pandas as pd

def extract_traffic_sources(df):
    """
    LOGIC for 'Organic Traffic Analysis' (Pie Chart):
    1. Context: Corresponds to JSON key `organic_traffic.channels`.
    2. Look for the "Grand Total" row (usually Row 8).
    3. Extract the value from the "Total Sessions" column (Column 51).
    4. Look for the rows in Column A labeled 'Direct', 'Organic Search', 'Referral', etc.
    5. Calculate the percentage: (Channel Session Count / Grand Total) * 100.
    """
    pass

def extract_top_countries(df):
    """
    LOGIC for 'Organic Traffic Analysis' (Top Countries Bar Chart):
    1. Context: Corresponds to JSON key `organic_traffic.top_countries`.
    2. Do NOT assume specific countries are in specific columns.
    3. Scan Row 6 (Header Row) to find ALL country names present in this specific export.
    4. For each country found, go to the "Grand Total" row (Row 8) and extract its Sessions count.
    5. Sort the results descending to find the actual Top 5 for this client.
    """
    pass
```
