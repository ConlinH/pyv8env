from .flags import *
from .v8_svg_animation_element import SVGAnimationElement


@construct_100001
class SVGAnimateMotionElement(SVGAnimationElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGAnimateMotionElement, self).__init__(*args, **kw)
