from .flags import *
from .v8_credential import Credential


@construct_100001
class OTPCredential(Credential):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(OTPCredential, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("code", "get_code", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_code(self):
        val = self._attr.get('code')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_otp_credential.py -> OTPCredential.code -> get attr')
