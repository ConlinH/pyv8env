from .flags import *


@construct_112001
class USBInterface:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("interfaceNumber", "get_interfaceNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("alternate", "get_alternate", None, 0, 1, 0, 0, 0, 0, 1),
        ("alternates", "get_alternates", None, 0, 1, 0, 0, 0, 0, 1),
        ("claimed", "get_claimed", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_interfaceNumber(self):
        val = self._attr.get('interfaceNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_interface.py -> USBInterface.interfaceNumber -> get attr')

    def get_alternate(self):
        val = self._attr.get('alternate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_interface.py -> USBInterface.alternate -> get attr')

    def get_alternates(self):
        val = self._attr.get('alternates')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_interface.py -> USBInterface.alternates -> get attr')

    def get_claimed(self):
        val = self._attr.get('claimed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_interface.py -> USBInterface.claimed -> get attr')
