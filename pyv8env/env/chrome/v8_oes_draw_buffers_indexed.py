from .flags import *


@construct_000000
class OESDrawBuffersIndexed:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("blendEquationSeparateiOES", "fn_blendEquationSeparateiOES", 3, 0, 1, 0, 0, 0, 0),
        ("blendEquationiOES", "fn_blendEquationiOES", 2, 0, 1, 0, 0, 0, 0),
        ("blendFuncSeparateiOES", "fn_blendFuncSeparateiOES", 5, 0, 1, 0, 0, 0, 0),
        ("blendFunciOES", "fn_blendFunciOES", 3, 0, 1, 0, 0, 0, 0),
        ("colorMaskiOES", "fn_colorMaskiOES", 5, 0, 1, 0, 0, 0, 0),
        ("disableiOES", "fn_disableiOES", 2, 0, 1, 0, 0, 0, 0),
        ("enableiOES", "fn_enableiOES", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_blendEquationSeparateiOES(self, *args):
        logger.debug(f'patch -> v8_oes_draw_buffers_indexed.py -> OESDrawBuffersIndexed.blendEquationSeparateiOES{tuple(args)} -> method')

    def fn_blendEquationiOES(self, *args):
        logger.debug(f'patch -> v8_oes_draw_buffers_indexed.py -> OESDrawBuffersIndexed.blendEquationiOES{tuple(args)} -> method')

    def fn_blendFuncSeparateiOES(self, *args):
        logger.debug(f'patch -> v8_oes_draw_buffers_indexed.py -> OESDrawBuffersIndexed.blendFuncSeparateiOES{tuple(args)} -> method')

    def fn_blendFunciOES(self, *args):
        logger.debug(f'patch -> v8_oes_draw_buffers_indexed.py -> OESDrawBuffersIndexed.blendFunciOES{tuple(args)} -> method')

    def fn_colorMaskiOES(self, *args):
        logger.debug(f'patch -> v8_oes_draw_buffers_indexed.py -> OESDrawBuffersIndexed.colorMaskiOES{tuple(args)} -> method')

    def fn_disableiOES(self, *args):
        logger.debug(f'patch -> v8_oes_draw_buffers_indexed.py -> OESDrawBuffersIndexed.disableiOES{tuple(args)} -> method')

    def fn_enableiOES(self, *args):
        logger.debug(f'patch -> v8_oes_draw_buffers_indexed.py -> OESDrawBuffersIndexed.enableiOES{tuple(args)} -> method')
