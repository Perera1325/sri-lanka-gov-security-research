#!/usr/bin/env python3
"""Validate the repository's structure and data.

    python3 scripts/validate.py

Checks: required files, CSV format and vocabularies, unique IDs, that the
inventory matches the research plan, that every register row is complete,
that relative Markdown links resolve, that the dashboard is current, and that
no script in this repository can make network connections.

Reads local files only. Exits 1 if any check fails.
"""

import re
import sys
from datetime import date

import repo_data as rd
import build_dashboard
import build_reports

REQUIRED_FILES = [
    "README.md", "CONTRIBUTING.md", "DASHBOARD.md",
    "research/research-plan.md", "research/methodology.md", "research/scope.md",
    "research/government-sites.md", "research/technology-risk-reference.md",
    "research/assessment-checklist.md",
    "evidence/evidence-register.csv", "evidence/evidence-guidelines.md",
    "evidence/sources/README.md",
    "reports/executive-summary.md", "reports/individual-sites/_TEMPLATE.md",
    "disclosure/responsible-disclosure-policy.md",
    "disclosure/templates/cert-report-template.md",
    "disclosure/templates/institution-notification-template.md",
    "disclosure/templates/follow-up-template.md",
    "data/website-inventory.csv", "data/scorecard-template.csv",
    "docs/research-limitations.md", "docs/risk-classification.md",
    "docs/evidence-classification.md", "docs/confidence-risk-matrix.md",
    "data/reserve-sites.csv", "data/historical-incidents.csv",
    "research/cert-compliance-mapping.md",
    "research/ai-code-security-literature-review.md",
    "reports/national-research-matrix.md",
    "reports/historical-incident-timeline.md",
]

# Modules that would let a script contact a website or run other programs.
FORBIDDEN_IMPORTS = [
    "requests", "urllib", "http", "httpx", "aiohttp", "socket", "ssl",
    "subprocess", "selenium", "playwright", "scapy", "nmap", "ftplib",
    "smtplib", "telnetlib", "webbrowser",
]

SEVERITY_ALLOWED = {
    "CONFIRMED OBSERVATION": set(rd.SEVERITIES),
    "SUSPECTED": {"Medium", "Low", "Informational"},
    "NOT TESTED": {"Informational"},
    "INFORMATIONAL": {"Informational"},
}

errors = []
passed = []


def check(name, problems):
    if problems:
        errors.extend(f"{name}: {p}" for p in problems)
    else:
        passed.append(name)


def valid_date(text):
    try:
        date.fromisoformat(text)
        return True
    except ValueError:
        return False


def required_files():
    return [f"missing {p}" for p in REQUIRED_FILES if not (rd.ROOT / p).is_file()]


def inventory():
    problems = []
    header, rows = rd.read_csv(rd.INVENTORY)
    if header != rd.INVENTORY_COLUMNS:
        return [f"header must be {','.join(rd.INVENTORY_COLUMNS)}"]
    if len(rows) != 10:
        problems.append(f"expected 10 sites, found {len(rows)}")
    for column in ("site_id", "domain"):
        values = [r[column] for r in rows]
        for value in sorted({v for v in values if values.count(v) > 1}):
            problems.append(f"duplicate {column} {value}")
    for r in rows:
        where = r["site_id"] or r["domain"] or "(blank row)"
        for column in ("site_id", "institution", "domain", "sector",
                       "official_source_reference"):
            if not r[column].strip():
                problems.append(f"{where}: {column} is empty")
        if not re.fullmatch(r"[A-Z]{2,6}", r["site_id"]):
            problems.append(f"{where}: site_id must be 2-6 capital letters")
        if not r["official_source_reference"].startswith("https://"):
            problems.append(f"{where}: official_source_reference must be an https URL")
        if r["verification_checks_passed"] not in ("0", "1", "2"):
            problems.append(f"{where}: verification_checks_passed must be 0, 1 or 2")
        if r["domain_verification_status"] not in rd.VERIFICATION_STATUSES:
            problems.append(f"{where}: unknown verification status")
        elif (r["domain_verification_status"] in ("VERIFIED", "PRELIMINARY")
              and r["verification_checks_passed"] != "2"):
            problems.append(f"{where}: {r['domain_verification_status']} needs 2 checks passed")
        if r["research_status"] not in rd.RESEARCH_STATUSES:
            problems.append(f"{where}: unknown research status")
        last = r["last_observation_date"]
        if last and not valid_date(last):
            problems.append(f"{where}: last_observation_date must be YYYY-MM-DD")
        if r["research_status"] == "NOT STARTED" and last:
            problems.append(f"{where}: NOT STARTED but has an observation date")
        if r["research_status"] != "NOT STARTED" and not last:
            problems.append(f"{where}: {r['research_status']} needs an observation date")
        if (r["research_status"] != "NOT STARTED"
                and r["domain_verification_status"] != "VERIFIED"):
            problems.append(f"{where}: assessment started before domain is VERIFIED")
    return problems


