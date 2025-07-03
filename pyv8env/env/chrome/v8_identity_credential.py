from .flags import *
from .v8_credential import Credential


@construct_100001
class IdentityCredential(Credential):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(IdentityCredential, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("token", "get_token", None, 0, 1, 0, 0, 0, 0, 1),
        ("isAutoSelected", "get_isAutoSelected", None, 0, 1, 0, 0, 0, 0, 1),
        ("configURL", "get_configURL", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("disconnect", "fn_disconnect", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_token(self):
        val = self._attr.get('token')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_identity_credential.py -> IdentityCredential.token -> get attr')

    def get_isAutoSelected(self):
        val = self._attr.get('isAutoSelected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_identity_credential.py -> IdentityCredential.isAutoSelected -> get attr')

    def get_configURL(self):
        val = self._attr.get('configURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_identity_credential.py -> IdentityCredential.configURL -> get attr')

    @classmethod
    def fn_disconnect(cls, *args):
        logger.debug(f'patch -> v8_identity_credential.py -> IdentityCredential.disconnect{tuple(args)} -> method')
