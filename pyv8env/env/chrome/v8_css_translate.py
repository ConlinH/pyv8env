from .flags import *
from .v8_css_transform_component import CSSTransformComponent


@construct_112001
class CSSTranslate(CSSTransformComponent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSTranslate, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", "set_x", 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", "set_y", 0, 1, 0, 0, 0, 0, 1),
        ("z", "get_z", "set_z", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_translate.py -> CSSTranslate.x -> get attr')

    def set_x(self, val):
        self._attr['x'] = val

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_translate.py -> CSSTranslate.y -> get attr')

    def set_y(self, val):
        self._attr['y'] = val

    def get_z(self):
        val = self._attr.get('z')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_translate.py -> CSSTranslate.z -> get attr')

    def set_z(self, val):
        self._attr['z'] = val
