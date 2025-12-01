# SEO Audit Proposal — Placeholder Mapping

> **Version:** 2.0 (Automation-Ready)  
> **Total Slides:** 26 (Index 0-25)  
> **Aligned With:** `slide_logic.md`, `gsc_schema.md`, `pagespeed_schema.md`, `SKILL.md`

---

## Document Architecture

```
CHAPTER 1: SETUP (Slides 0-3)           → No analysis required
CHAPTER 2: EXECUTIVE SUMMARY (Slide 4)  → Generated LAST (pulls from section summaries)
CHAPTER 3: WHERE YOU STAND (Slides 5-10)  → Feeds Slide 10 Summary → Slide 4
CHAPTER 4: CONTENT GAPS (Slides 11-15)    → Feeds Slide 15 Summary → Slide 4
CHAPTER 5: TECHNICAL GAPS (Slides 16-18)  → Feeds Slide 18 Summary → Slide 4
CHAPTER 6: AUTHORITY (Slides 19-21)       → Feeds Slide 21 Summary → Slide 4
CHAPTER 7: PATH FORWARD (Slides 22-25)    → Consolidates all findings
```

---

## Data Flow Diagram

```
Slide 6  (Organic Traffic)    ──┐
Slide 7  (Competitive)        ──┼──→ Slide 10 Summary ──→ Slide 4: General Overview
Slide 8  (Engagement)         ──┤
Slide 9  (Site Health)        ──┘

Slide 12 (Meta Tags)          ──┐
Slide 13 (Keyword Gap Table)  ──┼──→ Slide 15 Summary ──→ Slide 4: Content SEO
Slide 14 (Keyword Intent)     ──┘

Slide 17 (Technical Issues)   ──────→ Slide 18 Summary ──→ Slide 4: Technical SEO

Slide 20 (Domain Authority)   ──────→ Slide 21 Summary ──→ Slide 4: Domain Authority

All Section Summaries ─────────────────────────────────→ Slide 23: Findings Summary
                                                       → Slide 24: KPIs
```

---

## Priority Badge Reference

| Badge | Label | Criteria | Color |
|-------|-------|----------|-------|
| `C` | Critical | Blocking core functionality, >20% traffic impact | Red |
| `H` | High | Significant ranking/traffic impact, competitive disadvantage | Purple |
| `M` | Medium | Optimization opportunity, incremental gains | Yellow |
| `L` | Low | Minor issues, nice-to-have improvements | Yellow |

---

# CHAPTER 1: SETUP (Slides 0-3)

## Slide 0: Cover Page
**Type:** Static  
**Analysis Required:** None

| Placeholder | Field Name | Data Type | Source | Example |
|-------------|------------|-----------|--------|---------|
| `{Brand}` | `brand_name` | string | User input | "Acme Corp" |
| `{Logo}` | `client_logo_path` | image_path | User upload | "/assets/client_logo.png" |
| `{Current month}` | `audit_month` | string | System date | "November" |

---

## Slide 1: SEO Audit Overview
**Type:** Setup  
**Analysis Required:** Date range calculation, tool detection

| Placeholder | Field Name | Data Type | Source | Calculation |
|-------------|------------|-----------|--------|-------------|
| `{Brand}` | `brand_name` | string | User input | — |
| `{dd/mm/yyyy - dd/mm/yyyy}` | `audit_period` | string | Calculated | Min/max dates across all datasets |

**Auto-Detected Fields:**

| Field Name | Data Type | Detection Logic |
|------------|-----------|-----------------|
| `tools_detected` | array[string] | File header pattern matching |
| `data_freshness_warning` | boolean | `true` if date range < 6 months |

---

## Slide 2: Planning Phase
**Type:** Static  
**Analysis Required:** None

---

## Slide 3: Index
**Type:** Navigation  
**Analysis Required:** None

| Placeholder | Field Name | Data Type | Source |
|-------------|------------|-----------|--------|
| `{Brand}` | `brand_name` | string | User input |

---

# CHAPTER 2: EXECUTIVE SUMMARY (Slide 4)

## Slide 4: Path to Digital Visibility
**Type:** Executive Summary  
**⚠️ GENERATE LAST — Requires outputs from all section summaries**

**Layout:** 4 columns

| Column | Placeholder | Field Name | Feeds From |
|--------|-------------|------------|------------|
| General Overview | `{Summary overall SEO Audit}` | `exec_summary_general` | Slide 10: `section_summary_organic.key_highlight` |
| Content SEO | `{Summary of Current Content SEO structure}` | `exec_summary_content` | Slide 15: `section_summary_content.key_highlight` |
| Technical SEO | `{Summary of Current Technical SEO}` | `exec_summary_technical` | Slide 18: `section_summary_technical.key_highlight` |
| Domain Authority | `{Interpretation of Domain Authority}` | `exec_summary_authority` | Slide 21: `section_summary_authority.key_highlight` |

