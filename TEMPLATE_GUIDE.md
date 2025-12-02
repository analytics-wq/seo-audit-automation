# Template-Based PowerPoint Generation Guide

## Overview

The SEO Audit tool now uses a **template-based approach** to generate standardized, professional presentations. Instead of creating slides from scratch, the tool loads a pre-formatted template and populates placeholders with extracted data.

This ensures **consistent branding** and **professional output** matching the `brand_template_ppt_report.pdf` reference.

---

## How It Works

### 1. Template Loading

```python
# In generate_seo_report.py
template_file = Path(__file__).parent / "template_base.pptx"
prs = Presentation(str(template_file))
```

The script automatically loads `template_base.pptx` when generating reports.

### 2. Placeholder Population

The template contains placeholder text that gets replaced with actual data:

| Placeholder | Replaced With | Example |
|-------------|---------------|---------|
| `{Brand}` | Client name | "Acme Corporation" |
| `{Logo}` | Logo path/text | "[Client Logo]" |
| `{Current month}` | Audit date | "December 2025" |
| `{Key Highlight}` | Strategic insight | "Site health at 75% indicates..." |
| `{Priority}` | Priority badge | "🟡 MEDIUM" |
| `{Observation & Analysis}` | Supporting data | "Crawled 10,000 pages..." |
| `{Summary *}` | Section summaries | Executive summary text |

### 3. Template Structure

The template contains 26 pre-formatted slides:

```
Slides 0-3:   Setup (Cover, Overview, Planning, Index)
Slide 4:      Executive Summary (4-column layout)
Slides 5-10:  Where You Stand (includes section divider, data, summary)
Slides 11-15: Content Gaps (includes section divider, data, summary)
Slides 16-18: Technical Gaps (includes section divider, data, summary)
Slides 19-21: Domain Authority (includes section divider, data, summary)
Slides 22-25: Path Forward (includes divider, findings, KPIs, thank you)
```

---

## Customizing the Template

### Option 1: Modify the Template File Directly

1. **Open the template**:
   ```bash
   open template_base.pptx  # macOS
   # or
   start template_base.pptx  # Windows
   # or
   xdg-open template_base.pptx  # Linux
   ```

2. **Edit slides**:
   - Change colors, fonts, layouts
   - Add your company logo
   - Modify placeholder text positions
   - Adjust text box sizes

3. **Save the template**:
   - Keep the filename as `template_base.pptx`
   - Preserve placeholder text (e.g., `{Brand}`, `{Key Highlight}`)

4. **Test**:
   ```bash
   python3 generate_seo_report.py
   ```

### Option 2: Regenerate Template Programmatically

Edit `create_template.py` to customize:

```python
# Brand colors
BRAND_PRIMARY = RGBColor(0, 32, 96)      # Dark blue
BRAND_SECONDARY = RGBColor(156, 39, 176)  # Purple
BRAND_ACCENT = RGBColor(255, 193, 7)      # Yellow/Gold

# Change to your brand colors:
BRAND_PRIMARY = RGBColor(255, 0, 0)      # Red
BRAND_SECONDARY = RGBColor(0, 128, 255)  # Light blue
BRAND_ACCENT = RGBColor(255, 215, 0)     # Gold
```

Then regenerate:

```bash
python3 create_template.py
# This creates a new template_base.pptx
```

### Option 3: Use a Different Template File

1. **Create your custom template**:
   - Name it `my_custom_template.pptx`
   - Include 26 slides with placeholders

2. **Specify in code**:
   ```python
   # In main() function:
   generator = PowerPointGenerator(strategist, extracted_data,
                                   template_path="my_custom_template.pptx")
   ```

---

## Brand Colors Reference

The default template uses these colors:

```python
BRAND_PRIMARY   = RGBColor(0, 32, 96)      # #002060 Dark Navy Blue
BRAND_SECONDARY = RGBColor(156, 39, 176)   # #9C27B0 Purple
BRAND_ACCENT    = RGBColor(255, 193, 7)    # #FFC107 Amber/Gold
TEXT_GRAY       = RGBColor(100, 100, 100)  # #646464 Medium Gray
```

### How to Change Colors

**In PowerPoint (Manual)**:
1. Open `template_base.pptx`
2. Select text/shape
3. Format → Text Fill/Shape Fill → More Colors → Custom RGB

