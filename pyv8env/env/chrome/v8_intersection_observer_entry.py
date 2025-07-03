from .flags import *


@construct_100001
class IntersectionObserverEntry:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("time", "get_time", None, 0, 1, 0, 0, 0, 0, 1),
        ("rootBounds", "get_rootBounds", None, 0, 1, 0, 0, 0, 0, 1),
        ("boundingClientRect", "get_boundingClientRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("intersectionRect", "get_intersectionRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("isIntersecting", "get_isIntersecting", None, 0, 1, 0, 0, 0, 0, 1),
        ("isVisible", "get_isVisible", None, 0, 1, 0, 0, 0, 0, 1),
        ("intersectionRatio", "get_intersectionRatio", None, 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_time(self):
        val = self._attr.get('time')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.time -> get attr')

    def get_rootBounds(self):
        val = self._attr.get('rootBounds')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.rootBounds -> get attr')

    def get_boundingClientRect(self):
        val = self._attr.get('boundingClientRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.boundingClientRect -> get attr')

    def get_intersectionRect(self):
        val = self._attr.get('intersectionRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.intersectionRect -> get attr')

    def get_isIntersecting(self):
        val = self._attr.get('isIntersecting')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.isIntersecting -> get attr')

    def get_isVisible(self):
        val = self._attr.get('isVisible')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.isVisible -> get attr')

    def get_intersectionRatio(self):
        val = self._attr.get('intersectionRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.intersectionRatio -> get attr')

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer_entry.py -> IntersectionObserverEntry.target -> get attr')
