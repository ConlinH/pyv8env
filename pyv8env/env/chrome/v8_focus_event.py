from .flags import *
from .v8_ui_event import UIEvent


@construct_111001
class FocusEvent(UIEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FocusEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("relatedTarget", "get_relatedTarget", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_relatedTarget(self):
        val = self._attr.get('relatedTarget')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_focus_event.py -> FocusEvent.relatedTarget -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_focus_event.py -> FocusEvent.isTrusted -> get attr')
