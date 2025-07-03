from .flags import *


@construct_111001
class ReportingObserver:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("disconnect", "fn_disconnect", 0, 0, 1, 0, 0, 0, 0),
        ("observe", "fn_observe", 0, 0, 1, 0, 0, 0, 0),
        ("takeRecords", "fn_takeRecords", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_disconnect(self, *args):
        logger.debug(f'patch -> v8_reporting_observer.py -> ReportingObserver.disconnect{tuple(args)} -> method')

    def fn_observe(self, *args):
        logger.debug(f'patch -> v8_reporting_observer.py -> ReportingObserver.observe{tuple(args)} -> method')

    def fn_takeRecords(self, *args):
        logger.debug(f'patch -> v8_reporting_observer.py -> ReportingObserver.takeRecords{tuple(args)} -> method')
