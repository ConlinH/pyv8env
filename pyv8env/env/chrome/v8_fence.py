from .flags import *


@construct_100001
class Fence:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getNestedConfigs", "fn_getNestedConfigs", 0, 0, 1, 0, 0, 0, 0),
        ("reportEvent", "fn_reportEvent", 1, 0, 1, 0, 0, 0, 0),
        ("setReportEventDataForAutomaticBeacons", "fn_setReportEventDataForAutomaticBeacons", 1, 0, 1, 0, 0, 0, 0),
        ("disableUntrustedNetwork", "fn_disableUntrustedNetwork", 0, 0, 1, 0, 1, 0, 0),
        ("notifyEvent", "fn_notifyEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_getNestedConfigs(self, *args):
        logger.debug(f'patch -> v8_fence.py -> Fence.getNestedConfigs{tuple(args)} -> method')

    def fn_reportEvent(self, *args):
        logger.debug(f'patch -> v8_fence.py -> Fence.reportEvent{tuple(args)} -> method')

    def fn_setReportEventDataForAutomaticBeacons(self, *args):
        logger.debug(f'patch -> v8_fence.py -> Fence.setReportEventDataForAutomaticBeacons{tuple(args)} -> method')

    def fn_disableUntrustedNetwork(self, *args):
        logger.debug(f'patch -> v8_fence.py -> Fence.disableUntrustedNetwork{tuple(args)} -> method')

    def fn_notifyEvent(self, *args):
        logger.debug(f'patch -> v8_fence.py -> Fence.notifyEvent{tuple(args)} -> method')
