from core.diff import compute_diff, summarize_hosts


def test_diff():
    prev = summarize_hosts({'hosts': []})
    curr = summarize_hosts({'hosts': [{'address':'1.1.1.1'}]})
    diff = compute_diff(prev, curr)
    assert 'changes' in diff
