from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLMarqueeElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLMarqueeElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("behavior", "get_behavior", "set_behavior", 0, 1, 0, 0, 0, 0, 1),
        ("bgColor", "get_bgColor", "set_bgColor", 0, 1, 0, 0, 0, 0, 1),
        ("direction", "get_direction", "set_direction", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("hspace", "get_hspace", "set_hspace", 0, 1, 0, 0, 0, 0, 1),
        ("loop", "get_loop", "set_loop", 0, 1, 0, 0, 0, 0, 1),
        ("scrollAmount", "get_scrollAmount", "set_scrollAmount", 0, 1, 0, 0, 0, 0, 1),
        ("scrollDelay", "get_scrollDelay", "set_scrollDelay", 0, 1, 0, 0, 0, 0, 1),
        ("trueSpeed", "get_trueSpeed", "set_trueSpeed", 0, 1, 0, 0, 0, 0, 1),
        ("vspace", "get_vspace", "set_vspace", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("start", "fn_start", 0, 0, 1, 0, 0, 0, 0),
        ("stop", "fn_stop", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_behavior(self):
        val = self._attr.get('behavior')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.behavior -> get attr')

    def set_behavior(self, val):
        self._attr['behavior'] = val

    def get_bgColor(self):
        val = self._attr.get('bgColor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.bgColor -> get attr')

    def set_bgColor(self, val):
        self._attr['bgColor'] = val

    def get_direction(self):
        val = self._attr.get('direction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.direction -> get attr')

    def set_direction(self, val):
        self._attr['direction'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_hspace(self):
        val = self._attr.get('hspace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.hspace -> get attr')

    def set_hspace(self, val):
        self._attr['hspace'] = val

    def get_loop(self):
        val = self._attr.get('loop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.loop -> get attr')

    def set_loop(self, val):
        self._attr['loop'] = val

    def get_scrollAmount(self):
        val = self._attr.get('scrollAmount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.scrollAmount -> get attr')

    def set_scrollAmount(self, val):
        self._attr['scrollAmount'] = val

    def get_scrollDelay(self):
        val = self._attr.get('scrollDelay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.scrollDelay -> get attr')

    def set_scrollDelay(self, val):
        self._attr['scrollDelay'] = val

    def get_trueSpeed(self):
        val = self._attr.get('trueSpeed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.trueSpeed -> get attr')

    def set_trueSpeed(self, val):
        self._attr['trueSpeed'] = val

    def get_vspace(self):
        val = self._attr.get('vspace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.vspace -> get attr')

    def set_vspace(self, val):
        self._attr['vspace'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.start{tuple(args)} -> method')

    def fn_stop(self, *args):
        logger.debug(f'patch -> v8_html_marquee_element.py -> HTMLMarqueeElement.stop{tuple(args)} -> method')
