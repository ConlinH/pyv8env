from .flags import *


@construct_100001
class TrustedScriptURL:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),
        ("fromLiteral", "fn_fromLiteral", 1, 0, 2, 0, 1, 1, 0),

    )

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_trusted_script_url.py -> TrustedScriptURL.toJSON{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_trusted_script_url.py -> TrustedScriptURL.toString{tuple(args)} -> method')

    @classmethod
    def fn_fromLiteral(cls, *args):
        logger.debug(f'patch -> v8_trusted_script_url.py -> TrustedScriptURL.fromLiteral{tuple(args)} -> method')
