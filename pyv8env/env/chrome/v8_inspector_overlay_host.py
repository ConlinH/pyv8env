from .flags import *


@construct_000000
class InspectorOverlayHost:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("send", "fn_send", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_send(self, *args):
        logger.debug(f'patch -> v8_inspector_overlay_host.py -> InspectorOverlayHost.send{tuple(args)} -> method')
