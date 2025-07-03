from .flags import *


@construct_100001
class CaretPosition:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("offsetNode", "get_offsetNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("offset", "get_offset", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getClientRect", "fn_getClientRect", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_offsetNode(self):
        val = self._attr.get('offsetNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_caret_position.py -> CaretPosition.offsetNode -> get attr')

    def get_offset(self):
        val = self._attr.get('offset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_caret_position.py -> CaretPosition.offset -> get attr')

    def fn_getClientRect(self, *args):
        logger.debug(f'patch -> v8_caret_position.py -> CaretPosition.getClientRect{tuple(args)} -> method')
