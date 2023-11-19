try:
    import js
except Exception as err:
    raise OSError("This version of requests can only be used in the browser")

# TODO try to support streaming xhr requests, a-la pyodide-http

from .response import Response

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

    print("About to open")

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

    return Response(xhr.status, {}, xhr.responseText)

def get(url, **kw):
    return request("GET", url, **kw)