from .flags import *
from .v8_report_body import ReportBody


@construct_000000
class DocumentPolicyViolationReportBody(ReportBody):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DocumentPolicyViolationReportBody, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("featureId", "get_featureId", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceFile", "get_sourceFile", None, 0, 1, 0, 0, 0, 0, 1),
        ("lineNumber", "get_lineNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("columnNumber", "get_columnNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("disposition", "get_disposition", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_featureId(self):
        val = self._attr.get('featureId')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_policy_violation_report_body.py -> DocumentPolicyViolationReportBody.featureId -> get attr')

    def get_sourceFile(self):
        val = self._attr.get('sourceFile')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_policy_violation_report_body.py -> DocumentPolicyViolationReportBody.sourceFile -> get attr')

    def get_lineNumber(self):
        val = self._attr.get('lineNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_policy_violation_report_body.py -> DocumentPolicyViolationReportBody.lineNumber -> get attr')

    def get_columnNumber(self):
        val = self._attr.get('columnNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_policy_violation_report_body.py -> DocumentPolicyViolationReportBody.columnNumber -> get attr')

    def get_disposition(self):
        val = self._attr.get('disposition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_policy_violation_report_body.py -> DocumentPolicyViolationReportBody.disposition -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_policy_violation_report_body.py -> DocumentPolicyViolationReportBody.message -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_document_policy_violation_report_body.py -> DocumentPolicyViolationReportBody.toJSON{tuple(args)} -> method')
