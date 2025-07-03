from .flags import *
from .v8_character_data import CharacterData


@construct_110001
class Text(CharacterData):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Text, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("wholeText", "get_wholeText", None, 0, 1, 0, 0, 0, 0, 1),
        ("assignedSlot", "get_assignedSlot", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("splitText", "fn_splitText", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_wholeText(self):
        val = self._attr.get('wholeText')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text.py -> Text.wholeText -> get attr')

    def get_assignedSlot(self):
        val = self._attr.get('assignedSlot')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text.py -> Text.assignedSlot -> get attr')

    def fn_splitText(self, *args):
        logger.debug(f'patch -> v8_text.py -> Text.splitText{tuple(args)} -> method')
