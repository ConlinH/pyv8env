from .flags import *


@construct_110001
class Blob:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("arrayBuffer", "fn_arrayBuffer", 0, 0, 1, 0, 1, 0, 0),
        ("slice", "fn_slice", 0, 0, 1, 0, 0, 0, 0),
        ("stream", "fn_stream", 0, 0, 1, 0, 0, 0, 0),
        ("text", "fn_text", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_blob.py -> Blob.size -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_blob.py -> Blob.type -> get attr')

    def fn_arrayBuffer(self, *args):
        logger.debug(f'patch -> v8_blob.py -> Blob.arrayBuffer{tuple(args)} -> method')

    def fn_slice(self, *args):
        logger.debug(f'patch -> v8_blob.py -> Blob.slice{tuple(args)} -> method')

    def fn_stream(self, *args):
        logger.debug(f'patch -> v8_blob.py -> Blob.stream{tuple(args)} -> method')

    def fn_text(self, *args):
        logger.debug(f'patch -> v8_blob.py -> Blob.text{tuple(args)} -> method')
