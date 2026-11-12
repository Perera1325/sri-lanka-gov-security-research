"""Shared helpers for reading this repository's data files.

Local file access only. Nothing in scripts/ may open a network connection.
"""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INVENTORY = ROOT / "data" / "website-inventory.csv"
REGISTER = ROOT / "evidence" / "evidence-register.csv"
SCORECARD = ROOT / "data" / "scorecard-template.csv"
PLAN = ROOT / "research" / "research-plan.md"
SELECTION = ROOT / "research" / "government-sites.md"
RESERVE = ROOT / "data" / "reserve-sites.csv"
INCIDENTS = ROOT / "data" / "historical-incidents.csv"
AUTHORIZATIONS = ROOT / "data" / "authorizations.csv"
SCORECARDS = ROOT / "data" / "scorecards"
TIMELINE = ROOT / "reports" / "historical-incident-timeline.md"
MATRIX = ROOT / "reports" / "national-research-matrix.md"
REPORTS = ROOT / "reports" / "individual-sites"
TEMPLATE = REPORTS / "_TEMPLATE.md"
DASHBOARD = ROOT / "DASHBOARD.md"

INVENTORY_COLUMNS = [
    "site_id", "institution", "domain", "sector", "official_source_reference",
    "verification_checks_passed", "domain_verification_status",
    "research_status", "last_observation_date", "notes",
]
REGISTER_COLUMNS = [
    "finding_id", "website", "public_url", "observation_date", "component",
    "observation", "evidence_source", "technical_explanation",
    "owasp_category", "finding_status", "potential_impact", "remediation",
    "severity", "confidence",
]
SCORECARD_COLUMNS = [
    "site_id", "observation_date", "check_id", "check_name", "result",
    "evidence_file", "notes",
]

INCIDENT_COLUMNS = [
    "incident_id", "site_id", "institution", "official_domain", "incident_date",
    "publication_date", "system_affected", "summary", "confirmed_details",
    "alleged_or_unconfirmed_details", "investigation_announced",
    "investigation_outcome", "remediation_confirmed", "source_url",
    "supporting_source_url", "additional_source_urls", "source_type", "label",
    "confidence", "sources_opened", "notes",
]
# The seven research labels (docs/evidence-classification.md). CSV files use a
# plain hyphen in "POTENTIAL RISK - NOT VERIFIED".
RESEARCH_LABELS = [
    "CONFIRMED HISTORICAL INCIDENT", "CONFIRMED PUBLIC SECURITY REQUIREMENT",
    "OBSERVED CONFIGURATION", "CONFIRMED SECURITY WEAKNESS",
    "POTENTIAL RISK - NOT VERIFIED", "NOT TESTED",
    "NO PUBLIC EVIDENCE AVAILABLE",
]
INCIDENT_LABELS = [
    "CONFIRMED HISTORICAL INCIDENT", "POTENTIAL RISK - NOT VERIFIED",
    "NO PUBLIC EVIDENCE AVAILABLE",
]
SYSTEMS = ["WEBSITE", "OTHER SYSTEM", "SOCIAL MEDIA", "SHARED INFRASTRUCTURE",
           "IMPERSONATION"]
SHARED_SITE_ID = "NAT"

AUTHORIZATION_COLUMNS = [
    "institution_id", "institution", "domain", "authorization_status",
    "request_sent_date", "authorization_reference", "scope_summary",
    "valid_from", "valid_to", "notes",
]
# A GRANTED row is the only state that permits active testing of that system.
AUTHORIZATION_STATUSES = [
    "NONE REQUESTED", "REQUESTED", "GRANTED", "DECLINED", "EXPIRED",
]

VERIFICATION_STATUSES = ["VERIFIED", "PRELIMINARY", "PARTIAL", "UNVERIFIED"]
RESEARCH_STATUSES = ["NOT STARTED", "IN PROGRESS", "ASSESSED", "REPORTED"]
FINDING_STATUSES = ["CONFIRMED OBSERVATION", "SUSPECTED", "NOT TESTED", "INFORMATIONAL"]
SEVERITIES = ["Critical", "High", "Medium", "Low", "Informational"]
CONFIDENCES = ["High", "Medium", "Low"]


def read_csv(path):
    """Return (header, rows) where rows are dicts. Raises on malformed CSV."""
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle, strict=True)
        table = list(reader)
    if not table:
        return [], []
    header = table[0]
    rows = []
    for number, cells in enumerate(table[1:], start=2):
        if not any(cell.strip() for cell in cells):
            continue
        if len(cells) != len(header):
            raise ValueError(
                f"{path.relative_to(ROOT)} line {number}: expected "
                f"{len(header)} fields, found {len(cells)}"
            )
        rows.append(dict(zip(header, cells)))
    return header, rows


def report_path(domain):
    return REPORTS / f"{domain}.md"


def public_records_path(domain):
    return REPORTS / f"{domain}-public-records.md"
