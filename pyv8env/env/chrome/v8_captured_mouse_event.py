from .flags import *
from .v8_event import Event


@construct_111001
class CapturedMouseEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CapturedMouseEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("surfaceX", "get_surfaceX", None, 0, 1, 0, 0, 0, 0, 1),
        ("surfaceY", "get_surfaceY", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_surfaceX(self):
        val = self._attr.get('surfaceX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_captured_mouse_event.py -> CapturedMouseEvent.surfaceX -> get attr')

    def get_surfaceY(self):
        val = self._attr.get('surfaceY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_captured_mouse_event.py -> CapturedMouseEvent.surfaceY -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_captured_mouse_event.py -> CapturedMouseEvent.isTrusted -> get attr')
