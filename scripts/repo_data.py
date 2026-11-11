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
