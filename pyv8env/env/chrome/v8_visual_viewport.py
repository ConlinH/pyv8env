from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class VisualViewport(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(VisualViewport, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("offsetLeft", "get_offsetLeft", None, 0, 1, 0, 0, 0, 0, 1),
        ("offsetTop", "get_offsetTop", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageLeft", "get_pageLeft", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageTop", "get_pageTop", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("scale", "get_scale", None, 0, 1, 0, 0, 0, 0, 1),
        ("onresize", "get_onresize", "set_onresize", 0, 1, 0, 0, 0, 0, 1),
        ("onscroll", "get_onscroll", "set_onscroll", 0, 1, 0, 0, 0, 0, 1),
        ("onscrollend", "get_onscrollend", "set_onscrollend", 0, 1, 0, 0, 0, 0, 1),
        ("segments", "get_segments", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_offsetLeft(self):
        val = self._attr.get('offsetLeft')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.offsetLeft -> get attr')

    def get_offsetTop(self):
        val = self._attr.get('offsetTop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.offsetTop -> get attr')

    def get_pageLeft(self):
        val = self._attr.get('pageLeft')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.pageLeft -> get attr')

    def get_pageTop(self):
        val = self._attr.get('pageTop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.pageTop -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.height -> get attr')

    def get_scale(self):
        val = self._attr.get('scale')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.scale -> get attr')

    def get_onresize(self):
        val = self._attr.get('onresize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.onresize -> get attr')

    def set_onresize(self, val):
        self._attr['onresize'] = val

    def get_onscroll(self):
        val = self._attr.get('onscroll')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.onscroll -> get attr')

    def set_onscroll(self, val):
        self._attr['onscroll'] = val

    def get_onscrollend(self):
        val = self._attr.get('onscrollend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.onscrollend -> get attr')

    def set_onscrollend(self, val):
        self._attr['onscrollend'] = val

    def get_segments(self):
        val = self._attr.get('segments')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_visual_viewport.py -> VisualViewport.segments -> get attr')