**Generation Rules:**
- Pull highest-priority issue from each section summary
- Identify dominant theme across all pillars
- Frame as unified narrative, not four separate bullets
- Max 2 sentences per column

---

# CHAPTER 3: WHERE YOU STAND (Slides 5-10)

## Slide 5: Section Divider — Where {Brand} Stands Today?
**Type:** Divider  
**Analysis Required:** None

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Brand}` | `brand_name` | string |

---

## Slide 6: Organic Traffic Analysis
**Type:** Data Slide  
**Feeds Into:** Slide 10 → Slide 4 (General Overview)

### Key Message (Required)

| Placeholder | Field Name | Data Type | Formula |
|-------------|------------|-----------|---------|
| `{Key Highlight}` | `organic_traffic.key_message` | string | `[Insight] + [Significance] + [Business Consequence]` |
| `{Observation & Analysis}` | `organic_traffic.observation` | string | Supporting analysis (2-3 sentences) |

**Key Message Pattern:**
> "Organic search is [status] but [limitation], leaving [business consequence]."

**Example:**
> "Organic search is stable but limited by underperforming mid-position keywords, leaving significant non-branded demand uncaptured."

### Priority Badge

| Field Name | Data Type | Assignment Rules |
|------------|-----------|------------------|
| `organic_traffic.priority` | enum | See below |

| Condition | Priority |
|-----------|----------|
| Organic < 30% of total traffic | `C` |
| Organic declining >15% YoY | `H` |
| >50% keywords on page 2+ | `H` |
| Traffic stable, minor gaps | `M` |
| Organic dominant, growing | `L` |

### Chart Data Objects

**Chart 1: Organic vs Other Channels (Pie)**

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `organic_traffic.channels.organic_pct` | float | GA4: `sessions` where `sessionDefaultChannelGroup` = "Organic Search" / total |
| `organic_traffic.channels.direct_pct` | float | GA4: "Direct" / total |
| `organic_traffic.channels.paid_pct` | float | GA4: "Paid Search" / total |
| `organic_traffic.channels.social_pct` | float | GA4: "Organic Social" + "Paid Social" / total |
| `organic_traffic.channels.referral_pct` | float | GA4: "Referral" / total |

**Chart 2: Top Countries by Sessions (Bar)**

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `organic_traffic.top_countries` | array[object] | GA4: `country`, `sessions` (top 5) |
| `organic_traffic.top_countries[].country` | string | Country name |
| `organic_traffic.top_countries[].sessions` | integer | Session count |
| `organic_traffic.top_countries[].percentage` | float | % of total organic sessions |

**Fallback:** GSC `Countries` sheet if GA4 unavailable

**Chart 3: Keyword Position Distribution (Bar)**

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `organic_traffic.keyword_distribution.pos_1_3` | float | SEMrush: % keywords position 1-3 |
| `organic_traffic.keyword_distribution.pos_4_10` | float | SEMrush: % keywords position 4-10 |
| `organic_traffic.keyword_distribution.pos_11_20` | float | SEMrush: % keywords position 11-20 |
| `organic_traffic.keyword_distribution.pos_21_plus` | float | SEMrush: % keywords position 21+ |

---

## Slide 7: Competitive Benchmarking
**Type:** Data Slide  
**Feeds Into:** Slide 10 → Slide 4 (General Overview)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `competitive.key_message` | string |
| `{Observation & Analysis}` | `competitive.observation` | string |

**Key Message Pattern:**
> "{Brand} [competitive position] competitors on [metric], which [business consequence]."

### Priority Badge

| Field Name | Data Type | Assignment Rules |
|------------|-----------|------------------|
| `competitive.priority` | enum | See below |

| Condition | Priority |
|-----------|----------|
| {Brand} ranks last on 3+ metrics | `C` |
| {Brand} has <50% of leader's traffic | `H` |
| {Brand} has <50% of leader's Page 1 Keywords | `H` |
| {Brand} competitive but trailing on authority | `M` |
| {Brand} leads or ties on most metrics | `L` |

### Competitor Table Data

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `competitive.brand_name` | string | User input |
| `competitive.competitors` | array[string] | User input / SEMrush competitor analysis |
| `competitive.metrics` | object | See below |

**Metrics Object Structure:**

```json
{
  "domain_rating": {
    "brand": 45,
    "competitor_1": 62,
    "competitor_2": 58
  },
  "monthly_traffic": {
    "brand": 25000,
    "competitor_1": 85000
  },
  "total_keywords": {
    "brand": 1250
  },
  "page_1_keywords": {
    "brand": 180
  },
  "referring_domains": {
    "brand": 450
  }
}
```

| Metric | Definition | Primary Source | Fallback |
|--------|------------|----------------|----------|
| `domain_rating` | Authority score (0-100) | Ahrefs: `Domain Rating` | SEMrush: `Authority Score` |
| `monthly_traffic` | Organic sessions/month | SEMrush: `Organic Traffic` | Ahrefs: `Organic Traffic` |
| `total_keywords` | Ranking keywords | SEMrush: `Organic Keywords` | Ahrefs: `Organic Keywords` |
| `page_1_keywords` | Keywords position 1-10 | SEMrush: filter Position ≤10 | Ahrefs: filter Position ≤10 |
| `referring_domains` | Unique linking domains | Ahrefs: `Referring Domains` | SEMrush: `Referring Domains` |

---

## Slide 8: User Engagement
**Type:** Data Slide  
**Feeds Into:** Slide 10 → Slide 4 (General Overview)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `engagement.key_message` | string |
| `{Observation & Analysis}` | `engagement.observation` | string |

**Key Message Pattern:**
> "Engagement [trend] despite [context], indicating [business consequence]."

### Priority Badge

| Condition | Priority |
|-----------|----------|
| Engagement rate dropped >10% | `H` |
| Avg engagement time <30s | `H` |
| Engagement stable but below benchmark | `M` |
| Engagement rate >50% and stable/growing | `L` |

### Engagement Metrics

| Placeholder | Field Name | Data Type | Source |
|-------------|------------|-----------|--------|
| `{67.24%}` | `engagement.prev_period.engagement_rate` | string | GA4: `engagementRate` (formatted %) |
| `{178,119}` | `engagement.prev_period.engaged_sessions` | string | GA4: `engagedSessions` (formatted) |
| `{64.42%}` | `engagement.curr_period.engagement_rate` | string | GA4: `engagementRate` (formatted %) |
| `{170,943}` | `engagement.curr_period.engaged_sessions` | string | GA4: `engagedSessions` (formatted) |
| `1m 09s` | `engagement.prev_period.avg_engagement_time` | string | GA4: `averageSessionDuration` |
| `1m 09s` | `engagement.curr_period.avg_engagement_time` | string | GA4: `averageSessionDuration` |

### Period Definitions

| Field Name | Data Type | Calculation |
|------------|-----------|-------------|
| `engagement.prev_period.range` | string | 6 months before current period |
| `engagement.curr_period.range` | string | Most recent 6 months |
| `engagement.trend_pct` | float | `(curr - prev) / prev * 100` |
| `engagement.trend_direction` | enum | `up` / `down` / `stable` |

---

## Slide 9: Site Health
**Type:** Data Slide  
**Feeds Into:** Slide 10 → Slide 4 (General Overview)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `site_health.key_message` | string |
| `{Observation & Analysis}` | `site_health.observation` | string |

**Key Message Pattern:**
> "Site health score of [X]% reflects [primary issue], causing [business consequence]."

### Priority Badge

| Condition | Priority |
|-----------|----------|
| Health Score <60% | `C` |
| Health Score 60-75% | `H` |
| Health Score 75-85% | `M` |
| Health Score >85% | `L` |

### Health Score Metrics

| Placeholder | Field Name | Data Type | Source |
|-------------|------------|-----------|--------|
| `{78}` | `site_health.score` | integer | SEMrush: `Health Score` |
| `{15,000}` | `site_health.pages_crawled` | string | SEMrush: `Pages Crawled` (formatted) |
| `{1,500}` | `site_health.total_errors` | string | SEMrush: `Errors` count (formatted) |

### Issues Tables

**Critical Issues Table:**

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `site_health.critical_issues` | array[object] | SEMrush: `Errors` by type |
| `site_health.critical_issues[].issue_name` | string | Issue type name |
| `site_health.critical_issues[].url_count` | integer | Affected URLs |

**High Priority Issues Table:**

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `site_health.high_priority_issues` | array[object] | SEMrush: `Warnings` by type |
| `site_health.high_priority_issues[].issue_name` | string | Issue type name |
| `site_health.high_priority_issues[].url_count` | integer | Affected URLs |

---

## Slide 10: Summary — Where {Brand} Stands Today?
**Type:** Section Summary  
**Feeds Into:** Slide 4 (Executive Summary: General Overview) + Slide 23

### Section Summary Object

| Field Name | Data Type | Description |
|------------|-----------|-------------|
| `section_summary_organic` | object | Complete summary object |
| `section_summary_organic.key_highlight` | string | Title for summary slide |
| `section_summary_organic.observation` | string | Supporting observation |
| `section_summary_organic.priority` | enum | Highest priority from child slides |

### 3-Box Layout

| Box | Placeholders | Field Names | Aggregation Source |
|-----|--------------|-------------|-------------------|
| What is the Issue? | `{Issue 1}`, `{Issue 2}`, `{Issue 3}` | `section_summary_organic.issues[0-2]` | Top 3 from Slides 6-9 by priority |
| What is the Impact? | `{Impact 1}`, `{Impact 2}`, `{Impact 3}` | `section_summary_organic.impacts[0-2]` | Business consequence of each |
| Our Next Action | `{Next Action 1}`, `{Next Action 2}`, `{Next Action 3}` | `section_summary_organic.actions[0-2]` | Recommended fix for each |

**Aggregation Logic:**
1. Collect `key_message` from Slides 6, 7, 8, 9
2. Rank by `priority` (C > H > M > L)
3. Select top 3
4. For each: generate Issue → Impact → Action

**Writing Rules:**
- Issues: Problem statement, not technical finding (max 15 words)
- Impacts: Quantified business consequence where possible
- Actions: Actionable and specific, imply timeline

---

# CHAPTER 4: CONTENT GAPS (Slides 11-15)

## Slide 11: Section Divider — Content Visibility Gaps & Insights
**Type:** Divider  
**Analysis Required:** None

---

## Slide 12: Meta Tags & Heading
**Type:** Data Slide  
**Feeds Into:** Slide 15 → Slide 4 (Content SEO)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `meta_tags.key_message` | string |
| `{Observation & Analysis}` | `meta_tags.observation` | string |

**Key Message Pattern:**
> "[X pages/% of site] have [meta issue], which [ranking/visibility consequence]."

### Priority Badge

| Condition | Priority |
|-----------|----------|
| >20% pages with title issues | `C` |
| >30% pages missing meta descriptions | `H` |
| H1 issues on key landing pages | `H` |
| Minor issues on low-traffic pages | `M` |
| <5% affected | `L` |

### Issues Tables (Left + Right)

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `meta_tags.issues` | array[object] | SEMrush Site Audit / Screaming Frog |
| `meta_tags.issues[].issue_name` | string | Issue category |
| `meta_tags.issues[].url_count` | integer | Affected URLs |
| `meta_tags.issues[].priority` | enum | C/H/M/L |

**Common Issue Categories:**

| Issue Name | Source Field | Priority Threshold |
|------------|--------------|-------------------|
| Missing title tag | `Title 1` is empty | H if >5% |
| Duplicate title tag | Multiple pages same title | H if >10% |
| Title too long (>60 chars) | `Title 1 Length` | M |
| Missing meta description | `Meta Description 1` empty | H if >20% |
| Duplicate meta description | Multiple pages same | M |
| Missing H1 | `H1-1` empty | H if landing pages |
| Multiple H1 | `H1-2` exists | M |
| Low word count (<300) | `Word Count` | M |

---

## Slide 13: Keyword Gap & Content Opportunity (Table View)
**Type:** Data Slide  
**Feeds Into:** Slide 15 → Slide 4 (Content SEO)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `keyword_gap.key_message` | string |
| `{Observation & Analysis}` | `keyword_gap.observation` | string |

### Keyword Gap Tables

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `keyword_gap.missing_keywords` | array[object] | SEMrush Keyword Gap |
| `keyword_gap.missing_keywords[].keyword` | string | Missing keyword |
| `keyword_gap.missing_keywords[].volume` | integer | Search volume |
| `keyword_gap.missing_keywords[].difficulty` | integer | Keyword difficulty |
| `keyword_gap.missing_keywords[].competitor_positions` | object | Which competitors rank |

---

## Slide 14: Keyword Gap & Content Opportunity (Intent Distribution)
**Type:** Data Slide  
**Feeds Into:** Slide 15 → Slide 4 (Content SEO)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `keyword_intent.key_message` | string |
| `{Observation & Analysis}` | `keyword_intent.observation` | string |

**Key Message Pattern:**
> "[X]% of keyword portfolio is [category], which [alignment/opportunity consequence]."

### Priority Badge

| Condition | Priority |
|-----------|----------|
| Behavioral >80% with weak Device & Utility | `H` |
| Brand keywords <5% total | `M` |
| Location keywords <10% for local business | `H` |
| Gap >5K keywords across categories | `C` |
| Balanced distribution with strong coverage | `L` |

### Keyword Category Breakdown Table

| Field Name | Data Type | Classification Logic |
|------------|-----------|---------------------|
| `keyword_intent.categories` | array[object] | — |
| `keyword_intent.categories[].name` | string | "Behavioral", "Device & Utility", "Brand", "Location" |
| `keyword_intent.categories[].percentage` | float | % of total keywords |
| `keyword_intent.categories[].volume` | string | Total search volume (formatted) |
| `keyword_intent.categories[].examples` | string | 2-3 example keywords |

**Category Classification Signals:**

| Category | Contains |
|----------|----------|
| **Behavioral** | "how to", "what is", "why", "benefits of", "ways to", "guide", question words |
| **Device & Utility** | "best", "top", product types, comparisons, utility terms |
| **Brand** | brand name, "review", "coupon", "discount", "alternative to" |
| **Location** | country names, city names, "near me", regional modifiers |

### Pie Chart Data

| Field Name | Data Type |
|------------|-----------|
| `keyword_intent.distribution.behavioral_pct` | float |
| `keyword_intent.distribution.device_utility_pct` | float |
| `keyword_intent.distribution.brand_pct` | float |
| `keyword_intent.distribution.location_pct` | float |

---

## Slide 15: Summary — Content Visibility Gaps
**Type:** Section Summary  
**Feeds Into:** Slide 4 (Executive Summary: Content SEO) + Slide 23

### Section Summary Object

| Field Name | Data Type |
|------------|-----------|
| `section_summary_content` | object |
| `section_summary_content.key_highlight` | string |
| `section_summary_content.observation` | string |
| `section_summary_content.priority` | enum |

### 3-Box Layout

| Box | Field Names | Aggregation Source |
|-----|-------------|-------------------|
| What is the Issue? | `section_summary_content.issues[0-2]` | Top 3 from Slides 12-14 by priority |
| What is the Impact? | `section_summary_content.impacts[0-2]` | Business consequence |
| Our Next Action | `section_summary_content.actions[0-2]` | Recommended fix |

---

# CHAPTER 5: TECHNICAL GAPS (Slides 16-18)

## Slide 16: Section Divider — Technical Gaps that Limiting Growth
**Type:** Divider  
**Analysis Required:** None

---

## Slide 17: Technical SEO Issues Overview
**Type:** Data Slide  
**Feeds Into:** Slide 18 → Slide 4 (Technical SEO)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `technical_seo.key_message` | string |
| `{Observation & Analysis}` | `technical_seo.observation` | string |

**Key Message Pattern:**
> "[Technical issue category] affects [X pages/%], which [crawl/index/ranking consequence]."

### Priority Badge

| Condition | Priority |
|-----------|----------|
| Indexing blocked on >10% pages | `C` |
| Core Web Vitals failing on key pages | `H` |
| Redirect chains >3 hops | `H` |
| Minor issues on low-value pages | `M` |
| Clean technical foundation | `L` |

### Technical Issues Tables

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `technical_seo.issues` | array[object] | SEMrush / Screaming Frog / GSC |
| `technical_seo.issues[].issue_name` | string | Issue category |
| `technical_seo.issues[].url_count` | integer | Affected URLs |
| `technical_seo.issues[].priority` | enum | C/H/M/L |
| `technical_seo.issues[].category` | string | "Crawlability" / "Indexability" / "Performance" / "Structured Data" |

**Issue Categories & Sources:**

| Category | Issue Examples | Source |
|----------|---------------|--------|
| Crawlability | 5xx errors, robots.txt blocks, redirect chains | SEMrush, Screaming Frog |
| Indexability | noindex pages, canonicalization issues | GSC Coverage, SEMrush |
| Performance | Core Web Vitals failures | PageSpeed Insights |
| Structured Data | Schema errors, missing markup | GSC Rich Results |

### Core Web Vitals (from PageSpeed Schema)

| Field Name | Data Type | Source | Good Threshold |
|------------|-----------|--------|----------------|
| `technical_seo.cwv.lcp` | string | PageSpeed: `Largest Contentful Paint` | ≤2.5s |
| `technical_seo.cwv.lcp_status` | enum | — | "good" / "needs_improvement" / "poor" |
| `technical_seo.cwv.fid` | string | PageSpeed: `Total Blocking Time` (proxy) | ≤200ms |
| `technical_seo.cwv.fid_status` | enum | — | "good" / "needs_improvement" / "poor" |
| `technical_seo.cwv.cls` | string | PageSpeed: `Cumulative Layout Shift` | ≤0.1 |
| `technical_seo.cwv.cls_status` | enum | — | "good" / "needs_improvement" / "poor" |
| `technical_seo.cwv.performance_score` | integer | PageSpeed: Performance gauge | 90+ good |

---

## Slide 18: Summary — Technical Gaps
**Type:** Section Summary  
**Feeds Into:** Slide 4 (Executive Summary: Technical SEO) + Slide 23

### Section Summary Object

| Field Name | Data Type |
|------------|-----------|
| `section_summary_technical` | object |
| `section_summary_technical.key_highlight` | string |
| `section_summary_technical.observation` | string |
| `section_summary_technical.priority` | enum |

### 3-Box Layout

| Box | Field Names | Aggregation Source |
|-----|-------------|-------------------|
| What is the Issue? | `section_summary_technical.issues[0-2]` | Top 3 from Slide 17 by priority |
| What is the Impact? | `section_summary_technical.impacts[0-2]` | Business consequence |
| Our Next Action | `section_summary_technical.actions[0-2]` | Recommended fix |

---

# CHAPTER 6: AUTHORITY (Slides 19-21)

## Slide 19: Section Divider — Understanding Domain Authority
**Type:** Divider  
**Analysis Required:** None

---

## Slide 20: Domain Authority
**Type:** Data Slide  
**Feeds Into:** Slide 21 → Slide 4 (Domain Authority)

### Key Message (Required)

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Key Highlight}` | `domain_authority.key_message` | string |
| `{Observation & Analysis}` | `domain_authority.observation` | string |

