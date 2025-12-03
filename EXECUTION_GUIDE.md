# How to Execute the SEO Automation Tool

This guide explains how to run the complete end-to-end SEO Audit Automation Tool that you've just built.

## Overview

The SEO Audit Automation Tool is now fully operational! It follows a 3-phase workflow to transform raw SEO data into executive-ready PowerPoint presentations.

## Prerequisites Check

Before running, ensure you have:

✅ Python 3.9+ installed
✅ All dependencies installed (`pip install -r requirements.txt`)
✅ SEO data files in a directory
✅ Brand name ready

## Quick Execution

### Minimal Command

```bash
python seo_audit_tool.py -d ./raw_data -b "Your Brand Name"
```

### Recommended Command

```bash
python seo_audit_tool.py \
  --data-dir ./raw_data \
  --brand-name "Your Company" \
  --website-type ecommerce \
  --verbose
```

## Step-by-Step Execution

### 1. Install Dependencies (First Time Only)

```bash
pip install -r requirements.txt
```

### 2. Prepare Data Directory

Place your SEO export files in a directory (e.g., `raw_data/`):

```bash
ls raw_data/
# Example output:
# GA4_Countries_report.xlsx
# semrush_audit.csv
# ahrefs_backlinks.xlsx
# gsc_queries.csv
```

### 3. Run the Tool

```bash
python seo_audit_tool.py \
  --data-dir ./raw_data \
  --brand-name "Acme Corporation" \
  --website-type saas
```

### 4. Follow Interactive Workflow

#### Phase 1: Data Analysis & Strategic Insights

The tool will:
1. Load all data files from your directory
2. Auto-detect data sources (GA4, SEMrush, Ahrefs, etc.)
3. Analyze each aspect:
   - Organic traffic patterns
   - Competitive positioning
   - User engagement metrics
   - Site health
   - Meta tags & on-page SEO
   - Keyword gaps
   - Technical SEO issues
   - Domain authority
4. Display strategic insights with priority badges (C/H/M/L)

**You will see:**
```
Strategic Insights:

[H] Organic Traffic: Organic search is stable but limited by 60% of keywords...
[H] Competitive Position: Brand trails competitors on domain authority by 15 points...
[M] User Engagement: Engagement rate declined 4% despite stable traffic...
...
```

**Action Required:**
```
? Do these insights accurately reflect the data priorities? Proceed to Phase 2? (Y/n)
```

Press `Y` to continue or `n` to review.

#### Phase 2: Narrative & Storyline Architecture

The tool will:
1. Map insights to slide structure
2. Generate executive summary
3. Create unified narrative across all pillars
4. Display storyline draft

**You will see:**
```
Executive Summary:

General Overview:
  Organic traffic limited by keyword position performance. Significant non-branded demand remains uncaptured.

Content SEO:
  420+ pages lack optimized titles and meta descriptions. Search engines struggle to properly index and rank pages.

Technical SEO:
  850 pages blocked from indexing waste content investment. 12% of site content invisible to organic search.

Domain Authority:
  Domain rating 15 points below competitor average. Cannot compete for keywords above difficulty 50.
```

**Action Required:**
```
? Is this storyline engaging and accurate? Proceed to Phase 3? (Y/n)
```

Press `Y` to generate the final PowerPoint.

#### Phase 3: Final PowerPoint Output Generation

The tool will:
1. Generate PowerPoint presentation with all slides
2. Create JSON content file with structured data
3. Save both files to `output/` directory

**You will see:**
```
✓ PowerPoint generated: output/SEO_Audit_AcmeCorporation_raw_data.pptx
✓ Content JSON generated: output/SEO_Audit_AcmeCorporation_raw_data_content.json

✓ SEO Audit Complete!
```

## Command Reference

### All Available Options

```bash
python seo_audit_tool.py [OPTIONS]

Required:
  -d, --data-dir DIRECTORY     Path to directory with SEO data files
  -b, --brand-name TEXT        Client/brand name for the audit

Optional:
  -w, --website-type TYPE      Website type: ecommerce, saas, content, local, marketplace
                               Default: ecommerce
  -v, --verbose                Enable detailed logging for debugging

Help:
  --help                       Show help message and exit
```

### Examples

#### Example 1: E-commerce Site
```bash
python seo_audit_tool.py \
  -d ./client_data \
  -b "Fashion Boutique" \
  -w ecommerce
```

#### Example 2: SaaS Company with Verbose Logging
```bash
python seo_audit_tool.py \
  --data-dir ./saas_data \
  --brand-name "CloudApp Inc" \
  --website-type saas \
  --verbose
```

#### Example 3: Content Publisher
```bash
python seo_audit_tool.py \
  -d ./publisher_exports \
  -b "Tech News Daily" \
  -w content \
  -v
```

#### Example 4: Local Business
```bash
python seo_audit_tool.py \
  -d ./local_seo_data \
  -b "Downtown Dental" \
  -w local
```

## Output Files

After successful execution, you'll have:

### 1. PowerPoint Presentation
- **Path**: `output/SEO_Audit_{BrandName}_{DataDir}.pptx`
- **Slides**: 26 professional slides including:
  - Cover & Overview
  - Executive Summary
  - Traffic Analysis
  - Competitive Benchmarking
  - Engagement Metrics
  - Site Health
  - Meta Tags Analysis
  - Keyword Gap
  - Keyword Intent
  - Technical SEO
  - Domain Authority
  - Findings Summary
  - KPIs & Benchmarks

