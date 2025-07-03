from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFEMorphologyElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFEMorphologyElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("in1", "get_in1", None, 0, 1, 0, 0, 0, 0, 1),
        ("operator", "get_operator", None, 0, 1, 0, 0, 0, 0, 1),
        ("radiusX", "get_radiusX", None, 0, 1, 0, 0, 0, 0, 1),
        ("radiusY", "get_radiusY", None, 0, 1, 0, 0, 0, 0, 1),
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
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.in1 -> get attr')

    def get_operator(self):
        val = self._attr.get('operator')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.operator -> get attr')

    def get_radiusX(self):
        val = self._attr.get('radiusX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.radiusX -> get attr')

    def get_radiusY(self):
        val = self._attr.get('radiusY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.radiusY -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_morphology_element.py -> SVGFEMorphologyElement.result -> get attr')
