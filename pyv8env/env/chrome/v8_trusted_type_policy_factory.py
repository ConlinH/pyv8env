from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class TrustedTypePolicyFactory(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TrustedTypePolicyFactory, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("emptyHTML", "get_emptyHTML", None, 0, 1, 0, 0, 0, 0, 1),
        ("emptyScript", "get_emptyScript", None, 0, 1, 0, 0, 0, 0, 1),
        ("defaultPolicy", "get_defaultPolicy", None, 0, 1, 0, 0, 0, 0, 1),
        ("onbeforecreatepolicy", "get_onbeforecreatepolicy", "set_onbeforecreatepolicy", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("createPolicy", "fn_createPolicy", 1, 0, 1, 0, 0, 0, 0),
        ("getAttributeType", "fn_getAttributeType", 2, 0, 1, 0, 0, 0, 0),
        ("getPropertyType", "fn_getPropertyType", 2, 0, 1, 0, 0, 0, 0),
        ("getTypeMapping", "fn_getTypeMapping", 0, 0, 1, 0, 0, 0, 0),
        ("isHTML", "fn_isHTML", 1, 0, 1, 0, 0, 0, 0),
        ("isScript", "fn_isScript", 1, 0, 1, 0, 0, 0, 0),
        ("isScriptURL", "fn_isScriptURL", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_emptyHTML(self):
        val = self._attr.get('emptyHTML')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.emptyHTML -> get attr')

    def get_emptyScript(self):
        val = self._attr.get('emptyScript')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.emptyScript -> get attr')

    def get_defaultPolicy(self):
        val = self._attr.get('defaultPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.defaultPolicy -> get attr')

    def get_onbeforecreatepolicy(self):
        val = self._attr.get('onbeforecreatepolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.onbeforecreatepolicy -> get attr')

    def set_onbeforecreatepolicy(self, val):
        self._attr['onbeforecreatepolicy'] = val

    def fn_createPolicy(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.createPolicy{tuple(args)} -> method')

    def fn_getAttributeType(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.getAttributeType{tuple(args)} -> method')

    def fn_getPropertyType(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.getPropertyType{tuple(args)} -> method')

    def fn_getTypeMapping(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.getTypeMapping{tuple(args)} -> method')

    def fn_isHTML(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.isHTML{tuple(args)} -> method')

    def fn_isScript(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.isScript{tuple(args)} -> method')

    def fn_isScriptURL(self, *args):
        logger.debug(f'patch -> v8_trusted_type_policy_factory.py -> TrustedTypePolicyFactory.isScriptURL{tuple(args)} -> method')
