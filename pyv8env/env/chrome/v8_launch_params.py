from .flags import *


@construct_100001
class LaunchParams:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("targetURL", "get_targetURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("files", "get_files", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_targetURL(self):
        val = self._attr.get('targetURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_launch_params.py -> LaunchParams.targetURL -> get attr')

    def get_files(self):
        val = self._attr.get('files')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_launch_params.py -> LaunchParams.files -> get attr')
