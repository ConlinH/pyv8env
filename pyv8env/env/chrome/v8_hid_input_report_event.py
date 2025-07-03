from .flags import *
from .v8_event import Event


@construct_100001
class HIDInputReportEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HIDInputReportEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("device", "get_device", None, 0, 1, 0, 0, 0, 0, 1),
        ("reportId", "get_reportId", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_device(self):
        val = self._attr.get('device')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_input_report_event.py -> HIDInputReportEvent.device -> get attr')

    def get_reportId(self):
        val = self._attr.get('reportId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_input_report_event.py -> HIDInputReportEvent.reportId -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_input_report_event.py -> HIDInputReportEvent.data -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_input_report_event.py -> HIDInputReportEvent.isTrusted -> get attr')
