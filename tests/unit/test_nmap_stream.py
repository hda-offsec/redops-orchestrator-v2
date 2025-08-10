from fastapi.testclient import TestClient

from api.main import app


client = TestClient(app)


def test_nmap_stream_endpoint_returns_event():
    resp = client.get(
        "/api/v1/nmap/streams/nonexistent",
        headers={"X-RedOps-Token": "changeme"},
    )
    assert resp.status_code == 200
    assert resp.headers["content-type"].startswith("text/event-stream")
    assert "event:" in resp.text
