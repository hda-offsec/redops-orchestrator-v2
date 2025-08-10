from typing import List, Dict

CRITICAL_PORTS = {22, 80, 443, 3389}


def score(ports: List[int]) -> int:
    return sum(10 if p in CRITICAL_PORTS else 1 for p in ports)
