from .flags import *


@construct_000000
class DeprecatedStorageQuota:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("queryUsageAndQuota", "fn_queryUsageAndQuota", 1, 0, 1, 0, 0, 0, 0),
        ("requestQuota", "fn_requestQuota", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_queryUsageAndQuota(self, *args):
        logger.debug(f'patch -> v8_deprecated_storage_quota.py -> DeprecatedStorageQuota.queryUsageAndQuota{tuple(args)} -> method')

    def fn_requestQuota(self, *args):
        logger.debug(f'patch -> v8_deprecated_storage_quota.py -> DeprecatedStorageQuota.requestQuota{tuple(args)} -> method')
