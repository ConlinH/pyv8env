from .flags import *
from .v8_event import Event


@construct_111001
class TextFormatUpdateEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TextFormatUpdateEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getTextFormats", "fn_getTextFormats", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_format_update_event.py -> TextFormatUpdateEvent.isTrusted -> get attr')

    def fn_getTextFormats(self, *args):
        logger.debug(f'patch -> v8_text_format_update_event.py -> TextFormatUpdateEvent.getTextFormats{tuple(args)} -> method')
