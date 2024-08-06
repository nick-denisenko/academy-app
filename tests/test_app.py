from app import app


async def test_echo() -> None:
    test_client = app.test_client()
    response = await test_client.post("/echo", json={"a": "b"})
    data = await response.get_json()
    assert data == {"extra":True,"input":{"a":"b"}}
