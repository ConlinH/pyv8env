from .flags import *
from .v8_webgl_object import WebGLObject


@construct_100001
class WebGLSampler(WebGLObject):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WebGLSampler, self).__init__(*args, **kw)
