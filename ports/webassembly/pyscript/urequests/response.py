from uio import StringIO

class Response:
    def __init__(self, status_code, headers, body):
        self.status_code = status_code
        self.headers = headers
        self.body = body

    @property
    def text(self):
        return str(self.content, self.encoding)

    @property
    def raw(self):
        return StringIO(self.body)

    def json(self):
        import ujson

        return ujson.loads(self.content)

    def close(self):
        pass

    
    #status_code: int
    #headers: Dict[str, str]
    #body: bytes

"""
Oriinal implementation

class Response:
    def __init__(self, f):
        self.raw = f
        self.encoding = "utf-8"
        self._cached = None

    def json(self):
        import ujson

        return ujson.loads(self.content)

    def close(self):
        return
        if self.raw:
            self.raw.close()
            self.raw = None
        self._cached = None

    @property
    def content(self):
        if self._cached is None:
            try:
                self._cached = self.raw.read()
            finally:
                self.raw.close()
                self.raw = None
        return self._cached

    @property
    def text(self):
        return str(self.content, self.encoding)

    def json(self):
        import ujson

        return ujson.loads(self.content)
"""