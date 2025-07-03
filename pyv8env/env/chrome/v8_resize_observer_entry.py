from .flags import *


@construct_100001
class ResizeObserverEntry:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentRect", "get_contentRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentBoxSize", "get_contentBoxSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("borderBoxSize", "get_borderBoxSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("devicePixelContentBoxSize", "get_devicePixelContentBoxSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_resize_observer_entry.py -> ResizeObserverEntry.target -> get attr')

    def get_contentRect(self):
        val = self._attr.get('contentRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_resize_observer_entry.py -> ResizeObserverEntry.contentRect -> get attr')

    def get_contentBoxSize(self):
        val = self._attr.get('contentBoxSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_resize_observer_entry.py -> ResizeObserverEntry.contentBoxSize -> get attr')

    def get_borderBoxSize(self):
        val = self._attr.get('borderBoxSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_resize_observer_entry.py -> ResizeObserverEntry.borderBoxSize -> get attr')

    def get_devicePixelContentBoxSize(self):
        val = self._attr.get('devicePixelContentBoxSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_resize_observer_entry.py -> ResizeObserverEntry.devicePixelContentBoxSize -> get attr')
