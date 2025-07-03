from .flags import *


@construct_100001
class XRAnchor:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("anchorSpace", "get_anchorSpace", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("delete", "fn_delete", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_anchorSpace(self):
        val = self._attr.get('anchorSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_anchor.py -> XRAnchor.anchorSpace -> get attr')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_xr_anchor.py -> XRAnchor.delete{tuple(args)} -> method')
