from .flags import *


@construct_100001
class SVGLength:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    SVG_LENGTHTYPE_UNKNOWN = 0
    SVG_LENGTHTYPE_NUMBER = 1
    SVG_LENGTHTYPE_PERCENTAGE = 2
    SVG_LENGTHTYPE_EMS = 3
    SVG_LENGTHTYPE_EXS = 4
    SVG_LENGTHTYPE_PX = 5
    SVG_LENGTHTYPE_CM = 6
    SVG_LENGTHTYPE_MM = 7
    SVG_LENGTHTYPE_IN = 8
    SVG_LENGTHTYPE_PT = 9
    SVG_LENGTHTYPE_PC = 10

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("unitType", "get_unitType", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("valueInSpecifiedUnits", "get_valueInSpecifiedUnits", "set_valueInSpecifiedUnits", 0, 1, 0, 0, 0, 0, 1),
        ("valueAsString", "get_valueAsString", "set_valueAsString", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("convertToSpecifiedUnits", "fn_convertToSpecifiedUnits", 1, 0, 1, 0, 0, 0, 0),
        ("newValueSpecifiedUnits", "fn_newValueSpecifiedUnits", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_unitType(self):
        val = self._attr.get('unitType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_length.py -> SVGLength.unitType -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_length.py -> SVGLength.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_valueInSpecifiedUnits(self):
        val = self._attr.get('valueInSpecifiedUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_length.py -> SVGLength.valueInSpecifiedUnits -> get attr')

    def set_valueInSpecifiedUnits(self, val):
        self._attr['valueInSpecifiedUnits'] = val

    def get_valueAsString(self):
        val = self._attr.get('valueAsString')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_length.py -> SVGLength.valueAsString -> get attr')

    def set_valueAsString(self, val):
        self._attr['valueAsString'] = val

    def fn_convertToSpecifiedUnits(self, *args):
        logger.debug(f'patch -> v8_svg_length.py -> SVGLength.convertToSpecifiedUnits{tuple(args)} -> method')

    def fn_newValueSpecifiedUnits(self, *args):
        logger.debug(f'patch -> v8_svg_length.py -> SVGLength.newValueSpecifiedUnits{tuple(args)} -> method')
