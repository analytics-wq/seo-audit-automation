# PageSpeed Insights Schema

This document defines the structure of PageSpeed Insights data used in the SEO Audit Proposal. This schema definition is just a reference & data inside is only an example how to read. **DO NOT use any data from this file** for the actual audit. **ONLY extract data from the user-uploaded Screenshot**.

---

## Extraction Logic (Visual Reference)

**System Note:** Do not look for text numbers in this document. You must perform Optical Character Recognition (OCR) and visual analysis on the provided screenshot to extract the real values.

**Step 1: Identify Data Source (Visual Priority)**
1.  **Scan for Field Data:** Look for the heading "Discover what your real users are experiencing".
    * *IF FOUND:* Extract LCP, INP/FID, and CLS from this section.
    * *IF "No Data Available":* Proceed to Step 2.
2.  **Scan for Lab Data:** Look for the heading "Diagnose performance issues".
    * *ALWAYS:* Extract Performance Score (0-100) from the large circular gauge.
    * *FALLBACK:* Use LCP, TBT, and CLS from this section only if Field Data was empty.

**Step 2: Metric Extraction Rules**
* **Context:** These metrics map to the JSON key `technical_seo.cwv` (Slide 17).
* **Performance Score:** Extract the large integer inside the colored circle (0-100).
* **LCP (Largest Contentful Paint):** Look for "LCP" label. Extract value (e.g., "2.5 s").
* **TBT (Total Blocking Time):** Look for "TBT" label. Extract value (e.g., "600 ms").
* **CLS (Cumulative Layout Shift):** Look for "CLS" label. Extract value (e.g., "0.05").

**Step 3: Color Interpretation**
* **Red (▲ / Triangle):** Critical Issue (Priority: C)
* **Orange (■ / Square):** Needs Improvement (Priority: H)
* **Green (● / Circle):** Good (Priority: L)

**Step 4: Dynamic Message Generation**
* Do NOT use pre-written templates.
* Compare extracted LCP to 2.5s threshold.
* Compare extracted TBT to 200ms threshold.
* *Output Example:* "LCP of [Extracted Value] exceeds 2.5s threshold, delaying main content rendering."

---

## Priority Assignment Rules

**System Note:** Apply these thresholds to the values extracted from the image.

| Condition | Priority |
|-----------|----------|
| Performance < 50 AND any CWV in Poor | **C** |
| Performance < 50 | **H** |
| Performance 50-89 AND any CWV in Poor | **H** |
| Performance 50-89 | **M** |
| Performance ≥ 90 | **L** |

| Metric | Poor (Critical) | Needs Work (High) | Good (Low) |
|--------|-----------------|-------------------|------------|
| LCP | > 4.0s | 2.5-4.0s | ≤ 2.5s |
| TBT | > 600ms | 200-600ms | ≤ 200ms |
| CLS | > 0.25 | 0.1-0.25 | ≤ 0.1 |

---

## Common Issues & Validation

| Check | Validation |
|-------|------------|
| Screenshot clarity | All metrics visible and readable |
| Device tab | Confirm Mobile vs Desktop (Mobile preferred) |
| Complete data | All 5 core metrics present |