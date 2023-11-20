try:
    import js
except Exception as err:
    raise OSError("This version of requests can only be used in the browser")

# TODO try to support streaming xhr requests, a-la pyodide-http

from .response import Response
from uio import StringIO

HEADERS_TO_IGNORE = ("user-agent",)


def request(
    method,
    url,
    data=None,
    json=None,
    headers={},
    stream=None,
    auth=None,
    timeout=None,
    parse_headers=True,
):
    from js import XMLHttpRequest

    xhr = XMLHttpRequest.new()
    xhr.withCredentials = False

    if auth is not None:
        import ubinascii

        username, password = auth
        xhr.open(method, url, False, username, password)
    else:
        xhr.open(method, url, False)

    for name, value in headers.items():
        if name.lower() not in HEADERS_TO_IGNORE:
            xhr.setRequestHeader(name, value)

    xhr.send(data)
    
    # Emulates the construction process in the original urequests
    resp = Response(StringIO(xhr.responseText))
    resp.status_code = xhr.status
    resp.reason = xhr.statusText
    resp.headers = xhr.getAllResponseHeaders()

    return resp

def head(url, **kw):
    return request("HEAD", url, **kw)


def get(url, **kw):
    return request("GET", url, **kw)


def post(url, **kw):
    return request("POST", url, **kw)


def put(url, **kw):
    return request("PUT", url, **kw)


def patch(url, **kw):
    return request("PATCH", url, **kw)


def delete(url, **kw):
    return request("DELETE", url, **kw)