def selection_match():
    """The inventory must list exactly the sites in research/government-sites.md,
    and every Phase 0 plan site must still be tracked (inventory or reserve)."""
    _, rows = rd.read_csv(rd.INVENTORY)
    header, reserve = rd.read_csv(rd.RESERVE)
    problems = []
    if header != rd.INVENTORY_COLUMNS:
        problems.append("reserve-sites.csv header does not match the inventory")
    inv = {r["domain"]: r["site_id"] for r in rows}
    text = rd.SELECTION.read_text(encoding="utf-8")
    section = text.split("## Selected sites", 1)[-1].split("\n## ", 1)[0]
    selected = dict((d, i) for i, d in re.findall(
        r"^\| ([A-Z]{2,6}) \| [^|]+ \| ([a-z0-9.-]+\.lk) \|", section, flags=re.M))
    if len(selected) != 10:
        problems.append(f"expected 10 selected sites in government-sites.md, found {len(selected)}")
    for d in sorted(set(selected) - set(inv)):
        problems.append(f"{d} is selected but not in the inventory")
    for d in sorted(set(inv) - set(selected)):
        problems.append(f"{d} is in the inventory but not selected")
    for d, i in selected.items():
        if d in inv and inv[d] != i:
            problems.append(f"{d}: site ID differs between selection and inventory")
    plan = rd.PLAN.read_text(encoding="utf-8")
    plan_domains = re.findall(
        r"^\| \d+ \| [^|]+ \| ([a-z0-9.-]+\.lk) \|", plan, flags=re.M)
    tracked = set(inv) | {r["domain"] for r in reserve}
    for d in sorted(set(plan_domains) - tracked):
        problems.append(f"{d} from the Phase 0 plan is in neither inventory nor reserve")
    both = set(inv) & {r["domain"] for r in reserve}
    for d in sorted(both):
        problems.append(f"{d} is in both the inventory and the reserve")
    return problems


def incidents():
    problems = []
    header, rows = rd.read_csv(rd.INCIDENTS)
    if header != rd.INCIDENT_COLUMNS:
        return ["header does not match INCIDENT_COLUMNS"]
    _, sites = rd.read_csv(rd.INVENTORY)
    domain_by_id = {s["site_id"]: s["domain"] for s in sites}
    ids = [r["incident_id"] for r in rows]
    for value in sorted({v for v in ids if ids.count(v) > 1}):
        problems.append(f"duplicate incident_id {value}")
    partial = re.compile(r"\d{4}(-\d{2}(-\d{2})?)?")
    for r in rows:
        iid = r["incident_id"] or "(no id)"
        if not re.fullmatch(r"INC-\d{2}", r["incident_id"]):
            problems.append(f"{iid}: incident_id must look like INC-01")
        if r["site_id"] == rd.SHARED_SITE_ID:
            if r["official_domain"]:
                problems.append(f"{iid}: shared entries carry no domain")
        elif r["site_id"] not in domain_by_id:
            problems.append(f"{iid}: site_id is not in the inventory")
        elif r["official_domain"] != domain_by_id[r["site_id"]]:
            problems.append(f"{iid}: official_domain does not match the inventory")
        for column in ("institution", "publication_date", "system_affected",
                       "summary", "source_type", "label", "confidence", "notes"):
            if not r[column].strip():
                problems.append(f"{iid}: {column} is empty")
        for column in ("incident_date", "publication_date"):
            value = r[column]
            if value and not partial.fullmatch(value):
                problems.append(f"{iid}: {column} must be YYYY, YYYY-MM or YYYY-MM-DD")
            elif len(value) == 10 and not valid_date(value):
                problems.append(f"{iid}: {column} is not a real date")
        if r["system_affected"] not in rd.SYSTEMS:
            problems.append(f"{iid}: unknown system_affected")
        if r["label"] not in rd.INCIDENT_LABELS:
            problems.append(f"{iid}: label not allowed for incident records")
        for column in ("source_url", "supporting_source_url"):
            if r[column] and not r[column].startswith(("https://", "http://")):
                problems.append(f"{iid}: {column} must be a full URL")
        if r["label"] == "NO PUBLIC EVIDENCE AVAILABLE":
            if r["confirmed_details"] and not r["source_url"]:
                problems.append(f"{iid}: confirmed details need a source")
        else:
            if not r["source_url"]:
                problems.append(f"{iid}: a source_url is required")
            if not r["incident_date"]:
                problems.append(f"{iid}: an incident_date is required")
            if r["confidence"] not in rd.CONFIDENCES:
                problems.append(f"{iid}: unknown confidence")
        if r["label"] == "CONFIRMED HISTORICAL INCIDENT" and not r["confirmed_details"]:
            problems.append(f"{iid}: a confirmed incident needs confirmed_details")
        if (r["label"] == "POTENTIAL RISK - NOT VERIFIED"
                and r["confidence"] == "High"):
            problems.append(f"{iid}: an unverified report cannot have High confidence")
    return problems


