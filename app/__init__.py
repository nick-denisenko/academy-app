from quart import Quart
from quart import request
# from quart import jsonify

app = Quart(__name__)

def run() -> None:
    app.run()

@app.post("/echo")
async def echo():
    data = await request.get_json()
    return {"input": data, "extra": True}

# @app.get("/example")
# async def example():
#     return jsonify(["a", "b"])