**Key Message Pattern:**
> "[Authority status/trend] [comparison context], which [competitive consequence]."

### Priority Badge

| Condition | Priority |
|-----------|----------|
| DR declining >5 points in 6 months | `C` |
| DR significantly below competitor average | `H` |
| Flat DR, minimal new referring domains | `M` |
| Growing DR, healthy backlink profile | `L` |

### Authority Metrics

| Field Name | Data Type | Source |
|------------|-----------|--------|
| `domain_authority.current_dr` | integer | Ahrefs: `Domain Rating` |
| `domain_authority.dr_6_months_ago` | integer | Ahrefs: `DR History` |
| `domain_authority.dr_trend` | enum | "growing" / "stable" / "declining" |
| `domain_authority.dr_change` | integer | Current - 6 months ago |
| `domain_authority.referring_domains` | integer | Ahrefs: `Referring Domains` |
| `domain_authority.new_rd_monthly_avg` | integer | New RDs / 6 months |
| `domain_authority.competitor_avg_dr` | integer | Average of competitor DRs |
| `domain_authority.dr_gap` | integer | Competitor avg - Brand DR |

### Referring Domains Graph

| Placeholder | Field Name | Data Type |
|-------------|------------|-----------|
| `{Images Referring Domain Month to Month Graph}` | `domain_authority.rd_trend_image` | image_path |