### 2. JSON Content File
- **Path**: `output/SEO_Audit_{BrandName}_{DataDir}_content.json`
- **Contents**: All structured data used in the presentation
- **Use Cases**:
  - Custom integrations
  - Further analysis in Excel/Python
  - Template population
  - API responses

## Supported Data Sources

The tool auto-detects and processes:

| Tool | Detection | Required Columns |
|------|-----------|------------------|
| Google Analytics 4 | Automatic | `sessionDefaultChannelGroup`, `sessions`, `country` |
| Google Search Console | Automatic | `queries`, `clicks`, `impressions`, `ctr`, `position` |
| SEMrush | Automatic | `url`, `issue type`, `position` |
| Ahrefs | Automatic | `Domain Rating`, `Referring Domains` |
| Screaming Frog | Automatic | `address`, `status code`, `title 1` |
| PageSpeed Insights | Automatic | `Largest Contentful Paint`, `Cumulative Layout Shift` |

## Workflow Tips

### For Best Results

1. **Include Multiple Data Sources**
   - Minimum: GA4 + GSC
   - Recommended: GA4 + GSC + SEMrush + Ahrefs
   - Optimal: All sources above + Screaming Frog + PageSpeed

2. **Use Recent Data**
   - Ideal: Last 6-12 months
   - Minimum: Last 3 months

3. **Review Each Phase**
   - Phase 1: Verify insights match your understanding
   - Phase 2: Check narrative aligns with business goals
   - Phase 3: Receive final output

4. **Enable Verbose Logging**
   - Use `-v` flag to see detailed progress
   - Helpful for troubleshooting
   - Shows data processing steps

### If Something Goes Wrong

1. **Check data files** exist and are valid CSV/XLSX
2. **Run with --verbose** to see detailed errors
3. **Verify column names** match expected schemas (see `schema/` directory)
4. **Check Python version** is 3.9+
5. **Reinstall dependencies**: `pip install -r requirements.txt --force-reinstall`

## Advanced Usage

### Batch Processing

Process multiple clients:

```bash
for client in client1 client2 client3; do
  python seo_audit_tool.py \
    -d ./data/$client \
    -b "$client" \
    -w ecommerce
done
```

### Custom Output Location

The tool saves to `output/` by default. To customize, modify `seo_audit_tool.py`:

```python
output_dir = Path('custom_output_dir')
```

### Integrating with Other Tools

Use the JSON output for:
- Custom dashboards
- API integrations
- Database imports
- Further analysis in Jupyter notebooks

Example: Load JSON in Python
```python
import json

with open('output/SEO_Audit_Client_raw_data_content.json', 'r') as f:
    audit_data = json.load(f)

# Access specific insights
organic_traffic = audit_data['organic_traffic']
print(f"Priority: {organic_traffic['priority']}")
print(f"Key Message: {organic_traffic['key_message']}")
```

## Complete Example Session

```bash
$ python seo_audit_tool.py -d ./raw_data -b "Acme Corp" -w saas -v

┌─────────────────────────────────┐
│  SEO Audit Automation Tool      │
│  Client: Acme Corp              │
│  Website Type: saas             │
└─────────────────────────────────┘

INFO     Loading data from ./raw_data...

┌────────────────────────┐
│ Loaded Data Summary    │
├─────────────┬──────────┤
│ Tool        │ Rows     │
├─────────────┼──────────┤
│ GA4_export  │ 1,245    │
│ GSC_queries │ 3,521    │
│ SEMrush_...│ 15,000   │
└─────────────┴──────────┘

INFO     Data period: 01/01/2024 - 30/11/2024

┌────────────────────────────────────────┐
│ Phase 1: Data Analysis & Insights     │
└────────────────────────────────────────┘

INFO     Analyzing organic traffic...
INFO     Analyzing competitive landscape...
INFO     Analyzing user engagement...
...

[H] Organic Traffic: Organic search is stable but limited by underperforming mid-position keywords, leaving significant non-branded demand uncaptured.
...

? Do these insights accurately reflect the data priorities? Proceed to Phase 2? Yes

┌────────────────────────────────────────┐
│ Phase 2: Narrative & Storyline        │
└────────────────────────────────────────┘

INFO     Crafting executive summary...

Executive Summary:

General Overview:
  Organic traffic limited by keyword position performance...
...

? Is this storyline engaging and accurate? Proceed to Phase 3? Yes

┌────────────────────────────────────────┐
│ Phase 3: PowerPoint Generation        │
└────────────────────────────────────────┘

INFO     Generating structured content...
INFO     Generated JSON content file: output/SEO_Audit_AcmeCorp_raw_data_content.json
INFO     Generated PowerPoint file: output/SEO_Audit_AcmeCorp_raw_data.pptx

✓ PowerPoint generated: output/SEO_Audit_AcmeCorp_raw_data.pptx
✓ Content JSON generated: output/SEO_Audit_AcmeCorp_raw_data_content.json

✓ SEO Audit Complete!
```

## Next Steps

1. **Open the PowerPoint** in Microsoft Office or Google Slides
2. **Review each slide** for accuracy
3. **Customize branding** (add logo, adjust colors)
4. **Present to stakeholders**

## Support & Documentation

- **Quick Start**: See [QUICKSTART.md](QUICKSTART.md)
- **Full Documentation**: See [README.md](README.md)
- **Strategic Framework**: See [SKILL.md](SKILL.md)
- **Data Schemas**: See `schema/` directory
- **Analysis Logic**: See `slide_logic.md`
- **Voice & Tone**: See `template_rules.md`

---

**You're all set!** The SEO Audit Automation Tool is ready to transform your SEO data into executive-ready insights. 🚀
