from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFEGaussianBlurElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFEGaussianBlurElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("in1", "get_in1", None, 0, 1, 0, 0, 0, 0, 1),
        ("stdDeviationX", "get_stdDeviationX", None, 0, 1, 0, 0, 0, 0, 1),
        ("stdDeviationY", "get_stdDeviationY", None, 0, 1, 0, 0, 0, 0, 1),
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setStdDeviation", "fn_setStdDeviation", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_in1(self):
        val = self._attr.get('in1')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.in1 -> get attr')

    def get_stdDeviationX(self):
        val = self._attr.get('stdDeviationX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.stdDeviationX -> get attr')

    def get_stdDeviationY(self):
        val = self._attr.get('stdDeviationY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.stdDeviationY -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.result -> get attr')

    def fn_setStdDeviation(self, *args):
        logger.debug(f'patch -> v8_svg_fe_gaussian_blur_element.py -> SVGFEGaussianBlurElement.setStdDeviation{tuple(args)} -> method')
