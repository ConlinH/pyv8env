from .flags import *


@construct_100001
class GPUQuerySet:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("count", "get_count", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", "set_label", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("destroy", "fn_destroy", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_query_set.py -> GPUQuerySet.type -> get attr')

    def get_count(self):
        val = self._attr.get('count')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_query_set.py -> GPUQuerySet.count -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_gpu_query_set.py -> GPUQuerySet.label -> get attr')

    def set_label(self, val):
        self._attr['label'] = val

    def fn_destroy(self, *args):
        logger.debug(f'patch -> v8_gpu_query_set.py -> GPUQuerySet.destroy{tuple(args)} -> method')
