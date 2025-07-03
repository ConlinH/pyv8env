from .flags import *


@construct_111001
class USBInTransferResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("status", "get_status", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_in_transfer_result.py -> USBInTransferResult.data -> get attr')

    def get_status(self):
        val = self._attr.get('status')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_in_transfer_result.py -> USBInTransferResult.status -> get attr')
