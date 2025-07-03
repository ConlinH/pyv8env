from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFEDisplacementMapElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFEDisplacementMapElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("in1", "get_in1", None, 0, 1, 0, 0, 0, 0, 1),
        ("in2", "get_in2", None, 0, 1, 0, 0, 0, 0, 1),
        ("scale", "get_scale", None, 0, 1, 0, 0, 0, 0, 1),
        ("xChannelSelector", "get_xChannelSelector", None, 0, 1, 0, 0, 0, 0, 1),
        ("yChannelSelector", "get_yChannelSelector", None, 0, 1, 0, 0, 0, 0, 1),
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
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.in1 -> get attr')

    def get_in2(self):
        val = self._attr.get('in2')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.in2 -> get attr')

    def get_scale(self):
        val = self._attr.get('scale')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.scale -> get attr')

    def get_xChannelSelector(self):
        val = self._attr.get('xChannelSelector')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.xChannelSelector -> get attr')

    def get_yChannelSelector(self):
        val = self._attr.get('yChannelSelector')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.yChannelSelector -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_displacement_map_element.py -> SVGFEDisplacementMapElement.result -> get attr')
