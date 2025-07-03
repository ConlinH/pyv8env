from .flags import *


@construct_111001
class USBOutTransferResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("bytesWritten", "get_bytesWritten", None, 0, 1, 0, 0, 0, 0, 1),
        ("status", "get_status", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_bytesWritten(self):
        val = self._attr.get('bytesWritten')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_out_transfer_result.py -> USBOutTransferResult.bytesWritten -> get attr')

    def get_status(self):
        val = self._attr.get('status')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_out_transfer_result.py -> USBOutTransferResult.status -> get attr')
