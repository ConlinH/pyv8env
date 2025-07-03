from .flags import *


@construct_111001
class CSSVariableReferenceValue:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("variable", "get_variable", "set_variable", 0, 1, 0, 0, 0, 0, 1),
        ("fallback", "get_fallback", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_variable(self):
        val = self._attr.get('variable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_variable_reference_value.py -> CSSVariableReferenceValue.variable -> get attr')

    def set_variable(self, val):
        self._attr['variable'] = val

    def get_fallback(self):
        val = self._attr.get('fallback')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_variable_reference_value.py -> CSSVariableReferenceValue.fallback -> get attr')
