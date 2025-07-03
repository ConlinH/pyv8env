from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGComponentTransferFunctionElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGComponentTransferFunctionElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("tableValues", "get_tableValues", None, 0, 1, 0, 0, 0, 0, 1),
        ("slope", "get_slope", None, 0, 1, 0, 0, 0, 0, 1),
        ("intercept", "get_intercept", None, 0, 1, 0, 0, 0, 0, 1),
        ("amplitude", "get_amplitude", None, 0, 1, 0, 0, 0, 0, 1),
        ("exponent", "get_exponent", None, 0, 1, 0, 0, 0, 0, 1),
        ("offset", "get_offset", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_component_transfer_function_element.py -> SVGComponentTransferFunctionElement.type -> get attr')

    def get_tableValues(self):
        val = self._attr.get('tableValues')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_component_transfer_function_element.py -> SVGComponentTransferFunctionElement.tableValues -> get attr')

    def get_slope(self):
        val = self._attr.get('slope')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_component_transfer_function_element.py -> SVGComponentTransferFunctionElement.slope -> get attr')

    def get_intercept(self):
        val = self._attr.get('intercept')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_component_transfer_function_element.py -> SVGComponentTransferFunctionElement.intercept -> get attr')

    def get_amplitude(self):
        val = self._attr.get('amplitude')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_component_transfer_function_element.py -> SVGComponentTransferFunctionElement.amplitude -> get attr')

    def get_exponent(self):
        val = self._attr.get('exponent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_component_transfer_function_element.py -> SVGComponentTransferFunctionElement.exponent -> get attr')

    def get_offset(self):
        val = self._attr.get('offset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_component_transfer_function_element.py -> SVGComponentTransferFunctionElement.offset -> get attr')
