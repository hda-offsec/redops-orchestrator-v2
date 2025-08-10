from typing import Any, Dict


def summarize_hosts(scan_result: Dict[str, Any]) -> Dict[str, Any]:
    return {"hosts": scan_result.get("hosts", [])}


def compute_diff(prev: Dict[str, Any], curr: Dict[str, Any]) -> Dict[str, Any]:
    return {"changes": curr.get("hosts", [])}
