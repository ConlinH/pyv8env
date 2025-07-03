from .flags import *


@construct_100001
class SVGAnimatedBoolean:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("baseVal", "get_baseVal", "set_baseVal", 0, 1, 0, 0, 0, 0, 1),
        ("animVal", "get_animVal", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_baseVal(self):
        val = self._attr.get('baseVal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animated_boolean.py -> SVGAnimatedBoolean.baseVal -> get attr')

    def set_baseVal(self, val):
        self._attr['baseVal'] = val

    def get_animVal(self):
        val = self._attr.get('animVal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_animated_boolean.py -> SVGAnimatedBoolean.animVal -> get attr')
