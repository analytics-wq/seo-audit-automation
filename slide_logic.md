# Slide Logic

This document defines the analytical framework for each slide in the SEO Audit Proposal template. Every slide must answer a business question, not just display data.

---

## Core Principles

### Narrative Logic
Every insight must follow this chain:
```
DATA → PROBLEM → BUSINESS CONSEQUENCE → ACTION
```

### Deck Storytelling Arc

The 26-slide deck tells one story in six chapters:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ CHAPTER 1: SETUP (Slides 1-4)                                               │
│ "Here's what we're doing and why"                                           │
│ → Establishes context, no analysis required                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHAPTER 2: EXECUTIVE SUMMARY (Slide 5)                                      │
│ "Here's the headline — read this if nothing else"                           │
│ → Generated LAST, synthesizes all findings                                  │
│ → Feeds: Final recommendation to stakeholders                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHAPTER 3: WHERE YOU STAND (Slides 6-11)                                    │
│ "Here's your current position — the 'before' picture"                       │
│ → Establishes baseline: traffic, competitors, engagement, health            │
│ → Feeds: Executive Summary (General Overview column)                        │
│ → Narrative tension: "You're here, but gaps exist"                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHAPTER 4: CONTENT GAPS (Slides 12-16)                                      │
│ "Here's what you're missing — the content opportunity"                      │
│ → Identifies: meta issues, keyword gaps, intent misalignment                │
│ → Feeds: Executive Summary (Content SEO column)                             │
│ → Narrative tension: "Competitors are capturing this demand"                │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHAPTER 5: TECHNICAL GAPS (Slides 17-19)                                    │
│ "Here's what's blocking you — the technical debt"                           │
│ → Identifies: crawl/index issues, speed, structured data                    │
│ → Feeds: Executive Summary (Technical SEO column)                           │
│ → Narrative tension: "Even good content can't rank with these issues"       │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHAPTER 6: AUTHORITY (Slides 20-22)                                         │
│ "Here's your competitive weight — the trust factor"                         │
│ → Identifies: backlink profile, DR trend, toxic links                       │
│ → Feeds: Executive Summary (Domain Authority column)                        │
│ → Narrative tension: "Authority limits what you can compete for"            │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHAPTER 7: PATH FORWARD (Slides 23-26)                                      │
│ "Here's what to do — the action plan"                                       │
│ → Consolidates all findings into prioritized recommendations                │
│ → Sets KPIs and expectations                                                │
│ → Narrative resolution: "Fix these, achieve this"                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

### How Slides Feed the Executive Summary

```
Slide 7  (Organic Traffic)     ──┐
Slide 8  (Competitive)         ──┼──→ Slide 11 Summary ──→ Slide 5: General Overview
Slide 9  (Engagement)          ──┤
Slide 10 (Site Health)         ──┘

Slide 13 (Meta Tags)           ──┐
Slide 14 (Keyword Gap +        ──┼──→ Slide 15 Summary ──→ Slide 5: Content SEO
          Intent Distribution) ──┘

Slide 17 (Technical Issues)    ──────→ Slide 18 Summary ──→ Slide 5: Technical SEO

Slide 20 (Domain Authority)    ──────→ Slide 21 Summary ──→ Slide 5: Domain Authority

All Section Summaries ─────────────────────────────────→ Slide 23: Findings Summary
                                                       → Slide 24: KPIs
```

### Unified Key Message Formula

Every data slide must produce a **single-sentence conclusion** that captures three elements:

```
[Insight] + [Significance] + [Business Consequence]
```

**Structure:**
> "{What's happening} {but/which/leaving} {why it matters to the business}."

**Examples:**

| Slide | Unified Key Message |
|-------|---------------------|
| Organic Traffic | "Organic search is stable but limited by underperforming mid-position keywords, leaving significant non-branded demand uncaptured." |
| Competitive | "Domain authority trails competitors by 15 points, which restricts ranking potential for high-volume commercial terms." |
| Engagement | "Engagement rate declined 12% despite traffic growth, indicating content-intent mismatch that erodes conversion potential." |
| Site Health | "Site health score of 67% reflects 1,200 crawl errors, causing Googlebot to waste budget on broken pages instead of indexable content." |
| Keyword Gap | "Competitors rank for 8K keywords {Brand} doesn't target, representing 45K monthly searches flowing to alternatives." |
| Domain Authority | "Referring domains have stagnated while competitors grew 20%, widening the authority gap that limits SERP competitiveness." |

**Writing Rules:**
- Must be one sentence (no periods mid-sentence)
- Must include a transition word (but, which, leaving, causing, indicating)
- Must end with business consequence, not technical observation
- Max 30 words

---

### Cross-Slide Consistency Rules

All insights must reinforce a single narrative. No slide may contradict a previous slide.

**Core Principle:**
```
Every slide builds on the previous. The story tightens, not scatters.
```

**Cause-and-Effect Relationships:**

These relationships MUST be consistent across slides:

| Cause (Earlier Slide) | Effect (Later Slide) | Consistency Check |
|-----------------------|----------------------|-------------------|
| Low authority (Slide 8, 21) | Weak rankings for competitive terms (Slide 14, 15) | If DR is low, keyword gap should show high-difficulty terms as unreachable |
| Technical issues (Slide 10, 18) | Indexing/traffic problems (Slide 7) | If pages aren't indexed, traffic slide should reflect limited organic reach |
| Content gaps (Slide 13, 14) | Engagement issues (Slide 9) | If content is thin/misaligned, engagement should show low time-on-site |
| Keyword gap (Slide 14) | Traffic gap vs competitors (Slide 8) | Missing keywords should correlate with traffic differential |

**Conflict Resolution:**

If a conflict is detected between slides:
1. Identify which insight is more data-backed (larger sample, more recent data)
2. Prioritize the data-backed insight
3. Harmonize wording in the weaker slide to align
4. Never contradict — reframe as nuance if needed

