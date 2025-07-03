from .flags import *


@construct_100001
class Part:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("root", "get_root", None, 0, 1, 0, 0, 0, 0, 1),
        ("metadata", "get_metadata", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("disconnect", "fn_disconnect", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_root(self):
        val = self._attr.get('root')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_part.py -> Part.root -> get attr')

    def get_metadata(self):
        val = self._attr.get('metadata')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_part.py -> Part.metadata -> get attr')

    def fn_disconnect(self, *args):
        logger.debug(f'patch -> v8_part.py -> Part.disconnect{tuple(args)} -> method')
