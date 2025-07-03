from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGMarkerElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGMarkerElement, self).__init__(*args, **kw)
    SVG_MARKERUNITS_UNKNOWN = 0
    SVG_MARKERUNITS_USERSPACEONUSE = 1
    SVG_MARKERUNITS_STROKEWIDTH = 2
    SVG_MARKER_ORIENT_UNKNOWN = 0
    SVG_MARKER_ORIENT_AUTO = 1
    SVG_MARKER_ORIENT_ANGLE = 2

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("refX", "get_refX", None, 0, 1, 0, 0, 0, 0, 1),
        ("refY", "get_refY", None, 0, 1, 0, 0, 0, 0, 1),
        ("markerUnits", "get_markerUnits", None, 0, 1, 0, 0, 0, 0, 1),
        ("markerWidth", "get_markerWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("markerHeight", "get_markerHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientType", "get_orientType", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientAngle", "get_orientAngle", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewBox", "get_viewBox", None, 0, 1, 0, 0, 0, 0, 1),
        ("preserveAspectRatio", "get_preserveAspectRatio", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setOrientToAngle", "fn_setOrientToAngle", 1, 0, 1, 0, 0, 0, 0),
        ("setOrientToAuto", "fn_setOrientToAuto", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_refX(self):
        val = self._attr.get('refX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.refX -> get attr')

    def get_refY(self):
        val = self._attr.get('refY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.refY -> get attr')

    def get_markerUnits(self):
        val = self._attr.get('markerUnits')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.markerUnits -> get attr')

    def get_markerWidth(self):
        val = self._attr.get('markerWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.markerWidth -> get attr')

    def get_markerHeight(self):
        val = self._attr.get('markerHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.markerHeight -> get attr')

    def get_orientType(self):
        val = self._attr.get('orientType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.orientType -> get attr')

    def get_orientAngle(self):
        val = self._attr.get('orientAngle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.orientAngle -> get attr')

    def get_viewBox(self):
        val = self._attr.get('viewBox')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.viewBox -> get attr')

    def get_preserveAspectRatio(self):
        val = self._attr.get('preserveAspectRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.preserveAspectRatio -> get attr')

    def fn_setOrientToAngle(self, *args):
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.setOrientToAngle{tuple(args)} -> method')

    def fn_setOrientToAuto(self, *args):
        logger.debug(f'patch -> v8_svg_marker_element.py -> SVGMarkerElement.setOrientToAuto{tuple(args)} -> method')
