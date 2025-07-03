from .flags import *
from .v8_ui_event import UIEvent


@construct_111001
class TouchEvent(UIEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TouchEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("touches", "get_touches", None, 0, 1, 0, 0, 0, 0, 1),
        ("targetTouches", "get_targetTouches", None, 0, 1, 0, 0, 0, 0, 1),
        ("changedTouches", "get_changedTouches", None, 0, 1, 0, 0, 0, 0, 1),
        ("altKey", "get_altKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("metaKey", "get_metaKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("ctrlKey", "get_ctrlKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("shiftKey", "get_shiftKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_touches(self):
        val = self._attr.get('touches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.touches -> get attr')

    def get_targetTouches(self):
        val = self._attr.get('targetTouches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.targetTouches -> get attr')

    def get_changedTouches(self):
        val = self._attr.get('changedTouches')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.changedTouches -> get attr')

    def get_altKey(self):
        val = self._attr.get('altKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.altKey -> get attr')

    def get_metaKey(self):
        val = self._attr.get('metaKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.metaKey -> get attr')

    def get_ctrlKey(self):
        val = self._attr.get('ctrlKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.ctrlKey -> get attr')

    def get_shiftKey(self):
        val = self._attr.get('shiftKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.shiftKey -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_touch_event.py -> TouchEvent.isTrusted -> get attr')
