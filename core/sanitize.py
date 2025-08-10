import ipaddress
import re

FQDN_RE = re.compile(r"^[A-Za-z0-9_.-]{1,253}$")
IMDS_NET = ipaddress.ip_network("169.254.0.0/16")


def validate_target(target: str) -> bool:
    try:
        ipaddress.ip_network(target, strict=False)
        net = ipaddress.ip_network(target, strict=False)
        if net.overlaps(IMDS_NET):
            return False
        return True
    except ValueError:
        if FQDN_RE.fullmatch(target):
            return True
    return False


NMAP_WHITELIST = {
    "-sS", "-sT", "-sV", "-sC", "-O", "-Pn", "-n", "-6", "-F",
    "--top-ports", "--open", "-T0", "-T1", "-T2", "-T3", "-T4", "-T5",
    "--max-retries", "--max-rate", "--min-rate", "--host-timeout",
    "--scan-delay", "--max-scan-delay", "-oX", "-oN", "-p"
}


def sanitize_nmap_options(opts: list[str]) -> list[str]:
    safe = []
    for opt in opts:
        if opt.split("=")[0] in NMAP_WHITELIST:
            safe.append(opt)
    return safe
