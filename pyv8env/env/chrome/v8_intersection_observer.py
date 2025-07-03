from .flags import *


@construct_111001
class IntersectionObserver:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("root", "get_root", None, 0, 1, 0, 0, 0, 0, 1),
        ("rootMargin", "get_rootMargin", None, 0, 1, 0, 0, 0, 0, 1),
        ("thresholds", "get_thresholds", None, 0, 1, 0, 0, 0, 0, 1),
        ("delay", "get_delay", None, 0, 1, 0, 0, 0, 0, 1),
        ("trackVisibility", "get_trackVisibility", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollMargin", "get_scrollMargin", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("disconnect", "fn_disconnect", 0, 0, 1, 0, 0, 0, 0),
        ("observe", "fn_observe", 1, 0, 1, 0, 0, 0, 0),
        ("takeRecords", "fn_takeRecords", 0, 0, 1, 0, 0, 0, 0),
        ("unobserve", "fn_unobserve", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_root(self):
        val = self._attr.get('root')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.root -> get attr')

    def get_rootMargin(self):
        val = self._attr.get('rootMargin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.rootMargin -> get attr')

    def get_thresholds(self):
        val = self._attr.get('thresholds')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.thresholds -> get attr')

    def get_delay(self):
        val = self._attr.get('delay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.delay -> get attr')

    def get_trackVisibility(self):
        val = self._attr.get('trackVisibility')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.trackVisibility -> get attr')

    def get_scrollMargin(self):
        val = self._attr.get('scrollMargin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.scrollMargin -> get attr')

    def fn_disconnect(self, *args):
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.disconnect{tuple(args)} -> method')

    def fn_observe(self, *args):
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.observe{tuple(args)} -> method')

    def fn_takeRecords(self, *args):
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.takeRecords{tuple(args)} -> method')

    def fn_unobserve(self, *args):
        logger.debug(f'patch -> v8_intersection_observer.py -> IntersectionObserver.unobserve{tuple(args)} -> method')
