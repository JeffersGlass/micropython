from uio import StringIO

class Response:
    def __init__(self, f):
        self.raw = f
        self.encoding = "utf-8"
        self._cached = None

    def json(self):
        import ujson

        return ujson.loads(self.content)

    def close(self):
        # There is no stream to close; this is preserved as a no-op for compatibility
        pass

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