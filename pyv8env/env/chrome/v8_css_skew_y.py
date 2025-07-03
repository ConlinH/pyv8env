from .flags import *
from .v8_css_transform_component import CSSTransformComponent


@construct_111001
class CSSSkewY(CSSTransformComponent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSSkewY, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("ay", "get_ay", "set_ay", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_ay(self):
        val = self._attr.get('ay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_skew_y.py -> CSSSkewY.ay -> get attr')

    def set_ay(self, val):
        self._attr['ay'] = val
