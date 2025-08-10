import xml.etree.ElementTree as ET
from typing import Dict, Any


def parse(xml_str: str) -> Dict[str, Any]:
    root = ET.fromstring(xml_str)
    hosts = []
    for host in root.findall('host'):
        addr_el = host.find('address')
        addr = addr_el.get('addr') if addr_el is not None else ''
        ports = []
        for p in host.findall('./ports/port'):
            portid = p.get('portid')
            if portid:
                ports.append(int(portid))
        hosts.append({'address': addr, 'ports': ports})
    return {'hosts': hosts}
