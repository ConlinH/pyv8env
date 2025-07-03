from .flags import *
from .v8_pointer_event import PointerEvent


@construct_100001
class HighlightPointerEvent(PointerEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HighlightPointerEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("range", "get_range", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_range(self):
        val = self._attr.get('range')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_highlight_pointer_event.py -> HighlightPointerEvent.range -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_highlight_pointer_event.py -> HighlightPointerEvent.isTrusted -> get attr')
