from .flags import *


@construct_110001
class CustomElementRegistry:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("define", "fn_define", 2, 0, 1, 0, 0, 0, 0),
        ("get", "fn_get", 1, 0, 1, 0, 0, 0, 0),
        ("upgrade", "fn_upgrade", 1, 0, 1, 0, 0, 0, 0),
        ("whenDefined", "fn_whenDefined", 1, 0, 1, 0, 1, 0, 0),
        ("getName", "fn_getName", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_define(self, *args):
        logger.debug(f'patch -> v8_custom_element_registry.py -> CustomElementRegistry.define{tuple(args)} -> method')

    def fn_get(self, *args):
        logger.debug(f'patch -> v8_custom_element_registry.py -> CustomElementRegistry.get{tuple(args)} -> method')

    def fn_upgrade(self, *args):
        logger.debug(f'patch -> v8_custom_element_registry.py -> CustomElementRegistry.upgrade{tuple(args)} -> method')

    def fn_whenDefined(self, *args):
        logger.debug(f'patch -> v8_custom_element_registry.py -> CustomElementRegistry.whenDefined{tuple(args)} -> method')

    def fn_getName(self, *args):
        logger.debug(f'patch -> v8_custom_element_registry.py -> CustomElementRegistry.getName{tuple(args)} -> method')