def generated_reports_current():
    problems = []
    for path, text in build_reports.outputs().items():
        name = path.relative_to(rd.ROOT)
        if not path.is_file():
            problems.append(f"{name} is missing; run scripts/build_reports.py")
        elif path.read_text(encoding="utf-8") != text:
            problems.append(f"{name} is out of date; run scripts/build_reports.py")
    return problems


def matrix_covers_all_sites():
    _, rows = rd.read_csv(rd.INVENTORY)
    text = rd.MATRIX.read_text(encoding="utf-8")
    return [f"{r['domain']} is missing from the national research matrix"
            for r in rows if r["domain"] not in text]


def site_reports():
    _, rows = rd.read_csv(rd.INVENTORY)
    problems = []
    for r in rows:
        path = rd.report_path(r["domain"])
        if not path.is_file():
            problems.append(f"no report file for {r['domain']}")
        elif "{{" in path.read_text(encoding="utf-8"):
            problems.append(f"{path.name} has unfilled placeholders")
    return problems


def register():
    problems = []
    header, rows = rd.read_csv(rd.REGISTER)
    if header != rd.REGISTER_COLUMNS:
        return [f"header must be {','.join(rd.REGISTER_COLUMNS)}"]
    _, sites = rd.read_csv(rd.INVENTORY)
    id_by_domain = {s["domain"]: s["site_id"] for s in sites}
    ids = [r["finding_id"] for r in rows]
    for value in sorted({v for v in ids if ids.count(v) > 1}):
        problems.append(f"duplicate finding_id {value}")
    for r in rows:
        fid = r["finding_id"] or "(no id)"
        for column in rd.REGISTER_COLUMNS:
            if not r[column].strip():
                problems.append(f"{fid}: {column} is empty")
        if r["website"] not in id_by_domain:
            problems.append(f"{fid}: website is not in the inventory")
        else:
            prefix = id_by_domain[r["website"]]
            if not re.fullmatch(rf"{prefix}-\d{{2}}", r["finding_id"]):
                problems.append(f"{fid}: finding_id must look like {prefix}-01")
            if r["website"] not in r["public_url"]:
                problems.append(f"{fid}: public_url is not on {r['website']}")
        if not r["public_url"].startswith(("https://", "http://")):
            problems.append(f"{fid}: public_url must be a full URL")
        if not valid_date(r["observation_date"]):
            problems.append(f"{fid}: observation_date must be YYYY-MM-DD")
        elif date.fromisoformat(r["observation_date"]) > date.today():
            problems.append(f"{fid}: observation_date is in the future")
        if r["finding_status"] not in rd.FINDING_STATUSES:
            problems.append(f"{fid}: unknown finding_status")
        elif r["severity"] not in SEVERITY_ALLOWED[r["finding_status"]]:
            problems.append(f"{fid}: severity {r['severity']!r} not allowed "
                            f"for {r['finding_status']}")
        if r["severity"] not in rd.SEVERITIES:
            problems.append(f"{fid}: unknown severity")
        if r["confidence"] not in rd.CONFIDENCES:
            problems.append(f"{fid}: unknown confidence")
        if not re.match(r"A(0[1-9]|10) ", r["owasp_category"]):
            problems.append(f"{fid}: owasp_category must start with A01 to A10")
        source = r["evidence_source"]
        if source and not source.startswith(("https://", "http://")):
            for part in source.split(";"):
                if part.strip() and not (rd.ROOT / part.strip()).exists():
                    problems.append(f"{fid}: evidence file {part.strip()} not found")
    return problems


def scorecard():
    header, rows = rd.read_csv(rd.SCORECARD)
    if header != rd.SCORECARD_COLUMNS:
        return [f"header must be {','.join(rd.SCORECARD_COLUMNS)}"]
    ids = [r["check_id"] for r in rows]
    return [f"duplicate check_id {v}" for v in sorted({v for v in ids if ids.count(v) > 1})]


