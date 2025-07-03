from .flags import *


@construct_111001
class ClipboardItem:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("types", "get_types", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getType", "fn_getType", 1, 0, 1, 0, 1, 0, 0),
        ("supports", "fn_supports", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_types(self):
        val = self._attr.get('types')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_clipboard_item.py -> ClipboardItem.types -> get attr')

    def fn_getType(self, *args):
        logger.debug(f'patch -> v8_clipboard_item.py -> ClipboardItem.getType{tuple(args)} -> method')

    @classmethod
    def fn_supports(cls, *args):
        logger.debug(f'patch -> v8_clipboard_item.py -> ClipboardItem.supports{tuple(args)} -> method')
