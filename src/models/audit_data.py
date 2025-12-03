"""Data models for SEO audit report structure."""
from typing import List, Dict, Optional, Literal
from pydantic import BaseModel, Field


class ChannelDistribution(BaseModel):
    """Channel traffic distribution."""
    organic_pct: float
    direct_pct: float
    paid_pct: float
    social_pct: float
    referral_pct: float


class CountryData(BaseModel):
    """Country traffic data."""
    country: str
    sessions: int
    percentage: float


class KeywordDistribution(BaseModel):
    """Keyword position distribution."""
    pos_1_3: float
    pos_4_10: float
    pos_11_20: float
    pos_21_plus: float


class OrganicTrafficData(BaseModel):
    """Organic traffic analysis data."""
    key_message: str = Field(..., max_length=200)
    observation: str
    priority: Literal["C", "H", "M", "L"]
    channels: ChannelDistribution
    top_countries: List[CountryData]
    keyword_distribution: KeywordDistribution
    yoy_change_pct: Optional[float] = None


class CompetitiveMetrics(BaseModel):
    """Competitive benchmarking metrics."""
    domain_rating: Dict[str, int]
    monthly_traffic: Dict[str, int]
    total_keywords: Dict[str, int]
    page_1_keywords: Dict[str, int]
    referring_domains: Dict[str, int]


class CompetitiveData(BaseModel):
    """Competitive analysis data."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    brand_name: str
    competitors: List[str]
    metrics: CompetitiveMetrics


class PeriodEngagement(BaseModel):
    """Engagement metrics for a time period."""
    range: str
    engagement_rate: str
    engaged_sessions: str
    avg_engagement_time: str


class EngagementData(BaseModel):
    """User engagement data."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    prev_period: PeriodEngagement
    curr_period: PeriodEngagement
    trend_pct: float
    trend_direction: Literal["up", "down", "stable"]


class IssueItem(BaseModel):
    """Generic issue item."""
    issue_name: str
    url_count: int


class SiteHealthData(BaseModel):
    """Site health metrics."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    score: int
    pages_crawled: str
    total_errors: str
    critical_issues: List[IssueItem]
    high_priority_issues: List[IssueItem]


class SectionSummary(BaseModel):
    """Section summary data."""
    key_highlight: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    issues: List[str]
    impacts: List[str]
    actions: List[str]


class MetaTagIssue(BaseModel):
    """Meta tag issue."""
    issue_name: str
    url_count: int
    priority: Literal["C", "H", "M", "L"]


class MetaTagsData(BaseModel):
    """Meta tags analysis data."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    issues: List[MetaTagIssue]


class KeywordGapItem(BaseModel):
    """Keyword gap item."""
    keyword: str
    volume: int
    difficulty: int


class KeywordGapData(BaseModel):
    """Keyword gap analysis data."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    total_gap_keywords: int
    total_gap_volume: int
    missing_keywords: List[KeywordGapItem]


class KeywordCategory(BaseModel):
    """Keyword category breakdown."""
    name: str
    percentage: float
    volume: str
    examples: str


class KeywordIntentDistribution(BaseModel):
    """Keyword intent distribution percentages."""
    behavioral_pct: float
    device_utility_pct: float
    brand_pct: float
    location_pct: float


class KeywordIntentData(BaseModel):
    """Keyword intent analysis data."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    categories: List[KeywordCategory]
    distribution: KeywordIntentDistribution


class TechnicalIssue(BaseModel):
    """Technical SEO issue."""
    issue_name: str
    url_count: int
    priority: Literal["C", "H", "M", "L"]
    category: Literal["crawlability", "indexability", "performance", "structured_data"]


class CoreWebVitals(BaseModel):
    """Core Web Vitals metrics."""
    lcp: str
    lcp_status: Literal["good", "needs_improvement", "poor"]
    fid: str
    fid_status: Literal["good", "needs_improvement", "poor"]
    cls: str
    cls_status: Literal["good", "needs_improvement", "poor"]
    performance_score: int


class TechnicalSEOData(BaseModel):
    """Technical SEO analysis data."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    issues: List[TechnicalIssue]
    cwv: CoreWebVitals


class RDTrendPoint(BaseModel):
    """Referring domains trend point."""
    month: str
    referring_domains: int


class DomainAuthorityData(BaseModel):
    """Domain authority analysis data."""
    key_message: str
    observation: str
    priority: Literal["C", "H", "M", "L"]
    current_dr: int
    dr_6_months_ago: int
    dr_trend: Literal["growing", "stable", "declining"]
    dr_change: int
    referring_domains: int
    new_rd_monthly_avg: int
    competitor_avg_dr: int
    dr_gap: int
    rd_trend: List[RDTrendPoint]


class ExecutiveSummary(BaseModel):
    """Executive summary content."""
    general: str
    content: str
    technical: str
    authority: str


class FindingsPillar(BaseModel):
    """Findings for a pillar (technical/content/authority)."""
    priority: Literal["C", "H", "M", "L"]
    issues: List[str]
    actions: List[str]


class FindingsSummary(BaseModel):
    """Overall findings summary."""
    key_message: str
    subtitle: str
    technical: FindingsPillar
    content: FindingsPillar
    authority: FindingsPillar


class KPIData(BaseModel):
    """KPI and benchmark data."""
    current_ctr: str
    current_avg_position: str
    current_organic_sessions: str
    target_ctr: str
    target_position_improvement: str
    target_traffic_improvement: str
    benchmark_ctr: str


class AuditMetadata(BaseModel):
    """Audit metadata."""
    brand_name: str
    client_logo_path: Optional[str] = None
    audit_month: str
    audit_period: str
    tools_detected: List[str]
    website_type: Literal["ecommerce", "saas", "content", "local", "marketplace"]


class SEOAuditReport(BaseModel):
    """Complete SEO audit report data structure."""
    metadata: AuditMetadata
    organic_traffic: OrganicTrafficData
    competitive: CompetitiveData
    engagement: EngagementData
    site_health: SiteHealthData
    section_summary_organic: SectionSummary
    meta_tags: MetaTagsData
    keyword_gap: KeywordGapData
    keyword_intent: KeywordIntentData
    section_summary_content: SectionSummary
    technical_seo: TechnicalSEOData
    section_summary_technical: SectionSummary
    domain_authority: DomainAuthorityData
    section_summary_authority: SectionSummary
    exec_summary: ExecutiveSummary
    findings_summary: FindingsSummary
    kpi: KPIData