**Example Conflict:**
- Slide 7 says: "Organic traffic is growing 15% YoY"
- Slide 9 says: "Engagement is declining, suggesting traffic quality issues"

**Resolution:** Both can be true. Harmonize:
- Slide 7: "Organic traffic is growing 15% YoY, though quality metrics warrant attention."
- Slide 9: "Despite traffic growth, engagement rate declined 12%, indicating volume gains may not convert."

**Pre-Output Validation Checklist:**

Before generating final output, cross-check these relationships:

| Check | Validation |
|-------|------------|
| Keyword gap ↔ Traffic analysis | Does the keyword gap size explain the traffic differential vs competitors? |
| Authority gap ↔ Competitive benchmarking | Does lower DR correlate with weaker rankings on high-difficulty terms? |
| Technical issues ↔ Site health | Do technical issues in Slide 18 align with health score in Slide 10? |
| Engagement trends ↔ Content findings | Does content quality (Slide 13-15) explain engagement patterns (Slide 9)? |
| Section summaries ↔ Executive summary | Does Slide 5 ONLY contain insights from Slides 11, 16, 19, 22? |

**Executive Summary Rule (Slide 5):**
```
⚠️ STRICT RULE: Slide 5 must ONLY pull from Slides 11, 16, 19, 22.
   No new insights may appear in the Executive Summary.
   No data or conclusions that weren't established in section summaries.
```

---

### Business Interpretation Rules

| Technical Finding | Business Translation |
|-------------------|---------------------|
| Indexing issues | Missed market demand — Google can't serve pages to searchers |
| Weak content signals | Lost ranking opportunities — competitors win the click |
| Poor domain authority | Inability to compete in SERPs — even good content won't rank |
| Low CTR | Leakage in conversion — demand exists but traffic doesn't follow |
| Slow page speed | Abandoned visits — users leave before engaging |
| Cannibalization | Diluted authority — you compete against yourself |

### Website-Type Variations

| Type | Primary Focus | Key Metrics | Business Frame |
|------|---------------|-------------|----------------|
| **Ecommerce** | Product discoverability, category architecture, PDP depth | Revenue per session, product page rankings, category visibility | "Unseen products = unsold inventory" |
| **SaaS** | BOFU intent, trust signals, solution awareness | Demo/trial conversions, branded vs non-branded ratio, competitor gap | "Weak authority = lost deals to competitors" |
| **Content/Publisher** | Content freshness, topical clustering, engagement | Pageviews, time on site, returning visitors | "Stale content = declining audience" |
| **Local Business** | GMB optimization, local pack, NAP consistency | Local pack appearances, "near me" rankings, GMB actions | "Invisible locally = foot traffic to competitors" |
| **Marketplace** | Taxonomy coherence, internal linking, seller/product pages | Category rankings, long-tail coverage, crawl efficiency | "Poor structure = buried listings" |

---

## Data Source Reference

All data sources map to schema files in `/schemas/`. Use this table for consistent field lookups.

| Tool | Schema File | Primary Use Cases |
|------|-------------|-------------------|
| Google Analytics 4 | `schemas/ga4_schema.md` | Traffic, engagement, channels, geography |
| Google Search Console | `schemas/gsc_schema.md` | Impressions, clicks, CTR, position, queries |
| SEMrush | `schemas/semrush_schema.md` | Keywords, competitors, site audit, backlinks |
| Ahrefs | `schemas/ahrefs_schema.md` | Domain rating, backlinks, keyword gap |
| Screaming Frog | `schemas/screaming_frog_schema.md` | Technical crawl, meta tags, status codes |

When slide logic references a field like `GA4: sessions`, look up the exact column name in `schemas/ga4_schema.md`.

---

## Slide-by-Slide Analysis Framework

---

### Slide 1: Cover
**Type:** Static
**Purpose:** Brand identification — first impression, sets professional tone
**Narrative Role:** None (visual only)

**Placeholders:**
| Placeholder | Source |
|-------------|--------|
| `{Brand}` | User input |
| `{Current month}` | System date |
| `{Logo}` | User upload |

**Analysis Required:** None

---

### Slide 2: SEO Audit Overview
**Type:** Setup
**Purpose:** Frame the audit scope — tells client what they're getting and how we got it
**Narrative Role:** Establishes credibility and methodology

**Placeholders:**
| Placeholder | Source | Notes |
|-------------|--------|-------|
| `{Brand}` | User input | |
| `{dd/mm/yyyy - dd/mm/yyyy}` | Calculated from data | Default: trailing 12 months |
| Tools list | Auto-detected | Based on uploaded files |

**Data Sources:**
| What to Detect | How |
|----------------|-----|
| Date range | Min/max dates across all uploaded datasets |
| Tools used | File type detection (SEMrush CSV headers, GA4 export format, etc.) |

**Analysis Required:**
- Calculate date range from uploaded data
- Detect which tools are present
- Flag if date range < 6 months (warn: trend analysis limited)

---

### Slide 3: Planning Phase
**Type:** Static
**Purpose:** Position audit within service lifecycle
**Narrative Role:** Sets expectation — this is research, not implementation

**Analysis Required:** None

---

### Slide 4: Index
**Type:** Navigation
**Purpose:** Outline deck structure
**Narrative Role:** Roadmap for the reader

**Analysis Required:** None

---

### Slide 5: Path to Digital Visibility (Executive Summary)
**Type:** Executive Summary
**Purpose:** 30-second snapshot of SEO health across all pillars — the slide executives read if they read nothing else
**Narrative Role:** **CONCLUSION** — this is where all insights converge

**⚠️ Generate this slide LAST — it requires outputs from all section summaries.**

**Layout:** 4 columns

| Column | Placeholder | Feeds From |
|--------|-------------|------------|
| General Overview | `{Summary overall SEO Audit}` | Slide 11 (highest-priority finding) |
| Content SEO | `{Summary of Current Content SEO structure}` | Slide 16 (highest-priority finding) |
| Technical SEO | `{Summary of Current Technical SEO}` | Slide 19 (highest-priority finding) |
| Domain Authority | `{Interpretation of Domain Authority}` | Slide 22 (highest-priority finding) |

