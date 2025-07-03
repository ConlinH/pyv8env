from .flags import *
from .v8_css_transform_component import CSSTransformComponent


@construct_111001
class CSSPerspective(CSSTransformComponent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSPerspective, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("length", "get_length", "set_length", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_perspective.py -> CSSPerspective.length -> get attr')

    def set_length(self, val):
        self._attr['length'] = val
