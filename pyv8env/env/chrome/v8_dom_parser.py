from .flags import *


@construct_110001
class DOMParser:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("parseFromString", "fn_parseFromString", 2, 0, 1, 0, 0, 0, 0),

    )

    def fn_parseFromString(self, *args):
        logger.debug(f'patch -> v8_dom_parser.py -> DOMParser.parseFromString{tuple(args)} -> method')
