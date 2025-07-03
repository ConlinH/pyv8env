from .flags import *


@construct_100001
class FragmentDirective:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("items", "get_items", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createSelectorDirective", "fn_createSelectorDirective", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_items(self):
        val = self._attr.get('items')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_fragment_directive.py -> FragmentDirective.items -> get attr')

    def fn_createSelectorDirective(self, *args):
        logger.debug(f'patch -> v8_fragment_directive.py -> FragmentDirective.createSelectorDirective{tuple(args)} -> method')
