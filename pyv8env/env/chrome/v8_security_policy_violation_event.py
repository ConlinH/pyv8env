from .flags import *
from .v8_event import Event


@construct_111001
class SecurityPolicyViolationEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(SecurityPolicyViolationEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("documentURI", "get_documentURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("referrer", "get_referrer", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockedURI", "get_blockedURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("violatedDirective", "get_violatedDirective", None, 0, 1, 0, 0, 0, 0, 1),
        ("effectiveDirective", "get_effectiveDirective", None, 0, 1, 0, 0, 0, 0, 1),
        ("originalPolicy", "get_originalPolicy", None, 0, 1, 0, 0, 0, 0, 1),
        ("disposition", "get_disposition", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceFile", "get_sourceFile", None, 0, 1, 0, 0, 0, 0, 1),
        ("statusCode", "get_statusCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("lineNumber", "get_lineNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("columnNumber", "get_columnNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("sample", "get_sample", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_documentURI(self):
        val = self._attr.get('documentURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.documentURI -> get attr')

    def get_referrer(self):
        val = self._attr.get('referrer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.referrer -> get attr')

    def get_blockedURI(self):
        val = self._attr.get('blockedURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.blockedURI -> get attr')

    def get_violatedDirective(self):
        val = self._attr.get('violatedDirective')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.violatedDirective -> get attr')

    def get_effectiveDirective(self):
        val = self._attr.get('effectiveDirective')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.effectiveDirective -> get attr')

    def get_originalPolicy(self):
        val = self._attr.get('originalPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.originalPolicy -> get attr')

    def get_disposition(self):
        val = self._attr.get('disposition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.disposition -> get attr')

    def get_sourceFile(self):
        val = self._attr.get('sourceFile')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.sourceFile -> get attr')

    def get_statusCode(self):
        val = self._attr.get('statusCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.statusCode -> get attr')

    def get_lineNumber(self):
        val = self._attr.get('lineNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.lineNumber -> get attr')

    def get_columnNumber(self):
        val = self._attr.get('columnNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.columnNumber -> get attr')

    def get_sample(self):
        val = self._attr.get('sample')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.sample -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_security_policy_violation_event.py -> SecurityPolicyViolationEvent.isTrusted -> get attr')
