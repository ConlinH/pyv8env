from .flags import *


@construct_100001
class IntrinsicSizes:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("minContentSize", "get_minContentSize", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxContentSize", "get_maxContentSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_minContentSize(self):
        val = self._attr.get('minContentSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intrinsic_sizes.py -> IntrinsicSizes.minContentSize -> get attr')

    def get_maxContentSize(self):
        val = self._attr.get('maxContentSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_intrinsic_sizes.py -> IntrinsicSizes.maxContentSize -> get attr')
