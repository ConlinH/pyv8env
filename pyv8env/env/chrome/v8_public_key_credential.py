from .flags import *
from .v8_credential import Credential


@construct_100001
class PublicKeyCredential(Credential):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PublicKeyCredential, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rawId", "get_rawId", None, 0, 1, 0, 0, 0, 0, 1),
        ("response", "get_response", None, 0, 1, 0, 0, 0, 0, 1),
        ("authenticatorAttachment", "get_authenticatorAttachment", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getClientExtensionResults", "fn_getClientExtensionResults", 0, 0, 1, 0, 0, 0, 0),
        ("isConditionalMediationAvailable", "fn_isConditionalMediationAvailable", 0, 0, 2, 0, 1, 1, 0),
        ("isUserVerifyingPlatformAuthenticatorAvailable", "fn_isUserVerifyingPlatformAuthenticatorAvailable", 0, 0, 2, 0, 1, 1, 0),
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),
        ("parseCreationOptionsFromJSON", "fn_parseCreationOptionsFromJSON", 1, 0, 2, 0, 1, 1, 0),

    )

    def get_rawId(self):
        val = self._attr.get('rawId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.rawId -> get attr')

    def get_response(self):
        val = self._attr.get('response')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.response -> get attr')

    def get_authenticatorAttachment(self):
        val = self._attr.get('authenticatorAttachment')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.authenticatorAttachment -> get attr')

    def fn_getClientExtensionResults(self, *args):
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.getClientExtensionResults{tuple(args)} -> method')

    @classmethod
    def fn_isConditionalMediationAvailable(cls, *args):
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.isConditionalMediationAvailable{tuple(args)} -> method')

    @classmethod
    def fn_isUserVerifyingPlatformAuthenticatorAvailable(cls, *args):
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.isUserVerifyingPlatformAuthenticatorAvailable{tuple(args)} -> method')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.toJSON{tuple(args)} -> method')

    @classmethod
    def fn_parseCreationOptionsFromJSON(cls, *args):
        logger.debug(f'patch -> v8_public_key_credential.py -> PublicKeyCredential.parseCreationOptionsFromJSON{tuple(args)} -> method')
