from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class PerformanceScriptTiming(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PerformanceScriptTiming, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("invokerType", "get_invokerType", None, 0, 1, 0, 0, 0, 0, 1),
        ("invoker", "get_invoker", None, 0, 1, 0, 0, 0, 0, 1),
        ("windowAttribution", "get_windowAttribution", None, 0, 1, 0, 0, 0, 0, 1),
        ("executionStart", "get_executionStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("forcedStyleAndLayoutDuration", "get_forcedStyleAndLayoutDuration", None, 0, 1, 0, 0, 0, 0, 1),
        ("pauseDuration", "get_pauseDuration", None, 0, 1, 0, 0, 0, 0, 1),
        ("window", "get_window", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceURL", "get_sourceURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceFunctionName", "get_sourceFunctionName", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceCharPosition", "get_sourceCharPosition", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_invokerType(self):
        val = self._attr.get('invokerType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.invokerType -> get attr')

    def get_invoker(self):
        val = self._attr.get('invoker')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.invoker -> get attr')

    def get_windowAttribution(self):
        val = self._attr.get('windowAttribution')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.windowAttribution -> get attr')

    def get_executionStart(self):
        val = self._attr.get('executionStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.executionStart -> get attr')

    def get_forcedStyleAndLayoutDuration(self):
        val = self._attr.get('forcedStyleAndLayoutDuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.forcedStyleAndLayoutDuration -> get attr')

    def get_pauseDuration(self):
        val = self._attr.get('pauseDuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.pauseDuration -> get attr')

    def get_window(self):
        val = self._attr.get('window')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.window -> get attr')

    def get_sourceURL(self):
        val = self._attr.get('sourceURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.sourceURL -> get attr')

    def get_sourceFunctionName(self):
        val = self._attr.get('sourceFunctionName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.sourceFunctionName -> get attr')

    def get_sourceCharPosition(self):
        val = self._attr.get('sourceCharPosition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.sourceCharPosition -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_performance_script_timing.py -> PerformanceScriptTiming.toJSON{tuple(args)} -> method')
