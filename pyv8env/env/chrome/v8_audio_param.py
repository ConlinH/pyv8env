from .flags import *


@construct_100001
class AudioParam:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("automationRate", "get_automationRate", "set_automationRate", 0, 1, 0, 0, 0, 0, 1),
        ("defaultValue", "get_defaultValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("minValue", "get_minValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxValue", "get_maxValue", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cancelAndHoldAtTime", "fn_cancelAndHoldAtTime", 1, 0, 1, 0, 0, 0, 0),
        ("cancelScheduledValues", "fn_cancelScheduledValues", 1, 0, 1, 0, 0, 0, 0),
        ("exponentialRampToValueAtTime", "fn_exponentialRampToValueAtTime", 2, 0, 1, 0, 0, 0, 0),
        ("linearRampToValueAtTime", "fn_linearRampToValueAtTime", 2, 0, 1, 0, 0, 0, 0),
        ("setTargetAtTime", "fn_setTargetAtTime", 3, 0, 1, 0, 0, 0, 0),
        ("setValueAtTime", "fn_setValueAtTime", 2, 0, 1, 0, 0, 0, 0),
        ("setValueCurveAtTime", "fn_setValueCurveAtTime", 3, 0, 1, 0, 0, 0, 0),

    )

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_automationRate(self):
        val = self._attr.get('automationRate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.automationRate -> get attr')

    def set_automationRate(self, val):
        self._attr['automationRate'] = val

    def get_defaultValue(self):
        val = self._attr.get('defaultValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.defaultValue -> get attr')

    def get_minValue(self):
        val = self._attr.get('minValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.minValue -> get attr')

    def get_maxValue(self):
        val = self._attr.get('maxValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.maxValue -> get attr')

    def fn_cancelAndHoldAtTime(self, *args):
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.cancelAndHoldAtTime{tuple(args)} -> method')

    def fn_cancelScheduledValues(self, *args):
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.cancelScheduledValues{tuple(args)} -> method')

    def fn_exponentialRampToValueAtTime(self, *args):
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.exponentialRampToValueAtTime{tuple(args)} -> method')

    def fn_linearRampToValueAtTime(self, *args):
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.linearRampToValueAtTime{tuple(args)} -> method')

    def fn_setTargetAtTime(self, *args):
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.setTargetAtTime{tuple(args)} -> method')

    def fn_setValueAtTime(self, *args):
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.setValueAtTime{tuple(args)} -> method')

    def fn_setValueCurveAtTime(self, *args):
        logger.debug(f'patch -> v8_audio_param.py -> AudioParam.setValueCurveAtTime{tuple(args)} -> method')
