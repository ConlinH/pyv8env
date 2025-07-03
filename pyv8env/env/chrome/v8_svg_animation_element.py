from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGAnimationElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGAnimationElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("targetElement", "get_targetElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("onbegin", "get_onbegin", "set_onbegin", 0, 1, 0, 0, 0, 0, 1),
        ("onend", "get_onend", "set_onend", 0, 1, 0, 0, 0, 0, 1),
        ("onrepeat", "get_onrepeat", "set_onrepeat", 0, 1, 0, 0, 0, 0, 1),
        ("requiredExtensions", "get_requiredExtensions", None, 0, 1, 0, 0, 0, 0, 1),
        ("systemLanguage", "get_systemLanguage", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("beginElement", "fn_beginElement", 0, 0, 1, 0, 0, 0, 0),
        ("beginElementAt", "fn_beginElementAt", 1, 0, 1, 0, 0, 0, 0),
        ("endElement", "fn_endElement", 0, 0, 1, 0, 0, 0, 0),
        ("endElementAt", "fn_endElementAt", 1, 0, 1, 0, 0, 0, 0),
        ("getCurrentTime", "fn_getCurrentTime", 0, 0, 1, 0, 0, 0, 0),
        ("getSimpleDuration", "fn_getSimpleDuration", 0, 0, 1, 0, 0, 0, 0),
        ("getStartTime", "fn_getStartTime", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_targetElement(self):
        val = self._attr.get('targetElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.targetElement -> get attr')

    def get_onbegin(self):
        val = self._attr.get('onbegin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.onbegin -> get attr')

    def set_onbegin(self, val):
        self._attr['onbegin'] = val

    def get_onend(self):
        val = self._attr.get('onend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.onend -> get attr')

    def set_onend(self, val):
        self._attr['onend'] = val

    def get_onrepeat(self):
        val = self._attr.get('onrepeat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.onrepeat -> get attr')

    def set_onrepeat(self, val):
        self._attr['onrepeat'] = val

    def get_requiredExtensions(self):
        val = self._attr.get('requiredExtensions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.requiredExtensions -> get attr')

    def get_systemLanguage(self):
        val = self._attr.get('systemLanguage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.systemLanguage -> get attr')

    def fn_beginElement(self, *args):
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.beginElement{tuple(args)} -> method')

    def fn_beginElementAt(self, *args):
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.beginElementAt{tuple(args)} -> method')

    def fn_endElement(self, *args):
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.endElement{tuple(args)} -> method')

    def fn_endElementAt(self, *args):
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.endElementAt{tuple(args)} -> method')

    def fn_getCurrentTime(self, *args):
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.getCurrentTime{tuple(args)} -> method')

    def fn_getSimpleDuration(self, *args):
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.getSimpleDuration{tuple(args)} -> method')

    def fn_getStartTime(self, *args):
        logger.debug(f'patch -> v8_svg_animation_element.py -> SVGAnimationElement.getStartTime{tuple(args)} -> method')
