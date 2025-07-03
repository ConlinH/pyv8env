from .flags import *


@construct_100001
class XRHitTestResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getPose", "fn_getPose", 1, 0, 1, 0, 0, 0, 0),
        ("createAnchor", "fn_createAnchor", 0, 0, 1, 0, 1, 0, 0),

    )

    def fn_getPose(self, *args):
        logger.debug(f'patch -> v8_xr_hit_test_result.py -> XRHitTestResult.getPose{tuple(args)} -> method')

    def fn_createAnchor(self, *args):
        logger.debug(f'patch -> v8_xr_hit_test_result.py -> XRHitTestResult.createAnchor{tuple(args)} -> method')
