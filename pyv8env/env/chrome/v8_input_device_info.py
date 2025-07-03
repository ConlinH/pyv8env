from .flags import *
from .v8_media_device_info import MediaDeviceInfo


@construct_100001
class InputDeviceInfo(MediaDeviceInfo):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(InputDeviceInfo, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getCapabilities", "fn_getCapabilities", 0, 0, 1, 0, 0, 0, 0),

    )

    def fn_getCapabilities(self, *args):
        logger.debug(f'patch -> v8_input_device_info.py -> InputDeviceInfo.getCapabilities{tuple(args)} -> method')
