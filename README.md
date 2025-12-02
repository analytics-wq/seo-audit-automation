# SEO Audit Automation Tool

**Transform technical SEO data into executive-ready strategic narratives**

![Version](https://img.shields.io/badge/version-1.0-blue)
![Python](https://img.shields.io/badge/python-3.11+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

---

## 🎯 Overview

This automation tool extracts data from SEMrush Site Audit PDFs and generates compelling PowerPoint presentations that transform technical findings into C-suite business language.

**Persona:** Senior SEO Strategist with 20+ years of experience
**Philosophy:** Human-centric first, ecosystem thinking, urgency & loss aversion

---

## ✨ Key Features

### Strategic Narrative Generation
- **Business-First Language**: Translates technical jargon into executive impact
- **Unified Key Messages**: Every slide includes insight + significance + consequence
- **Priority-Based Analysis**: Automatically assigns C/H/M/L badges based on business impact

### Automated Data Extraction
- **PDF Parsing**: Uses pdfplumber to extract structured data from SEMrush reports
- **Pattern Recognition**: Identifies 12+ critical issue types automatically
- **Smart Fallbacks**: Uses defaults when data is incomplete

### Professional Presentation
- **26 Strategic Slides**: Complete audit framework (Index 0-25)
- **Executive Summary**: Generated from section insights
- **Business Impact Translation**: Technical issues → Revenue risk/opportunity
- **7 Chapters**: Setup → Executive Summary → Analysis → Action Plan

---

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd seo-audit-automation

# Install Python dependencies
pip install pdfplumber python-pptx

# (Optional) Install additional packages for advanced features
pip install --ignore-installed cffi cryptography
```

### 2. Prepare Your Data

Place your SEMrush Site Audit PDF in the `raw_data/` folder:

```
raw_data/
└── Semrush-Full_Site_Audit_Report_schema.pdf
```

### 3. Run the Tool

```bash
python3 generate_seo_report.py
```

### 4. Output

The tool generates `SEO_Strategy.pptx` with:
- ✅ Cover slide with branding
- ✅ Executive summary with strategic insights
- ✅ Site health analysis with business impact
- ✅ Meta tag issues with visibility consequences
- ✅ Technical barriers with ranking implications
- ✅ Action plan with prioritized recommendations

---

## 📊 Slide Structure (26 Slides Total)

### Chapter 1: Setup (Slides 0-3)
- **Slide 0: Cover** - Title and audit period
- **Slide 1: Overview** - Framework and methodology
- **Slide 2: Planning Phase** - Strategic context
- **Slide 3: Index** - Navigation structure

### Chapter 2: Executive Summary (Slide 4)
- **Slide 4: Path to Digital Visibility**
- 4-column strategic summary (General/Content/Technical/Authority)
- Generated from section summaries
- Translates technical debt → business constraint

### Chapter 3: Where You Stand (Slides 5-10)
- **Slide 5: Section Divider**
- **Slide 6: Organic Traffic Analysis** - Channel mix & keyword positioning
- **Slide 7: Competitive Benchmarking** - Market position assessment
- **Slide 8: User Engagement Quality** - Traffic quality metrics
- **Slide 9: Site Health Assessment** - Technical foundation analysis
- **Slide 10: Section Summary** - 3-box layout (Issue → Impact → Action)

### Chapter 4: Content Gaps (Slides 11-15)
- **Slide 11: Section Divider**
- **Slide 12: Meta Tags & Heading** - On-page optimization gaps
- **Slide 13: Keyword Gap Analysis** - Uncaptured demand
- **Slide 14: Keyword Intent Distribution** - Funnel coverage
- **Slide 15: Section Summary** - 3-box layout (Issue → Impact → Action)

### Chapter 5: Technical Gaps (Slides 16-18)
- **Slide 16: Section Divider**
- **Slide 17: Technical SEO Issues** - Crawlability/indexability barriers
- **Slide 18: Section Summary** - 3-box layout (Issue → Impact → Action)

### Chapter 6: Domain Authority (Slides 19-21)
- **Slide 19: Section Divider**
- **Slide 20: Domain Authority Assessment** - Competitive authority gap
- **Slide 21: Section Summary** - 3-box layout (Issue → Impact → Action)

### Chapter 7: Path Forward (Slides 22-25)
- **Slide 22: Section Divider**
- **Slide 23: SEO Audit Findings Summary** - 3-column action plan (Technical/Content/Authority)
- **Slide 24: KPI Targets & Benchmarks** - Success metrics
- **Slide 25: Thank You** - Professional close

---

## 🧠 Strategic Narrative Framework

### The "So What?" Test
Every insight must answer:
- **What's happening?** (Data observation)
- **Why does it matter?** (Business significance)
- **What's the cost of inaction?** (Consequence)

### Phrasing Patterns

| ❌ Technician | ✅ Strategic Partner |
|--------------|---------------------|
| "Get more traffic" | "Establish digital pipeline for qualified opportunities" |
| "We did keyword research" | "Deployed needs-led content strategy" |
| "Rankings improved" | "Secured market leadership position" |
| "Traffic dropped 15%" | "Volatility destabilized traffic flow" |

### Priority Assignment

| Badge | Label | Criteria | Example |
|-------|-------|----------|---------|
| **C** | Critical | >20% impact, blocking core function | Health score <60% |
| **H** | High | Significant ranking/traffic impact | >500 technical errors |
| **M** | Medium | Optimization opportunity | Minor meta tag issues |
| **L** | Low | Nice-to-have improvements | Cosmetic fixes |

---

## 🔧 Configuration

### Customization Options

Edit the script to customize:

```python
# In SEOStrategist.__init__()
self.brand_name = "Your Client Name"  # Default: "Client"
self.audit_date = "December 2025"     # Default: Current month
```

### Adding New Issue Patterns

In `PDFDataExtractor._parse_issues()`:

```python
issue_patterns = {
    "Your New Issue": r'(\d{1,3}(?:,\d{3})*)\s+.*?your\s+pattern',
    # Add more patterns...
}
```

### Slide Layout Customization

Modify `PowerPointGenerator` class methods:
- `_add_cover_slide()` - Branding and colors
- `_add_executive_summary_slide()` - Summary structure
- `_add_technical_issues_slide()` - Issue presentation

---

## 📁 Project Structure

```
seo-audit-automation/
├── generate_seo_report.py          # Main automation script
├── SKILL.md                         # Persona and operational protocol
├── slide_logic.md                   # Analytical framework per slide
├── template_rules.md                # Communication style guide
├── seo_audit_placeholder_mapping.md # Data structure reference
├── schema/                          # Data schema definitions
│   ├── ga4_schema.md
│   ├── gsc_schema.md
│   ├── semrush_schema.md
│   ├── ahrefs_schema.md
│   └── screaming_frog.md
├── raw_data/                        # Input data (PDFs, CSVs)
│   └── Semrush-Full_Site_Audit_Report_schema.pdf
├── sample_report/                   # Reference examples
└── SEO_Strategy.pptx               # Generated output
```

---

## 💡 Advanced Usage

### Batch Processing

Process multiple client reports:

```python
clients = ["ClientA", "ClientB", "ClientC"]

for client in clients:
    strategist = SEOStrategist()
    strategist.brand_name = client

    pdf_path = f"raw_data/{client}_audit.pdf"
    output_path = f"output/{client}_SEO_Strategy.pptx"

    # ... rest of processing
```

### Custom Data Sources

Extend the extractor to support additional tools:

```python
class MultiSourceExtractor(PDFDataExtractor):
    def extract_ahrefs_data(self, csv_path):
        # Parse Ahrefs export
        pass

    def extract_gsc_data(self, xlsx_path):
        # Parse Google Search Console
        pass
```

### API Integration

Connect to live data sources:

```python
import requests

def fetch_semrush_api(domain, api_key):
    url = f"https://api.semrush.com/?key={api_key}&domain={domain}"
    response = requests.get(url)
    return response.json()
```

---

## 🎨 Design Philosophy

### Human-Centric First
Start with consumer need, not algorithm. Frame findings as customer journey friction.

### Ecosystem Thinking
View SEO as part of larger digital machine (omnichannel, social, brand health).

### Urgency & Loss Aversion
Use language implying cost of inaction:
- "**Uncaptured demand**"
- "**Leaking revenue**"
- "**Eroding market share**"

### Problem-Focused, Not Metric-Focused
Lead with business problem, support with data — never reverse.

---

## 📝 Data Sources Supported

| Tool | Data Type | Used For |
|------|-----------|----------|
| **SEMrush Site Audit** | Technical crawl | Health score, errors, warnings |
| Google Analytics 4 | Traffic | Channel mix, geography, engagement |
| Google Search Console | Performance | CTR, position, impressions |
| Ahrefs | Backlinks | Domain rating, referring domains |
| Screaming Frog | Crawl data | Meta tags, H1, title issues |

---

## 🔍 Troubleshooting

### "Health Score not found"
**Cause:** PDF structure varies by report
**Fix:** Script uses default 75% and continues processing

### "No technical issues found"
**Cause:** Pattern matching didn't recognize issue names
**Fix:** Update regex patterns in `issue_patterns` dictionary

### "Module not found" errors
**Cause:** Missing dependencies
**Fix:** Run `pip install --ignore-installed cffi cryptography pdfplumber python-pptx`

### PDF too large warning
**Cause:** File exceeds expected size
**Fix:** Tool handles this automatically, extraction may take longer

---

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Contribution Ideas
- Add support for additional SEO tools (Moz, Majestic)
- Create custom slide templates
- Build data visualization charts
- Implement natural language generation for insights

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgments

- **SEMrush** for comprehensive site audit capabilities
- **pdfplumber** for robust PDF parsing
- **python-pptx** for PowerPoint generation
- **SEO Community** for insights on strategic communication

---

## 📧 Support

For questions, issues, or feature requests:
- Open an issue on GitHub
- Contact: [your-email@domain.com]
- Documentation: See `SKILL.md` and `slide_logic.md`

---

## 🚀 Roadmap

### Version 1.1 (Q1 2026)
- [ ] Multi-file batch processing
- [ ] Custom color themes
- [ ] Chart/graph generation
- [ ] Export to PDF format

### Version 2.0 (Q2 2026)
- [ ] Web interface (Streamlit/Flask)
- [ ] Real-time API integrations
- [ ] AI-powered insight generation
- [ ] Competitor comparison slides

---

**Built with ❤️ by SEO Strategists, for SEO Strategists**
