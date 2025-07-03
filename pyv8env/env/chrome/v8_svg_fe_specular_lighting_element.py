from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFESpecularLightingElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFESpecularLightingElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("in1", "get_in1", None, 0, 1, 0, 0, 0, 0, 1),
        ("surfaceScale", "get_surfaceScale", None, 0, 1, 0, 0, 0, 0, 1),
        ("specularConstant", "get_specularConstant", None, 0, 1, 0, 0, 0, 0, 1),
        ("specularExponent", "get_specularExponent", None, 0, 1, 0, 0, 0, 0, 1),
        ("kernelUnitLengthX", "get_kernelUnitLengthX", None, 0, 1, 0, 0, 0, 0, 1),
        ("kernelUnitLengthY", "get_kernelUnitLengthY", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_in1(self):
        val = self._attr.get('in1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.in1 -> get attr')

    def get_surfaceScale(self):
        val = self._attr.get('surfaceScale')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.surfaceScale -> get attr')

    def get_specularConstant(self):
        val = self._attr.get('specularConstant')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.specularConstant -> get attr')

    def get_specularExponent(self):
        val = self._attr.get('specularExponent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.specularExponent -> get attr')

    def get_kernelUnitLengthX(self):
        val = self._attr.get('kernelUnitLengthX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.kernelUnitLengthX -> get attr')

    def get_kernelUnitLengthY(self):
        val = self._attr.get('kernelUnitLengthY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.kernelUnitLengthY -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_specular_lighting_element.py -> SVGFESpecularLightingElement.result -> get attr')
