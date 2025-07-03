from .flags import *
from .v8_svg_graphics_element import SVGGraphicsElement


@construct_100001
class SVGImageElement(SVGGraphicsElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGImageElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("x", "get_x", None, 0, 1, 0, 0, 0, 0, 1),
        ("y", "get_y", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("preserveAspectRatio", "get_preserveAspectRatio", None, 0, 1, 0, 0, 0, 0, 1),
        ("decoding", "get_decoding", "set_decoding", 0, 1, 0, 0, 0, 0, 1),
        ("href", "get_href", None, 0, 1, 0, 0, 0, 0, 1),
        ("crossOrigin", "get_crossOrigin", "set_crossOrigin", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("decode", "fn_decode", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_x(self):
        val = self._attr.get('x')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.x -> get attr')

    def get_y(self):
        val = self._attr.get('y')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.y -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.height -> get attr')

    def get_preserveAspectRatio(self):
        val = self._attr.get('preserveAspectRatio')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.preserveAspectRatio -> get attr')

    def get_decoding(self):
        val = self._attr.get('decoding')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.decoding -> get attr')

    def set_decoding(self, val):
        self._attr['decoding'] = val

    def get_href(self):
        val = self._attr.get('href')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.href -> get attr')

    def get_crossOrigin(self):
        val = self._attr.get('crossOrigin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.crossOrigin -> get attr')

    def set_crossOrigin(self, val):
        self._attr['crossOrigin'] = val

    def fn_decode(self, *args):
        logger.debug(f'patch -> v8_svg_image_element.py -> SVGImageElement.decode{tuple(args)} -> method')
