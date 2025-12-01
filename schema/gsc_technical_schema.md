# GSC Technical Schema (Visual)

This document defines the structure for extracting Technical SEO data from Google Search Console screenshots. This schema is a reference for **Visual Extraction** only. **DO NOT use any sample data from this file.**

---

## Part 1: Page Indexing Analysis

**Source:** Screenshot of the "Page indexing" report (Index Status + "Why pages aren't indexed" table).
**Purpose:** Identify crawlability blockers and indexation ratio.

### Extraction Logic (Visual Reference)

**Integration Note:**
* **Index Status** maps to JSON key: `technical_seo.indexation`
* **Crawl Issues** maps to JSON key: `technical_seo.crawl_issues`

**Step 1: Extract Header Metrics**
* **Not Indexed:** Look for the grey box. Extract the large number (e.g., "30.3K").
* **Indexed:** Look for the green box. Extract the large number (e.g., "9.82K").
* **Total Pages:** Calculate `Not Indexed + Indexed`.

**Step 2: Extract "Why pages aren't indexed" Table**
* Scan the table rows below the chart.
* Extract the **Reason** (Column 1) and **Pages** count (Far right column).
* **Priority Rule:**
    * `Server error (5xx)` -> **Critical**
    * `Not found (404)` (if high volume) -> **High**
    * `Soft 404` -> **High**
    * `Blocked by robots.txt` -> **Medium** (Check if intentional)
    * `Redirect error` -> **High**

**Step 3: Calculate Indexation Ratio**
* Formula: `(Indexed / Total Pages) * 100`
* **Interpretation:**
    * < 10%: Critical Crawl Issue
    * 10-50%: Poor Indexation efficiency
    * > 80%: Healthy

---

## Part 2: Schema Markup Analysis

**Source:** Screenshot of "Enhancements" reports (e.g., Breadcrumbs, FAQ, Review Snippets).
**Purpose:** Validate structured data health.

### Extraction Logic (Visual Reference)

**Integration Note:**
* **Schema Data** maps to JSON key: `technical_seo.structured_data`

**Step 1: Extract Status Metrics**
* **Invalid (Red Box):** Extract the large number (Critical Errors).
* **Valid (Green Box):** Extract the large number (Healthy Items).

**Step 2: Identify Trend**
* Look at the Bar Chart.
* **Trend:** Is the Green bar stable, rising, or falling?
* **Drop Detection:** If there is a sudden drop in green bars (like in the Breadcrumbs example), flag as "Schema Implementation Error."

---

## Priority Assignment Rules

| Condition | Priority |
|---|---|
| **Invalid Schema Items > 0** | **C** (Critical) - Rich results are broken. |
| **Server Errors (5xx) > 0** | **C** (Critical) - Site is down for Google. |
| **Indexation Ratio < 20%** | **H** (High) - Most content is invisible. |
| **Sudden Drop in Valid Items** | **H** (High) - Recent code break. |
| **404 Errors > 5% of total** | **M** (Medium) - Clean up dead links. |

---

## Data Quality Checks

| Check | Validation |
|---|---|
| Screenshot Clarity | Text must be legible (OCR possible). |
| Context | Ensure image contains the "Why pages aren't indexed" header for Part 1. |
| Completeness | Ensure both "Invalid" and "Valid" boxes are visible for Part 2. |