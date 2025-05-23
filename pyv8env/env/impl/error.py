from pyv8env.env.chrome.flags import *
from pyv8env.env.chrome.v8_dom_error import DOMError as V8DOMError
from pyv8env.env.chrome.v8_dom_exception import DOMException as V8DOMException


class V8Error(Exception):
    __v8_error__ = True


class V8TypeError(TypeError):
    __v8_error__ = True


class V8RangeError(Exception):
    __v8_error__ = True


class V8ReferenceError(ReferenceError):
    __v8_error__ = True


class V8SyntaxError(SyntaxError):
    __v8_error__ = True


@impl_warp
class DOMError(V8DOMError):
    __v8_error__ = True

    def get_name(self):
        return self._name

    def get_message(self):
        return self._message

    def __init__(self, name=None, message=None):
        if name is None:
            raise V8TypeError("Failed to construct 'DOMError': 1 argument required, but only 0 present")

        self._name = name
        self._message = message or ''
        super().__init__(message)
        self._attr = {}


@impl_warp
class DOMException(V8DOMException):
    __v8_error__ = True

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

    def get_message(self):
        return self._message

    def __call__(self, message, code=None):
        if code is not None:
            self._code = code
        return DOMException(message=message, name=self._name, code=self._code)

    def __init__(self, message=None, name=None, code=0, *args, **kw):
        self._name = name or "Error"
        self._message = message or ''
        self._code = code
        super(DOMException, self).__init__(message)
        self._attr = {}


IndexSizeError = DOMException(name="IndexSizeError", code=1)
InvalidCharacterError = DOMException(name="InvalidCharacterError", code=5)
NotFoundError = DOMException(name="NotFoundError", code=8)
NotSupportedError = DOMException(name="NotSupportedError", code=9)
InvalidStateError = DOMException(name="InvalidStateError", code=11)
InvalidAccessError = DOMException(name="InvalidAccessError", code=15)
SecurityError = DOMException(name="SecurityError", code=18)
