from .flags import *
from .v8_credential import Credential


@construct_100001
class DigitalCredential(Credential):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DigitalCredential, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("protocol", "get_protocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_digital_credential.py -> DigitalCredential.protocol -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_digital_credential.py -> DigitalCredential.data -> get attr')
