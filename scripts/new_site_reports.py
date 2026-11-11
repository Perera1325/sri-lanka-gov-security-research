#!/usr/bin/env python3
"""Create a report file for each inventoried site from the template.

Existing report files are never overwritten.

    python3 scripts/new_site_reports.py

Reads and writes local files only.
"""

import repo_data as rd


def main():
    _, sites = rd.read_csv(rd.INVENTORY)
    template = rd.TEMPLATE.read_text(encoding="utf-8")
    for site in sites:
        path = rd.report_path(site["domain"])
        if path.exists():
            print(f"kept     {path.relative_to(rd.ROOT)}")
            continue
        text = template
        for key in ("site_id", "institution", "domain", "sector"):
            text = text.replace("{{" + key + "}}", site[key])
        path.write_text(text, encoding="utf-8")
        print(f"created  {path.relative_to(rd.ROOT)}")


if __name__ == "__main__":
    main()
