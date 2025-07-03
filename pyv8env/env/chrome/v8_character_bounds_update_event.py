from .flags import *
from .v8_event import Event


@construct_111001
class CharacterBoundsUpdateEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CharacterBoundsUpdateEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("rangeStart", "get_rangeStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("rangeEnd", "get_rangeEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_rangeStart(self):
        val = self._attr.get('rangeStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_character_bounds_update_event.py -> CharacterBoundsUpdateEvent.rangeStart -> get attr')

    def get_rangeEnd(self):
        val = self._attr.get('rangeEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_character_bounds_update_event.py -> CharacterBoundsUpdateEvent.rangeEnd -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_character_bounds_update_event.py -> CharacterBoundsUpdateEvent.isTrusted -> get attr')
