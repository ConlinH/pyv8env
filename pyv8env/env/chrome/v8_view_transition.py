from .flags import *


@construct_100001
class ViewTransition:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("finished", "get_finished", None, 0, 1, 0, 1, 0, 0, 1),
        ("ready", "get_ready", None, 0, 1, 0, 1, 0, 0, 1),
        ("updateCallbackDone", "get_updateCallbackDone", None, 0, 1, 0, 1, 0, 0, 1),
        ("types", "get_types", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("skipTransition", "fn_skipTransition", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_finished(self):
        val = self._attr.get('finished')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_transition.py -> ViewTransition.finished -> get attr')

    def get_ready(self):
        val = self._attr.get('ready')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_transition.py -> ViewTransition.ready -> get attr')

    def get_updateCallbackDone(self):
        val = self._attr.get('updateCallbackDone')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_transition.py -> ViewTransition.updateCallbackDone -> get attr')

    def get_types(self):
        val = self._attr.get('types')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_view_transition.py -> ViewTransition.types -> get attr')

    def fn_skipTransition(self, *args):
        logger.debug(f'patch -> v8_view_transition.py -> ViewTransition.skipTransition{tuple(args)} -> method')
