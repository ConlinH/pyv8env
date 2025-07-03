from .flags import *


@construct_100001
class LayoutFragment:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("inlineSize", "get_inlineSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockSize", "get_blockSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("inlineOffset", "get_inlineOffset", "set_inlineOffset", 0, 1, 0, 0, 0, 0, 1),
        ("blockOffset", "get_blockOffset", "set_blockOffset", 0, 1, 0, 0, 0, 0, 1),
        ("baseline", "get_baseline", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_inlineSize(self):
        val = self._attr.get('inlineSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_fragment.py -> LayoutFragment.inlineSize -> get attr')

    def get_blockSize(self):
        val = self._attr.get('blockSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_fragment.py -> LayoutFragment.blockSize -> get attr')

    def get_inlineOffset(self):
        val = self._attr.get('inlineOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_fragment.py -> LayoutFragment.inlineOffset -> get attr')

    def set_inlineOffset(self, val):
        self._attr['inlineOffset'] = val

    def get_blockOffset(self):
        val = self._attr.get('blockOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_fragment.py -> LayoutFragment.blockOffset -> get attr')

    def set_blockOffset(self, val):
        self._attr['blockOffset'] = val

    def get_baseline(self):
        val = self._attr.get('baseline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_fragment.py -> LayoutFragment.baseline -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_fragment.py -> LayoutFragment.data -> get attr')
