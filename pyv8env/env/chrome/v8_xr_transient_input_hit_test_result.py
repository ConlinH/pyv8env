from .flags import *


@construct_100001
class XRTransientInputHitTestResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("inputSource", "get_inputSource", None, 0, 1, 0, 0, 0, 0, 1),
        ("results", "get_results", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_inputSource(self):
        val = self._attr.get('inputSource')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_transient_input_hit_test_result.py -> XRTransientInputHitTestResult.inputSource -> get attr')

    def get_results(self):
        val = self._attr.get('results')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xr_transient_input_hit_test_result.py -> XRTransientInputHitTestResult.results -> get attr')
