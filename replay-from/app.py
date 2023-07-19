from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Route


# function to handle all requests
async def handle_all(request):
    return Response("", status_code=200, headers={"fly-replay": "app=replay-to"})


# define routes, here we use a wildcard to accept all routes
routes = [
    Route(
        "/{path:path}",
        handle_all,
        methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    )
]

app = Starlette(debug=True, routes=routes)
