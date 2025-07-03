from .flags import *


@construct_100001
class LayoutConstraints:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("fixedInlineSize", "get_fixedInlineSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("fixedBlockSize", "get_fixedBlockSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_fixedInlineSize(self):
        val = self._attr.get('fixedInlineSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_constraints.py -> LayoutConstraints.fixedInlineSize -> get attr')

    def get_fixedBlockSize(self):
        val = self._attr.get('fixedBlockSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_constraints.py -> LayoutConstraints.fixedBlockSize -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_layout_constraints.py -> LayoutConstraints.data -> get attr')
