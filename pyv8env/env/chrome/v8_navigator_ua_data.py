from .flags import *


@construct_100001
class NavigatorUAData:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("brands", "get_brands", None, 0, 1, 0, 0, 0, 0, 1),
        ("mobile", "get_mobile", None, 0, 1, 0, 0, 0, 0, 1),
        ("platform", "get_platform", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getHighEntropyValues", "fn_getHighEntropyValues", 1, 0, 1, 0, 1, 0, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_brands(self):
        val = self._attr.get('brands')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator_ua_data.py -> NavigatorUAData.brands -> get attr')

    def get_mobile(self):
        val = self._attr.get('mobile')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator_ua_data.py -> NavigatorUAData.mobile -> get attr')

    def get_platform(self):
        val = self._attr.get('platform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator_ua_data.py -> NavigatorUAData.platform -> get attr')

    def fn_getHighEntropyValues(self, *args):
        logger.debug(f'patch -> v8_navigator_ua_data.py -> NavigatorUAData.getHighEntropyValues{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_navigator_ua_data.py -> NavigatorUAData.toJSON{tuple(args)} -> method')