**Data Sources:**
| Input | Source |
|-------|--------|
| Organic Traffic Summary | Slide 11: `{Summary Organic Traffic Key Highlight}` |
| Content Summary | Slide 16: `{Summary Content Issue Key Highlight}` |
| Technical Summary | Slide 19: `{Summary Technical Issue Key Highlight}` |
| Authority Summary | Slide 22: `{Summary Domain Authority Key Highlight}` |

**Analytical Questions:**
1. What is the single biggest barrier to organic growth?
2. Is this a content problem, technical problem, or authority problem?
3. What would a competitor exploit first?
4. What's the one thing the client should remember from this audit?

**Synthesis Logic:**
1. Pull the highest-priority issue from each section summary
2. Identify the dominant theme (e.g., "technical debt is blocking otherwise good content")
3. Frame as a unified narrative, not four separate bullets

---

### Slide 6: Section Divider — "Where {Brand} Stands Today?"
**Type:** Divider
**Purpose:** Transition to performance baseline section
**Narrative Role:** Opens Chapter 3 — "Let's establish where you are"

**Analysis Required:** None

---

### Slide 7: Organic Traffic Analysis
**Type:** Data Slide
**Section:** §2 Where {Brand} Stands Today?
**Purpose:** Establish traffic baseline — how much organic traffic, from where, for what keywords
**Narrative Role:** The "before" picture — sets the baseline all improvements are measured against

**Feeds Into:**
- Slide 11 (Section Summary) → Slide 5 (Executive Summary: General Overview)

**Data Sources:**
| Metric | Schema Reference | Fallback |
|--------|------------------|----------|
| Organic vs Other Channels | `ga4_schema.md` → `sessionDefaultChannelGroup`, `sessions` | `semrush_schema.md` → `Traffic Analytics` |
| Top Countries by Sessions | `ga4_schema.md` → `country`, `sessions` | `gsc_schema.md` → `country` |
| Keyword Position Distribution | `semrush_schema.md` → `Position`, `Search Volume` | `ahrefs_schema.md` → `Position` |

**Analytical Questions:**
1. Is organic the dominant channel? If not, why? (Paid dependency = margin risk)
2. Is traffic geographically aligned with business targets?
3. What % of keywords are on page 1 vs page 2 vs page 3+?
4. Is organic traffic growing, flat, or declining YoY?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| Organic < 30% of total traffic | **C** | Paid dependency creates margin risk |
| Organic declining >15% YoY | **H** | Market share erosion |
| >50% keywords on page 2+ | **H** | Competitors capture demand |
| Traffic stable, minor gaps | **M** | Optimization opportunity |
| Organic dominant, growing | **L** | Healthy baseline |

**Website-Type Variations:**
| Type | Adjust Analysis To |
|------|--------------------|
| **Ecommerce** | Emphasize product/category page traffic share |
| **SaaS** | Separate branded vs non-branded traffic |
| **Local** | Highlight local market traffic concentration |

**Unified Key Message:**
Generate one sentence following this pattern:
> "Organic search is [status] but [limitation], leaving [business consequence]."

Examples:
- "Organic search is stable but limited by underperforming mid-position keywords, leaving significant non-branded demand uncaptured."
- "Organic traffic declined 18% YoY while paid dependency grew, exposing margin risk if ad costs increase."
- "Organic dominates at 65% of traffic but concentrates in one market, leaving international demand untapped."

---

### Slide 8: Competitive Benchmarking
**Type:** Data Slide
**Section:** §2 Where {Brand} Stands Today?
**Purpose:** Position {Brand} against competitors — where do you rank in the competitive set?
**Narrative Role:** The "comparison" — creates urgency by showing what competitors have

**Feeds Into:**
- Slide 11 (Section Summary) → Slide 5 (Executive Summary: General Overview)

**Table Structure:**
```
| Metrics              | {Brand} | Comp 1 | Comp 2 | Comp 3 | Comp 4 | Comp 5 |
|----------------------|---------|--------|--------|--------|--------|--------|
| Domain Rating        |         |        |        |        |        |        |
| Monthly Traffic      |         |        |        |        |        |        |
| Total Keywords       |         |        |        |        |        |        |
| Page 1 Keywords      |         |        |        |        |        |        |
| Referring Domains    |         |        |        |        |        |        |
```

**Metric Definitions (from template):**
| Metric | Definition |
|--------|------------|
| Domain Rating | Domain & page authority on 100 point scale, used to compare websites or track the "ranking strength" of a website over time |
| Monthly Traffic | Monthly Organic Session — organic session website visits per month |
| Total Keywords | Total keywords in website that drive organic traffic |
| Page 1 Keywords | Total ranking in page 1 keywords in website that drive organic traffic |
| Referring Domains | Total incoming links from other websites direct to our websites |

**Data Sources:**
| Metric | Schema Reference | Fallback |
|--------|------------------|----------|
| Domain Rating (DR) | `ahrefs_schema.md` → `Domain Rating` | `semrush_schema.md` → `Authority Score` |
| Monthly Traffic | `semrush_schema.md` → `Organic Traffic` | `ahrefs_schema.md` → `Organic Traffic` |
| Total Keywords | `semrush_schema.md` → `Organic Keywords` | `ahrefs_schema.md` → `Organic Keywords` |
| Page 1 Keywords | `semrush_schema.md` → `Keywords` (filter Position 1-10) | `ahrefs_schema.md` → `Organic Keywords` (filter Position 1-10) |
| Referring Domains | `ahrefs_schema.md` → `Referring Domains` | `semrush_schema.md` → `Referring Domains` |

**Competitor Selection Logic:**
1. Identify 5-6 competitors from client input or SEMrush/Ahrefs competitor analysis
2. Include direct business competitors (same products/services)
3. Include SEO competitors (ranking for same keywords, may differ from business competitors)
4. Prioritize competitors ranking higher than {Brand} for target keywords

