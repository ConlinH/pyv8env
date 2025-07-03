from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class VirtualKeyboard(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(VirtualKeyboard, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("boundingRect", "get_boundingRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("overlaysContent", "get_overlaysContent", "set_overlaysContent", 0, 1, 0, 0, 0, 0, 1),
        ("ongeometrychange", "get_ongeometrychange", "set_ongeometrychange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("hide", "fn_hide", 0, 0, 1, 0, 0, 0, 0),
        ("show", "fn_show", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_boundingRect(self):
        val = self._attr.get('boundingRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_virtual_keyboard.py -> VirtualKeyboard.boundingRect -> get attr')

    def get_overlaysContent(self):
        val = self._attr.get('overlaysContent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_virtual_keyboard.py -> VirtualKeyboard.overlaysContent -> get attr')

    def set_overlaysContent(self, val):
        self._attr['overlaysContent'] = val

    def get_ongeometrychange(self):
        val = self._attr.get('ongeometrychange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_virtual_keyboard.py -> VirtualKeyboard.ongeometrychange -> get attr')

    def set_ongeometrychange(self, val):
        self._attr['ongeometrychange'] = val

    def fn_hide(self, *args):
        logger.debug(f'patch -> v8_virtual_keyboard.py -> VirtualKeyboard.hide{tuple(args)} -> method')

    def fn_show(self, *args):
        logger.debug(f'patch -> v8_virtual_keyboard.py -> VirtualKeyboard.show{tuple(args)} -> method')
