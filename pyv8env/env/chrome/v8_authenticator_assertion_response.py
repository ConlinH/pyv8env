from .flags import *
from .v8_authenticator_response import AuthenticatorResponse


@construct_100001
class AuthenticatorAssertionResponse(AuthenticatorResponse):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AuthenticatorAssertionResponse, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("authenticatorData", "get_authenticatorData", None, 0, 1, 0, 0, 0, 0, 1),
        ("signature", "get_signature", None, 0, 1, 0, 0, 0, 0, 1),
        ("userHandle", "get_userHandle", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_authenticatorData(self):
        val = self._attr.get('authenticatorData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_authenticator_assertion_response.py -> AuthenticatorAssertionResponse.authenticatorData -> get attr')

    def get_signature(self):
        val = self._attr.get('signature')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_authenticator_assertion_response.py -> AuthenticatorAssertionResponse.signature -> get attr')

    def get_userHandle(self):
        val = self._attr.get('userHandle')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_authenticator_assertion_response.py -> AuthenticatorAssertionResponse.userHandle -> get attr')
