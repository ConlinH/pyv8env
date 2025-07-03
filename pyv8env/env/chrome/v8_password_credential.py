from .flags import *
from .v8_credential import Credential


@construct_111001
class PasswordCredential(Credential):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PasswordCredential, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("password", "get_password", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("iconURL", "get_iconURL", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_password(self):
        val = self._attr.get('password')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_password_credential.py -> PasswordCredential.password -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_password_credential.py -> PasswordCredential.name -> get attr')

    def get_iconURL(self):
        val = self._attr.get('iconURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_password_credential.py -> PasswordCredential.iconURL -> get attr')