**Analytical Questions:**
1. Where does {Brand} rank among competitors on each metric?
2. What's the biggest gap? (DR? Traffic? Keywords? Page 1 Keywords? Referring Domains?)
3. Which competitor is the most dangerous (closest + growing fastest)?
4. Is the gap closing or widening over time?
5. What's the ratio of Page 1 Keywords to Total Keywords for {Brand} vs competitors?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| {Brand} ranks last on 3+ metrics | **C** | Severely disadvantaged |
| {Brand} has <50% of leader's traffic | **H** | Significant market share gap |
| {Brand} has <50% of leader's Page 1 Keywords | **H** | Visibility gap on valuable terms |
| {Brand} competitive but trailing on authority | **M** | Authority is the constraint |
| {Brand} leads or ties on most metrics | **L** | Defensive position |

**Website-Type Variations:**
| Type | Adjust Analysis To |
|------|--------------------|
| **Ecommerce** | Compare product page depth and category coverage |
| **SaaS** | Highlight BOFU keyword gaps ("alternative to X", "X vs Y") |
| **Local** | Compare GMB metrics and local pack appearances |

**Unified Key Message:**
Generate one sentence following this pattern:
> "{Brand} [competitive position] competitors on [metric], which [business consequence]."

Examples:
- "Domain authority trails competitors by 15 points, which restricts ranking potential for high-volume commercial terms."
- "{Brand} leads on content volume but lags on referring domains, indicating authority is the growth constraint."
- "Competitors capture 3x more organic traffic despite similar keyword counts, suggesting content quality or authority gaps."
- "Only 15% of {Brand}'s keywords rank on Page 1 versus competitors averaging 35%, leaving significant traffic on the table."

---

### Slide 9: User Engagement
**Type:** Data Slide
**Section:** §2 Where {Brand} Stands Today?
**Purpose:** Assess traffic quality — is the traffic actually valuable, or just volume?
**Narrative Role:** The "quality check" — traffic means nothing if users don't engage

**Feeds Into:**
- Slide 11 (Section Summary) → Slide 5 (Executive Summary: General Overview)

**Data Sources:**
| Metric | Schema Reference |
|--------|------------------|
| Engagement Rate | `ga4_schema.md` → `engagementRate` |
| Engaged Sessions | `ga4_schema.md` → `engagedSessions` |
| Avg Engagement Time | `ga4_schema.md` → `averageSessionDuration` |
| Period Comparison | `ga4_schema.md` → `date` (filter by range) |

**Analytical Questions:**
1. Is engagement rate improving, stable, or declining?
2. Is engagement time sufficient for conversion? (Benchmark: >1min for most sites)
3. Are engaged sessions growing proportionally to total sessions?
4. Is traffic quality eroding even as volume grows?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| Engagement rate dropped >10% | **H** | Traffic quality eroding |
| Avg engagement time <30s | **H** | Content-intent mismatch |
| Engagement stable but below benchmark | **M** | Optimization opportunity |
| Engagement rate >50% and stable/growing | **L** | Quality traffic |

**Website-Type Variations:**
| Type | Adjust Analysis To |
|------|--------------------|
| **Ecommerce** | Compare engagement on product vs category pages |
| **SaaS** | Focus on demo/pricing page engagement |
| **Content** | Emphasize scroll depth and time on page |

**Unified Key Message:**
Generate one sentence following this pattern:
> "Engagement [trend] despite [context], indicating [business consequence]."

Examples:
- "Engagement rate declined 12% despite traffic growth, indicating content-intent mismatch that erodes conversion potential."
- "Average session duration of 25 seconds suggests visitors aren't finding value, limiting downstream conversion."
- "Engagement rate exceeds benchmark at 62%, confirming traffic quality supports conversion goals."

---

### Slide 10: Site Health
**Type:** Data Slide
**Section:** §2 Where {Brand} Stands Today?
**Purpose:** Quantify technical debt — what's the crawl/index efficiency?
**Narrative Role:** The "foundation check" — reveals hidden barriers before content analysis

**Feeds Into:**
- Slide 11 (Section Summary) → Slide 5 (Executive Summary: General Overview)
- Also previews Chapter 5 (Technical Gaps)

**Data Sources:**
| Metric | Schema Reference | Fallback |
|--------|------------------|----------|
| Site Health Score | `semrush_schema.md` → `Health Score` | `ahrefs_schema.md` → `Health Score` |
| Pages Crawled | `semrush_schema.md` → `Pages Crawled` | `screaming_frog_schema.md` → row count |
| Total Errors | `semrush_schema.md` → `Errors` | `screaming_frog_schema.md` → filter by issue |
| Critical Issues | `semrush_schema.md` → `Errors` (by type) | `screaming_frog_schema.md` → `Issue Type` |
| High Priority Issues | `semrush_schema.md` → `Warnings` | `screaming_frog_schema.md` → `Issue Type` |

**Analytical Questions:**
1. What % of crawled pages have errors?
2. Which issues affect the most URLs?
3. Are critical issues blocking indexing or rendering?
4. Is technical debt concentrated on high-value pages?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| Health Score <60% | **C** | Fundamental crawl/index problems |
| Health Score 60-75% | **H** | Significant technical debt |
| Health Score 75-85% | **M** | Maintenance issues |
| Health Score >85% | **L** | Clean foundation |

**Website-Type Variations:**
| Type | Adjust Analysis To |
|------|--------------------|
| **Ecommerce** | Emphasize product page indexability, faceted navigation |
| **SaaS** | Focus on JavaScript rendering, core landing pages |
| **Large sites** | Emphasize crawl budget efficiency |

**Unified Key Message:**
Generate one sentence following this pattern:
> "Site health score of [X]% reflects [primary issue], causing [business consequence]."

Examples:
- "Site health score of 67% reflects 1,200 crawl errors, causing Googlebot to waste budget on broken pages instead of indexable content."
- "Critical indexing issues affect 15% of product pages, rendering recent content investments invisible to search."
- "Technical foundation is strong at 89% health, allowing focus to shift to content and authority gaps."

