from .flags import *
from .v8_worklet_global_scope import WorkletGlobalScope


@construct_100031
class SharedStorageWorkletGlobalScope(WorkletGlobalScope):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SharedStorageWorkletGlobalScope, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("sharedStorage", "get_sharedStorage", None, 0, 0, 0, 0, 0, 0, 1),
        ("crypto", "get_crypto", None, 0, 0, 0, 0, 0, 0, 1),
        ("privateAggregation", "get_privateAggregation", None, 0, 0, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("register", "fn_register", 2, 0, 0, 0, 0, 0, 0),

    )

    def get_sharedStorage(self):
        val = self._attr.get('sharedStorage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shared_storage_worklet_global_scope.py -> SharedStorageWorkletGlobalScope.sharedStorage -> get attr')

    def get_crypto(self):
        val = self._attr.get('crypto')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shared_storage_worklet_global_scope.py -> SharedStorageWorkletGlobalScope.crypto -> get attr')

    def get_privateAggregation(self):
        val = self._attr.get('privateAggregation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_shared_storage_worklet_global_scope.py -> SharedStorageWorkletGlobalScope.privateAggregation -> get attr')

    def fn_register(self, *args):
        logger.debug(f'patch -> v8_shared_storage_worklet_global_scope.py -> SharedStorageWorkletGlobalScope.register{tuple(args)} -> method')
