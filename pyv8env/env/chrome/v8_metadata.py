from .flags import *


@construct_000000
class Metadata:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("modificationTime", "get_modificationTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_modificationTime(self):
        val = self._attr.get('modificationTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_metadata.py -> Metadata.modificationTime -> get attr')

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_metadata.py -> Metadata.size -> get attr')
