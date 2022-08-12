# The idea is that you can add this is a middleware right into your stack and take full
# advantage of the NimbleBox LMAO system.

try:
  # importing like this is a bit of a hack, but it works since we don't need to add
  # starlette as a dependency
  from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
  from starlette.types import ASGIApp
except ImportError:
  raise ImportError("Please install starlette to use this middleware. pip install starlette")

class LMAOMiddleware(BaseHTTPMiddleware):
  def __init__(self, app: ASGIApp) -> None:
    """LMAO Middleware for Starlette plugs into the ASGI stack and sends metrics to NimbleBox LMAO.
    Such as request count, response count, request processing time, and exceptions raised."""
    # simply added here so in future we can add more options
    super().__init__(app)


from starlette_prometheus import metrics, PrometheusMiddleware

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics/", metrics)