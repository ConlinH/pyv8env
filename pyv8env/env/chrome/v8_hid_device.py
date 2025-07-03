from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class HIDDevice(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HIDDevice, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("oninputreport", "get_oninputreport", "set_oninputreport", 0, 1, 0, 0, 0, 0, 1),
        ("opened", "get_opened", None, 0, 1, 0, 0, 0, 0, 1),
        ("vendorId", "get_vendorId", None, 0, 1, 0, 0, 0, 0, 1),
        ("productId", "get_productId", None, 0, 1, 0, 0, 0, 0, 1),
        ("productName", "get_productName", None, 0, 1, 0, 0, 0, 0, 1),
        ("collections", "get_collections", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 1, 0, 0),
        ("forget", "fn_forget", 0, 0, 1, 0, 1, 0, 0),
        ("open", "fn_open", 0, 0, 1, 0, 1, 0, 0),
        ("receiveFeatureReport", "fn_receiveFeatureReport", 1, 0, 1, 0, 1, 0, 0),
        ("sendFeatureReport", "fn_sendFeatureReport", 2, 0, 1, 0, 1, 0, 0),
        ("sendReport", "fn_sendReport", 2, 0, 1, 0, 1, 0, 0),

    )

    def get_oninputreport(self):
        val = self._attr.get('oninputreport')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.oninputreport -> get attr')

    def set_oninputreport(self, val):
        self._attr['oninputreport'] = val

    def get_opened(self):
        val = self._attr.get('opened')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.opened -> get attr')

    def get_vendorId(self):
        val = self._attr.get('vendorId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.vendorId -> get attr')

    def get_productId(self):
        val = self._attr.get('productId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.productId -> get attr')

    def get_productName(self):
        val = self._attr.get('productName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.productName -> get attr')

    def get_collections(self):
        val = self._attr.get('collections')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.collections -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.close{tuple(args)} -> method')

    def fn_forget(self, *args):
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.forget{tuple(args)} -> method')

    def fn_open(self, *args):
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.open{tuple(args)} -> method')

    def fn_receiveFeatureReport(self, *args):
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.receiveFeatureReport{tuple(args)} -> method')

    def fn_sendFeatureReport(self, *args):
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.sendFeatureReport{tuple(args)} -> method')

    def fn_sendReport(self, *args):
        logger.debug(f'patch -> v8_hid_device.py -> HIDDevice.sendReport{tuple(args)} -> method')
