from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class IdleDetector(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IdleDetector, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("userState", "get_userState", None, 0, 1, 0, 0, 0, 0, 1),
        ("screenState", "get_screenState", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("start", "fn_start", 0, 0, 1, 0, 1, 0, 0),
        ("requestPermission", "fn_requestPermission", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_userState(self):
        val = self._attr.get('userState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idle_detector.py -> IdleDetector.userState -> get attr')

    def get_screenState(self):
        val = self._attr.get('screenState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idle_detector.py -> IdleDetector.screenState -> get attr')

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_idle_detector.py -> IdleDetector.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def fn_start(self, *args):
        logger.debug(f'patch -> v8_idle_detector.py -> IdleDetector.start{tuple(args)} -> method')

    @classmethod
    def fn_requestPermission(cls, *args):
        logger.debug(f'patch -> v8_idle_detector.py -> IdleDetector.requestPermission{tuple(args)} -> method')