---

### Slide 11: Summary — Where {Brand} Stands Today?
**Type:** Section Summary
**Purpose:** Synthesize §2 findings into three actionable takeaways
**Narrative Role:** Chapter 3 conclusion — "This is what the baseline tells us"

**Feeds Into:**
- Slide 5 (Executive Summary: General Overview column)
- Slide 24 (Findings Summary)

**Layout:** 3-box format

| Box | Placeholder | Content |
|-----|-------------|---------|
| What is the Issue? | `{Issue 1-3}` | Top 3 findings from slides 7-10 |
| What is the Impact? | `{Impact 1-3}` | Business consequence of each |
| Our Next Action | `{Next Action 1-3}` | Recommended fix for each |

**Data Sources:**
| Input | Source |
|-------|--------|
| Issue candidates | Slides 7-10: highest-priority findings |
| Priority ranking | Badge from each slide (C > H > M > L) |

**Analytical Questions:**
1. What are the top 3 issues by business impact (not volume)?
2. How do these issues connect? (e.g., low authority → weak rankings → low traffic)
3. What's the logical sequence of fixes?

**Aggregation Logic:**
1. Collect the key finding from each slide (7, 8, 9, 10)
2. Rank by priority badge
3. Select top 3
4. For each: write Issue → Impact → Action

---

### Slide 12: Section Divider — "Content Visibility Gaps & Insights"
**Type:** Divider
**Purpose:** Transition to content analysis
**Narrative Role:** Opens Chapter 4 — "Now let's look at what you're missing"

**Analysis Required:** None

---

### Slide 13: Meta Tags & Heading
**Type:** Data Slide
**Section:** §3 Content Visibility Gaps
**Purpose:** Identify on-page optimization gaps — are pages properly signaling their content?
**Narrative Role:** The "signals check" — Google needs clear signals to rank pages correctly

**Feeds Into:**
- Slide 16 (Section Summary) → Slide 5 (Executive Summary: Content SEO)

**Data Sources:**
| Metric | Schema Reference | Fallback |
|--------|------------------|----------|
| Missing/Duplicate Titles | `semrush_schema.md` → `Issue Type: Title` | `screaming_frog_schema.md` → `Title 1` |
| Missing/Duplicate Descriptions | `semrush_schema.md` → `Issue Type: Meta Description` | `screaming_frog_schema.md` → `Meta Description 1` |
| H1 Issues | `semrush_schema.md` → `Issue Type: H1` | `screaming_frog_schema.md` → `H1-1` |
| Thin Content | `semrush_schema.md` → `Issue Type: Low Word Count` | `screaming_frog_schema.md` → `Word Count` |

**Analytical Questions:**
1. What % of pages have missing/duplicate titles?
2. Are high-traffic pages affected?
3. Is there a pattern? (e.g., all product pages missing descriptions)
4. What's the estimated ranking impact?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| >20% pages with title issues | **C** | Major ranking signal loss |
| >30% pages missing meta descriptions | **H** | CTR suppression |
| H1 issues on key landing pages | **H** | Topical confusion |
| Minor issues on low-traffic pages | **M** | Maintenance task |
| <5% affected | **L** | Clean on-page foundation |

**Website-Type Variations:**
| Type | Adjust Analysis To |
|------|--------------------|
| **Ecommerce** | Focus on product and category page titles |
| **SaaS** | Ensure feature/solution pages have unique titles |
| **Content** | Check article H1/title alignment with target keywords |

**Unified Key Message:**
Generate one sentence following this pattern:
> "[X pages/% of site] have [meta issue], which [ranking/visibility consequence]."

Examples:
- "420 pages have duplicate titles, which prevents Google from differentiating them in search results and dilutes ranking signals."
- "35% of product pages lack meta descriptions, leaving snippet generation to Google and reducing click-through control."
- "H1 structure is clean across the site, confirming on-page signals are not limiting visibility."

---

### Slide 14: Keyword Gap & Content Opportunity
**Type:** Data Slide
**Section:** §3 Content Visibility Gaps
**Purpose:** Identify keyword opportunities and analyze keyword portfolio by category and intent
**Narrative Role:** The "opportunity" — shows what's being left on the table and how keywords are distributed

**Feeds Into:**
- Slide 16 (Section Summary) → Slide 5 (Executive Summary: Content SEO)

**Slide Layout:**
```
┌────────────────────────────┬────────────────────────────────────────────────┐
│  Keyword Distribution      │           Keyword Category Breakdown           │
│       by Intent            │                                                │
│      (Pie Chart)           │  Category     | %    | Volume | Examples       │
│                            │  ──────────────────────────────────────────    │
│   ┌─────────────┐          │  Behavioral   | 70%  | 75K    | "how to...",   │
│   │             │          │               |      |        | "benefits of"   │
│   │   [Pie]     │          │  Device &     | 15%  | 15.5K  | "best X",      │
│   │             │          │  Utility      |      |        | "eco filter"    │
│   └─────────────┘          │  Brand        | 10%  | 12K    | "Brand review" │
│                            │  Location     | 5%   | 5K     | "X UK", "X CA" │
└────────────────────────────┴────────────────────────────────────────────────┘
```

**Keyword Category Breakdown Table:**
| Category | Definition | Examples |
|----------|------------|----------|
| Behavioral | Intent-driven queries about actions, how-tos, benefits | "how to start zero waste," "benefits of bamboo" |
| Device & Utility | Product-focused comparison and utility queries | "best sustainable humidifier," "eco water filter" |
| Brand | Brand-specific queries including reviews and coupons | "{Brand} reviews," "{Brand} coupon" |
| Location | Geo-modified queries for regional targeting | "eco home goods UK," "sustainable decor Canada" |

**Data Sources:**
| Metric | Schema Reference |
|--------|------------------|
| Keyword List | `semrush_schema.md` → `Keyword`, `Position`, `Search Volume` |
| Intent Classification | `semrush_schema.md` → `Intent` |
| Volume by Category | `semrush_schema.md` → `Search Volume` (grouped by category) |
| Competitor Keyword Gap | `semrush_schema.md` → `Keyword Gap: Missing` |

