from .flags import *
from .v8_css_numeric_value import CSSNumericValue


@construct_112001
class CSSUnitValue(CSSNumericValue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSUnitValue, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("unit", "get_unit", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_unit_value.py -> CSSUnitValue.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_unit(self):
        val = self._attr.get('unit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_unit_value.py -> CSSUnitValue.unit -> get attr')
