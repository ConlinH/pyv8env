from .flags import *
from .v8_css_style_declaration import CSSStyleDeclaration


@construct_100001
class CSSPositionTryDescriptors(CSSStyleDeclaration):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSSPositionTryDescriptors, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("margin", "get_margin", "set_margin", 0, 1, 0, 0, 0, 0, 1),
        ("marginTop", "get_marginTop", "set_marginTop", 0, 1, 0, 0, 0, 0, 1),
        ("marginRight", "get_marginRight", "set_marginRight", 0, 1, 0, 0, 0, 0, 1),
        ("marginBottom", "get_marginBottom", "set_marginBottom", 0, 1, 0, 0, 0, 0, 1),
        ("marginLeft", "get_marginLeft", "set_marginLeft", 0, 1, 0, 0, 0, 0, 1),
        ("marginBlock", "get_marginBlock", "set_marginBlock", 0, 1, 0, 0, 0, 0, 1),
        ("marginBlockStart", "get_marginBlockStart", "set_marginBlockStart", 0, 1, 0, 0, 0, 0, 1),
        ("marginBlockEnd", "get_marginBlockEnd", "set_marginBlockEnd", 0, 1, 0, 0, 0, 0, 1),
        ("marginInline", "get_marginInline", "set_marginInline", 0, 1, 0, 0, 0, 0, 1),
        ("marginInlineStart", "get_marginInlineStart", "set_marginInlineStart", 0, 1, 0, 0, 0, 0, 1),
        ("marginInlineEnd", "get_marginInlineEnd", "set_marginInlineEnd", 0, 1, 0, 0, 0, 0, 1),
        ("margin-top", "get_margin_top", "set_margin_top", 0, 1, 0, 0, 0, 0, 1),
        ("margin-right", "get_margin_right", "set_margin_right", 0, 1, 0, 0, 0, 0, 1),
        ("margin-bottom", "get_margin_bottom", "set_margin_bottom", 0, 1, 0, 0, 0, 0, 1),
        ("margin-left", "get_margin_left", "set_margin_left", 0, 1, 0, 0, 0, 0, 1),
        ("margin-block", "get_margin_block", "set_margin_block", 0, 1, 0, 0, 0, 0, 1),
        ("margin-block-start", "get_margin_block_start", "set_margin_block_start", 0, 1, 0, 0, 0, 0, 1),
        ("margin-block-end", "get_margin_block_end", "set_margin_block_end", 0, 1, 0, 0, 0, 0, 1),
        ("margin-inline", "get_margin_inline", "set_margin_inline", 0, 1, 0, 0, 0, 0, 1),
        ("margin-inline-start", "get_margin_inline_start", "set_margin_inline_start", 0, 1, 0, 0, 0, 0, 1),
        ("margin-inline-end", "get_margin_inline_end", "set_margin_inline_end", 0, 1, 0, 0, 0, 0, 1),
        ("inset", "get_inset", "set_inset", 0, 1, 0, 0, 0, 0, 1),
        ("insetBlock", "get_insetBlock", "set_insetBlock", 0, 1, 0, 0, 0, 0, 1),
        ("insetBlockStart", "get_insetBlockStart", "set_insetBlockStart", 0, 1, 0, 0, 0, 0, 1),
        ("insetBlockEnd", "get_insetBlockEnd", "set_insetBlockEnd", 0, 1, 0, 0, 0, 0, 1),
        ("insetInline", "get_insetInline", "set_insetInline", 0, 1, 0, 0, 0, 0, 1),
        ("insetInlineStart", "get_insetInlineStart", "set_insetInlineStart", 0, 1, 0, 0, 0, 0, 1),
        ("insetInlineEnd", "get_insetInlineEnd", "set_insetInlineEnd", 0, 1, 0, 0, 0, 0, 1),
        ("top", "get_top", "set_top", 0, 1, 0, 0, 0, 0, 1),
        ("left", "get_left", "set_left", 0, 1, 0, 0, 0, 0, 1),
        ("right", "get_right", "set_right", 0, 1, 0, 0, 0, 0, 1),
        ("bottom", "get_bottom", "set_bottom", 0, 1, 0, 0, 0, 0, 1),
        ("inset-block", "get_inset_block", "set_inset_block", 0, 1, 0, 0, 0, 0, 1),
        ("inset-block-start", "get_inset_block_start", "set_inset_block_start", 0, 1, 0, 0, 0, 0, 1),
        ("inset-block-end", "get_inset_block_end", "set_inset_block_end", 0, 1, 0, 0, 0, 0, 1),
        ("inset-inline", "get_inset_inline", "set_inset_inline", 0, 1, 0, 0, 0, 0, 1),
        ("inset-inline-start", "get_inset_inline_start", "set_inset_inline_start", 0, 1, 0, 0, 0, 0, 1),
        ("inset-inline-end", "get_inset_inline_end", "set_inset_inline_end", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("minWidth", "get_minWidth", "set_minWidth", 0, 1, 0, 0, 0, 0, 1),
        ("maxWidth", "get_maxWidth", "set_maxWidth", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("minHeight", "get_minHeight", "set_minHeight", 0, 1, 0, 0, 0, 0, 1),
        ("maxHeight", "get_maxHeight", "set_maxHeight", 0, 1, 0, 0, 0, 0, 1),
        ("blockSize", "get_blockSize", "set_blockSize", 0, 1, 0, 0, 0, 0, 1),
        ("minBlockSize", "get_minBlockSize", "set_minBlockSize", 0, 1, 0, 0, 0, 0, 1),
        ("maxBlockSize", "get_maxBlockSize", "set_maxBlockSize", 0, 1, 0, 0, 0, 0, 1),
        ("inlineSize", "get_inlineSize", "set_inlineSize", 0, 1, 0, 0, 0, 0, 1),
        ("minInlineSize", "get_minInlineSize", "set_minInlineSize", 0, 1, 0, 0, 0, 0, 1),
        ("maxInlineSize", "get_maxInlineSize", "set_maxInlineSize", 0, 1, 0, 0, 0, 0, 1),
        ("min-width", "get_min_width", "set_min_width", 0, 1, 0, 0, 0, 0, 1),
        ("max-width", "get_max_width", "set_max_width", 0, 1, 0, 0, 0, 0, 1),
        ("min-height", "get_min_height", "set_min_height", 0, 1, 0, 0, 0, 0, 1),
        ("max-height", "get_max_height", "set_max_height", 0, 1, 0, 0, 0, 0, 1),
        ("block-size", "get_block_size", "set_block_size", 0, 1, 0, 0, 0, 0, 1),
        ("min-block-size", "get_min_block_size", "set_min_block_size", 0, 1, 0, 0, 0, 0, 1),
        ("max-block-size", "get_max_block_size", "set_max_block_size", 0, 1, 0, 0, 0, 0, 1),
        ("inline-size", "get_inline_size", "set_inline_size", 0, 1, 0, 0, 0, 0, 1),
        ("min-inline-size", "get_min_inline_size", "set_min_inline_size", 0, 1, 0, 0, 0, 0, 1),
        ("max-inline-size", "get_max_inline_size", "set_max_inline_size", 0, 1, 0, 0, 0, 0, 1),
        ("placeSelf", "get_placeSelf", "set_placeSelf", 0, 1, 0, 0, 0, 0, 1),
        ("alignSelf", "get_alignSelf", "set_alignSelf", 0, 1, 0, 0, 0, 0, 1),
        ("justifySelf", "get_justifySelf", "set_justifySelf", 0, 1, 0, 0, 0, 0, 1),
        ("place-self", "get_place_self", "set_place_self", 0, 1, 0, 0, 0, 0, 1),
        ("align-self", "get_align_self", "set_align_self", 0, 1, 0, 0, 0, 0, 1),
        ("justify-self", "get_justify_self", "set_justify_self", 0, 1, 0, 0, 0, 0, 1),
        ("positionAnchor", "get_positionAnchor", "set_positionAnchor", 0, 1, 0, 0, 0, 0, 1),
        ("position-anchor", "get_position_anchor", "set_position_anchor", 0, 1, 0, 0, 0, 0, 1),
        ("insetArea", "get_insetArea", "set_insetArea", 0, 1, 0, 0, 0, 0, 1),
        ("inset-area", "get_inset_area", "set_inset_area", 0, 1, 0, 0, 0, 0, 1),

    )

    def get_margin(self):
        val = self._attr.get('margin')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin -> get attr')

    def set_margin(self, val):
        self._attr['margin'] = val

    def get_marginTop(self):
        val = self._attr.get('marginTop')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginTop -> get attr')

    def set_marginTop(self, val):
        self._attr['marginTop'] = val

    def get_marginRight(self):
        val = self._attr.get('marginRight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginRight -> get attr')

    def set_marginRight(self, val):
        self._attr['marginRight'] = val

    def get_marginBottom(self):
        val = self._attr.get('marginBottom')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginBottom -> get attr')

    def set_marginBottom(self, val):
        self._attr['marginBottom'] = val

    def get_marginLeft(self):
        val = self._attr.get('marginLeft')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginLeft -> get attr')

    def set_marginLeft(self, val):
        self._attr['marginLeft'] = val

    def get_marginBlock(self):
        val = self._attr.get('marginBlock')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginBlock -> get attr')

    def set_marginBlock(self, val):
        self._attr['marginBlock'] = val

    def get_marginBlockStart(self):
        val = self._attr.get('marginBlockStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginBlockStart -> get attr')

    def set_marginBlockStart(self, val):
        self._attr['marginBlockStart'] = val

    def get_marginBlockEnd(self):
        val = self._attr.get('marginBlockEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginBlockEnd -> get attr')

    def set_marginBlockEnd(self, val):
        self._attr['marginBlockEnd'] = val

    def get_marginInline(self):
        val = self._attr.get('marginInline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginInline -> get attr')

    def set_marginInline(self, val):
        self._attr['marginInline'] = val

    def get_marginInlineStart(self):
        val = self._attr.get('marginInlineStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginInlineStart -> get attr')

    def set_marginInlineStart(self, val):
        self._attr['marginInlineStart'] = val

    def get_marginInlineEnd(self):
        val = self._attr.get('marginInlineEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.marginInlineEnd -> get attr')

    def set_marginInlineEnd(self, val):
        self._attr['marginInlineEnd'] = val

    def get_margin_top(self):
        val = self._attr.get('margin-top')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-top -> get attr')

    def set_margin_top(self, val):
        self._attr['margin-top'] = val

    def get_margin_right(self):
        val = self._attr.get('margin-right')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-right -> get attr')

    def set_margin_right(self, val):
        self._attr['margin-right'] = val

    def get_margin_bottom(self):
        val = self._attr.get('margin-bottom')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-bottom -> get attr')

    def set_margin_bottom(self, val):
        self._attr['margin-bottom'] = val

    def get_margin_left(self):
        val = self._attr.get('margin-left')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-left -> get attr')

    def set_margin_left(self, val):
        self._attr['margin-left'] = val

    def get_margin_block(self):
        val = self._attr.get('margin-block')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-block -> get attr')

    def set_margin_block(self, val):
        self._attr['margin-block'] = val

    def get_margin_block_start(self):
        val = self._attr.get('margin-block-start')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-block-start -> get attr')

    def set_margin_block_start(self, val):
        self._attr['margin-block-start'] = val

    def get_margin_block_end(self):
        val = self._attr.get('margin-block-end')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-block-end -> get attr')

    def set_margin_block_end(self, val):
        self._attr['margin-block-end'] = val

    def get_margin_inline(self):
        val = self._attr.get('margin-inline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-inline -> get attr')

    def set_margin_inline(self, val):
        self._attr['margin-inline'] = val

    def get_margin_inline_start(self):
        val = self._attr.get('margin-inline-start')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-inline-start -> get attr')

    def set_margin_inline_start(self, val):
        self._attr['margin-inline-start'] = val

    def get_margin_inline_end(self):
        val = self._attr.get('margin-inline-end')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.margin-inline-end -> get attr')

    def set_margin_inline_end(self, val):
        self._attr['margin-inline-end'] = val

    def get_inset(self):
        val = self._attr.get('inset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset -> get attr')

    def set_inset(self, val):
        self._attr['inset'] = val

    def get_insetBlock(self):
        val = self._attr.get('insetBlock')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.insetBlock -> get attr')

    def set_insetBlock(self, val):
        self._attr['insetBlock'] = val

    def get_insetBlockStart(self):
        val = self._attr.get('insetBlockStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.insetBlockStart -> get attr')

    def set_insetBlockStart(self, val):
        self._attr['insetBlockStart'] = val

    def get_insetBlockEnd(self):
        val = self._attr.get('insetBlockEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.insetBlockEnd -> get attr')

    def set_insetBlockEnd(self, val):
        self._attr['insetBlockEnd'] = val

    def get_insetInline(self):
        val = self._attr.get('insetInline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.insetInline -> get attr')

    def set_insetInline(self, val):
        self._attr['insetInline'] = val

    def get_insetInlineStart(self):
        val = self._attr.get('insetInlineStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.insetInlineStart -> get attr')

    def set_insetInlineStart(self, val):
        self._attr['insetInlineStart'] = val

    def get_insetInlineEnd(self):
        val = self._attr.get('insetInlineEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.insetInlineEnd -> get attr')

    def set_insetInlineEnd(self, val):
        self._attr['insetInlineEnd'] = val

    def get_top(self):
        val = self._attr.get('top')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.top -> get attr')

    def set_top(self, val):
        self._attr['top'] = val

    def get_left(self):
        val = self._attr.get('left')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.left -> get attr')

    def set_left(self, val):
        self._attr['left'] = val

    def get_right(self):
        val = self._attr.get('right')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.right -> get attr')

    def set_right(self, val):
        self._attr['right'] = val

    def get_bottom(self):
        val = self._attr.get('bottom')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.bottom -> get attr')

    def set_bottom(self, val):
        self._attr['bottom'] = val

    def get_inset_block(self):
        val = self._attr.get('inset-block')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset-block -> get attr')

    def set_inset_block(self, val):
        self._attr['inset-block'] = val

    def get_inset_block_start(self):
        val = self._attr.get('inset-block-start')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset-block-start -> get attr')

    def set_inset_block_start(self, val):
        self._attr['inset-block-start'] = val

    def get_inset_block_end(self):
        val = self._attr.get('inset-block-end')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset-block-end -> get attr')

    def set_inset_block_end(self, val):
        self._attr['inset-block-end'] = val

    def get_inset_inline(self):
        val = self._attr.get('inset-inline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset-inline -> get attr')

    def set_inset_inline(self, val):
        self._attr['inset-inline'] = val

    def get_inset_inline_start(self):
        val = self._attr.get('inset-inline-start')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset-inline-start -> get attr')

    def set_inset_inline_start(self, val):
        self._attr['inset-inline-start'] = val

    def get_inset_inline_end(self):
        val = self._attr.get('inset-inline-end')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset-inline-end -> get attr')

    def set_inset_inline_end(self, val):
        self._attr['inset-inline-end'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_minWidth(self):
        val = self._attr.get('minWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.minWidth -> get attr')

    def set_minWidth(self, val):
        self._attr['minWidth'] = val

    def get_maxWidth(self):
        val = self._attr.get('maxWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.maxWidth -> get attr')

    def set_maxWidth(self, val):
        self._attr['maxWidth'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_minHeight(self):
        val = self._attr.get('minHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.minHeight -> get attr')

    def set_minHeight(self, val):
        self._attr['minHeight'] = val

    def get_maxHeight(self):
        val = self._attr.get('maxHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.maxHeight -> get attr')

    def set_maxHeight(self, val):
        self._attr['maxHeight'] = val

    def get_blockSize(self):
        val = self._attr.get('blockSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.blockSize -> get attr')

    def set_blockSize(self, val):
        self._attr['blockSize'] = val

    def get_minBlockSize(self):
        val = self._attr.get('minBlockSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.minBlockSize -> get attr')

    def set_minBlockSize(self, val):
        self._attr['minBlockSize'] = val

    def get_maxBlockSize(self):
        val = self._attr.get('maxBlockSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.maxBlockSize -> get attr')

    def set_maxBlockSize(self, val):
        self._attr['maxBlockSize'] = val

    def get_inlineSize(self):
        val = self._attr.get('inlineSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inlineSize -> get attr')

    def set_inlineSize(self, val):
        self._attr['inlineSize'] = val

    def get_minInlineSize(self):
        val = self._attr.get('minInlineSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.minInlineSize -> get attr')

    def set_minInlineSize(self, val):
        self._attr['minInlineSize'] = val

    def get_maxInlineSize(self):
        val = self._attr.get('maxInlineSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.maxInlineSize -> get attr')

    def set_maxInlineSize(self, val):
        self._attr['maxInlineSize'] = val

    def get_min_width(self):
        val = self._attr.get('min-width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.min-width -> get attr')

    def set_min_width(self, val):
        self._attr['min-width'] = val

    def get_max_width(self):
        val = self._attr.get('max-width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.max-width -> get attr')

    def set_max_width(self, val):
        self._attr['max-width'] = val

    def get_min_height(self):
        val = self._attr.get('min-height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.min-height -> get attr')

    def set_min_height(self, val):
        self._attr['min-height'] = val

    def get_max_height(self):
        val = self._attr.get('max-height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.max-height -> get attr')

    def set_max_height(self, val):
        self._attr['max-height'] = val

    def get_block_size(self):
        val = self._attr.get('block-size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.block-size -> get attr')

    def set_block_size(self, val):
        self._attr['block-size'] = val

    def get_min_block_size(self):
        val = self._attr.get('min-block-size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.min-block-size -> get attr')

    def set_min_block_size(self, val):
        self._attr['min-block-size'] = val

    def get_max_block_size(self):
        val = self._attr.get('max-block-size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.max-block-size -> get attr')

    def set_max_block_size(self, val):
        self._attr['max-block-size'] = val

    def get_inline_size(self):
        val = self._attr.get('inline-size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inline-size -> get attr')

    def set_inline_size(self, val):
        self._attr['inline-size'] = val

    def get_min_inline_size(self):
        val = self._attr.get('min-inline-size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.min-inline-size -> get attr')

    def set_min_inline_size(self, val):
        self._attr['min-inline-size'] = val

    def get_max_inline_size(self):
        val = self._attr.get('max-inline-size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.max-inline-size -> get attr')

    def set_max_inline_size(self, val):
        self._attr['max-inline-size'] = val

    def get_placeSelf(self):
        val = self._attr.get('placeSelf')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.placeSelf -> get attr')

    def set_placeSelf(self, val):
        self._attr['placeSelf'] = val

    def get_alignSelf(self):
        val = self._attr.get('alignSelf')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.alignSelf -> get attr')

    def set_alignSelf(self, val):
        self._attr['alignSelf'] = val

    def get_justifySelf(self):
        val = self._attr.get('justifySelf')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.justifySelf -> get attr')

    def set_justifySelf(self, val):
        self._attr['justifySelf'] = val

    def get_place_self(self):
        val = self._attr.get('place-self')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.place-self -> get attr')

    def set_place_self(self, val):
        self._attr['place-self'] = val

    def get_align_self(self):
        val = self._attr.get('align-self')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.align-self -> get attr')

    def set_align_self(self, val):
        self._attr['align-self'] = val

    def get_justify_self(self):
        val = self._attr.get('justify-self')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.justify-self -> get attr')

    def set_justify_self(self, val):
        self._attr['justify-self'] = val

    def get_positionAnchor(self):
        val = self._attr.get('positionAnchor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.positionAnchor -> get attr')

    def set_positionAnchor(self, val):
        self._attr['positionAnchor'] = val

    def get_position_anchor(self):
        val = self._attr.get('position-anchor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.position-anchor -> get attr')

    def set_position_anchor(self, val):
        self._attr['position-anchor'] = val

    def get_insetArea(self):
        val = self._attr.get('insetArea')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.insetArea -> get attr')

    def set_insetArea(self, val):
        self._attr['insetArea'] = val

    def get_inset_area(self):
        val = self._attr.get('inset-area')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_css_position_try_descriptors.py -> CSSPositionTryDescriptors.inset-area -> get attr')

    def set_inset_area(self, val):
        self._attr['inset-area'] = val
