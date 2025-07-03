from .flags import *
from .v8_svg_graphics_element import SVGGraphicsElement


@construct_100001
class SVGTextContentElement(SVGGraphicsElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SVGTextContentElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("textLength", "get_textLength", None, 0, 1, 0, 0, 0, 0, 1),
        ("lengthAdjust", "get_lengthAdjust", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getCharNumAtPosition", "fn_getCharNumAtPosition", 1, 0, 1, 0, 0, 0, 0),
        ("getComputedTextLength", "fn_getComputedTextLength", 0, 0, 1, 0, 0, 0, 0),
        ("getEndPositionOfChar", "fn_getEndPositionOfChar", 1, 0, 1, 0, 0, 0, 0),
        ("getExtentOfChar", "fn_getExtentOfChar", 1, 0, 1, 0, 0, 0, 0),
        ("getNumberOfChars", "fn_getNumberOfChars", 0, 0, 1, 0, 0, 0, 0),
        ("getRotationOfChar", "fn_getRotationOfChar", 1, 0, 1, 0, 0, 0, 0),
        ("getStartPositionOfChar", "fn_getStartPositionOfChar", 1, 0, 1, 0, 0, 0, 0),
        ("getSubStringLength", "fn_getSubStringLength", 2, 0, 1, 0, 0, 0, 0),
        ("selectSubString", "fn_selectSubString", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_textLength(self):
        val = self._attr.get('textLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.textLength -> get attr')

    def get_lengthAdjust(self):
        val = self._attr.get('lengthAdjust')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.lengthAdjust -> get attr')

    def fn_getCharNumAtPosition(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getCharNumAtPosition{tuple(args)} -> method')

    def fn_getComputedTextLength(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getComputedTextLength{tuple(args)} -> method')

    def fn_getEndPositionOfChar(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getEndPositionOfChar{tuple(args)} -> method')

    def fn_getExtentOfChar(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getExtentOfChar{tuple(args)} -> method')

    def fn_getNumberOfChars(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getNumberOfChars{tuple(args)} -> method')

    def fn_getRotationOfChar(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getRotationOfChar{tuple(args)} -> method')

    def fn_getStartPositionOfChar(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getStartPositionOfChar{tuple(args)} -> method')

    def fn_getSubStringLength(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.getSubStringLength{tuple(args)} -> method')

    def fn_selectSubString(self, *args):
        logger.debug(f'patch -> v8_svg_text_content_element.py -> SVGTextContentElement.selectSubString{tuple(args)} -> method')
