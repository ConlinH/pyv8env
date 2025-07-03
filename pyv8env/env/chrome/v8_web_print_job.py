from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class WebPrintJob(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(WebPrintJob, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onjobstatechange", "get_onjobstatechange", "set_onjobstatechange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("attributes", "fn_attributes", 0, 0, 1, 0, 0, 0, 0),
        ("cancel", "fn_cancel", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_onjobstatechange(self):
        val = self._attr.get('onjobstatechange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_web_print_job.py -> WebPrintJob.onjobstatechange -> get attr')

    def set_onjobstatechange(self, val):
        self._attr['onjobstatechange'] = val

    def fn_attributes(self, *args):
        logger.debug(f'patch -> v8_web_print_job.py -> WebPrintJob.attributes{tuple(args)} -> method')

    def fn_cancel(self, *args):
        logger.debug(f'patch -> v8_web_print_job.py -> WebPrintJob.cancel{tuple(args)} -> method')
