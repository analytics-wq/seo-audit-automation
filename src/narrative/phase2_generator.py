"""Phase 2: Narrative & Storyline Architecture Generator."""
import logging
from typing import Dict, Any
from src.models.audit_data import ExecutiveSummary, FindingsSummary, FindingsPillar

logger = logging.getLogger(__name__)


class Phase2Generator:
    """Generates Phase 2: Narrative & Storyline Architecture."""

    def __init__(self, phase1_insights: Dict[str, Any]):
        """Initialize with Phase 1 insights.

        Args:
            phase1_insights: Dictionary of insights from Phase 1
        """
        self.insights = phase1_insights

    def execute(self) -> Dict[str, Any]:
        """Execute Phase 2 narrative generation.

        Returns:
            Dictionary with executive summary and findings summary
        """
        logger.info("=== Starting Phase 2: Narrative & Storyline Architecture ===")

        narrative = {}

        # Generate Executive Summary (Slide 5)
        logger.info("Crafting executive summary...")
        narrative['exec_summary'] = self._generate_executive_summary()

        # Generate Findings Summary (Slide 24)
        logger.info("Consolidating findings summary...")
        narrative['findings_summary'] = self._generate_findings_summary()

        logger.info("=== Phase 2 Complete ===")
        return narrative

    def _generate_executive_summary(self) -> ExecutiveSummary:
        """Generate executive summary from section summaries.

        CRITICAL: Must ONLY pull from section summaries (Slides 11, 16, 19, 22)
        """
        # Extract key highlights from each section summary
        general = self.insights.get('section_summary_organic', {})
        content = self.insights.get('section_summary_content', {})
        technical = self.insights.get('section_summary_technical', {})
        authority = self.insights.get('section_summary_authority', {})

        return ExecutiveSummary(
            general=self._craft_exec_summary_text(general, "General Overview"),
            content=self._craft_exec_summary_text(content, "Content SEO"),
            technical=self._craft_exec_summary_text(technical, "Technical SEO"),
            authority=self._craft_exec_summary_text(authority, "Domain Authority")
        )

    def _craft_exec_summary_text(self, section_data: Dict, pillar_name: str) -> str:
        """Craft executive summary text for a pillar.

        Args:
            section_data: Section summary data
            pillar_name: Name of the pillar

        Returns:
            Formatted executive summary text
        """
        if not section_data:
            return f"{pillar_name}: Analysis pending."

        # Get the top issue and impact
        issues = section_data.get('issues', [])
        impacts = section_data.get('impacts', [])

        if issues and impacts:
            # Combine top issue with impact in strategic language
            top_issue = issues[0]
            top_impact = impacts[0]

            return f"{top_issue}. {top_impact}"
        elif 'key_highlight' in section_data:
            return section_data['key_highlight']
        else:
            return f"{pillar_name}: Optimization opportunities identified."

    def _generate_findings_summary(self) -> FindingsSummary:
        """Generate consolidated findings summary across all pillars."""
        # Determine dominant theme
        priorities = [
            self.insights.get('section_summary_technical', {}).get('priority', 'M'),
            self.insights.get('section_summary_content', {}).get('priority', 'M'),
            self.insights.get('section_summary_authority', {}).get('priority', 'M')
        ]

        # Generate unified key message
        key_message = self._generate_unified_key_message()

        # Get primary traffic issue
        organic_data = self.insights.get('organic_traffic', {})
        subtitle = organic_data.get('key_message', '') if organic_data else ""

        # Extract technical pillar findings
        technical_summary = self.insights.get('section_summary_technical', {})
        technical_pillar = FindingsPillar(
            priority=technical_summary.get('priority', 'M'),
            issues=technical_summary.get('issues', [])[:3],
            actions=technical_summary.get('actions', [])[:3]
        )

        # Extract content pillar findings
        content_summary = self.insights.get('section_summary_content', {})
        content_pillar = FindingsPillar(
            priority=content_summary.get('priority', 'M'),
            issues=content_summary.get('issues', [])[:3],
            actions=content_summary.get('actions', [])[:3]
        )

        # Extract authority pillar findings
        authority_summary = self.insights.get('section_summary_authority', {})
        authority_pillar = FindingsPillar(
            priority=authority_summary.get('priority', 'M'),
            issues=authority_summary.get('issues', [])[:3],
            actions=authority_summary.get('actions', [])[:3]
        )

        return FindingsSummary(
            key_message=key_message,
            subtitle=subtitle,
            technical=technical_pillar,
            content=content_pillar,
            authority=authority_pillar
        )

    def _generate_unified_key_message(self) -> str:
        """Generate unified key message across all pillars."""
        # Analyze which pillar is the biggest barrier
        priorities = {
            'technical': self.insights.get('section_summary_technical', {}).get('priority', 'M'),
            'content': self.insights.get('section_summary_content', {}).get('priority', 'M'),
            'authority': self.insights.get('section_summary_authority', {}).get('priority', 'M')
        }

        priority_order = {'C': 0, 'H': 1, 'M': 2, 'L': 3}
        dominant_pillar = min(priorities.items(), key=lambda x: priority_order.get(x[1], 3))[0]

        messages = {
            'technical': "Technical barriers must be resolved before content investments can deliver full ROI.",
            'content': "Content gaps and on-page optimization represent the primary growth lever.",
            'authority': "Authority constraints limit competitive reach regardless of content quality."
        }

        return messages.get(dominant_pillar, "Systematic optimization across all pillars will unlock organic growth potential.")