**Category Classification Logic:**
| Category | Classification Signals |
|----------|----------------------|
| **Behavioral** | Contains: "how to", "what is", "why", "benefits of", "ways to", "guide", question words |
| **Device & Utility** | Contains: "best", "top", product types, comparisons, utility terms |
| **Brand** | Contains: brand name, "review", "coupon", "discount", "alternative to {Brand}" |
| **Location** | Contains: country names, city names, "near me", regional modifiers |

**Analytical Questions:**
1. What % of keywords fall into each category?
2. Is the category distribution aligned with business goals?
3. Which category has the highest volume but lowest coverage?
4. What's the gap between {Brand} and competitors in each category?
5. Are high-value Device & Utility keywords being captured?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| Behavioral >80% with weak Device & Utility | **H** | Conversion-stage content gap |
| Brand keywords <5% total | **M** | Brand awareness opportunity |
| Location keywords <10% for local business | **H** | Local visibility gap |
| Gap >5K keywords across categories | **C** | Massive missed demand |
| Balanced distribution with strong coverage | **L** | Healthy content portfolio |

**Website-Type Variations:**
| Type | Expected Category Balance |
|------|--------------------------|
| **Ecommerce** | Device & Utility >30%, Behavioral ~40% |
| **SaaS** | Device & Utility >25%, Behavioral ~50% |
| **Content/Publisher** | Behavioral >60%, monetize via ads |
| **Local Business** | Location >20%, Behavioral ~40% |

**Unified Key Message:**
Generate one sentence following this pattern:
> "[X]% of keyword portfolio is [category], which [alignment/opportunity consequence]."

Examples:
- "70% of rankings are Behavioral terms, which drives awareness but leaves Device & Utility purchase-intent searches to competitors."
- "Device & Utility keywords represent only 15% of portfolio, leaving comparison shoppers to find alternatives."
- "Location keywords at 5% indicate untapped regional demand for international expansion."
- "Keyword category distribution aligns with ecommerce funnel, with 35% Device & Utility terms capturing consideration-stage traffic."

---

### Slide 15: Summary — Content Visibility Gaps
**Type:** Section Summary
**Purpose:** Synthesize §3 findings (Meta Tags + Keyword Gap/Intent)
**Narrative Role:** Chapter 4 conclusion — "This is the content opportunity"

**Feeds Into:**
- Slide 5 (Executive Summary: Content SEO column)
- Slide 23 (Findings Summary)

**Layout:** 3-box format

**Data Sources:**
| Input | Source |
|-------|--------|
| Issue candidates | Slides 13-14: highest-priority findings |
| Priority ranking | Badge from each slide |

**Aggregation Logic:**
1. Pull highest-priority issues from slides 13-14
2. Connect: meta issues → ranking impact → traffic loss
3. Frame as content opportunity, not just problems
4. Include category distribution insights from Slide 14

---

### Slide 16: Section Divider — "Technical Gaps that Limiting Growth"
**Type:** Divider
**Purpose:** Transition to technical analysis
**Narrative Role:** Opens Chapter 5 — "Now let's look at what's blocking you"

**Analysis Required:** None

---

### Slide 17: Technical SEO Issues Overview
**Type:** Data Slide
**Section:** §4 Technical Gaps
**Purpose:** Detail technical issues blocking crawling, indexing, or rendering
**Narrative Role:** The "blocker analysis" — even good content can't rank if Google can't access it

**Feeds Into:**
- Slide 18 (Section Summary) → Slide 5 (Executive Summary: Technical SEO)

**Data Sources:**
| Metric | Schema Reference | Fallback |
|--------|------------------|----------|
| Crawl Errors | `semrush_schema.md` → `Issue Type: Crawlability` | `screaming_frog_schema.md` → `Status Code` |
| Indexing Issues | `gsc_schema.md` → `Coverage Status` | `semrush_schema.md` → `Indexability` |
| Core Web Vitals | `pagespeed_schema.md` → `LCP`, `FID`, `CLS` | Manual input |
| Structured Data Errors | `gsc_schema.md` → `Rich Results` | Manual input |

**Issue Categories:**
| Category | Examples | Impact |
|----------|----------|--------|
| Crawlability | robots.txt blocks, 5xx errors, redirect chains | Google can't find pages |
| Indexability | noindex, canonicalization, duplicates | Google won't show pages |
| Renderability | JavaScript issues, blocked resources | Google sees empty pages |
| Performance | Core Web Vitals, page speed | Ranking suppression |
| Structured Data | Schema errors, missing markup | Lost rich results |

**Analytical Questions:**
1. What issues block Google from crawling or indexing pages?
2. What issues affect Core Web Vitals (ranking factor)?
3. Are issues concentrated on high-value pages?
4. What's the estimated traffic impact?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| Indexing blocked on >10% pages | **C** | Content investment wasted |
| Core Web Vitals failing on key pages | **H** | Ranking suppression |
| Redirect chains >3 hops | **H** | Link equity loss |
| Minor issues on low-value pages | **M** | Maintenance task |
| Clean technical foundation | **L** | No blockers |

**Website-Type Variations:**
| Type | Adjust Analysis To |
|------|--------------------|
| **Ecommerce** | Faceted navigation, pagination, product URLs |
| **SaaS** | JavaScript rendering, single-page app issues |
| **Large sites** | Crawl budget optimization, sitemap hygiene |

**Unified Key Message:**
Generate one sentence following this pattern:
> "[Technical issue category] affects [X pages/%], which [crawl/index/ranking consequence]."

Examples:
- "Indexing issues block 12% of pages from Google, rendering content investments invisible to organic search."
- "Redirect chains averaging 4 hops dilute link equity, preventing authority from flowing to target pages."
- "Core Web Vitals fail on 8 of 10 top landing pages, triggering ranking suppression and user abandonment."

---

