# SEO Audit Automation Tool

A complete end-to-end automation tool that generates executive-ready SEO audits following a strategic 3-phase workflow. This tool transforms technical SEO data into compelling business narratives and professional PowerPoint presentations.

## Overview

This tool produces **executive-ready SEO audits**, not technical checklists. It acts as a Strategic Partner transforming SEO data into business impact by following a coherent, defensible narrative across the entire deck.

### Strategic Communication Principles

- **Human-Centric First**: Start with the consumer's need, not the algorithm
- **Ecosystem Thinking**: View SEO as part of a larger machine (omnichannel, social, brand health)
- **Urgency & Loss Aversion**: Use language that implies the cost of inaction
- **Impact over jargon**: Translate technical SEO issues into revenue risk, traffic opportunity, or competitive threat
- **Prioritized, not exhaustive**: Surface the 20% of issues driving 80% of impact

## 3-Phase Workflow

The tool follows a mandatory 3-phase workflow with user approval at each stage:

### Phase 1: Data Analysis & Strategic Insights
- Ingest & validate SEO data from multiple tools (GA4, SEMrush, Ahrefs, GSC, Screaming Frog)
- Apply analytical logic from `slide_logic.md`
- Synthesize top 3-5 critical priorities based on business impact
- **Output**: Strategic insights in bulleted format with priority badges (C/H/M/L)

### Phase 2: Narrative & Storyline Architecture
- Map insights to slide structure from `placeholder_mapping.md`
- Draft compelling narrative following voice/tone from `template_rules.md`
- Check constraints for slide limitations (concise, punchy)
- **Output**: Markdown storyboard organized by slide title

### Phase 3: Final PowerPoint Output Generation
- Convert approved narrative into exact placeholders
- Apply template rules (formatting, character limits, tone)
- Generate PowerPoint presentation + JSON content file
- **Output**: Professional PowerPoint deck ready for client presentation

## Installation

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Setup

1. **Clone or navigate to the repository:**
   ```bash
   cd seo-audit-automation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation:**
   ```bash
   python seo_audit_tool.py --help
   ```

## Data Preparation

### Required Data Files

Place your SEO data exports in a directory (e.g., `raw_data/`). The tool supports:

| Tool | File Format | Detection Method |
|------|-------------|------------------|
| **Google Analytics 4** | CSV/XLSX | Column headers: `sessionDefaultChannelGroup`, `sessions`, `country` |
| **Google Search Console** | CSV/XLSX | Columns: `queries`, `clicks`, `impressions`, `ctr`, `position` |
| **SEMrush** | CSV/XLSX | Columns: `url`, `issue type`, `position`, `search volume` |
| **Ahrefs** | CSV/XLSX | Sheet names: `Backlinks`, `Referring domains`, or columns: `Domain Rating` |
| **Screaming Frog** | CSV/XLSX | Columns: `address`, `status code`, `title 1` |
| **PageSpeed Insights** | CSV/XLSX | Columns: `largest contentful paint`, `cumulative layout shift` |

### Data File Organization

```
seo-audit-automation/
├── raw_data/                    # Your SEO data files
│   ├── ga4_export.xlsx
│   ├── gsc_queries.csv
│   ├── semrush_audit.csv
│   ├── ahrefs_backlinks.xlsx
│   └── screaming_frog_crawl.csv
├── output/                      # Generated reports (auto-created)
└── seo_audit_tool.py           # Main tool
```

## Usage

### Basic Usage

```bash
python seo_audit_tool.py --data-dir ./raw_data --brand-name "YourBrand"
```

### Full Command Options

```bash
python seo_audit_tool.py \
  --data-dir ./raw_data \
  --brand-name "YourBrand" \
  --website-type ecommerce \
  --verbose
