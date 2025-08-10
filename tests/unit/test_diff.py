from core.diff import summarize_hosts, compute_diff

def test_diff():
    prev = summarize_hosts({'hosts': []})
    curr = summarize_hosts({'hosts': [{'address':'1.1.1.1'}]})
    diff = compute_diff(prev, curr)
    assert 'changes' in diff
