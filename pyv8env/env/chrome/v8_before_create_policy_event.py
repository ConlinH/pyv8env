from .flags import *
from .v8_event import Event


@construct_100001
class BeforeCreatePolicyEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BeforeCreatePolicyEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("policyName", "get_policyName", "set_policyName", 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_policyName(self):
        val = self._attr.get('policyName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_before_create_policy_event.py -> BeforeCreatePolicyEvent.policyName -> get attr')

    def set_policyName(self, val):
        self._attr['policyName'] = val

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_before_create_policy_event.py -> BeforeCreatePolicyEvent.isTrusted -> get attr')
