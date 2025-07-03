from .flags import *
from .v8_report_body import ReportBody


@construct_000000
class CoopAccessViolationReportBody(ReportBody):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CoopAccessViolationReportBody, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("sourceFile", "get_sourceFile", None, 0, 1, 0, 0, 0, 0, 1),
        ("lineNumber", "get_lineNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("columnNumber", "get_columnNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("property", "get_property", None, 0, 1, 0, 0, 0, 0, 1),
        ("openeeURL", "get_openeeURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("openerURL", "get_openerURL", None, 0, 1, 0, 0, 0, 0, 1),
        ("otherDocumentURL", "get_otherDocumentURL", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_sourceFile(self):
        val = self._attr.get('sourceFile')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.sourceFile -> get attr')

    def get_lineNumber(self):
        val = self._attr.get('lineNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.lineNumber -> get attr')

    def get_columnNumber(self):
        val = self._attr.get('columnNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.columnNumber -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.type -> get attr')

    def get_property(self):
        val = self._attr.get('property')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.property -> get attr')

    def get_openeeURL(self):
        val = self._attr.get('openeeURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.openeeURL -> get attr')

    def get_openerURL(self):
        val = self._attr.get('openerURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.openerURL -> get attr')

    def get_otherDocumentURL(self):
        val = self._attr.get('otherDocumentURL')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.otherDocumentURL -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_coop_access_violation_report_body.py -> CoopAccessViolationReportBody.toJSON{tuple(args)} -> method')
