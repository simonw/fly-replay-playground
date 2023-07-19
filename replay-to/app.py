from starlette.applications import Starlette
from starlette.responses import HTMLResponse, JSONResponse
from starlette.routing import Route

app = Starlette()

HOMEPAGE = """
<html>
<head>
<title>Example</title>
</head>
<body>
<h1>Example</h1>
<form action="/post" method="post">
<p><input type="text" name="singleline" value="example"></p>
<p><textarea name="multiline" rows="5" cols="40"></textarea></p>
<p><input type="submit" value="Submit"></p>
</form>
</body>
</html>
"""


@app.route("/")
async def homepage(request):
    return HTMLResponse(HOMEPAGE)


@app.route("/post", methods=["POST"])
async def post_handler(request):
    headers = dict(request.headers)
    content = await request.body()
    text = content.decode("utf-8")

    data = {"method": request.method, "headers": headers, "body": text}

    return JSONResponse(data)
