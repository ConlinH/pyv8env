from .flags import *


@construct_100001
class LayoutEdges:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("inlineStart", "get_inlineStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("inlineEnd", "get_inlineEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockStart", "get_blockStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockEnd", "get_blockEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("inline", "get_inline", None, 0, 1, 0, 0, 0, 0, 1),
        ("block", "get_block", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_inlineStart(self):
        val = self._attr.get('inlineStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_edges.py -> LayoutEdges.inlineStart -> get attr')

    def get_inlineEnd(self):
        val = self._attr.get('inlineEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_edges.py -> LayoutEdges.inlineEnd -> get attr')

    def get_blockStart(self):
        val = self._attr.get('blockStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_edges.py -> LayoutEdges.blockStart -> get attr')

    def get_blockEnd(self):
        val = self._attr.get('blockEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_edges.py -> LayoutEdges.blockEnd -> get attr')

    def get_inline(self):
        val = self._attr.get('inline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_edges.py -> LayoutEdges.inline -> get attr')

    def get_block(self):
        val = self._attr.get('block')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_edges.py -> LayoutEdges.block -> get attr')
