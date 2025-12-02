# SEO Audit Automation Tool - Usage Guide

## Table of Contents
1. [Quick Start](#quick-start)
2. [Understanding the Output](#understanding-the-output)
3. [Customization](#customization)
4. [Best Practices](#best-practices)
5. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Installation

```bash
# 1. Navigate to project directory
cd seo-audit-automation

# 2. Install dependencies
pip install -r requirements.txt

# Alternative: Install with ignore flag (if system conflicts)
pip install --ignore-installed -r requirements.txt
```

### Running the Tool

```bash
# Basic usage
python3 generate_seo_report.py

# The script will:
# 1. Look for PDF in raw_data/Semrush-Full_Site_Audit_Report_schema.pdf
# 2. Extract health score, errors, and technical issues
# 3. Generate SEO_Strategy.pptx in the project root
```

### Expected Output

```
============================================================
SEO AUDIT AUTOMATION TOOL
Adopting Senior SEO Strategist Persona
============================================================

PHASE 1: DATA EXTRACTION
📄 Opening PDF...
   ✓ Health Score: 75%
   ✓ Total Errors: 500
   ✓ Found: Internal links are broken (53 instances)
   ✓ Found: duplicate meta descriptions (277 instances)
   ...

PHASE 2: STRATEGIC NARRATIVE GENERATION
🎨 Generating PowerPoint presentation...
✅ Presentation generated!

PHASE 3: SAVING PRESENTATION
✅ Presentation saved: SEO_Strategy.pptx

EXECUTION COMPLETE
📊 Health Score: 75%
🔧 Technical Issues: 8
📝 Meta Issues: 4
📄 Total Slides: 14
```

---

## Understanding the Output

### Presentation Structure

The generated PowerPoint contains 14 slides organized into 6 chapters:

#### **Chapter 1: Setup (Slides 1-4)**
- **Slide 1: Cover** - Client branding and audit period
- **Slide 2: Overview** - Audit scope and methodology
- **Slide 3: Planning Phase** - Strategic context
- **Slide 4: Index** - Table of contents

#### **Chapter 2: Executive Summary (Slide 5)**
- **Slide 5: Path to Digital Visibility**
  - Synthesizes all findings into C-suite language
  - Presents dominant strategic theme
  - Frames technical issues as business constraints

#### **Chapter 3: Where You Stand (Slides 6-7)**
- **Slide 6: Site Health Assessment**
  - Health score with business interpretation
  - Pages crawled and error counts
  - Priority badge (C/H/M/L)
  - Business impact statement

#### **Chapter 4: Content Gaps (Slide 8)**
- **Slide 8: Meta Tags & Content Signals**
  - On-page optimization issues
  - Duplicate/missing titles and descriptions
  - H1 structure problems
  - CTR suppression analysis

#### **Chapter 5: Technical Gaps (Slide 9)**
- **Slide 9: Technical Barriers to Growth**
  - Crawlability/indexability issues
  - Broken links and redirect chains
  - JavaScript/CSS caching problems
  - Each issue includes:
    - Business-focused description
    - Impact on rankings/traffic
    - Recommended action

#### **Chapter 6: Path Forward (Slides 10-14)**
- **Slide 10: Strategic Action Plan**
  - Consolidated findings
  - Prioritized by business impact
  - Next steps organized by pillar:
    - Technical SEO
    - Content SEO
    - Domain Authority

---

## Customization

### 1. Client Branding

Edit `generate_seo_report.py`:

```python
class SEOStrategist:
    def __init__(self):
        self.brand_name = "Acme Corporation"  # Change this
        self.audit_date = "December 2025"      # Change this
```

### 2. Color Scheme

Modify color values in PowerPoint generation methods:

```python
# In _add_cover_slide()
title_text.font.color.rgb = RGBColor(0, 32, 96)  # Dark blue
# Change to your brand colors:
# RGBColor(R, G, B) where each value is 0-255
```

### 3. Font Sizes

Adjust presentation text sizes:

```python
# In any slide generation method
p.font.size = Pt(16)  # Change point size
# Common sizes:
# - Headings: Pt(36-44)
# - Subheadings: Pt(18-24)
# - Body text: Pt(14-16)
# - Fine print: Pt(10-12)
```

### 4. Adding New Issue Patterns

Extend the issue detection in `_parse_issues()`:

```python
issue_patterns = {
    # Existing patterns...
    "Your Custom Issue": r'(\d{1,3}(?:,\d{3})*)\s+.*?custom\s+pattern',
}
```

### 5. Custom Business Impact Translations

Add new translations in `translate_to_business_impact()`:

```python
impact_map = {
    # Existing translations...
    "your issue name": {
        "issue": "Clear problem statement",
        "impact": "**Business consequence** explained",
        "action": "Specific remediation step"
    }
}
```

---

## Best Practices

### Data Preparation

1. **Use Recent Data**: Ensure your SEMrush PDF is from the last 30 days
2. **Complete Crawl**: Let SEMrush complete a full site crawl before exporting
3. **PDF Quality**: Export as PDF, not print-to-PDF (maintains text structure)

### Strategic Narrative

1. **Know Your Audience**: Adjust language based on:
   - **C-Suite**: Focus on revenue, market share, competitive position
   - **Marketing Director**: Balance technical + business impact
   - **SEO Team**: Include more tactical details

2. **Prioritization**:
   - **Critical (C)**: Show immediate revenue risk
   - **High (H)**: Emphasize competitive disadvantage
   - **Medium (M)**: Frame as optimization opportunity
   - **Low (L)**: Note for completeness

3. **Framing Issues**:
   ```
   ❌ "500 pages have duplicate meta descriptions"
   ✅ "Meta tag inconsistencies across 500 pages suppress click-through
      potential, leaving qualified demand flowing to competitors"
   ```

### Presentation Delivery

1. **Executive Summary First**: Start with Slide 5 in live presentations
2. **Data on Demand**: Keep detailed slides ready but don't lead with them
3. **Action-Oriented**: End every section with "What we do next"

---

## Troubleshooting

### Issue: "PDF not found"

**Error Message:**
```
❌ Error: PDF not found at /path/to/pdf
```

**Solution:**
1. Verify PDF exists in `raw_data/` folder
2. Check filename matches: `Semrush-Full_Site_Audit_Report_schema.pdf`
3. Ensure no spaces/special characters in path

---

### Issue: "Health Score not found"

**Warning Message:**
```
⚠ Health Score not found - using default 75%
```

**Explanation:**
- SEMrush PDFs have varying structures
- Tool searches for multiple patterns but may not find all
- Default value allows processing to continue

**Solution:**
- Review generated slides to verify other data extracted correctly
- Manually update slide if needed
- Add custom pattern if you know PDF structure:
  ```python
  patterns = [
      r'Your Custom Pattern: (\d+)%',
  ]
  ```

---

### Issue: "Module not found" errors

**Error Message:**
```
ModuleNotFoundError: No module named 'pdfplumber'
```

**Solution:**
```bash
# Standard install
pip install -r requirements.txt

# If conflicts with system packages
pip install --ignore-installed -r requirements.txt

# Force specific versions
pip install pdfplumber==0.11.8 python-pptx==1.0.2
```

---

### Issue: Cryptography errors

**Error Message:**
```
ModuleNotFoundError: No module named '_cffi_backend'
```

**Solution:**
```bash
# Install/upgrade dependencies
pip install --ignore-installed cffi cryptography

# Verify installation
python3 -c "import cffi; import cryptography; print('OK')"
```

---

### Issue: "No technical issues found"

**Warning:**
```
Total technical issues found: 0
```

**Causes:**
1. PDF text extraction failed
2. Pattern matching didn't recognize issue names
3. PDF has unusual structure

**Solutions:**
1. **Verify PDF content**:
   ```python
   import pdfplumber
   with pdfplumber.open("your.pdf") as pdf:
       text = pdf.pages[0].extract_text()
       print(text[:500])  # Check first 500 chars
   ```

2. **Update regex patterns**:
   ```python
   # Add debug output in _parse_issues()
   print(f"Searching for: {issue_name}")
   print(f"Match found: {match is not None}")
   ```

3. **Manual verification**:
   - Open PDF and locate issue section
   - Find exact text format
   - Update pattern to match

---

### Issue: Presentation formatting issues

**Problem:** Text overlaps, sizes are wrong, colors don't match

**Solutions:**
1. **Adjust text box sizes**:
   ```python
   content_box = slide.shapes.add_textbox(
       Inches(1),    # Left position
       Inches(2),    # Top position
       Inches(8),    # Width
       Inches(4)     # Height - increase if text cuts off
   )
   ```

2. **Enable word wrap**:
   ```python
   tf.word_wrap = True
   ```

3. **Add spacing**:
   ```python
   p.space_after = Pt(20)  # Add space after paragraph
   ```

---

## Advanced Techniques

### Batch Processing Multiple Clients

```python
import os
from pathlib import Path

clients = {
    "ClientA": "raw_data/ClientA_audit.pdf",
    "ClientB": "raw_data/ClientB_audit.pdf",
    "ClientC": "raw_data/ClientC_audit.pdf",
}

for client_name, pdf_path in clients.items():
    print(f"\n{'='*60}")
    print(f"Processing: {client_name}")
    print('='*60)

    strategist = SEOStrategist()
    strategist.brand_name = client_name

    extractor = PDFDataExtractor(pdf_path)
    data = extractor.extract_all_data()

    generator = PowerPointGenerator(strategist, data)
    prs = generator.generate_presentation()

    output_path = f"output/{client_name}_SEO_Strategy.pptx"
    prs.save(output_path)

    print(f"✅ Saved: {output_path}")
```

### Logging and Debugging

Add comprehensive logging:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('seo_audit.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# In your code
logger.info(f"Processing PDF: {pdf_path}")
logger.warning(f"Health score not found, using default")
logger.error(f"Failed to extract data: {error}")
```

### Export to Multiple Formats

```python
# Save as PDF (requires additional library)
from pptx2pdf import convert

prs.save("output.pptx")
convert("output.pptx", "output.pdf")

# Generate summary report
with open("audit_summary.txt", "w") as f:
    f.write(f"Client: {strategist.brand_name}\n")
    f.write(f"Health Score: {data['site_health']['score']}%\n")
    f.write(f"Technical Issues: {len(data['technical_issues'])}\n")
    f.write(f"Meta Issues: {len(data['meta_issues'])}\n")
```

---

## Performance Optimization

### Large PDF Files

For PDFs > 100 pages:

```python
# Process specific page ranges
def extract_from_range(pdf_path, start_page, end_page):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages[start_page:end_page]:
            text += page.extract_text()
    return text

# Use multiprocessing
from concurrent.futures import ProcessPoolExecutor

def process_page(page):
    return page.extract_text()

with pdfplumber.open(pdf_path) as pdf:
    with ProcessPoolExecutor() as executor:
        texts = list(executor.map(process_page, pdf.pages))
```

---

## Support Resources

- **Documentation**: See `SKILL.md` for persona details
- **Slide Logic**: See `slide_logic.md` for analytical framework
- **Template Rules**: See `template_rules.md` for writing style
- **Schema Reference**: See `schema/` folder for data structures

---

**Questions? Issues? Feature Requests?**

Open an issue on GitHub or contact the development team.

**Happy Auditing! 🚀**
