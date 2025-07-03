from .flags import *


@construct_000001
class HitTestLayerRect:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("layerRect", "get_layerRect", None, 0, 1, 0, 0, 0, 0, 1),
        ("hitTestRect", "get_hitTestRect", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_layerRect(self):
        val = self._attr.get('layerRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hit_test_layer_rect.py -> HitTestLayerRect.layerRect -> get attr')

    def get_hitTestRect(self):
        val = self._attr.get('hitTestRect')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hit_test_layer_rect.py -> HitTestLayerRect.hitTestRect -> get attr')
