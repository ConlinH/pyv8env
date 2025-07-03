from .flags import *


@construct_110001
class XMLSerializer:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("serializeToString", "fn_serializeToString", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_serializeToString(self, *args):
        logger.debug(f'patch -> v8_xml_serializer.py -> XMLSerializer.serializeToString{tuple(args)} -> method')
