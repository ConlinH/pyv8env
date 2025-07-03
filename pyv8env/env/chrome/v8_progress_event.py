from .flags import *
from .v8_event import Event


@construct_111001
class ProgressEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ProgressEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("lengthComputable", "get_lengthComputable", None, 0, 1, 0, 0, 0, 0, 1),
        ("loaded", "get_loaded", None, 0, 1, 0, 0, 0, 0, 1),
        ("total", "get_total", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_lengthComputable(self):
        val = self._attr.get('lengthComputable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_progress_event.py -> ProgressEvent.lengthComputable -> get attr')

    def get_loaded(self):
        val = self._attr.get('loaded')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_progress_event.py -> ProgressEvent.loaded -> get attr')

    def get_total(self):
        val = self._attr.get('total')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_progress_event.py -> ProgressEvent.total -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_progress_event.py -> ProgressEvent.isTrusted -> get attr')
