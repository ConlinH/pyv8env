from .flags import *
from .v8_event import Event


@construct_111001
class TextUpdateEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(TextUpdateEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("updateRangeStart", "get_updateRangeStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("updateRangeEnd", "get_updateRangeEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("text", "get_text", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectionStart", "get_selectionStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectionEnd", "get_selectionEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_updateRangeStart(self):
        val = self._attr.get('updateRangeStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_update_event.py -> TextUpdateEvent.updateRangeStart -> get attr')

    def get_updateRangeEnd(self):
        val = self._attr.get('updateRangeEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_update_event.py -> TextUpdateEvent.updateRangeEnd -> get attr')

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_update_event.py -> TextUpdateEvent.text -> get attr')

    def get_selectionStart(self):
        val = self._attr.get('selectionStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_update_event.py -> TextUpdateEvent.selectionStart -> get attr')

    def get_selectionEnd(self):
        val = self._attr.get('selectionEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_update_event.py -> TextUpdateEvent.selectionEnd -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_update_event.py -> TextUpdateEvent.isTrusted -> get attr')