**In Code (Programmatic)**:
```python
# In create_template.py, change the color values:
BRAND_PRIMARY = RGBColor(R, G, B)  # Replace R, G, B with your values

# Examples:
# Red: RGBColor(255, 0, 0)
# Green: RGBColor(0, 128, 0)
# Blue: RGBColor(0, 0, 255)
# Orange: RGBColor(255, 165, 0)
```

---

## Adding Your Company Logo

### Method 1: Replace Placeholder in Template

1. Open `template_base.pptx`
2. Go to Slide 0 (Cover page)
3. Delete the `{Logo}` text box
4. Insert → Picture → Select your logo
5. Position: Top right corner (8 inches from left, 0.5 inches from top)
6. Resize: Width ~1.5 inches
7. Save template

### Method 2: Programmatic Logo Insertion

Add to `generate_seo_report.py`:

```python
def _add_logo_to_slide(self, slide, logo_path):
    """Add company logo to slide"""
    logo = slide.shapes.add_picture(
        logo_path,
        left=Inches(8),
        top=Inches(0.5),
        height=Inches(0.8)
    )

# In _populate_template():
if Path("client_logo.png").exists():
    self._add_logo_to_slide(self.prs.slides[0], "client_logo.png")
```

---

## Slide Layout Types

The template uses 3 layout types:

### 1. **Data Slide** (Most Common)
Used for: Organic Traffic, Competitive Benchmarking, Site Health, etc.

```
┌─────────────────────────────────────┐
│ Title                    [Priority] │
│─────────────────────────────────────│
│ KEY INSIGHT                         │
│ {Key Highlight}                     │
│─────────────────────────────────────│
│ {Observation & Analysis}            │
│                                     │
│ [Charts and data visualizations]   │
└─────────────────────────────────────┘
```

### 2. **Summary Slide**
Used for: Section summaries (Slides 10, 15, 18, 21)

```
┌─────────────────────────────────────┐
│ Summary Title                       │
│─────────────────────────────────────│
│ 📋 What is the Issue?              │
│ • {Issue description}              │
│                                     │
│ 💥 What is the Impact?             │
│ • {Business impact}                │
│                                     │
│ 🎯 Our Next Action                 │
│ • {Recommended action}             │
└─────────────────────────────────────┘
```

### 3. **Section Divider**
Used for: Chapter introductions (Slides 5, 11, 16, 19, 22)

```
┌─────────────────────────────────────┐
│                                     │
│                                     │
│        Section Title Text           │
│                                     │
│                                     │
└─────────────────────────────────────┘
```

---

## Placeholder Reference Table

Complete list of placeholders used in the template:

| Slide | Placeholder | Purpose | Data Source |
|-------|-------------|---------|-------------|
| 0 | `{Brand}` | Client name | User input |
| 0 | `{Logo}` | Company logo | User upload |
| 0 | `{Current month}` | Audit date | System date |
| 4 | `{Summary general overview}` | Executive summary column 1 | Generated |
| 4 | `{Summary content seo}` | Executive summary column 2 | Generated |
| 4 | `{Summary technical seo}` | Executive summary column 3 | Generated |
| 4 | `{Summary domain authority}` | Executive summary column 4 | Generated |
| 5-25 | `{Brand}` | Client name (repeated) | User input |
| 6-24 | `{Priority}` | Priority badge | Calculated |
| 6-24 | `{Key Highlight}` | Unified key message | Generated |
| 6-24 | `{Observation & Analysis}` | Supporting details | Extracted/Generated |
| 10,15,18,21 | `{Summary content...}` | Section summary text | Generated |

---

## Fallback Mode

If `template_base.pptx` is not found, the script automatically falls back to **from-scratch generation**:

```
⚠ Template not found at /path/to/template_base.pptx
⚠ Using from-scratch generation (fallback mode)
```

This ensures the tool works even without the template file, though output won't be standardized.

---

## Testing Your Customized Template

### 1. Visual Inspection

```bash
python3 generate_seo_report.py
# Open SEO_Strategy.pptx
# Check: colors, fonts, layouts, placeholders replaced
```

### 2. Verify Placeholder Replacement

Ensure no placeholders remain in the output:
- Search for `{Brand}` → Should be replaced with client name
- Search for `{Key Highlight}` → Should be replaced with insights
- Search for `{Logo}` → Should be replaced or have actual logo

