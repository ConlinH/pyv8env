from .flags import *


@construct_112001
class USBConfiguration:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("configurationValue", "get_configurationValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("configurationName", "get_configurationName", None, 0, 1, 0, 0, 0, 0, 1),
        ("interfaces", "get_interfaces", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_configurationValue(self):
        val = self._attr.get('configurationValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_configuration.py -> USBConfiguration.configurationValue -> get attr')

    def get_configurationName(self):
        val = self._attr.get('configurationName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_configuration.py -> USBConfiguration.configurationName -> get attr')

    def get_interfaces(self):
        val = self._attr.get('interfaces')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_configuration.py -> USBConfiguration.interfaces -> get attr')
