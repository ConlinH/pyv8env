from .flags import *
from .v8_svg_element import SVGElement


@construct_100001
class SVGFEConvolveMatrixElement(SVGElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGFEConvolveMatrixElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("in1", "get_in1", None, 0, 1, 0, 0, 0, 0, 1),
        ("orderX", "get_orderX", None, 0, 1, 0, 0, 0, 0, 1),
        ("orderY", "get_orderY", None, 0, 1, 0, 0, 0, 0, 1),
        ("kernelMatrix", "get_kernelMatrix", None, 0, 1, 0, 0, 0, 0, 1),
        ("divisor", "get_divisor", None, 0, 1, 0, 0, 0, 0, 1),
        ("bias", "get_bias", None, 0, 1, 0, 0, 0, 0, 1),
        ("targetX", "get_targetX", None, 0, 1, 0, 0, 0, 0, 1),
        ("targetY", "get_targetY", None, 0, 1, 0, 0, 0, 0, 1),
        ("edgeMode", "get_edgeMode", None, 0, 1, 0, 0, 0, 0, 1),
        ("kernelUnitLengthX", "get_kernelUnitLengthX", None, 0, 1, 0, 0, 0, 0, 1),
        ("kernelUnitLengthY", "get_kernelUnitLengthY", None, 0, 1, 0, 0, 0, 0, 1),
        ("preserveAlpha", "get_preserveAlpha", None, 0, 1, 0, 0, 0, 0, 1),
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
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.in1 -> get attr')

    def get_orderX(self):
        val = self._attr.get('orderX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.orderX -> get attr')

    def get_orderY(self):
        val = self._attr.get('orderY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.orderY -> get attr')

    def get_kernelMatrix(self):
        val = self._attr.get('kernelMatrix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.kernelMatrix -> get attr')

    def get_divisor(self):
        val = self._attr.get('divisor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.divisor -> get attr')

    def get_bias(self):
        val = self._attr.get('bias')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.bias -> get attr')

    def get_targetX(self):
        val = self._attr.get('targetX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.targetX -> get attr')

    def get_targetY(self):
        val = self._attr.get('targetY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.targetY -> get attr')

    def get_edgeMode(self):
        val = self._attr.get('edgeMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.edgeMode -> get attr')

    def get_kernelUnitLengthX(self):
        val = self._attr.get('kernelUnitLengthX')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.kernelUnitLengthX -> get attr')

    def get_kernelUnitLengthY(self):
        val = self._attr.get('kernelUnitLengthY')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.kernelUnitLengthY -> get attr')

    def get_preserveAlpha(self):
        val = self._attr.get('preserveAlpha')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.preserveAlpha -> get attr')

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.height -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_fe_convolve_matrix_element.py -> SVGFEConvolveMatrixElement.result -> get attr')
