from .flags import *


@construct_112001
class USBAlternateInterface:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("alternateSetting", "get_alternateSetting", None, 0, 1, 0, 0, 0, 0, 1),
        ("interfaceClass", "get_interfaceClass", None, 0, 1, 0, 0, 0, 0, 1),
        ("interfaceSubclass", "get_interfaceSubclass", None, 0, 1, 0, 0, 0, 0, 1),
        ("interfaceProtocol", "get_interfaceProtocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("interfaceName", "get_interfaceName", None, 0, 1, 0, 0, 0, 0, 1),
        ("endpoints", "get_endpoints", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_alternateSetting(self):
        val = self._attr.get('alternateSetting')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_alternate_interface.py -> USBAlternateInterface.alternateSetting -> get attr')

    def get_interfaceClass(self):
        val = self._attr.get('interfaceClass')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_alternate_interface.py -> USBAlternateInterface.interfaceClass -> get attr')

    def get_interfaceSubclass(self):
        val = self._attr.get('interfaceSubclass')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_alternate_interface.py -> USBAlternateInterface.interfaceSubclass -> get attr')

    def get_interfaceProtocol(self):
        val = self._attr.get('interfaceProtocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_alternate_interface.py -> USBAlternateInterface.interfaceProtocol -> get attr')

    def get_interfaceName(self):
        val = self._attr.get('interfaceName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_alternate_interface.py -> USBAlternateInterface.interfaceName -> get attr')

    def get_endpoints(self):
        val = self._attr.get('endpoints')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_alternate_interface.py -> USBAlternateInterface.endpoints -> get attr')
