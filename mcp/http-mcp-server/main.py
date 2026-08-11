import json
import urllib.error
import urllib.parse
import urllib.request

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("http-server")

TIMEOUT = 15
ALLOWED = ("https://", "http://")


def _check(url: str) -> None:
    if not url.startswith(ALLOWED):
        raise ValueError("only http/https URLs allowed")


def _fetch(req: urllib.request.Request) -> str:
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        body = resp.read()
        try:
            text = body.decode("utf-8")
        except UnicodeDecodeError:
            text = f"<binary response, {len(body)} bytes>"
        return f"status: {resp.status}\nheaders: {dict(resp.headers)}\nbody:\n{text[:4000]}"


@mcp.tool()
def http_get(url: str, headers: str = "{}") -> str:
    """Perform a GET request. headers is a JSON object string."""
    _check(url)
    req = urllib.request.Request(url, headers=json.loads(headers or "{}"))
    try:
        return _fetch(req)
    except urllib.error.HTTPError as e:
        return f"error {e.code}: {e.reason}\n{e.read().decode('utf-8', 'replace')[:2000]}"
    except urllib.error.URLError as e:
        return f"request failed: {e.reason}"


@mcp.tool()
def http_post(url: str, data: str = "", content_type: str = "application/json") -> str:
    """Perform a POST request with a raw body. content_type defaults to JSON."""
    _check(url)
    req = urllib.request.Request(
        url, data=data.encode("utf-8"), method="POST",
        headers={"Content-Type": content_type},
    )
    try:
        return _fetch(req)
    except urllib.error.HTTPError as e:
        return f"error {e.code}: {e.reason}\n{e.read().decode('utf-8', 'replace')[:2000]}"
    except urllib.error.URLError as e:
        return f"request failed: {e.reason}"


if __name__ == "__main__":
    mcp.run()
