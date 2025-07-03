from .flags import *
from .v8_report_body import ReportBody


@construct_000000
class CSPViolationReportBody(ReportBody):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CSPViolationReportBody, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("documentURL", "get_documentURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("referrer", "get_referrer", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockedURL", "get_blockedURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("effectiveDirective", "get_effectiveDirective", None, 0, 1, 0, 0, 0, 0, 1),
        ("originalPolicy", "get_originalPolicy", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceFile", "get_sourceFile", None, 0, 1, 0, 0, 0, 0, 1),
        ("sample", "get_sample", None, 0, 1, 0, 0, 0, 0, 1),
        ("disposition", "get_disposition", None, 0, 1, 0, 0, 0, 0, 1),
        ("statusCode", "get_statusCode", None, 0, 1, 0, 0, 0, 0, 1),
        ("lineNumber", "get_lineNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("columnNumber", "get_columnNumber", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_documentURL(self):
        val = self._attr.get('documentURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.documentURL -> get attr')

    def get_referrer(self):
        val = self._attr.get('referrer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.referrer -> get attr')

    def get_blockedURL(self):
        val = self._attr.get('blockedURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.blockedURL -> get attr')

    def get_effectiveDirective(self):
        val = self._attr.get('effectiveDirective')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.effectiveDirective -> get attr')

    def get_originalPolicy(self):
        val = self._attr.get('originalPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.originalPolicy -> get attr')

    def get_sourceFile(self):
        val = self._attr.get('sourceFile')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.sourceFile -> get attr')

    def get_sample(self):
        val = self._attr.get('sample')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.sample -> get attr')

    def get_disposition(self):
        val = self._attr.get('disposition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.disposition -> get attr')

    def get_statusCode(self):
        val = self._attr.get('statusCode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.statusCode -> get attr')

    def get_lineNumber(self):
        val = self._attr.get('lineNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.lineNumber -> get attr')

    def get_columnNumber(self):
        val = self._attr.get('columnNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.columnNumber -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_csp_violation_report_body.py -> CSPViolationReportBody.toJSON{tuple(args)} -> method')
