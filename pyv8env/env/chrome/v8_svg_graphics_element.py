from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGGraphicsElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGGraphicsElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("transform", "get_transform", None, 0, 1, 0, 0, 0, 0, 1),
        ("nearestViewportElement", "get_nearestViewportElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("farthestViewportElement", "get_farthestViewportElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("requiredExtensions", "get_requiredExtensions", None, 0, 1, 0, 0, 0, 0, 1),
        ("systemLanguage", "get_systemLanguage", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getBBox", "fn_getBBox", 0, 0, 1, 0, 0, 0, 0),
        ("getCTM", "fn_getCTM", 0, 0, 1, 0, 0, 0, 0),
        ("getScreenCTM", "fn_getScreenCTM", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_transform(self):
        val = self._attr.get('transform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.transform -> get attr')

    def get_nearestViewportElement(self):
        val = self._attr.get('nearestViewportElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.nearestViewportElement -> get attr')

    def get_farthestViewportElement(self):
        val = self._attr.get('farthestViewportElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.farthestViewportElement -> get attr')

    def get_requiredExtensions(self):
        val = self._attr.get('requiredExtensions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.requiredExtensions -> get attr')

    def get_systemLanguage(self):
        val = self._attr.get('systemLanguage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.systemLanguage -> get attr')

    def fn_getBBox(self, *args):
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.getBBox{tuple(args)} -> method')

    def fn_getCTM(self, *args):
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.getCTM{tuple(args)} -> method')

    def fn_getScreenCTM(self, *args):
        logger.debug(f'patch -> v8_svg_graphics_element.py -> SVGGraphicsElement.getScreenCTM{tuple(args)} -> method')
