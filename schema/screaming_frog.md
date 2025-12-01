# Screaming Frog Schema

This document defines the structure of Screaming Frog exports used in the SEO Audit Proposal. This schema definition is just a reference & data inside is only an example how to read. **DO NOT use any data from this file** for the actual audit. **ONLY extract data from the user-uploaded CSV/XLSX files**.

---

## File Structure

**Sheet Name:** `Website Issue` (or `Internal` if using custom export)
**Purpose:** Complete list of technical issues discovered during site crawl.

---

| Column | Header | Data Type | Description |
|--------|--------|-----------|-------------|
| 0 | `Issue Name` | String | Description (e.g., "H2: Duplicate") |
| 1 | `Issue Type` | Enum | "Issue", "Warning", "Opportunity" |
| 2 | `Issue Priority` | Enum | "High", "Medium", "Low" |
| 3 | `URLs` | Integer | Count of affected pages |
| 4 | `% of Total` | Float | Percentage of site affected |

---

## Extraction Logic (Reference)

**System Note:** Use the logic below to filter and categorize issues. Do not use static sample numbers.

**Integration Note:**
* **Meta Tag Data** maps to JSON key: `meta_tags.issues`
* **Technical Data** maps to JSON key: `technical_seo.issues`
* **Health Summary** maps to JSON key: `site_health`

```python
import pandas as pd

def extract_meta_tag_issues(df):
    """
    LOGIC for Slide 13 (Content Visibility):
    1. Filter 'Issue Name' column for strings strictly starting with:
       - 'Page Titles:'
       - 'Meta Description:'
       - 'H1:'
       - 'H2:'
    2. Sort by 'Issue Priority' (High > Medium > Low).
    3. Return the Issue Name and URL Count for the top issues.
    """
    pass

def extract_technical_issues(df):
    """
    LOGIC for Slide 17 (Technical Gaps):
    1. Filter 'Issue Name' column to EXCLUDE the meta tag prefixes above.
    2. Include categories like: 'Security:', 'Canonicals:', 'Response Codes:', 
       'Links:', 'Images:', 'URL:', 'Content:'.
    3. Sort by 'Issue Priority' (High > Medium > Low), then by 'URLs' (Descending).
    4. Return top 10-15 issues.
    """
    pass

def extract_site_health_summary(df):
    """
    LOGIC for Slide 10 (Site Health):
    1. Calculate total 'URLs' count for High Priority issues (Critical).
    2. Calculate total 'URLs' count for Medium Priority issues (High/Medium).
    3. Identify the Top 3 Critical Issues by volume.
    """
    pass
```

### Columns

| Column | Header | Data Type | Description |
|--------|--------|-----------|-------------|
| 0 | `Issue Name` | String | Description of the issue (e.g., "H2: Duplicate") |
| 1 | `Issue Type` | Enum | Category of issue ("Opportunity", "Warning", "Issue") |
| 2 | `Issue Priority` | Enum | Severity level ("Low", "Medium", "High") |
| 3 | `URLs` | Integer | Number of affected URLs |
| 4 | `% of Total` | Float | Percentage of crawled pages |

### Issue Type Definitions

| Type | Description | Severity |
|------|-------------|----------|
| `Issue` | Critical problems requiring immediate fix | Highest |
| `Warning` | Potential problems to review | Medium |
| `Opportunity` | Optimization suggestions | Lowest |

### Issue Priority Definitions

| Priority | Description | Action |
|----------|-------------|--------|
| `High` | Critical issues affecting crawlability/indexation | Fix immediately |
| `Medium` | Important issues affecting performance | Fix within 30 days |
| `Low` | Minor issues or optimization opportunities | Fix when possible |
---
## Priority Mapping to Slide Format

Map Screaming Frog to deck priority codes:

| SF Priority | SF Type | Slide Priority |
|-------------|---------|----------------|
| High | Issue | **C** (Critical) |
| High | Warning | **H** |
| Medium | Issue | **H** |
| Medium | Warning | **M** |
| Medium | Opportunity | **M** |
| Low | Issue | **M** |
| Low | Warning | **L** |
| Low | Opportunity | **L** |

### Volume-Based Priority Adjustment

| Condition | Adjustment |
|-----------|------------|
| URLs > 100 | Upgrade one level |
| URLs > 50% of site | Upgrade to **C** |
| URLs < 5 | Downgrade one level |

---

## Slide Mapping Summary

| Slide | Section | Filter | Limit |
|-------|---------|--------|-------|
| 10 | Critical Issues table | Priority = High | Top 8 by URLs |
| 10 | High Priority table | Priority = Medium | Top 8 by URLs |
| 13 | Title Issues | Issue Name starts with `Page Titles:` | All |
| 13 | Meta Description Issues | Issue Name starts with `Meta Description:` | All |
| 13 | H1 Issues | Issue Name starts with `H1:` | All |
| 17 | Technical Issues table | Exclude meta prefixes, sort by priority | Top 10-15 |

---

## Key Issue Interpretations

### High Priority Issues to Highlight

| Issue | Business Impact |
|-------|-----------------|
| Canonicals: Canonicalised | Pages may be excluded from index |
| Links: Pages Without Internal Outlinks | Orphan pages — poor crawlability |
| H1: Missing | Poor on-page SEO signals |
| Canonicals: Missing | Duplicate content risk |
| Images: Over 100 KB | Page speed impact |
| Content: Low Content Pages | Thin content penalty risk |

### Issues to Monitor (Medium)

| Issue | Business Impact |
|-------|-----------------|
| Page Titles: Over 60 Characters | Truncation in SERPs |
| Page Titles: Below 30 Characters | Underoptimized titles |
| Security headers missing | Trust/security signals |

### Lower Priority (Low)

| Issue | Business Impact |
|-------|-----------------|
| H2: Duplicate | Minor SEO signal |
| URL: Uppercase | URL hygiene |
| Alt text issues | Accessibility + image SEO |

---

## Data Quality Checks

| Check | Validation |
|-------|------------|
| Row count | > 0 issues (empty = crawl may have failed) |
| URL count | Sum > 0 |
| Priority coverage | Mix of High/Medium/Low expected |
| Type coverage | Mix of Issue/Warning/Opportunity expected |

---

## Common Issues

| Issue | Resolution |
|-------|------------|
| `% of Total` > 100 | Known SF bug — ignore percentage, use URL count |
| Empty export | Crawl may have failed — verify with user |
| All Low priority | Site may be healthy — note positive finding |
| Issue Category sheet empty | Normal — SF doesn't always populate this |

---

## Relationship with SEMrush Site Audit

| Use Case | Primary Source | Fallback |
|----------|----------------|----------|
| Site Health Score | SEMrush Site Audit | Not available in SF |
| Pages Crawled | SEMrush Site Audit | SF crawl count |
| Error/Warning counts | SEMrush Site Audit | SF Issue Type counts |
| Meta Tag Issues | Screaming Frog | SEMrush Site Audit |
| Detailed issue list | Screaming Frog | SEMrush Site Audit |

**Best Practice:** Use SEMrush Site Audit for Site Health Score and high-level metrics; use Screaming Frog for detailed meta tag analysis and technical issue breakdown.