### Slide 18: Summary — Technical Gaps
**Type:** Section Summary
**Purpose:** Synthesize §4 findings
**Narrative Role:** Chapter 5 conclusion — "These are the technical blockers"

**Feeds Into:**
- Slide 5 (Executive Summary: Technical SEO column)
- Slide 23 (Findings Summary)

**Layout:** 3-box format

**Data Sources:**
| Input | Source |
|-------|--------|
| Issue candidates | Slide 17: highest-priority findings |

**Aggregation Logic:**
1. Pull highest-priority issues from slide 17
2. Frame as blockers, not just bugs
3. Connect: technical issue → ranking/indexing impact → traffic loss

---

### Slide 19: Section Divider — "Understanding Domain Authority"
**Type:** Divider
**Purpose:** Transition to authority analysis
**Narrative Role:** Opens Chapter 6 — "Now let's look at your competitive weight"

**Analysis Required:** None

---

### Slide 20: Domain Authority
**Type:** Data Slide
**Section:** §5 Understanding Domain Authority
**Purpose:** Assess off-page strength — how much trust does Google place in this domain?
**Narrative Role:** The "weight class" — authority determines what keywords you can compete for

**Feeds Into:**
- Slide 21 (Section Summary) → Slide 5 (Executive Summary: Domain Authority)

**Data Sources:**
| Metric | Schema Reference | Fallback |
|--------|------------------|----------|
| Domain Rating (DR) | `ahrefs_schema.md` → `Domain Rating` | `semrush_schema.md` → `Authority Score` |
| Referring Domains | `ahrefs_schema.md` → `Referring Domains` | `semrush_schema.md` → `Referring Domains` |
| DR Trend | `ahrefs_schema.md` → `DR History` | Compare current vs 6 months ago |
| Backlink Quality | `ahrefs_schema.md` → `Referring Domain DR` | `majestic_schema.md` → `Trust Flow` |
| Toxic Backlinks | `semrush_schema.md` → `Toxic Score` | `ahrefs_schema.md` → `Spam Score` |

**Analytical Questions:**
1. Is domain authority growing, flat, or declining?
2. How does {Brand} compare to competitors?
3. Is backlink growth organic or at-risk (toxic links)?
4. What authority level is needed to compete for target keywords?

**Priority Assignment Rules:**
| Condition | Priority | Business Implication |
|-----------|----------|---------------------|
| DR declining >5 points in 6 months | **C** | Authority erosion |
| DR significantly below competitor average | **H** | Can't compete for target keywords |
| Flat DR, minimal new referring domains | **M** | Stagnation while competitors grow |
| Growing DR, healthy backlink profile | **L** | Competitive position |

**Website-Type Variations:**
| Type | Adjust Analysis To |
|------|--------------------|
| **Ecommerce** | Product review links, supplier/partner links |
| **SaaS** | Editorial links, industry publication mentions |
| **Local** | Local citations, directory presence |

**Unified Key Message:**
Generate one sentence following this pattern:
> "[Authority status/trend] [comparison context], which [competitive consequence]."

Examples:
- "Referring domains have stagnated at 850 while competitors grew 20%, widening the authority gap that limits SERP competitiveness."
- "Domain rating of 45 trails competitor average of 62, which restricts ranking potential for keywords above difficulty 50."
- "Authority is growing steadily with 15 new referring domains monthly, supporting gradual expansion into more competitive terms."

---

### Slide 21: Summary — Domain Authority
**Type:** Section Summary
**Purpose:** Synthesize §5 findings
**Narrative Role:** Chapter 6 conclusion — "This is your competitive weight"

**Feeds Into:**
- Slide 5 (Executive Summary: Domain Authority column)
- Slide 23 (Findings Summary)

**Layout:** 3-box format

**Data Sources:**
| Input | Source |
|-------|--------|
| Issue candidates | Slide 20: key finding |

**Aggregation Logic:**
1. Pull key finding from slide 20
2. Frame as competitive position, not just metric
3. Connect: authority level → keyword competition ability → traffic ceiling

---

### Slide 22: Section Divider — "Steps to Improve your SEO"
**Type:** Divider
**Purpose:** Transition to recommendations
**Narrative Role:** Opens Chapter 7 — "Here's what to do"

**Analysis Required:** None

---

### Slide 23: SEO Audit Findings Summary
**Type:** Action Summary
**Section:** §6 Steps to Improve
**Purpose:** Consolidate all findings into prioritized action plan
**Narrative Role:** The "action plan" — everything converges into clear next steps

**Layout:** 3-column (Technical SEO / Content SEO / Domain Authority)

**Placeholders:**
| Element | Placeholder | Source |
|---------|-------------|--------|
| Header | `{Next Action Key Message}` | Unified theme from all sections |
| Subheader | `{Organic Traffic Issue}` | Primary traffic problem |
| Technical column | Issues + Actions | Slide 18 summary |
| Content column | Issues + Actions | Slide 15 summary |
| Authority column | Issues + Actions | Slide 21 summary |

**Data Sources:**
| Input | Source |
|-------|--------|
| Technical issues/actions | Slide 18: top 3 |
| Content issues/actions | Slide 15: top 3 |
| Authority issues/actions | Slide 21: top 3 |
| Priority badges | From each section summary |

**Analytical Questions:**
1. What's the single most impactful action across all categories?
2. What's the logical sequence? (Usually: Technical → Content → Authority)
3. What can be done in 30/60/90 days?
4. What's the unified theme?

**Aggregation Logic:**
1. Pull top 3 issues from each section summary
2. Rank by priority badge (C > H > M > L)
3. Assign overall column priority
4. Write unified `{Next Action Key Message}` that ties everything together

---

### Slide 24: KPI & Benchmark
**Type:** KPI Slide
**Section:** §6 Steps to Improve
**Purpose:** Set measurable targets and expectations
**Narrative Role:** The "success criteria" — how will we know if it worked?

