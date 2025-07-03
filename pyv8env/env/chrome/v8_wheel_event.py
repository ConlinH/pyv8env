from .flags import *
from .v8_mouse_event import MouseEvent


@construct_111001
class WheelEvent(MouseEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WheelEvent, self).__init__(*args, **kw)
    DOM_DELTA_PIXEL = 0
    DOM_DELTA_LINE = 1
    DOM_DELTA_PAGE = 2

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("deltaX", "get_deltaX", None, 0, 1, 0, 0, 0, 0, 1),
        ("deltaY", "get_deltaY", None, 0, 1, 0, 0, 0, 0, 1),
        ("deltaZ", "get_deltaZ", None, 0, 1, 0, 0, 0, 0, 1),
        ("deltaMode", "get_deltaMode", None, 0, 1, 0, 0, 0, 0, 1),
        ("wheelDeltaX", "get_wheelDeltaX", None, 0, 1, 0, 0, 0, 0, 1),
        ("wheelDeltaY", "get_wheelDeltaY", None, 0, 1, 0, 0, 0, 0, 1),
        ("wheelDelta", "get_wheelDelta", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_deltaX(self):
        val = self._attr.get('deltaX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.deltaX -> get attr')

    def get_deltaY(self):
        val = self._attr.get('deltaY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.deltaY -> get attr')

    def get_deltaZ(self):
        val = self._attr.get('deltaZ')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.deltaZ -> get attr')

    def get_deltaMode(self):
        val = self._attr.get('deltaMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.deltaMode -> get attr')

    def get_wheelDeltaX(self):
        val = self._attr.get('wheelDeltaX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.wheelDeltaX -> get attr')

    def get_wheelDeltaY(self):
        val = self._attr.get('wheelDeltaY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.wheelDeltaY -> get attr')

    def get_wheelDelta(self):
        val = self._attr.get('wheelDelta')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.wheelDelta -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_wheel_event.py -> WheelEvent.isTrusted -> get attr')
