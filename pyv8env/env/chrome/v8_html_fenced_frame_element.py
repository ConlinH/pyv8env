from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLFencedFrameElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLFencedFrameElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("sandbox", "get_sandbox", "set_sandbox", 0, 1, 0, 0, 0, 0, 1),
        ("config", "get_config", "set_config", 0, 1, 0, 0, 0, 0, 1),
        ("allow", "get_allow", "set_allow", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("canLoadOpaqueURL", "fn_canLoadOpaqueURL", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_fenced_frame_element.py -> HTMLFencedFrameElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_fenced_frame_element.py -> HTMLFencedFrameElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_sandbox(self):
        val = self._attr.get('sandbox')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_fenced_frame_element.py -> HTMLFencedFrameElement.sandbox -> get attr')

    def set_sandbox(self, val):
        self._attr['sandbox'] = val

    def get_config(self):
        val = self._attr.get('config')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_fenced_frame_element.py -> HTMLFencedFrameElement.config -> get attr')

    def set_config(self, val):
        self._attr['config'] = val

    def get_allow(self):
        val = self._attr.get('allow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_fenced_frame_element.py -> HTMLFencedFrameElement.allow -> get attr')

    def set_allow(self, val):
        self._attr['allow'] = val

    @classmethod
    def fn_canLoadOpaqueURL(cls, *args):
        logger.debug(f'patch -> v8_html_fenced_frame_element.py -> HTMLFencedFrameElement.canLoadOpaqueURL{tuple(args)} -> method')
