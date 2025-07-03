from .flags import *


@construct_113001
class USBEndpoint:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("endpointNumber", "get_endpointNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("direction", "get_direction", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("packetSize", "get_packetSize", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_endpointNumber(self):
        val = self._attr.get('endpointNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_endpoint.py -> USBEndpoint.endpointNumber -> get attr')

    def get_direction(self):
        val = self._attr.get('direction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_endpoint.py -> USBEndpoint.direction -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_endpoint.py -> USBEndpoint.type -> get attr')

    def get_packetSize(self):
        val = self._attr.get('packetSize')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_endpoint.py -> USBEndpoint.packetSize -> get attr')
