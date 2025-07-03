from .flags import *
from .v8_report_body import ReportBody


@construct_000000
class DeprecationReportBody(ReportBody):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DeprecationReportBody, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("anticipatedRemoval", "get_anticipatedRemoval", None, 0, 1, 0, 0, 0, 0, 1),
        ("message", "get_message", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceFile", "get_sourceFile", None, 0, 1, 0, 0, 0, 0, 1),
        ("lineNumber", "get_lineNumber", None, 0, 1, 0, 0, 0, 0, 1),
        ("columnNumber", "get_columnNumber", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("toJSON", "fn_toJSON", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_deprecation_report_body.py -> DeprecationReportBody.id -> get attr')

    def get_anticipatedRemoval(self):
        val = self._attr.get('anticipatedRemoval')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_deprecation_report_body.py -> DeprecationReportBody.anticipatedRemoval -> get attr')

    def get_message(self):
        val = self._attr.get('message')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_deprecation_report_body.py -> DeprecationReportBody.message -> get attr')

    def get_sourceFile(self):
        val = self._attr.get('sourceFile')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_deprecation_report_body.py -> DeprecationReportBody.sourceFile -> get attr')

    def get_lineNumber(self):
        val = self._attr.get('lineNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_deprecation_report_body.py -> DeprecationReportBody.lineNumber -> get attr')

    def get_columnNumber(self):
        val = self._attr.get('columnNumber')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_deprecation_report_body.py -> DeprecationReportBody.columnNumber -> get attr')

    def fn_toJSON(self, *args):
        logger.debug(f'patch -> v8_deprecation_report_body.py -> DeprecationReportBody.toJSON{tuple(args)} -> method')