**Or Chart Data:**

| Field Name | Data Type |
|------------|-----------|
| `domain_authority.rd_trend` | array[object] |
| `domain_authority.rd_trend[].month` | string |
| `domain_authority.rd_trend[].referring_domains` | integer |

---

## Slide 21: Summary — Domain Authority
**Type:** Section Summary  
**Feeds Into:** Slide 4 (Executive Summary: Domain Authority) + Slide 23

### Section Summary Object

| Field Name | Data Type |
|------------|-----------|
| `section_summary_authority` | object |
| `section_summary_authority.key_highlight` | string |
| `section_summary_authority.observation` | string |
| `section_summary_authority.priority` | enum |

### 3-Box Layout

| Box | Field Names | Aggregation Source |
|-----|-------------|-------------------|
| What is the Issue? | `section_summary_authority.issues[0-2]` | From Slide 20 |
| What is the Impact? | `section_summary_authority.impacts[0-2]` | Business consequence |
| Our Next Action | `section_summary_authority.actions[0-2]` | Recommended fix |

---

# CHAPTER 7: PATH FORWARD (Slides 22-25)

## Slide 22: Section Divider — Steps to Improve your SEO
**Type:** Divider  
**Analysis Required:** None

---

## Slide 23: SEO Audit Findings Summary
**Type:** Action Summary  
**Layout:** 3 columns

