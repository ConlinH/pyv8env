from .flags import *
from .v8_svg_component_transfer_function_element import SVGComponentTransferFunctionElement


@construct_100001
class SVGFEFuncBElement(SVGComponentTransferFunctionElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFEFuncBElement, self).__init__(*args, **kw)
