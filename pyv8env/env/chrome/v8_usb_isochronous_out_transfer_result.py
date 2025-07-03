from .flags import *


@construct_111001
class USBIsochronousOutTransferResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("packets", "get_packets", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_packets(self):
        val = self._attr.get('packets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_isochronous_out_transfer_result.py -> USBIsochronousOutTransferResult.packets -> get attr')