### Header Section

| Placeholder | Field Name | Data Type | Source |
|-------------|------------|-----------|--------|
| `{Next Action Key Message}` | `findings_summary.key_message` | string | Unified theme from all sections |
| `{Organic Traffic Issue}` | `findings_summary.subtitle` | string | Primary traffic problem |

**Key Message Generation:**
> Synthesize dominant issue pattern across all three pillars

### Column Data

| Column | Field Names | Source |
|--------|-------------|--------|
| Technical SEO | `findings_summary.technical.issues[0-2]`, `findings_summary.technical.actions[0-2]` | Slide 18 |
| Content SEO | `findings_summary.content.issues[0-2]`, `findings_summary.content.actions[0-2]` | Slide 15 |
| Domain Authority | `findings_summary.authority.issues[0-2]`, `findings_summary.authority.actions[0-2]` | Slide 21 |

### Priority Badges per Column

| Field Name | Data Type | Calculation |
|------------|-----------|-------------|
| `findings_summary.technical.priority` | enum | Highest from Slide 18 |
| `findings_summary.content.priority` | enum | Highest from Slide 15 |
| `findings_summary.authority.priority` | enum | Highest from Slide 21 |

---

## Slide 24: KPI & Benchmark
**Type:** KPI Slide

### Current Metrics (from GSC Schema)

