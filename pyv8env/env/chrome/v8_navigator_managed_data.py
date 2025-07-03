from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class NavigatorManagedData(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NavigatorManagedData, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onmanagedconfigurationchange", "get_onmanagedconfigurationchange", "set_onmanagedconfigurationchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getAnnotatedAssetId", "fn_getAnnotatedAssetId", 0, 0, 1, 0, 1, 0, 0),
        ("getAnnotatedLocation", "fn_getAnnotatedLocation", 0, 0, 1, 0, 1, 0, 0),
        ("getDirectoryId", "fn_getDirectoryId", 0, 0, 1, 0, 1, 0, 0),
        ("getHostname", "fn_getHostname", 0, 0, 1, 0, 1, 0, 0),
        ("getSerialNumber", "fn_getSerialNumber", 0, 0, 1, 0, 1, 0, 0),
        ("getManagedConfiguration", "fn_getManagedConfiguration", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_onmanagedconfigurationchange(self):
        val = self._attr.get('onmanagedconfigurationchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator_managed_data.py -> NavigatorManagedData.onmanagedconfigurationchange -> get attr')

    def set_onmanagedconfigurationchange(self, val):
        self._attr['onmanagedconfigurationchange'] = val

    def fn_getAnnotatedAssetId(self, *args):
        logger.debug(f'patch -> v8_navigator_managed_data.py -> NavigatorManagedData.getAnnotatedAssetId{tuple(args)} -> method')

    def fn_getAnnotatedLocation(self, *args):
        logger.debug(f'patch -> v8_navigator_managed_data.py -> NavigatorManagedData.getAnnotatedLocation{tuple(args)} -> method')

    def fn_getDirectoryId(self, *args):
        logger.debug(f'patch -> v8_navigator_managed_data.py -> NavigatorManagedData.getDirectoryId{tuple(args)} -> method')

    def fn_getHostname(self, *args):
        logger.debug(f'patch -> v8_navigator_managed_data.py -> NavigatorManagedData.getHostname{tuple(args)} -> method')

    def fn_getSerialNumber(self, *args):
        logger.debug(f'patch -> v8_navigator_managed_data.py -> NavigatorManagedData.getSerialNumber{tuple(args)} -> method')

    def fn_getManagedConfiguration(self, *args):
        logger.debug(f'patch -> v8_navigator_managed_data.py -> NavigatorManagedData.getManagedConfiguration{tuple(args)} -> method')