### 3. Check All Slides

Go through all 26 slides and verify:
- [ ] Slide 0: Cover with client name and date
- [ ] Slides 1-3: Setup slides present
- [ ] Slide 4: Executive summary populated
- [ ] Slides 5-25: All data slides populated
- [ ] No placeholder text visible

---

## Troubleshooting

### Template Not Loading

**Error:**
```
⚠ Template not found at /path/to/template_base.pptx
```

**Solution:**
```bash
# Regenerate template
python3 create_template.py

# Or ensure template is in same directory as script
ls template_base.pptx  # Should exist
```

### Placeholders Not Replaced

**Problem:** Output still shows `{Brand}` or `{Key Highlight}`

**Solution:**
1. Check placeholder spelling in template (case-sensitive!)
2. Ensure placeholders are in text boxes, not shapes
3. Verify `_replace_placeholder()` method is working

```python
# Test placeholder replacement
generator._replace_placeholder(slide, "{Brand}", "Test Company")
```

### Colors Not Matching Brand

**Solution:**
```bash
# Option 1: Edit template manually
open template_base.pptx
# Change colors via PowerPoint UI

# Option 2: Regenerate with new colors
# Edit create_template.py → Update BRAND_* colors → Run
python3 create_template.py
```

### Slide Layout Broken

**Problem:** Text overlaps, boxes misaligned

**Solution:**
1. Open `template_base.pptx` in PowerPoint
2. Adjust text box positions and sizes
3. Save template
4. Regenerate report

---

## Advanced Customization

### Add Custom Fonts

```python
# In create_template.py
brand_p.font.name = "Your Custom Font"  # e.g., "Arial", "Helvetica"
```

### Add Background Image

```python
# In _add_cover_slide()
background = slide.shapes.add_picture(
    "background.jpg",
    left=0,
    top=0,
    width=prs.slide_width,
    height=prs.slide_height
)
# Send to back
slide.shapes._spTree.remove(background._element)
slide.shapes._spTree.insert(2, background._element)
```

### Add Custom Slide Layouts

```python
# In create_template.py, add new slide method:
def _add_custom_layout_slide(self):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    # Add your custom elements
    # ...
```

---

## Best Practices

1. **Preserve Placeholders**: Always keep placeholder text like `{Brand}` until they're replaced by code
2. **Test After Changes**: Run `python3 generate_seo_report.py` after every template modification
3. **Version Control**: Keep backup copies of working templates
4. **Document Changes**: Note any custom modifications in comments
5. **Consistent Naming**: Use descriptive placeholder names (e.g., `{Client_Company_Name}` instead of `{X}`)

---

## Example: Creating a Custom Template

Here's a complete example of creating a custom-branded template:

```python
#!/usr/bin/env python3
# my_custom_template.py

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# Define your brand colors
MY_BRAND_PRIMARY = RGBColor(10, 80, 160)    # Your company blue
MY_BRAND_ACCENT = RGBColor(255, 100, 50)     # Your company orange

prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Slide 0: Custom cover
slide = prs.slides.add_slide(prs.slide_layouts[6])

# Add company logo
logo = slide.shapes.add_picture(
    "my_company_logo.png",
    left=Inches(0.5),
    top=Inches(0.5),
    height=Inches(1)
)

# Add title with your brand color
title_box = slide.shapes.add_textbox(Inches(1.5), Inches(3), Inches(7), Inches(2))
title_frame = title_box.text_frame
title_p = title_frame.paragraphs[0]
title_p.text = "SEO Audit\n{Brand}"
title_p.font.size = Pt(48)
title_p.font.bold = True
title_p.font.color.rgb = MY_BRAND_PRIMARY

# ... add remaining 25 slides ...

# Save
prs.save("my_company_template.pptx")
```

Then use it:

```python
# In generate_seo_report.py main():
generator = PowerPointGenerator(strategist, extracted_data,
                               template_path="my_company_template.pptx")
```

---

## Support

For issues or questions:
- Check `template_base.pptx` structure
- Review `create_template.py` code
- Test with `python3 create_template.py`
- Verify placeholder names match exactly

**Remember**: The template system ensures **consistent, professional output** while maintaining flexibility for customization!
