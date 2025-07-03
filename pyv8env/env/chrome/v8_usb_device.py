from .flags import *


@construct_100001
class USBDevice:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("usbVersionMajor", "get_usbVersionMajor", None, 0, 1, 0, 0, 0, 0, 1),
        ("usbVersionMinor", "get_usbVersionMinor", None, 0, 1, 0, 0, 0, 0, 1),
        ("usbVersionSubminor", "get_usbVersionSubminor", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceClass", "get_deviceClass", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceSubclass", "get_deviceSubclass", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceProtocol", "get_deviceProtocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("vendorId", "get_vendorId", None, 0, 1, 0, 0, 0, 0, 1),
        ("productId", "get_productId", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceVersionMajor", "get_deviceVersionMajor", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceVersionMinor", "get_deviceVersionMinor", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceVersionSubminor", "get_deviceVersionSubminor", None, 0, 1, 0, 0, 0, 0, 1),
        ("manufacturerName", "get_manufacturerName", None, 0, 1, 0, 0, 0, 0, 1),
        ("productName", "get_productName", None, 0, 1, 0, 0, 0, 0, 1),
        ("serialNumber", "get_serialNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("configuration", "get_configuration", None, 0, 1, 0, 0, 0, 0, 1),
        ("configurations", "get_configurations", None, 0, 1, 0, 0, 0, 0, 1),
        ("opened", "get_opened", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("claimInterface", "fn_claimInterface", 1, 0, 1, 0, 1, 0, 0),
        ("clearHalt", "fn_clearHalt", 2, 0, 1, 0, 1, 0, 0),
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("controlTransferIn", "fn_controlTransferIn", 2, 0, 1, 0, 1, 0, 0),
        ("controlTransferOut", "fn_controlTransferOut", 1, 0, 1, 0, 1, 0, 0),
        ("forget", "fn_forget", 0, 0, 1, 0, 1, 0, 0),
        ("isochronousTransferIn", "fn_isochronousTransferIn", 2, 0, 1, 0, 1, 0, 0),
        ("isochronousTransferOut", "fn_isochronousTransferOut", 3, 0, 1, 0, 1, 0, 0),
        ("open", "fn_open", 0, 0, 1, 0, 1, 0, 0),
        ("releaseInterface", "fn_releaseInterface", 1, 0, 1, 0, 1, 0, 0),
        ("reset", "fn_reset", 0, 0, 1, 0, 1, 0, 0),
        ("selectAlternateInterface", "fn_selectAlternateInterface", 2, 0, 1, 0, 1, 0, 0),
        ("selectConfiguration", "fn_selectConfiguration", 1, 0, 1, 0, 1, 0, 0),
        ("transferIn", "fn_transferIn", 2, 0, 1, 0, 1, 0, 0),
        ("transferOut", "fn_transferOut", 2, 0, 1, 0, 1, 0, 0),

    )

    def get_usbVersionMajor(self):
        val = self._attr.get('usbVersionMajor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.usbVersionMajor -> get attr')

    def get_usbVersionMinor(self):
        val = self._attr.get('usbVersionMinor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.usbVersionMinor -> get attr')

    def get_usbVersionSubminor(self):
        val = self._attr.get('usbVersionSubminor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.usbVersionSubminor -> get attr')

    def get_deviceClass(self):
        val = self._attr.get('deviceClass')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.deviceClass -> get attr')

    def get_deviceSubclass(self):
        val = self._attr.get('deviceSubclass')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.deviceSubclass -> get attr')

    def get_deviceProtocol(self):
        val = self._attr.get('deviceProtocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.deviceProtocol -> get attr')

    def get_vendorId(self):
        val = self._attr.get('vendorId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.vendorId -> get attr')

    def get_productId(self):
        val = self._attr.get('productId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.productId -> get attr')

    def get_deviceVersionMajor(self):
        val = self._attr.get('deviceVersionMajor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.deviceVersionMajor -> get attr')

    def get_deviceVersionMinor(self):
        val = self._attr.get('deviceVersionMinor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.deviceVersionMinor -> get attr')

    def get_deviceVersionSubminor(self):
        val = self._attr.get('deviceVersionSubminor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.deviceVersionSubminor -> get attr')

    def get_manufacturerName(self):
        val = self._attr.get('manufacturerName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.manufacturerName -> get attr')

    def get_productName(self):
        val = self._attr.get('productName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.productName -> get attr')

    def get_serialNumber(self):
        val = self._attr.get('serialNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.serialNumber -> get attr')

    def get_configuration(self):
        val = self._attr.get('configuration')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.configuration -> get attr')

    def get_configurations(self):
        val = self._attr.get('configurations')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.configurations -> get attr')

    def get_opened(self):
        val = self._attr.get('opened')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.opened -> get attr')

    def fn_claimInterface(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.claimInterface{tuple(args)} -> method')

    def fn_clearHalt(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.clearHalt{tuple(args)} -> method')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.close{tuple(args)} -> method')

    def fn_controlTransferIn(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.controlTransferIn{tuple(args)} -> method')

    def fn_controlTransferOut(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.controlTransferOut{tuple(args)} -> method')

    def fn_forget(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.forget{tuple(args)} -> method')

    def fn_isochronousTransferIn(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.isochronousTransferIn{tuple(args)} -> method')

    def fn_isochronousTransferOut(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.isochronousTransferOut{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.open{tuple(args)} -> method')

    def fn_releaseInterface(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.releaseInterface{tuple(args)} -> method')

    def fn_reset(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.reset{tuple(args)} -> method')

    def fn_selectAlternateInterface(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.selectAlternateInterface{tuple(args)} -> method')

    def fn_selectConfiguration(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.selectConfiguration{tuple(args)} -> method')

    def fn_transferIn(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.transferIn{tuple(args)} -> method')

    def fn_transferOut(self, *args):
        logger.debug(f'patch -> v8_usb_device.py -> USBDevice.transferOut{tuple(args)} -> method')
