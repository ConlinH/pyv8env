from .flags import *


@construct_100001
class MediaDeviceInfo:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("deviceId", "get_deviceId", None, 0, 1, 0, 0, 0, 0, 1),
        ("kind", "get_kind", None, 0, 1, 0, 0, 0, 0, 1),
        ("label", "get_label", None, 0, 1, 0, 0, 0, 0, 1),
        ("groupId", "get_groupId", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_deviceId(self):
        val = self._attr.get('deviceId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_device_info.py -> MediaDeviceInfo.deviceId -> get attr')

    def get_kind(self):
        val = self._attr.get('kind')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_device_info.py -> MediaDeviceInfo.kind -> get attr')

    def get_label(self):
        val = self._attr.get('label')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_device_info.py -> MediaDeviceInfo.label -> get attr')

    def get_groupId(self):
        val = self._attr.get('groupId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_media_device_info.py -> MediaDeviceInfo.groupId -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_media_device_info.py -> MediaDeviceInfo.toJSON{tuple(args)} -> method')
