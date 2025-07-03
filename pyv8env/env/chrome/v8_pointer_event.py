from .flags import *
from .v8_mouse_event import MouseEvent


@construct_111001
class PointerEvent(MouseEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PointerEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("pointerId", "get_pointerId", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("pressure", "get_pressure", None, 0, 1, 0, 0, 0, 0, 1),
        ("tiltX", "get_tiltX", None, 0, 1, 0, 0, 0, 0, 1),
        ("tiltY", "get_tiltY", None, 0, 1, 0, 0, 0, 0, 1),
        ("azimuthAngle", "get_azimuthAngle", None, 0, 1, 0, 0, 0, 0, 1),
        ("altitudeAngle", "get_altitudeAngle", None, 0, 1, 0, 0, 0, 0, 1),
        ("tangentialPressure", "get_tangentialPressure", None, 0, 1, 0, 0, 0, 0, 1),
        ("twist", "get_twist", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointerType", "get_pointerType", None, 0, 1, 0, 0, 0, 0, 1),
        ("isPrimary", "get_isPrimary", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),
        ("deviceProperties", "get_deviceProperties", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getCoalescedEvents", "fn_getCoalescedEvents", 0, 0, 1, 0, 0, 0, 0),
        ("getPredictedEvents", "fn_getPredictedEvents", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_pointerId(self):
        val = self._attr.get('pointerId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.pointerId -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.height -> get attr')

    def get_pressure(self):
        val = self._attr.get('pressure')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.pressure -> get attr')

    def get_tiltX(self):
        val = self._attr.get('tiltX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.tiltX -> get attr')

    def get_tiltY(self):
        val = self._attr.get('tiltY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.tiltY -> get attr')

    def get_azimuthAngle(self):
        val = self._attr.get('azimuthAngle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.azimuthAngle -> get attr')

    def get_altitudeAngle(self):
        val = self._attr.get('altitudeAngle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.altitudeAngle -> get attr')

    def get_tangentialPressure(self):
        val = self._attr.get('tangentialPressure')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.tangentialPressure -> get attr')

    def get_twist(self):
        val = self._attr.get('twist')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.twist -> get attr')

    def get_pointerType(self):
        val = self._attr.get('pointerType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.pointerType -> get attr')

    def get_isPrimary(self):
        val = self._attr.get('isPrimary')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.isPrimary -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.isTrusted -> get attr')

    def get_deviceProperties(self):
        val = self._attr.get('deviceProperties')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.deviceProperties -> get attr')

    def fn_getCoalescedEvents(self, *args):
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.getCoalescedEvents{tuple(args)} -> method')

    def fn_getPredictedEvents(self, *args):
        logger.debug(f'patch -> v8_pointer_event.py -> PointerEvent.getPredictedEvents{tuple(args)} -> method')
