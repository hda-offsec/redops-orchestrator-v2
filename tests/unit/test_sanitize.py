from core.sanitize import validate_target, sanitize_nmap_options

def test_validate_target():
    assert validate_target('127.0.0.1')
    assert not validate_target('169.254.0.1')
    assert validate_target('example.com')

def test_sanitize_nmap_options():
    assert '-sS' in sanitize_nmap_options(['-sS', '--bad'])
