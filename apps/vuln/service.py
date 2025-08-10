from core.logging import logger
from .profiles import PROFILES
from .enrich_searchsploit import enrich
from .mitre_map import MITRE


def run_scan(params: dict):
    logger.info("vuln", target=params.get("target"))
    findings = [{"id": "test", "severity": "medium", "cve": ["CVE-0000"], "mitre_techniques": MITRE.get("CVE-0000", [])}]
    return {"findings": enrich(findings)}
