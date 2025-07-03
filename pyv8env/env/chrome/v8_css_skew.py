from .flags import *
from .v8_css_transform_component import CSSTransformComponent


@construct_112001
class CSSSkew(CSSTransformComponent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSSkew, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("ax", "get_ax", "set_ax", 0, 1, 0, 0, 0, 0, 1),
        ("ay", "get_ay", "set_ay", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_ax(self):
        val = self._attr.get('ax')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_skew.py -> CSSSkew.ax -> get attr')

    def set_ax(self, val):
        self._attr['ax'] = val

    def get_ay(self):
        val = self._attr.get('ay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_skew.py -> CSSSkew.ay -> get attr')

    def set_ay(self, val):
        self._attr['ay'] = val
