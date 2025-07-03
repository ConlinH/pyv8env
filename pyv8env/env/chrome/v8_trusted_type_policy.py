from .flags import *


@construct_100001
class TrustedTypePolicy:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createHTML", "fn_createHTML", 1, 0, 1, 0, 0, 0, 0),
        ("createScript", "fn_createScript", 1, 0, 1, 0, 0, 0, 0),
        ("createScriptURL", "fn_createScriptURL", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_trusted_type_policy.py -> TrustedTypePolicy.name -> get attr')

    def fn_createHTML(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy.py -> TrustedTypePolicy.createHTML{tuple(args)} -> method')

    def fn_createScript(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy.py -> TrustedTypePolicy.createScript{tuple(args)} -> method')

    def fn_createScriptURL(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy.py -> TrustedTypePolicy.createScriptURL{tuple(args)} -> method')