```

### Command-Line Arguments

| Argument | Short | Required | Description | Options |
|----------|-------|----------|-------------|---------|
| `--data-dir` | `-d` | Yes | Directory containing SEO data files | Any valid directory path |
| `--brand-name` | `-b` | Yes | Client brand name | Any string |
| `--website-type` | `-w` | No | Type of website (default: `ecommerce`) | `ecommerce`, `saas`, `content`, `local`, `marketplace` |
| `--verbose` | `-v` | No | Enable verbose logging | Flag (no value) |

### Interactive Workflow

The tool runs interactively with approval gates:

1. **Data Loading**: Tool loads and validates all data files
2. **Phase 1 Execution**: Analyzes data and presents insights
   - Displays strategic insights with priority badges
   - **User Decision**: "Do these insights accurately reflect the data priorities?"
3. **Phase 2 Execution**: Generates narrative and storyline
   - Displays executive summary draft
   - **User Decision**: "Is this storyline engaging and accurate?"
4. **Phase 3 Execution**: Generates final PowerPoint
   - Creates PowerPoint presentation
   - Creates JSON content file
   - **Complete**: Files saved to `output/` directory

### Example Session

```bash
$ python seo_audit_tool.py -d ./raw_data -b "Acme Corp" -w saas

┌─────────────────────────────────┐
│    SEO Audit Automation Tool    │
│  Client: Acme Corp              │
│  Website Type: saas             │
└─────────────────────────────────┘

Loading data from ./raw_data...

┌─────────────────────────┐
│  Loaded Data Summary    │
├──────────────┬──────────┤
│ Tool         │ Rows     │
├──────────────┼──────────┤
│ GA4_export   │ 1,245    │
│ GSC_queries  │ 3,521    │
│ SEMrush_audit│ 15,000   │
└──────────────┴──────────┘

Data period: 01/01/2024 - 30/11/2024

┌───────────────────────────────────────────────────┐
│  Phase 1: Data Analysis & Strategic Insights     │
│  Extracting insights from data...                │
└───────────────────────────────────────────────────┘

Strategic Insights:

[H] Organic Traffic: Organic search is stable but limited by 60% of keywords ranking beyond page 1, leaving significant non-branded demand uncaptured.
[H] Competitive Position: Acme Corp trails competitors on domain authority by 15 points, which restricts ranking potential for high-volume commercial terms.
[M] User Engagement: Engagement rate declined 4% despite stable traffic, indicating content-intent mismatch that may erode conversion potential.
...

? Do these insights accurately reflect the data priorities? Proceed to Phase 2? Yes

