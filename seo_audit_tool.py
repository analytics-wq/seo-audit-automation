#!/usr/bin/env python3
"""
SEO Audit Automation Tool - Main Entry Point

This tool follows a 3-phase workflow:
1. Phase 1: Data Analysis & Strategic Insights
2. Phase 2: Narrative & Storyline Architecture
3. Phase 3: Final PowerPoint Output Generation

Each phase requires user approval before proceeding to the next.
"""
import sys
import logging
from pathlib import Path
import click
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.markdown import Markdown
import questionary
import json

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.utils.logger import setup_logger
from src.data_ingestion.data_loader import DataLoader
from src.analyzers.phase1_orchestrator import Phase1Orchestrator
from src.narrative.phase2_generator import Phase2Generator
from src.ppt_generator.phase3_generator import Phase3Generator

console = Console()
logger = logging.getLogger(__name__)


class SEOAuditTool:
    """Main SEO Audit Tool orchestrator."""

    def __init__(self, data_dir: Path, brand_name: str, website_type: str):
        """Initialize the tool.

        Args:
            data_dir: Directory containing SEO data files
            brand_name: Client brand name
            website_type: Type of website
        """
        self.data_dir = data_dir
        self.brand_name = brand_name
        self.website_type = website_type
        self.phase1_results = None
        self.phase2_results = None
        self.phase3_results = None

    def run(self):
        """Run the complete 3-phase workflow."""
        console.print(Panel.fit(
            "[bold blue]SEO Audit Automation Tool[/bold blue]\n"
            f"Client: {self.brand_name}\n"
            f"Website Type: {self.website_type}",
            title="Welcome"
        ))

        # Load data
        if not self._load_data():
            console.print("[red]Failed to load data. Exiting.[/red]")
            return False

        # Phase 1: Data Analysis & Strategic Insights
        if not self._run_phase1():
            console.print("[red]Phase 1 failed. Exiting.[/red]")
            return False

        # Phase 2: Narrative & Storyline Architecture
        if not self._run_phase2():
            console.print("[red]Phase 2 failed. Exiting.[/red]")
            return False

        # Phase 3: Final PowerPoint Output
        if not self._run_phase3():
            console.print("[red]Phase 3 failed. Exiting.[/red]")
            return False

        console.print("\n[bold green]✓ SEO Audit Complete![/bold green]")
        return True

    def _load_data(self) -> bool:
        """Load and validate data files."""
        console.print(f"\n[bold]Loading data from {self.data_dir}...[/bold]")

        self.data_loader = DataLoader(self.data_dir)
        loaded_data = self.data_loader.load_all_files()

        if not loaded_data:
            console.print("[red]No data files found or failed to load.[/red]")
            return False

        # Display loaded data summary
        table = Table(title="Loaded Data Summary")
        table.add_column("Tool", style="cyan")
        table.add_column("Rows", justify="right", style="green")

        for key, df in loaded_data.items():
            table.add_row(key, str(len(df)))

        console.print(table)

        date_range = self.data_loader.get_date_range()
        console.print(f"[blue]Data period: {date_range[0]} - {date_range[1]}[/blue]")

        return True

    def _run_phase1(self) -> bool:
        """Execute Phase 1: Data Analysis & Strategic Insights."""
        console.print(Panel(
            "[bold yellow]Phase 1: Data Analysis & Strategic Insights[/bold yellow]\n"
            "Extracting insights from data and identifying critical priorities...",
            title="Phase 1"
        ))

        try:
            orchestrator = Phase1Orchestrator(
                self.data_loader,
                self.brand_name,
                self.website_type
            )

            self.phase1_results = orchestrator.execute()

            # Display insights summary
            self._display_phase1_insights()

            # Ask for approval
            return self._get_phase_approval(
                phase_num=1,
                question="Do these insights accurately reflect the data priorities?"
            )

        except Exception as e:
            logger.error(f"Phase 1 error: {e}", exc_info=True)
            console.print(f"[red]Error in Phase 1: {e}[/red]")
            return False

    def _display_phase1_insights(self):
        """Display Phase 1 insights summary."""
        console.print("\n[bold]Strategic Insights:[/bold]\n")

        sections = [
            ("Organic Traffic", self.phase1_results.get('organic_traffic')),
            ("Competitive Position", self.phase1_results.get('competitive')),
            ("User Engagement", self.phase1_results.get('engagement')),
            ("Site Health", self.phase1_results.get('site_health')),
            ("Meta Tags & Content", self.phase1_results.get('meta_tags')),
            ("Keyword Gap", self.phase1_results.get('keyword_gap')),
            ("Technical SEO", self.phase1_results.get('technical_seo')),
            ("Domain Authority", self.phase1_results.get('domain_authority'))
        ]

        for section_name, section_data in sections:
            if section_data:
                priority = section_data.priority if hasattr(section_data, 'priority') else 'M'
                key_msg = section_data.key_message if hasattr(section_data, 'key_message') else ''

                priority_colors = {'C': 'red', 'H': 'yellow', 'M': 'blue', 'L': 'green'}
                priority_color = priority_colors.get(priority, 'white')

                console.print(
                    f"[{priority_color}][{priority}][/{priority_color}] "
                    f"[bold]{section_name}:[/bold] {key_msg}"
                )

        console.print()

    def _run_phase2(self) -> bool:
        """Execute Phase 2: Narrative & Storyline Architecture."""
        console.print(Panel(
            "[bold yellow]Phase 2: Narrative & Storyline Architecture[/bold yellow]\n"
            "Crafting the strategic narrative and storyline...",
            title="Phase 2"
        ))

        try:
            generator = Phase2Generator(self.phase1_results)
            self.phase2_results = generator.execute()

            # Display narrative draft
            self._display_phase2_narrative()

            # Ask for approval
            return self._get_phase_approval(
                phase_num=2,
                question="Is this storyline engaging and accurate?"
            )

        except Exception as e:
            logger.error(f"Phase 2 error: {e}", exc_info=True)
            console.print(f"[red]Error in Phase 2: {e}[/red]")
            return False

    def _display_phase2_narrative(self):
        """Display Phase 2 narrative summary."""
        console.print("\n[bold]Executive Summary:[/bold]\n")

        exec_summary = self.phase2_results.get('exec_summary')
        if exec_summary:
            summary_dict = exec_summary.model_dump() if hasattr(exec_summary, 'model_dump') else exec_summary

            for pillar, content in summary_dict.items():
                console.print(f"[bold cyan]{pillar.replace('_', ' ').title()}:[/bold cyan]")
                console.print(f"  {content}\n")

        findings = self.phase2_results.get('findings_summary')
        if findings:
            key_msg = findings.key_message if hasattr(findings, 'key_message') else findings.get('key_message', '')
            console.print(f"[bold]Unified Key Message:[/bold]")
            console.print(f"  {key_msg}\n")

    def _run_phase3(self) -> bool:
        """Execute Phase 3: Final PowerPoint Output Generation."""
        console.print(Panel(
            "[bold yellow]Phase 3: Final PowerPoint Output Generation[/bold yellow]\n"
            "Generating the final presentation...",
            title="Phase 3"
        ))

        try:
            output_dir = Path('output')
            output_dir.mkdir(exist_ok=True)

            timestamp = Path(self.data_dir).stem
            output_filename = f"SEO_Audit_{self.brand_name}_{timestamp}.pptx"
            output_path = output_dir / output_filename

            generator = Phase3Generator(
                self.phase1_results,
                self.phase2_results
            )

            result_path = generator.execute(output_path)

            console.print(f"\n[bold green]✓ PowerPoint generated:[/bold green] {result_path}")
            console.print(f"[bold green]✓ Content JSON generated:[/bold green] {result_path.parent / f'{result_path.stem}_content.json'}")

            return True

        except Exception as e:
            logger.error(f"Phase 3 error: {e}", exc_info=True)
            console.print(f"[red]Error in Phase 3: {e}[/red]")
            return False

    def _get_phase_approval(self, phase_num: int, question: str) -> bool:
        """Get user approval to proceed to next phase.

        Args:
            phase_num: Current phase number
            question: Approval question

        Returns:
            True if approved, False otherwise
        """
        console.print()
        response = questionary.confirm(
            f"{question} Proceed to Phase {phase_num + 1}?",
            default=True
        ).ask()

        if response is None:
            return False

        if not response:
            console.print("[yellow]You can refine the analysis by providing feedback.[/yellow]")
            # In a full implementation, this would allow users to adjust parameters
            retry = questionary.confirm("Would you like to continue anyway?").ask()
            return retry if retry is not None else False

        return True


@click.command()
@click.option(
    '--data-dir',
    '-d',
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    required=True,
    help='Directory containing SEO data files (CSV/XLSX)'
)
@click.option(
    '--brand-name',
    '-b',
    required=True,
    help='Client brand name'
)
@click.option(
    '--website-type',
    '-w',
    type=click.Choice(['ecommerce', 'saas', 'content', 'local', 'marketplace']),
    default='ecommerce',
    help='Type of website'
)
@click.option(
    '--verbose',
    '-v',
    is_flag=True,
    help='Enable verbose logging'
)
def main(data_dir, brand_name, website_type, verbose):
    """SEO Audit Automation Tool

    Generates executive-ready SEO audits following a 3-phase workflow:
    \b
    Phase 1: Data Analysis & Strategic Insights
    Phase 2: Narrative & Storyline Architecture
    Phase 3: Final PowerPoint Output Generation
    """
    # Setup logging
    log_level = logging.DEBUG if verbose else logging.INFO
    setup_logger(log_level)

    # Run the tool
    tool = SEOAuditTool(data_dir, brand_name, website_type)
    success = tool.run()

    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
