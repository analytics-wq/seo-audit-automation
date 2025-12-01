# SEMrush Schema

This document defines the structure of SEMrush exports used in the SEO Audit Proposal. This schema definition is just a reference & data inside is only an example how to read. **DO NOT use any data from this file** for the actual audit. **ONLY extract data from the user-uploaded CSV/XLSX/PDF files**.

---

## Part 1: Domain Overview & Keywords (Excel)

**File:** `semrush_schema.xlsx` (or similar export)
**Structure:** Contains multiple sheets for competitive data.

### Sheet 1: Domain Overview

**Purpose:** Competitive benchmarking.
**Structure:** Row 0 = Headers, Row 1 = Brand, Row 2+ = Competitors.

| Column Index | Column Name | Data Type | Description |
|---|---|---|---|
| 0 | `Domain` | URL | Full domain URL |
| 1 | `Authority score` | Integer | SEMrush Authority (0-100) |
| 2 | `Org. Traffic` | Integer | Monthly organic traffic |
| 3 | `Org. Keywords` | Integer | Count of ranking keywords |
| 4 | `Backlinks` | Integer | Total backlinks |
| 5 | `Ref. Domains` | Integer | Unique referring domains |

### Sheet 2: Organic Keyword

**Purpose:** Current ranking performance.

| Column Index | Column Name | Data Type | Description |
|---|---|---|---|
| 0 | `Url` | URL | Ranking page URL |
| 1 | `Keyword` | String | Target keyword |
| 2 | `Position` | Integer | SERP position (1-100) |
| 3 | `Previous Position` | Integer | Previous ranking |
| 5 | `Search Volume` | Integer | Monthly volume |
| 6 | `Traffic` | Float | Estimated traffic |
| 8 | `Competition` | Float | 0-1 density |
| 10 | `Trends` | String | 12-month trend data |

### Sheet 3: Keyword Gap

**Purpose:** Opportunity analysis.

| Column Index | Column Name | Data Type | Description |
|---|---|---|---|
| 0 | `Keyword` | String | The opportunity keyword |
| 1 | `Search Volume` | Integer | Monthly volume |
| 2 | `Gap Type` | String | "Missing", "Weak", "Untapped" |
| 3 | `Best Competitor Domain` | String | Who is winning? |

---

## Extraction Logic: Excel (Reference)

**Integration Note:**
* **Competitive Data** maps to JSON key: `organic_traffic.benchmarking`
* **Keyword Intent** maps to JSON key: `keyword_analysis.intent_mix`
* **Gap Opportunities** maps to JSON key: `keyword_analysis.gap_opportunities`

```python
import pandas as pd

def extract_domain_benchmarking(df):
    """
    LOGIC for Slide 8 & 20:
    1. Identify Brand (Row 1) vs Competitors (Row 2+).
    2. Extract 'Authority score', 'Org. Traffic', 'Ref. Domains' for all.
    3. Calculate 'Authority Gap': Brand Authority - Average Competitor Authority.
    4. Calculate 'Traffic Gap %': ((Brand Traffic / Avg Competitor Traffic) - 1) * 100.
    """
    pass

def classify_keyword_intent(df):
    """
    LOGIC for Slide 14 (Intent Analysis):
    1. Scan 'Keyword' column in Organic Keywords sheet.
    2. Classify based on string matching:
       - Brand: Contains brand name.
       - Location: Contains city/country (e.g., 'Singapore', 'Near me').
       - Commercial/Utility: 'Best', 'Review', 'Vs', 'Agency', 'Service'.
       - Informational: 'How to', 'What is', 'Guide'.
    3. Calculate % breakdown of these categories.
    """
    pass

def extract_gap_opportunities(df):
    """
    LOGIC for Slide 14 (Content Gaps):
    1. Filter Keyword Gap sheet for 'Gap Type' = 'Missing'.
    2. Filter for high value: 'Search Volume' > 1000 AND 'Competition' < 0.5.
    3. Identify the 'Best Competitor Domain' that appears most frequently.
    """
    pass
```

## Part 2: Site Audit (PDF / Text)

**File:** `Semrush-Full_Site_Audit_Report.pdf`
**Purpose:** Technical health and crawl errors.

**System Note:** You must parse the text content of the PDF to find these patterns.

### Extraction Logic: Site Audit (Reference)

**Integration Note:**
* **Health Score** maps to JSON key: `site_health.score`
* **Core Vitals/Errors** maps to JSON key: `technical_seo.issues`

```python
import re

def extract_site_health(pdf_text):
    """
    LOGIC for Slide 10 (Site Health):
    1. Regex find: r'(\d+)\s*%\s*Health Score' (or similar pattern).
    2. Regex find: r'Errors\s*(\d+)'
    3. Regex find: r'Warnings\s*(\d+)'
    """
    pass

def extract_top_technical_issues(pdf_text):
    """
    LOGIC for Slide 13 & 17:
    1. Scan text for known error patterns (listed below).
    2. Extract the number preceding the error name.
    3. Map to Priority:
       - 'Internal links are broken' -> Critical
       - '4XX status code' -> Critical
       - 'Duplicate meta descriptions' -> High
       - 'Uncached JavaScript' -> Medium
    """
    pass
```
### Known Issue Patterns (Reference)

**Do not use specific counts.** Use these names to identify rows in the PDF.

| Issue Pattern | Severity |
|---|---|
| `Internal links are broken` | **Critical** |
| `Hreflang conflicts` | **Critical** |
| `Pages returned 4XX status code` | **Critical** |
| `Issue with expiring or expired certificate` | **Critical** |
| `Pages have duplicate meta descriptions` | **High** |
| `Pages have low text-HTML ratio` | **High** |
| `URLs with a temporary redirect` | **High** |
| `Issues with uncached JavaScript and CSS` | **Medium** |
| `Pages have duplicate H1 and title tags` | **Medium** |

---

## Data Quality Checks

| Check | Validation |
|---|---|
| Domain count | ≥ 2 domains in Overview |
| Keyword count | ≥ 50 keywords in Organic |
| Health score | 0-100 range |
| Date freshness | Export within 30 days |