**Placeholders:**
| Metric | Current Placeholder | Target | Benchmark |
|--------|---------------------|--------|-----------|
| Organic Traffic CTR | `{CTR}` | +1% | 3-5% industry avg |
| Ranking Page Position | `{Average Position}` | 10-50% improvement | — |
| Organic Traffic | `{Current month organic session}` | +15% | — |

**Data Sources:**
| Metric | Schema Reference |
|--------|------------------|
| Current CTR | `gsc_schema.md` → `CTR` |
| Current Avg Position | `gsc_schema.md` → `Position` (average) |
| Current Organic Sessions | `ga4_schema.md` → `sessions` (organic filter) |

**Target Calculation Logic:**
| Metric | Formula |
|--------|---------|
| CTR | Current + 1% (capped at industry benchmark) |
| Position | 10-50% improvement for target keywords |
| Traffic | +15% baseline; adjust based on gap size |

**Analytical Questions:**
1. Are current metrics above or below industry benchmarks?
2. What's realistic given the issues found?
3. What timeframe is appropriate? (Usually 6-12 months)

---

### Slide 25: Thank You
**Type:** Closing
**Purpose:** End the presentation
**Narrative Role:** Professional close

**Analysis Required:** None

---

## Appendix: Priority Badge Reference

| Badge | Label | Criteria | Color |
|-------|-------|----------|-------|
| **C** | Critical | Blocking core functionality, >20% traffic impact | Red |
| **H** | High | Significant ranking/traffic impact, competitive disadvantage | Purple |
| **M** | Medium | Optimization opportunity, incremental gains | Yellow |
| **L** | Low | Minor issues, nice-to-have improvements | Yellow |

---

## Appendix: Summary Box Generation Rules

Every section summary (slides 11, 16, 19, 22) uses the 3-box format:

### What is the Issue?
- Pull top 3 issues by priority (C > H > M > L)
- Write as problem statement, not technical finding
- Max 15 words per bullet

### What is the Impact?
- Translate each issue to business consequence
- Quantify where possible
- Connect to traffic, revenue, or competitive position

### Our Next Action
- One action per issue
- Actionable and specific
- Imply timeline (immediate, short-term, ongoing)

---

## Appendix: Final Output Validation Checklist

Before delivering the completed audit, run these checks:

### 1. Unified Key Message Check
| Slide | Has Key Message? | Follows Formula? | Under 30 Words? |
|-------|------------------|------------------|-----------------|
| 7 | ☐ | ☐ | ☐ |
| 8 | ☐ | ☐ | ☐ |
| 9 | ☐ | ☐ | ☐ |
| 10 | ☐ | ☐ | ☐ |
| 13 | ☐ | ☐ | ☐ |
| 14 | ☐ | ☐ | ☐ |
| 15 | ☐ | ☐ | ☐ |
| 18 | ☐ | ☐ | ☐ |
| 21 | ☐ | ☐ | ☐ |

### 2. Cross-Slide Consistency Check
| Relationship | Consistent? | If Not, Resolution |
|--------------|-------------|-------------------|
| Keyword gap (14) explains traffic gap (8) | ☐ | |
| Authority gap (21) explains ranking limits (14, 15) | ☐ | |
| Technical issues (18) align with health score (10) | ☐ | |
| Engagement trends (9) align with content quality (13-15) | ☐ | |
| Site health (10) correlates with technical issues (18) | ☐ | |

### 3. Narrative Flow Check
| Question | Yes/No |
|----------|--------|
| Does each section summary (11, 16, 19, 22) reflect its child slides? | ☐ |
| Does Slide 5 ONLY contain insights from Slides 11, 16, 19, 22? | ☐ |
| Are there any contradictions between slides? | ☐ |
| Does the story tighten from general → specific → action? | ☐ |

### 4. Priority Badge Consistency Check
| Check | Pass? |
|-------|-------|
| No Critical (C) issues appear without supporting data | ☐ |
| Priority badges in summaries match source slide badges | ☐ |
| Slide 24 column priorities reflect highest badge from each section | ☐ |

### 5. Business Language Check
| Check | Pass? |
|-------|-------|
| No technical jargon without business translation | ☐ |
| Every issue has a stated business consequence | ☐ |
| Quantified impact where data supports it | ☐ |
| No slide ends with observation only (must imply action) | ☐ |

---

## Appendix: Slide Dependency Map

Use this to trace data flow and ensure consistency:

```
                                    ┌─────────────────┐
                                    │   SLIDE 5       │
                                    │ Exec Summary    │
                                    │ (Generated LAST)│
                                    └────────┬────────┘
                                             │
              ┌──────────────┬───────────────┼───────────────┬──────────────┐
              │              │               │               │              │
              ▼              ▼               ▼               ▼              │
        ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐          │
        │ SLIDE 11 │   │ SLIDE 16 │   │ SLIDE 19 │   │ SLIDE 22 │          │
        │ Summary  │   │ Summary  │   │ Summary  │   │ Summary  │          │
        │ §2       │   │ §3       │   │ §4       │   │ §5       │          │
        └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘          │
             │              │              │              │                │
    ┌────────┼────────┐    ┌┴─────────┐    │              │                │
    │    │   │   │    │    │    │     │    │              │                │
    ▼    ▼   ▼   ▼    ▼    ▼    ▼     ▼    ▼              ▼                │
   S7   S8  S9  S10       S13  S14   S15  S18            S21               │
                                                                           │
                                                                           ▼
                                                                    ┌──────────┐
                                                                    │ SLIDE 24 │
                                                                    │ Findings │
                                                                    │ Summary  │
                                                                    └────┬─────┘
                                                                         │
                                                                         ▼
                                                                    ┌──────────┐
                                                                    │ SLIDE 25 │
                                                                    │   KPIs   │
                                                                    └──────────┘
```

**Reading the Map:**
- Data flows UP (child slides → summaries → executive summary)
- Generate in bottom-up order
- Slide 5 is generated LAST
- Slide 24 pulls from all section summaries
- Slide 25 pulls KPI metrics from Slides 7, 8 (GSC/GA4 data)
