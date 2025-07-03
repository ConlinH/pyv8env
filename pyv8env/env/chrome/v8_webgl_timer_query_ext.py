from .flags import *
from .v8_webgl_object import WebGLObject


@construct_000000
class WebGLTimerQueryEXT(WebGLObject):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WebGLTimerQueryEXT, self).__init__(*args, **kw)
