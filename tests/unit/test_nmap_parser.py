from apps.nmap.parser import parse


def test_parse_simple():
    xml = """<nmaprun><host><address addr='127.0.0.1'/><ports><port portid='80'/></ports></host></nmaprun>"""
    res = parse(xml)
    assert res['hosts'][0]['address'] == '127.0.0.1'
