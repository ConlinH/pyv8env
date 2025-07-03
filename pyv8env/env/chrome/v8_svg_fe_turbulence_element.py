from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFETurbulenceElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFETurbulenceElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("baseFrequencyX", "get_baseFrequencyX", None, 0, 1, 0, 0, 0, 0, 1),
        ("baseFrequencyY", "get_baseFrequencyY", None, 0, 1, 0, 0, 0, 0, 1),
        ("numOctaves", "get_numOctaves", None, 0, 1, 0, 0, 0, 0, 1),
        ("seed", "get_seed", None, 0, 1, 0, 0, 0, 0, 1),
        ("stitchTiles", "get_stitchTiles", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_baseFrequencyX(self):
        val = self._attr.get('baseFrequencyX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.baseFrequencyX -> get attr')

    def get_baseFrequencyY(self):
        val = self._attr.get('baseFrequencyY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.baseFrequencyY -> get attr')

    def get_numOctaves(self):
        val = self._attr.get('numOctaves')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.numOctaves -> get attr')

    def get_seed(self):
        val = self._attr.get('seed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.seed -> get attr')

    def get_stitchTiles(self):
        val = self._attr.get('stitchTiles')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.stitchTiles -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.type -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_turbulence_element.py -> SVGFETurbulenceElement.result -> get attr')
