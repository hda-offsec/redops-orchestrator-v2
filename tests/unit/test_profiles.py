from apps.nmap import profiles

def test_profiles_present():
    assert 'normal' in profiles.PROFILES
