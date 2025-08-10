from core.risk import score


def test_score():
    assert score([22]) > score([21])
