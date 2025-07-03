from .flags import *
from .v8_ui_event import UIEvent


@construct_111001
class KeyboardEvent(UIEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(KeyboardEvent, self).__init__(*args, **kw)
    DOM_KEY_LOCATION_STANDARD = 0
    DOM_KEY_LOCATION_LEFT = 1
    DOM_KEY_LOCATION_RIGHT = 2
    DOM_KEY_LOCATION_NUMPAD = 3

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("key", "get_key", None, 0, 1, 0, 0, 0, 0, 1),
        ("code", "get_code", None, 0, 1, 0, 0, 0, 0, 1),
        ("location", "get_location", None, 0, 1, 0, 0, 0, 0, 1),
        ("ctrlKey", "get_ctrlKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("shiftKey", "get_shiftKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("altKey", "get_altKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("metaKey", "get_metaKey", None, 0, 1, 0, 0, 0, 0, 1),
        ("repeat", "get_repeat", None, 0, 1, 0, 0, 0, 0, 1),
        ("isComposing", "get_isComposing", None, 0, 1, 0, 0, 0, 0, 1),
        ("charCode", "get_charCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("keyCode", "get_keyCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getModifierState", "fn_getModifierState", 1, 0, 1, 0, 0, 0, 0),
        ("initKeyboardEvent", "fn_initKeyboardEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_key(self):
        val = self._attr.get('key')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.key -> get attr')

    def get_code(self):
        val = self._attr.get('code')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.code -> get attr')

    def get_location(self):
        val = self._attr.get('location')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.location -> get attr')

    def get_ctrlKey(self):
        val = self._attr.get('ctrlKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.ctrlKey -> get attr')

    def get_shiftKey(self):
        val = self._attr.get('shiftKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.shiftKey -> get attr')

    def get_altKey(self):
        val = self._attr.get('altKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.altKey -> get attr')

    def get_metaKey(self):
        val = self._attr.get('metaKey')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.metaKey -> get attr')

    def get_repeat(self):
        val = self._attr.get('repeat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.repeat -> get attr')

    def get_isComposing(self):
        val = self._attr.get('isComposing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.isComposing -> get attr')

    def get_charCode(self):
        val = self._attr.get('charCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.charCode -> get attr')

    def get_keyCode(self):
        val = self._attr.get('keyCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.keyCode -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.isTrusted -> get attr')

    def fn_getModifierState(self, *args):
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.getModifierState{tuple(args)} -> method')

    def fn_initKeyboardEvent(self, *args):
        logger.debug(f'patch -> v8_keyboard_event.py -> KeyboardEvent.initKeyboardEvent{tuple(args)} -> method')