| Placeholder | Field Name | Data Type | Source | Calculation |
|-------------|------------|-----------|--------|-------------|
| `{CTR}` | `kpi.current_ctr` | string | GSC: `Queries` sheet | `sum(Clicks) / sum(Impressions) * 100` |
| `{Average Position}` | `kpi.current_avg_position` | string | GSC: `Queries` sheet | Impression-weighted average |
| `{Current month organic session}` | `kpi.current_organic_sessions` | string | GA4: `sessions` (organic filter) | — |

### Target Metrics

| Field Name | Data Type | Formula |
|------------|-----------|---------|
| `kpi.target_ctr` | string | `+1%` (capped at 5%) |
| `kpi.target_position_improvement` | string | `10-50%` |
| `kpi.target_traffic_improvement` | string | `+15%` |

### Benchmark

| Field Name | Data Type | Value |
|------------|-----------|-------|
| `kpi.benchmark_ctr` | string | "3-5%" |
| `kpi.benchmark_note` | string | "Industry average for median organic CTR" |

---

## Slide 25: Thank You
**Type:** Closing  
**Analysis Required:** None

---

# Complete JSON Schema

```json
{
  "metadata": {
    "brand_name": "string",
    "client_logo_path": "string",
    "audit_month": "string",
    "audit_period": "string",
    "tools_detected": ["string"],
    "website_type": "ecommerce|saas|content|local|marketplace"
  },
  
  "organic_traffic": {
    "key_message": "string (max 30 words)",
    "observation": "string",
    "priority": "C|H|M|L",
    "channels": {
      "organic_pct": "float",
      "direct_pct": "float",
      "paid_pct": "float",
      "social_pct": "float",
      "referral_pct": "float"
    },
    "top_countries": [
      {"country": "string", "sessions": "int", "percentage": "float"}
    ],
    "keyword_distribution": {
      "pos_1_3": "float",
      "pos_4_10": "float",
      "pos_11_20": "float",
      "pos_21_plus": "float"
    },
    "yoy_change_pct": "float"
  },
  
  "competitive": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "brand_name": "string",
    "competitors": ["string"],
    "metrics": {
      "domain_rating": {"brand": "int", "competitor_1": "int"},
      "monthly_traffic": {"brand": "int"},
      "total_keywords": {"brand": "int"},
      "page_1_keywords": {"brand": "int"},
      "referring_domains": {"brand": "int"}
    }
  },
  
  "engagement": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "prev_period": {
      "range": "string",
      "engagement_rate": "string",
      "engaged_sessions": "string",
      "avg_engagement_time": "string"
    },
    "curr_period": {
      "range": "string",
      "engagement_rate": "string",
      "engaged_sessions": "string",
      "avg_engagement_time": "string"
    },
    "trend_pct": "float",
    "trend_direction": "up|down|stable"
  },
  
  "site_health": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "score": "int",
    "pages_crawled": "string",
    "total_errors": "string",
    "critical_issues": [
      {"issue_name": "string", "url_count": "int"}
    ],
    "high_priority_issues": [
      {"issue_name": "string", "url_count": "int"}
    ]
  },
  
  "section_summary_organic": {
    "key_highlight": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "issues": ["string", "string", "string"],
    "impacts": ["string", "string", "string"],
    "actions": ["string", "string", "string"]
  },
  
  "meta_tags": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "issues": [
      {"issue_name": "string", "url_count": "int", "priority": "C|H|M|L"}
    ]
  },
  
  "keyword_gap": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "total_gap_keywords": "int",
    "total_gap_volume": "int",
    "missing_keywords": [
      {"keyword": "string", "volume": "int", "difficulty": "int"}
    ]
  },
  
  "keyword_intent": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "categories": [
      {
        "name": "string",
        "percentage": "float",
        "volume": "string",
        "examples": "string"
      }
    ],
    "distribution": {
      "behavioral_pct": "float",
      "device_utility_pct": "float",
      "brand_pct": "float",
      "location_pct": "float"
    }
  },
  
  "section_summary_content": {
    "key_highlight": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "issues": ["string", "string", "string"],
    "impacts": ["string", "string", "string"],
    "actions": ["string", "string", "string"]
  },
  
  "technical_seo": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "issues": [
      {
        "issue_name": "string",
        "url_count": "int",
        "priority": "C|H|M|L",
        "category": "crawlability|indexability|performance|structured_data"
      }
    ],
    "cwv": {
      "lcp": "string",
      "lcp_status": "good|needs_improvement|poor",
      "fid": "string",
      "fid_status": "good|needs_improvement|poor",
      "cls": "string",
      "cls_status": "good|needs_improvement|poor",
      "performance_score": "int"
    }
  },
  
  "section_summary_technical": {
    "key_highlight": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "issues": ["string", "string", "string"],
    "impacts": ["string", "string", "string"],
    "actions": ["string", "string", "string"]
  },
  
  "domain_authority": {
    "key_message": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "current_dr": "int",
    "dr_6_months_ago": "int",
    "dr_trend": "growing|stable|declining",
    "dr_change": "int",
    "referring_domains": "int",
    "new_rd_monthly_avg": "int",
    "competitor_avg_dr": "int",
    "dr_gap": "int",
    "rd_trend": [
      {"month": "string", "referring_domains": "int"}
    ]
  },
  
  "section_summary_authority": {
    "key_highlight": "string",
    "observation": "string",
    "priority": "C|H|M|L",
    "issues": ["string", "string", "string"],
    "impacts": ["string", "string", "string"],
    "actions": ["string", "string", "string"]
  },
  
  "exec_summary": {
    "general": "string",
    "content": "string",
    "technical": "string",
    "authority": "string"
  },
  
  "findings_summary": {
    "key_message": "string",
    "subtitle": "string",
    "technical": {
      "priority": "C|H|M|L",
      "issues": ["string", "string", "string"],
      "actions": ["string", "string", "string"]
    },
    "content": {
      "priority": "C|H|M|L",
      "issues": ["string", "string", "string"],
      "actions": ["string", "string", "string"]
    },
    "authority": {
      "priority": "C|H|M|L",
      "issues": ["string", "string", "string"],
      "actions": ["string", "string", "string"]
    }
  },
  
  "kpi": {
    "current_ctr": "string",
    "current_avg_position": "string",
    "current_organic_sessions": "string",
    "target_ctr": "string",
    "target_position_improvement": "string",
    "target_traffic_improvement": "string",
    "benchmark_ctr": "string"
  }
}
```