...
```

## Output Files

After successful execution, the tool generates:

### 1. PowerPoint Presentation
- **Location**: `output/SEO_Audit_{BrandName}_{timestamp}.pptx`
- **Contains**: 26-slide professional presentation
- **Format**: PowerPoint (.pptx) compatible with Microsoft Office and Google Slides

### 2. JSON Content File
- **Location**: `output/SEO_Audit_{BrandName}_{timestamp}_content.json`
- **Contains**: Structured data for all slides
- **Use**: For custom integrations, further analysis, or template population

### File Structure

```json
{
  "metadata": {
    "brand_name": "YourBrand",
    "audit_month": "December 2024",
    "audit_period": "01/01/2024 - 30/11/2024",
    "tools_detected": ["GA4", "SEMrush", "Ahrefs"],
    "website_type": "ecommerce"
  },
  "organic_traffic": {
    "key_message": "Organic search is...",
    "observation": "...",
    "priority": "H",
    "channels": {...},
    ...
  },
  ...
}
```

## Project Structure

```
seo-audit-automation/
├── seo_audit_tool.py           # Main entry point
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── SKILL.md                    # Skill definition
├── slide_logic.md              # Analytical framework
├── template_rules.md           # Voice & tone guidelines
├── seo_audit_placeholder_mapping.md  # Slide structure
├── src/
│   ├── data_ingestion/         # Data loading modules
│   │   ├── __init__.py
│   │   └── data_loader.py
│   ├── analyzers/              # Phase 1 analysis
│   │   ├── __init__.py
│   │   ├── organic_traffic_analyzer.py
│   │   └── phase1_orchestrator.py
│   ├── narrative/              # Phase 2 narrative generation
│   │   ├── __init__.py
│   │   └── phase2_generator.py
│   ├── ppt_generator/          # Phase 3 PPT generation
│   │   ├── __init__.py
│   │   └── phase3_generator.py
│   ├── models/                 # Data models
│   │   ├── __init__.py
│   │   └── audit_data.py
│   └── utils/                  # Utilities
│       ├── __init__.py
│       └── logger.py
├── schema/                     # SEO tool schemas
│   ├── ga4_schema.md
│   ├── gsc_schema.md
│   ├── semrush_schema.md
│   ├── ahrefs_schema.md
│   ├── screaming_frog.md
│   └── pagespeed_schema.md
├── raw_data/                   # SEO data files (user-provided)
├── sample_report/              # Example reports
└── output/                     # Generated reports
```

## Troubleshooting

### Common Issues

#### 1. No data files found

**Error**: `No data files found or failed to load.`

**Solution**:
- Verify data files are in the correct directory
- Check file formats (must be .csv, .xlsx, or .xls)
- Ensure files contain valid SEO tool exports

#### 2. Tool type not detected

**Warning**: `Could not detect tool type for filename.csv`

**Solution**:
- Check that CSV/XLSX files have proper column headers
- Refer to "Required Data Files" section for expected columns
- Add manual detection logic in `src/data_ingestion/data_loader.py`

#### 3. Missing dependencies

**Error**: `ModuleNotFoundError: No module named 'pandas'`

**Solution**:
```bash
pip install -r requirements.txt
```

#### 4. Permission denied

**Error**: `PermissionError: [Errno 13] Permission denied`

**Solution**:
```bash
chmod +x seo_audit_tool.py
```

### Debug Mode

For detailed logging, use the `--verbose` flag:

```bash
python seo_audit_tool.py -d ./raw_data -b "YourBrand" --verbose
```

## Advanced Usage

### Custom Data Schemas

To add support for additional SEO tools:

1. Add schema documentation to `schema/` directory
2. Update `src/data_ingestion/data_loader.py`:
   - Add detection logic in `detect_file_type()`
   - Add getter method (e.g., `get_custom_tool_data()`)

### Custom Analyzers

To create custom analysis logic:

1. Create new analyzer in `src/analyzers/`
2. Import in `phase1_orchestrator.py`
3. Add to `execute()` method

### Template Customization

The tool follows rules from:
- `slide_logic.md` - Analysis framework
- `template_rules.md` - Voice, tone, formatting
- `seo_audit_placeholder_mapping.md` - Slide structure

Modify these files to customize output.

## Priority Badge System

| Badge | Label | Criteria | Meaning |
|-------|-------|----------|---------|
| **C** | Critical | Blocking core functionality, >20% traffic impact | Immediate action required |
| **H** | High | Significant ranking/traffic impact, competitive disadvantage | High priority fix |
| **M** | Medium | Optimization opportunity, incremental gains | Moderate priority |
| **L** | Low | Minor issues, nice-to-have improvements | Low priority |

## Website Type Variations

The tool adjusts analysis based on website type:

| Type | Focus Areas | Key Metrics |
|------|-------------|-------------|
| **ecommerce** | Product discoverability, category architecture | Revenue per session, product rankings |
| **saas** | BOFU intent, trust signals, solution awareness | Demo/trial conversions, competitor gap |
| **content** | Freshness, topical clustering, engagement | Pageviews, time on site, returning visitors |
| **local** | GMB optimization, local pack, NAP consistency | Local pack appearances, "near me" rankings |
| **marketplace** | Taxonomy coherence, internal linking | Category rankings, long-tail coverage |

## Contributing

This tool is designed to be extended. Key extension points:

1. **Analyzers**: Add new analysis modules in `src/analyzers/`
2. **Data Sources**: Add support for new tools in `src/data_ingestion/`
3. **Narrative Templates**: Customize voice/tone in `template_rules.md`
4. **Slide Logic**: Adjust analysis framework in `slide_logic.md`

## License

See project license file.

## Support

For issues or questions:
1. Check the Troubleshooting section above
2. Review example data in `raw_data/`
3. Examine sample reports in `sample_report/`
4. Check schema documentation in `schema/`

## Version

Version 1.0.0 - Initial Release

## Acknowledgments

Built following the SEO Audit Proposal Skill methodology for strategic, executive-ready SEO analysis.
