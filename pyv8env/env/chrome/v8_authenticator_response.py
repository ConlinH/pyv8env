from .flags import *


@construct_100001
class AuthenticatorResponse:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("clientDataJSON", "get_clientDataJSON", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_clientDataJSON(self):
        val = self._attr.get('clientDataJSON')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_authenticator_response.py -> AuthenticatorResponse.clientDataJSON -> get attr')