def site_scorecards():
    """Per-site scorecards must match the template and hold no premature results."""
    problems = []
    folder = rd.ROOT / "data" / "scorecards"
    if not folder.is_dir():
        return problems
    _, sites = rd.read_csv(rd.INVENTORY)
    by_id = {s["site_id"]: s for s in sites}
    _, template_rows = rd.read_csv(rd.SCORECARD)
    template_checks = [r["check_id"] for r in template_rows]
    allowed = {"", "YES", "NO", "PARTIAL", "NOT OBSERVED", "NOT TESTED"}
    for path in sorted(folder.glob("*.csv")):
        name = path.relative_to(rd.ROOT)
        header, rows = rd.read_csv(path)
        if header != rd.SCORECARD_COLUMNS:
            problems.append(f"{name}: header does not match the template")
            continue
        if [r["check_id"] for r in rows] != template_checks:
            problems.append(f"{name}: checks differ from the template")
        for r in rows:
            site = by_id.get(r["site_id"])
            if site is None:
                problems.append(f"{name} {r['check_id']}: unknown site_id")
                continue
            if r["result"] not in allowed:
                problems.append(f"{name} {r['check_id']}: unknown result value")
            if r["result"]:
                if site["domain_verification_status"] != "VERIFIED":
                    problems.append(f"{name} {r['check_id']}: result recorded "
                                    "before the domain is VERIFIED")
                if not valid_date(r["observation_date"]):
                    problems.append(f"{name} {r['check_id']}: result needs an observation_date")
                if r["result"] != "NOT TESTED" and not r["evidence_file"]:
                    problems.append(f"{name} {r['check_id']}: result needs an evidence_file")
            if r["evidence_file"] and not (rd.ROOT / r["evidence_file"]).exists():
                problems.append(f"{name} {r['check_id']}: evidence file not found")
    return problems


def markdown_links():
    problems = []
    pattern = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    for path in sorted(rd.ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        for target in pattern.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if "{{" in target:  # template placeholder, filled per site
                continue
            local = target.split("#")[0]
            if local and not (path.parent / local).exists():
                problems.append(f"{path.relative_to(rd.ROOT)} -> {target}")
    return problems


def dashboard_current():
    if not rd.DASHBOARD.is_file():
        return ["DASHBOARD.md is missing; run scripts/build_dashboard.py"]
    if rd.DASHBOARD.read_text(encoding="utf-8") != build_dashboard.render():
        return ["DASHBOARD.md is out of date; run scripts/build_dashboard.py"]
    return []


def no_active_tooling():
    """No code in the repository may reach the network or run other programs."""
    problems = []
    names = "|".join(FORBIDDEN_IMPORTS)
    pattern = re.compile(rf"^\s*(?:import|from)\s+(?:{names})\b", flags=re.M)
    for path in sorted(rd.ROOT.rglob("*")):
        if ".git" in path.parts or not path.is_file():
            continue
        relative = path.relative_to(rd.ROOT)
        if path.suffix == ".py":
            if pattern.search(path.read_text(encoding="utf-8")):
                problems.append(f"{relative} imports a network or process module")
        elif path.suffix in (".sh", ".bash", ".ps1", ".bat", ".js", ".ts", ".go", ".rb"):
            problems.append(f"{relative}: executable code outside scripts/*.py is not allowed")
    return problems


def main():
    check("Required files present", required_files())
    for name, function in [
        ("Inventory format and values", inventory),
        ("Inventory matches the current selection; plan sites tracked", selection_match),
        ("Incident records: IDs, labels, dates, sources", incidents),
        ("Generated timeline and public-records summaries are current", generated_reports_current),
        ("National matrix covers all ten sites", matrix_covers_all_sites),
        ("Report file for every site", site_reports),
        ("Evidence register format, IDs and values", register),
        ("Scorecard template format", scorecard),
        ("Site scorecards hold only evidenced results", site_scorecards),
        ("Relative Markdown links resolve", markdown_links),
        ("Dashboard is current", dashboard_current),
        ("No network or scanning code", no_active_tooling),
    ]:
        try:
            check(name, function())
        except (OSError, ValueError, KeyError) as problem:
            check(name, [str(problem)])

    for name in passed:
        print(f"PASS  {name}")
    for line in errors:
        print(f"FAIL  {line}")
    _, rows = rd.read_csv(rd.REGISTER) if rd.REGISTER.is_file() else ([], [])
    print(f"\nEvidence register rows: {len(rows)}")
    print("Result: " + ("FAILED" if errors else "OK"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
