from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class LargestContentfulPaint(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(LargestContentfulPaint, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("renderTime", "get_renderTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("loadTime", "get_loadTime", None, 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("url", "get_url", None, 0, 1, 0, 0, 0, 0, 1),
        ("element", "get_element", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstAnimatedFrameTime", "get_firstAnimatedFrameTime", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_renderTime(self):
        val = self._attr.get('renderTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.renderTime -> get attr')

    def get_loadTime(self):
        val = self._attr.get('loadTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.loadTime -> get attr')

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.size -> get attr')

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.id -> get attr')

    def get_url(self):
        val = self._attr.get('url')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.url -> get attr')

    def get_element(self):
        val = self._attr.get('element')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.element -> get attr')

    def get_firstAnimatedFrameTime(self):
        val = self._attr.get('firstAnimatedFrameTime')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.firstAnimatedFrameTime -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_largest_contentful_paint.py -> LargestContentfulPaint.toJSON{tuple(args)} -> method')
