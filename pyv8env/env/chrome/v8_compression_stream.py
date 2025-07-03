from .flags import *


@construct_111001
class CompressionStream:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("readable", "get_readable", None, 0, 1, 0, 0, 0, 0, 1),
        ("writable", "get_writable", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_readable(self):
        val = self._attr.get('readable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_compression_stream.py -> CompressionStream.readable -> get attr')

    def get_writable(self):
        val = self._attr.get('writable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_compression_stream.py -> CompressionStream.writable -> get attr')
