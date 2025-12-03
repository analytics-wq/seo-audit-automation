# Quick Start Guide

Get up and running with the SEO Audit Automation Tool in 5 minutes.

## Step 1: Install Dependencies

```bash
cd seo-audit-automation
pip install -r requirements.txt
```

## Step 2: Prepare Your Data

Create a directory for your SEO data and add your exports:

```bash
mkdir -p my_audit_data
```

Copy your SEO data files to `my_audit_data/`:
- GA4 export (CSV or XLSX)
- Google Search Console queries export
- SEMrush site audit export
- Ahrefs backlinks export (optional)
- Screaming Frog crawl data (optional)

## Step 3: Run the Tool

```bash
python seo_audit_tool.py \
  --data-dir ./my_audit_data \
  --brand-name "Your Company Name" \
  --website-type ecommerce
```

**For example with the sample data:**

```bash
python seo_audit_tool.py \
  --data-dir ./raw_data \
  --brand-name "Sample Brand" \
  --website-type ecommerce
```

## Step 4: Follow the Interactive Prompts

The tool will guide you through 3 phases:

### Phase 1: Data Analysis
- Tool loads and analyzes your data
- Displays strategic insights with priorities
- **You approve** to proceed to Phase 2

### Phase 2: Narrative Generation
- Tool crafts executive summary
- Shows you the storyline
- **You approve** to proceed to Phase 3

### Phase 3: PowerPoint Generation
- Tool generates final presentation
- Saves to `output/` directory

## Step 5: Get Your Results

Find your generated files in the `output/` directory:
- `SEO_Audit_{BrandName}_{timestamp}.pptx` - PowerPoint presentation
- `SEO_Audit_{BrandName}_{timestamp}_content.json` - Structured data

## Example Output

After running the tool, you'll see:

```
✓ PowerPoint generated: output/SEO_Audit_SampleBrand_raw_data.pptx
✓ Content JSON generated: output/SEO_Audit_SampleBrand_raw_data_content.json

✓ SEO Audit Complete!
```

## Troubleshooting

### Issue: "No data files found"
**Solution**: Make sure your data directory contains CSV or XLSX files

### Issue: "Could not detect tool type"
**Solution**: Check that your CSV/XLSX files have the proper column headers for your SEO tool

### Issue: "ModuleNotFoundError"
**Solution**: Run `pip install -r requirements.txt` again

## Next Steps

- Review the generated PowerPoint presentation
- Customize the analysis by modifying `slide_logic.md`
- Adjust the narrative voice in `template_rules.md`
- Add more data sources for deeper analysis

## Getting Help

- Read the full [README.md](README.md)
- Check the [schema](schema/) directory for data format specifications
- Review [SKILL.md](SKILL.md) for the strategic framework

## Tips for Best Results

1. **Use recent data**: Ideally last 6-12 months for trend analysis
2. **Include multiple tools**: More data sources = better insights
3. **Provide competitor data**: For competitive benchmarking
4. **Run with --verbose**: To see detailed analysis steps

```bash
python seo_audit_tool.py \
  --data-dir ./my_audit_data \
  --brand-name "Your Company" \
  --website-type saas \
  --verbose
```

## Sample Command Reference

```bash
# Basic usage
python seo_audit_tool.py -d ./raw_data -b "MyBrand"

# With website type
python seo_audit_tool.py -d ./raw_data -b "MyBrand" -w saas

# With verbose logging
python seo_audit_tool.py -d ./raw_data -b "MyBrand" -v

# Full command
python seo_audit_tool.py \
  --data-dir ./raw_data \
  --brand-name "My Company" \
  --website-type ecommerce \
  --verbose
```

Happy auditing! 🚀
