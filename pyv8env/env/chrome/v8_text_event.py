from .flags import *
from .v8_ui_event import UIEvent


@construct_100001
class TextEvent(UIEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TextEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("initTextEvent", "fn_initTextEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_event.py -> TextEvent.data -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_event.py -> TextEvent.isTrusted -> get attr')

    def fn_initTextEvent(self, *args):
        logger.debug(f'patch -> v8_text_event.py -> TextEvent.initTextEvent{tuple(args)} -> method')
