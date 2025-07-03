from .flags import *
from .v8_svg_graphics_element import SVGGraphicsElement


@construct_100001
class SVGSVGElement(SVGGraphicsElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGSVGElement, self).__init__(*args, **kw)
    SVG_ZOOMANDPAN_UNKNOWN = 0
    SVG_ZOOMANDPAN_DISABLE = 1
    SVG_ZOOMANDPAN_MAGNIFY = 2

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentScale", "get_currentScale", "set_currentScale", 0, 1, 0, 0, 0, 0, 1),
        ("currentTranslate", "get_currentTranslate", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewBox", "get_viewBox", None, 0, 1, 0, 0, 0, 0, 1),
        ("preserveAspectRatio", "get_preserveAspectRatio", None, 0, 1, 0, 0, 0, 0, 1),
        ("zoomAndPan", "get_zoomAndPan", "set_zoomAndPan", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("animationsPaused", "fn_animationsPaused", 0, 0, 1, 0, 0, 0, 0),
        ("checkEnclosure", "fn_checkEnclosure", 2, 0, 1, 0, 0, 0, 0),
        ("checkIntersection", "fn_checkIntersection", 2, 0, 1, 0, 0, 0, 0),
        ("createSVGAngle", "fn_createSVGAngle", 0, 0, 1, 0, 0, 0, 0),
        ("createSVGLength", "fn_createSVGLength", 0, 0, 1, 0, 0, 0, 0),
        ("createSVGMatrix", "fn_createSVGMatrix", 0, 0, 1, 0, 0, 0, 0),
        ("createSVGNumber", "fn_createSVGNumber", 0, 0, 1, 0, 0, 0, 0),
        ("createSVGPoint", "fn_createSVGPoint", 0, 0, 1, 0, 0, 0, 0),
        ("createSVGRect", "fn_createSVGRect", 0, 0, 1, 0, 0, 0, 0),
        ("createSVGTransform", "fn_createSVGTransform", 0, 0, 1, 0, 0, 0, 0),
        ("createSVGTransformFromMatrix", "fn_createSVGTransformFromMatrix", 1, 0, 1, 0, 0, 0, 0),
        ("deselectAll", "fn_deselectAll", 0, 0, 1, 0, 0, 0, 0),
        ("forceRedraw", "fn_forceRedraw", 0, 0, 1, 0, 0, 0, 0),
        ("getCurrentTime", "fn_getCurrentTime", 0, 0, 1, 0, 0, 0, 0),
        ("getElementById", "fn_getElementById", 1, 0, 1, 0, 0, 0, 0),
        ("getEnclosureList", "fn_getEnclosureList", 2, 0, 1, 0, 0, 0, 0),
        ("getIntersectionList", "fn_getIntersectionList", 2, 0, 1, 0, 0, 0, 0),
        ("pauseAnimations", "fn_pauseAnimations", 0, 0, 1, 0, 0, 0, 0),
        ("setCurrentTime", "fn_setCurrentTime", 1, 0, 1, 0, 0, 0, 0),
        ("suspendRedraw", "fn_suspendRedraw", 1, 0, 1, 0, 0, 0, 0),
        ("unpauseAnimations", "fn_unpauseAnimations", 0, 0, 1, 0, 0, 0, 0),
        ("unsuspendRedraw", "fn_unsuspendRedraw", 1, 0, 1, 0, 0, 0, 0),
        ("unsuspendRedrawAll", "fn_unsuspendRedrawAll", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.height -> get attr')

    def get_currentScale(self):
        val = self._attr.get('currentScale')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.currentScale -> get attr')

    def set_currentScale(self, val):
        self._attr['currentScale'] = val

    def get_currentTranslate(self):
        val = self._attr.get('currentTranslate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.currentTranslate -> get attr')

    def get_viewBox(self):
        val = self._attr.get('viewBox')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.viewBox -> get attr')

    def get_preserveAspectRatio(self):
        val = self._attr.get('preserveAspectRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.preserveAspectRatio -> get attr')

    def get_zoomAndPan(self):
        val = self._attr.get('zoomAndPan')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.zoomAndPan -> get attr')

    def set_zoomAndPan(self, val):
        self._attr['zoomAndPan'] = val

    def fn_animationsPaused(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.animationsPaused{tuple(args)} -> method')

    def fn_checkEnclosure(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.checkEnclosure{tuple(args)} -> method')

    def fn_checkIntersection(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.checkIntersection{tuple(args)} -> method')

    def fn_createSVGAngle(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGAngle{tuple(args)} -> method')

    def fn_createSVGLength(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGLength{tuple(args)} -> method')

    def fn_createSVGMatrix(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGMatrix{tuple(args)} -> method')

    def fn_createSVGNumber(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGNumber{tuple(args)} -> method')

    def fn_createSVGPoint(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGPoint{tuple(args)} -> method')

    def fn_createSVGRect(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGRect{tuple(args)} -> method')

    def fn_createSVGTransform(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGTransform{tuple(args)} -> method')

    def fn_createSVGTransformFromMatrix(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.createSVGTransformFromMatrix{tuple(args)} -> method')

    def fn_deselectAll(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.deselectAll{tuple(args)} -> method')

    def fn_forceRedraw(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.forceRedraw{tuple(args)} -> method')

    def fn_getCurrentTime(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.getCurrentTime{tuple(args)} -> method')

    def fn_getElementById(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.getElementById{tuple(args)} -> method')

    def fn_getEnclosureList(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.getEnclosureList{tuple(args)} -> method')

    def fn_getIntersectionList(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.getIntersectionList{tuple(args)} -> method')

    def fn_pauseAnimations(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.pauseAnimations{tuple(args)} -> method')

    def fn_setCurrentTime(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.setCurrentTime{tuple(args)} -> method')

    def fn_suspendRedraw(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.suspendRedraw{tuple(args)} -> method')

    def fn_unpauseAnimations(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.unpauseAnimations{tuple(args)} -> method')

    def fn_unsuspendRedraw(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.unsuspendRedraw{tuple(args)} -> method')

    def fn_unsuspendRedrawAll(self, *args):
        logger.debug(f'patch -> v8_svg_svg_element.py -> SVGSVGElement.unsuspendRedrawAll{tuple(args)} -> method')
