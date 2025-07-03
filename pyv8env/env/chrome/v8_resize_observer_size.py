from .flags import *


@construct_100001
class ResizeObserverSize:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("inlineSize", "get_inlineSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockSize", "get_blockSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_inlineSize(self):
        val = self._attr.get('inlineSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_resize_observer_size.py -> ResizeObserverSize.inlineSize -> get attr')

    def get_blockSize(self):
        val = self._attr.get('blockSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_resize_observer_size.py -> ResizeObserverSize.blockSize -> get attr')
