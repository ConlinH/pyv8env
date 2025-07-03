from .flags import *


@construct_000000
class WebGLDrawBuffers:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    COLOR_ATTACHMENT0_WEBGL = 36064
    COLOR_ATTACHMENT1_WEBGL = 36065
    COLOR_ATTACHMENT2_WEBGL = 36066
    COLOR_ATTACHMENT3_WEBGL = 36067
    COLOR_ATTACHMENT4_WEBGL = 36068
    COLOR_ATTACHMENT5_WEBGL = 36069
    COLOR_ATTACHMENT6_WEBGL = 36070
    COLOR_ATTACHMENT7_WEBGL = 36071
    COLOR_ATTACHMENT8_WEBGL = 36072
    COLOR_ATTACHMENT9_WEBGL = 36073
    COLOR_ATTACHMENT10_WEBGL = 36074
    COLOR_ATTACHMENT11_WEBGL = 36075
    COLOR_ATTACHMENT12_WEBGL = 36076
    COLOR_ATTACHMENT13_WEBGL = 36077
    COLOR_ATTACHMENT14_WEBGL = 36078
    COLOR_ATTACHMENT15_WEBGL = 36079
    DRAW_BUFFER0_WEBGL = 34853
    DRAW_BUFFER1_WEBGL = 34854
    DRAW_BUFFER2_WEBGL = 34855
    DRAW_BUFFER3_WEBGL = 34856
    DRAW_BUFFER4_WEBGL = 34857
    DRAW_BUFFER5_WEBGL = 34858
    DRAW_BUFFER6_WEBGL = 34859
    DRAW_BUFFER7_WEBGL = 34860
    DRAW_BUFFER8_WEBGL = 34861
    DRAW_BUFFER9_WEBGL = 34862
    DRAW_BUFFER10_WEBGL = 34863
    DRAW_BUFFER11_WEBGL = 34864
    DRAW_BUFFER12_WEBGL = 34865
    DRAW_BUFFER13_WEBGL = 34866
    DRAW_BUFFER14_WEBGL = 34867
    DRAW_BUFFER15_WEBGL = 34868
    MAX_COLOR_ATTACHMENTS_WEBGL = 36063
    MAX_DRAW_BUFFERS_WEBGL = 34852

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("drawBuffersWEBGL", "fn_drawBuffersWEBGL", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_drawBuffersWEBGL(self, *args):
        logger.debug(f'patch -> v8_webgl_draw_buffers.py -> WebGLDrawBuffers.drawBuffersWEBGL{tuple(args)} -> method')
