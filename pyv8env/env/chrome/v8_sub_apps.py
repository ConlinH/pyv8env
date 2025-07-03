from .flags import *


@construct_100001
class SubApps:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("add", "fn_add", 1, 0, 1, 0, 1, 0, 0),
        ("list", "fn_list", 0, 0, 1, 0, 1, 0, 0),
        ("remove", "fn_remove", 1, 0, 1, 0, 1, 0, 0),

    )

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_sub_apps.py -> SubApps.add{tuple(args)} -> method')

    def fn_list(self, *args):
        logger.debug(f'patch -> v8_sub_apps.py -> SubApps.list{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_sub_apps.py -> SubApps.remove{tuple(args)} -> method')
