from .flags import *
from .v8_svg_geometry_element import SVGGeometryElement


@construct_100001
class SVGEllipseElement(SVGGeometryElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGEllipseElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("cx", "get_cx", None, 0, 1, 0, 0, 0, 0, 1),
        ("cy", "get_cy", None, 0, 1, 0, 0, 0, 0, 1),
        ("rx", "get_rx", None, 0, 1, 0, 0, 0, 0, 1),
        ("ry", "get_ry", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_cx(self):
        val = self._attr.get('cx')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_ellipse_element.py -> SVGEllipseElement.cx -> get attr')

    def get_cy(self):
        val = self._attr.get('cy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_ellipse_element.py -> SVGEllipseElement.cy -> get attr')

    def get_rx(self):
        val = self._attr.get('rx')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_ellipse_element.py -> SVGEllipseElement.rx -> get attr')

    def get_ry(self):
        val = self._attr.get('ry')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_ellipse_element.py -> SVGEllipseElement.ry -> get attr')
