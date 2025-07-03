from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLCanvasElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLCanvasElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("captureStream", "fn_captureStream", 0, 0, 1, 0, 0, 0, 0),
        ("getContext", "fn_getContext", 1, 0, 1, 0, 0, 0, 0),
        ("toBlob", "fn_toBlob", 1, 0, 1, 0, 0, 0, 0),
        ("toDataURL", "fn_toDataURL", 0, 0, 1, 0, 0, 0, 0),
        ("transferControlToOffscreen", "fn_transferControlToOffscreen", 0, 0, 1, 0, 0, 0, 0),
        ("configureHighDynamicRange", "fn_configureHighDynamicRange", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def fn_captureStream(self, *args):
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.captureStream{tuple(args)} -> method')

    def fn_getContext(self, *args):
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.getContext{tuple(args)} -> method')

    def fn_toBlob(self, *args):
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.toBlob{tuple(args)} -> method')

    def fn_toDataURL(self, *args):
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.toDataURL{tuple(args)} -> method')

    def fn_transferControlToOffscreen(self, *args):
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.transferControlToOffscreen{tuple(args)} -> method')

    def fn_configureHighDynamicRange(self, *args):
        logger.debug(f'patch -> v8_html_canvas_element.py -> HTMLCanvasElement.configureHighDynamicRange{tuple(args)} -> method')