---

# Validation Checklist

## 1. Unified Key Message Check

| Slide | Has Key Message? | Follows Formula? | Under 30 Words? |
|-------|------------------|------------------|-----------------|
| 6 (Organic Traffic) | ☐ | ☐ | ☐ |
| 7 (Competitive) | ☐ | ☐ | ☐ |
| 8 (Engagement) | ☐ | ☐ | ☐ |
| 9 (Site Health) | ☐ | ☐ | ☐ |
| 12 (Meta Tags) | ☐ | ☐ | ☐ |
| 13/14 (Keyword Gap) | ☐ | ☐ | ☐ |
| 17 (Technical) | ☐ | ☐ | ☐ |
| 20 (Authority) | ☐ | ☐ | ☐ |

## 2. Cross-Slide Consistency Check

| Relationship | Consistent? |
|--------------|-------------|
| Keyword gap (14) explains traffic gap (7) | ☐ |
| Authority gap (20) explains ranking limits (14) | ☐ |
| Technical issues (17) align with health score (9) | ☐ |
| Engagement trends (8) align with content quality (12-14) | ☐ |

## 3. Executive Summary Rule

```
⚠️ STRICT: Slide 4 must ONLY pull from Slides 10, 15, 18, 21.
   No new insights. No data not in section summaries.
```

## 4. Priority Badge Consistency

| Check | Pass? |
|-------|-------|
| No Critical (C) without supporting data | ☐ |
| Summary badges match source slide badges | ☐ |
| Slide 23 column priorities = highest from each section | ☐ |

---

# Key Message Templates by Slide

| Slide | Pattern | Transition Words |
|-------|---------|------------------|
| 6 | "Organic search is [status] but [limitation], leaving [consequence]." | but, leaving |
| 7 | "{Brand} [position] competitors on [metric], which [consequence]." | which |
| 8 | "Engagement [trend] despite [context], indicating [consequence]." | indicating |
| 9 | "Site health score of [X]% reflects [issue], causing [consequence]." | causing |
| 12 | "[X pages/%] have [issue], which [consequence]." | which |
| 14 | "[X]% of keyword portfolio is [category], which [consequence]." | which |
| 17 | "[Issue category] affects [X], which [consequence]." | which |
| 20 | "[Authority status] [comparison], which [consequence]." | which |

**Rules:**
- One sentence only (no mid-sentence periods)
- Must include transition word
- Must end with business consequence
- Max 30 words
