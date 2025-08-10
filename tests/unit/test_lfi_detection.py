from apps.lfi.detection import detect

def test_detect_empty():
    assert detect('http://example') == []
