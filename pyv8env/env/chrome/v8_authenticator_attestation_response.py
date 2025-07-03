from .flags import *
from .v8_authenticator_response import AuthenticatorResponse


@construct_100001
class AuthenticatorAttestationResponse(AuthenticatorResponse):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AuthenticatorAttestationResponse, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("attestationObject", "get_attestationObject", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getAuthenticatorData", "fn_getAuthenticatorData", 0, 0, 1, 0, 0, 0, 0),
        ("getPublicKey", "fn_getPublicKey", 0, 0, 1, 0, 0, 0, 0),
        ("getPublicKeyAlgorithm", "fn_getPublicKeyAlgorithm", 0, 0, 1, 0, 0, 0, 0),
        ("getTransports", "fn_getTransports", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_attestationObject(self):
        val = self._attr.get('attestationObject')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_authenticator_attestation_response.py -> AuthenticatorAttestationResponse.attestationObject -> get attr')

    def fn_getAuthenticatorData(self, *args):
        logger.debug(f'patch -> v8_authenticator_attestation_response.py -> AuthenticatorAttestationResponse.getAuthenticatorData{tuple(args)} -> method')

    def fn_getPublicKey(self, *args):
        logger.debug(f'patch -> v8_authenticator_attestation_response.py -> AuthenticatorAttestationResponse.getPublicKey{tuple(args)} -> method')

    def fn_getPublicKeyAlgorithm(self, *args):
        logger.debug(f'patch -> v8_authenticator_attestation_response.py -> AuthenticatorAttestationResponse.getPublicKeyAlgorithm{tuple(args)} -> method')

    def fn_getTransports(self, *args):
        logger.debug(f'patch -> v8_authenticator_attestation_response.py -> AuthenticatorAttestationResponse.getTransports{tuple(args)} -> method')
