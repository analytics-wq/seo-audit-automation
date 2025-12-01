# Google Search Console Schema

This document defines the structure of Google Search Console exports used in the SEO Audit Proposal. This schema definition is just a reference & data inside is only an example how to read. **DO NOT use any data from this file** for the actual audit. **ONLY extract data from the user-uploaded CSV/XLSX/PDF files**.

---

## File Structure

**File Type:** `.xlsx` or `.csv` (Standard GSC Export)
**Sheets:** `Queries`, `Pages`, `Countries`, `Devices`, `Search appearance`, `Dates`.

### Sheet 1: Queries

**Purpose:** Top search queries driving traffic.

| Column | Data Type | Description |
|---|---|---|
| `Top queries` | String | User search term |
| `Clicks` | Integer | Total clicks from SERP |
| `Impressions` | Integer | Total times seen in SERP |
| `CTR` | Float | Click-through rate (0-1) |
| `Position` | Float | Average ranking position |

### Sheet 6: Dates (For Trend Graphs)

**Purpose:** Daily performance trends (Clicks, CTR, Position).

| Column | Data Type | Description |
|---|---|---|
| `Date` | Date | Specific day (YYYY-MM-DD) |
| `Clicks` | Integer | Daily clicks |
| `Impressions` | Integer | Daily impressions |
| `CTR` | Float | Daily CTR |
| `Position` | Float | Daily avg position |

---

## Extraction Logic (Reference)

**Integration Note:**
* **KPI Data** maps to JSON key: `kpi.metrics`
* **Trend Graph Data** maps to JSON key: `kpi.trends`
* **Top Queries** maps to JSON key: `kpi.top_queries`

```python
import pandas as pd

def extract_kpi_metrics(df_dates):
    """
    LOGIC for Slide 24 (KPIs):
    1. Sum 'Clicks' column -> Total Clicks (Last 12 Months).
    2. Sum 'Impressions' column -> Total Impressions.
    3. Calculate Weighted Average CTR: (Total Clicks / Total Impressions) * 100.
    4. Calculate Weighted Average Position: Sum(Position * Impressions) / Total Impressions.
    """
    pass

def generate_trend_graphs(df_dates):
    """
    LOGIC for Trend Graphs (CTR & Position):
    1. Sort data by 'Date' (Ascending).
    2. Extract 'CTR' column series for the Line Chart.
    3. Extract 'Position' column series for the Line Chart (Note: Invert axis for Position, where 1 is top).
    4. Compare first 30 days vs last 30 days to determine Trend Direction (Rising/Falling).
    """
    pass

def classify_brand_vs_nonbrand(df_queries, brand_name):
    """
    LOGIC for Query Analysis:
    1. Filter 'Top queries' containing `brand_name` (string match).
    2. Label as 'Branded'.
    3. Label all others as 'Non-Branded'.
    4. Calculate split of Clicks between Branded vs Non-Branded.
    """
    pass
```
---

## CTR Benchmarks

| Position Range | Expected CTR |
|---|---|
| Position 1 | 25-35% |
| Position 2 | 12-18% |
| Position 3 | 8-12% |
| Positions 4-10 | 2-8% |
| Positions 11-20 | 1-3% |
| Positions 21+ | <1% |

### CTR Priority Assignment

| Condition | Priority |
|---|---|
| CTR < 2% for position 1-3 | **H** (High) – Click-through optimization needed |
| CTR < industry avg (3-5%) | **M** (Medium) – Room for improvement |
| CTR at or above benchmark | **L** (Low) – Healthy performance |

---

## Trend Interpretation Rules

| Trend Pattern | Interpretation |
|---|---|
| **Rising CTR + Stable Position** | "Snippet optimization is working." |
| **Falling CTR + Stable Position** | "Competitive pressure or poor title tags." |
| **Rising Position + Rising Clicks** | "Successful SEO momentum." |
| **Falling Position + Falling Clicks** | "Technical issue or algo penalty." |

---

## Position Interpretation

| Avg Position | Interpretation | Action |
|---|---|---|
| 1-3 | Strong rankings | Maintain, defend |
| 4-10 | Page 1 | Optimize for top 3 |
| 11-20 | Striking distance | Quick-win opportunity |
| 21-50 | Page 2-5 | Content/authority improvement needed |
| 50+ | Low visibility | Major optimization required |

---

## Data Quality Checks

| Check | Validation |
|---|---|
| Date range | Ensure full 12 months (or max available) |
| Total clicks | > 0 (otherwise no search traffic) |
| Search type | Must be 'Web' (not Image, Video, etc.) |

---

## Common Issues

| Issue | Resolution |
|---|---|
| No data | Property not verified or no traffic |
| Very high position (50+) | Low visibility — prioritize as issue |
| CTR shows as decimal | Multiply by 100 for percentage display |
| Missing dates | Incomplete export — request full range |
| Search type = Image | Re-export with Web filter |
