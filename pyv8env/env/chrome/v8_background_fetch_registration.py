from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class BackgroundFetchRegistration(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(BackgroundFetchRegistration, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("id", "get_id", None, 0, 1, 0, 0, 0, 0, 1),
        ("uploadTotal", "get_uploadTotal", None, 0, 1, 0, 0, 0, 0, 1),
        ("uploaded", "get_uploaded", None, 0, 1, 0, 0, 0, 0, 1),
        ("downloadTotal", "get_downloadTotal", None, 0, 1, 0, 0, 0, 0, 1),
        ("downloaded", "get_downloaded", None, 0, 1, 0, 0, 0, 0, 1),
        ("result", "get_result", None, 0, 1, 0, 0, 0, 0, 1),
        ("failureReason", "get_failureReason", None, 0, 1, 0, 0, 0, 0, 1),
        ("recordsAvailable", "get_recordsAvailable", None, 0, 1, 0, 0, 0, 0, 1),
        ("onprogress", "get_onprogress", "set_onprogress", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abort", "fn_abort", 0, 0, 1, 0, 1, 0, 0),
        ("match", "fn_match", 1, 0, 1, 0, 1, 0, 0),
        ("matchAll", "fn_matchAll", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_id(self):
        val = self._attr.get('id')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.id -> get attr')

    def get_uploadTotal(self):
        val = self._attr.get('uploadTotal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.uploadTotal -> get attr')

    def get_uploaded(self):
        val = self._attr.get('uploaded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.uploaded -> get attr')

    def get_downloadTotal(self):
        val = self._attr.get('downloadTotal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.downloadTotal -> get attr')

    def get_downloaded(self):
        val = self._attr.get('downloaded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.downloaded -> get attr')

    def get_result(self):
        val = self._attr.get('result')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.result -> get attr')

    def get_failureReason(self):
        val = self._attr.get('failureReason')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.failureReason -> get attr')

    def get_recordsAvailable(self):
        val = self._attr.get('recordsAvailable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.recordsAvailable -> get attr')

    def get_onprogress(self):
        val = self._attr.get('onprogress')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.onprogress -> get attr')

    def set_onprogress(self, val):
        self._attr['onprogress'] = val

    def fn_abort(self, *args):
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.abort{tuple(args)} -> method')

    def fn_match(self, *args):
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.match{tuple(args)} -> method')

    def fn_matchAll(self, *args):
        logger.debug(f'patch -> v8_background_fetch_registration.py -> BackgroundFetchRegistration.matchAll{tuple(args)} -> method')
