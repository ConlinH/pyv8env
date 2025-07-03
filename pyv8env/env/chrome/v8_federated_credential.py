from .flags import *
from .v8_credential import Credential


@construct_111001
class FederatedCredential(Credential):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FederatedCredential, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("provider", "get_provider", None, 0, 1, 0, 0, 0, 0, 1),
        ("protocol", "get_protocol", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("iconURL", "get_iconURL", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_provider(self):
        val = self._attr.get('provider')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_federated_credential.py -> FederatedCredential.provider -> get attr')

    def get_protocol(self):
        val = self._attr.get('protocol')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_federated_credential.py -> FederatedCredential.protocol -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_federated_credential.py -> FederatedCredential.name -> get attr')

    def get_iconURL(self):
        val = self._attr.get('iconURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_federated_credential.py -> FederatedCredential.iconURL -> get attr')
