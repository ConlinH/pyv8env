from .flags import *


@construct_010001
class OriginTrialsTest:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("throwingAttribute", "get_throwingAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("unconditionalAttribute", "get_unconditionalAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("staticUnconditionalAttribute", "get_staticUnconditionalAttribute", None, 0, 2, 0, 1, 1, 1, 1),
        ("secureStaticUnconditionalAttribute", "get_secureStaticUnconditionalAttribute", None, 0, 2, 0, 1, 1, 1, 1),
        ("normalAttribute", "get_normalAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("staticAttribute", "get_staticAttribute", None, 0, 2, 0, 1, 1, 1, 1),
        ("normalAttributePartial", "get_normalAttributePartial", None, 0, 1, 0, 0, 0, 0, 1),
        ("staticAttributePartial", "get_staticAttributePartial", None, 0, 2, 0, 1, 1, 1, 1),
        ("secureUnconditionalAttribute", "get_secureUnconditionalAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("secureAttribute", "get_secureAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("secureStaticAttribute", "get_secureStaticAttribute", None, 0, 2, 0, 1, 1, 1, 1),
        ("secureAttributePartial", "get_secureAttributePartial", None, 0, 1, 0, 0, 0, 0, 1),
        ("secureStaticAttributePartial", "get_secureStaticAttributePartial", None, 0, 2, 0, 1, 1, 1, 1),
        ("deprecationAttribute", "get_deprecationAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("impliedAttribute", "get_impliedAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("invalidOSAttribute", "get_invalidOSAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("thirdPartyAttribute", "get_thirdPartyAttribute", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("checkDictionaryMethod", "fn_checkDictionaryMethod", 1, 0, 1, 0, 0, 0, 0),
        ("getDictionaryMethod", "fn_getDictionaryMethod", 0, 0, 1, 0, 0, 0, 0),
        ("unconditionalDictionaryMethod", "fn_unconditionalDictionaryMethod", 1, 0, 1, 0, 0, 0, 0),
        ("unconditionalMethod", "fn_unconditionalMethod", 0, 0, 1, 0, 0, 0, 0),
        ("staticUnconditionalMethod", "fn_staticUnconditionalMethod", 0, 0, 2, 0, 1, 1, 0),
        ("navigationMethod", "fn_navigationMethod", 0, 0, 1, 0, 0, 0, 0),
        ("normalMethod", "fn_normalMethod", 0, 0, 1, 0, 0, 0, 0),
        ("normalMethodPartial", "fn_normalMethodPartial", 0, 0, 1, 0, 0, 0, 0),
        ("staticMethod", "fn_staticMethod", 0, 0, 2, 0, 1, 1, 0),
        ("staticMethodPartial", "fn_staticMethodPartial", 0, 0, 2, 0, 1, 1, 0),
        ("secureMethod", "fn_secureMethod", 0, 0, 1, 0, 0, 0, 0),
        ("secureMethodPartial", "fn_secureMethodPartial", 0, 0, 1, 0, 0, 0, 0),
        ("secureStaticMethod", "fn_secureStaticMethod", 0, 0, 2, 0, 1, 1, 0),
        ("secureStaticMethodPartial", "fn_secureStaticMethodPartial", 0, 0, 2, 0, 1, 1, 0),
        ("secureUnconditionalMethod", "fn_secureUnconditionalMethod", 0, 0, 1, 0, 0, 0, 0),
        ("secureStaticUnconditionalMethod", "fn_secureStaticUnconditionalMethod", 0, 0, 2, 0, 1, 1, 0),

    )

    def get_throwingAttribute(self):
        val = self._attr.get('throwingAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.throwingAttribute -> get attr')

    def get_unconditionalAttribute(self):
        val = self._attr.get('unconditionalAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.unconditionalAttribute -> get attr')

    @classmethod
    def get_staticUnconditionalAttribute(cls):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.staticUnconditionalAttribute -> get attr')

    @classmethod
    def get_secureStaticUnconditionalAttribute(cls):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureStaticUnconditionalAttribute -> get attr')

    def get_normalAttribute(self):
        val = self._attr.get('normalAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.normalAttribute -> get attr')

    @classmethod
    def get_staticAttribute(cls):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.staticAttribute -> get attr')

    def get_normalAttributePartial(self):
        val = self._attr.get('normalAttributePartial')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.normalAttributePartial -> get attr')

    @classmethod
    def get_staticAttributePartial(cls):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.staticAttributePartial -> get attr')

    def get_secureUnconditionalAttribute(self):
        val = self._attr.get('secureUnconditionalAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureUnconditionalAttribute -> get attr')

    def get_secureAttribute(self):
        val = self._attr.get('secureAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureAttribute -> get attr')

    @classmethod
    def get_secureStaticAttribute(cls):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureStaticAttribute -> get attr')

    def get_secureAttributePartial(self):
        val = self._attr.get('secureAttributePartial')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureAttributePartial -> get attr')

    @classmethod
    def get_secureStaticAttributePartial(cls):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureStaticAttributePartial -> get attr')

    def get_deprecationAttribute(self):
        val = self._attr.get('deprecationAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.deprecationAttribute -> get attr')

    def get_impliedAttribute(self):
        val = self._attr.get('impliedAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.impliedAttribute -> get attr')

    def get_invalidOSAttribute(self):
        val = self._attr.get('invalidOSAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.invalidOSAttribute -> get attr')

    def get_thirdPartyAttribute(self):
        val = self._attr.get('thirdPartyAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.thirdPartyAttribute -> get attr')

    def fn_checkDictionaryMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.checkDictionaryMethod{tuple(args)} -> method')

    def fn_getDictionaryMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.getDictionaryMethod{tuple(args)} -> method')

    def fn_unconditionalDictionaryMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.unconditionalDictionaryMethod{tuple(args)} -> method')

    def fn_unconditionalMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.unconditionalMethod{tuple(args)} -> method')

    @classmethod
    def fn_staticUnconditionalMethod(cls, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.staticUnconditionalMethod{tuple(args)} -> method')

    def fn_navigationMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.navigationMethod{tuple(args)} -> method')

    def fn_normalMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.normalMethod{tuple(args)} -> method')

    def fn_normalMethodPartial(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.normalMethodPartial{tuple(args)} -> method')

    @classmethod
    def fn_staticMethod(cls, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.staticMethod{tuple(args)} -> method')

    @classmethod
    def fn_staticMethodPartial(cls, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.staticMethodPartial{tuple(args)} -> method')

    def fn_secureMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureMethod{tuple(args)} -> method')

    def fn_secureMethodPartial(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureMethodPartial{tuple(args)} -> method')

    @classmethod
    def fn_secureStaticMethod(cls, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureStaticMethod{tuple(args)} -> method')

    @classmethod
    def fn_secureStaticMethodPartial(cls, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureStaticMethodPartial{tuple(args)} -> method')

    def fn_secureUnconditionalMethod(self, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureUnconditionalMethod{tuple(args)} -> method')

    @classmethod
    def fn_secureStaticUnconditionalMethod(cls, *args):
        logger.debug(f'patch -> v8_origin_trials_test.py -> OriginTrialsTest.secureStaticUnconditionalMethod{tuple(args)} -> method')
