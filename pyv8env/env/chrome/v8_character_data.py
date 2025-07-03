from .flags import *
from .v8_node import Node


@construct_100001
class CharacterData(Node):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(CharacterData, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", "set_data", 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("previousElementSibling", "get_previousElementSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextElementSibling", "get_nextElementSibling", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("after", "fn_after", 0, 0, 1, 0, 0, 0, 0),
        ("appendData", "fn_appendData", 1, 0, 1, 0, 0, 0, 0),
        ("before", "fn_before", 0, 0, 1, 0, 0, 0, 0),
        ("deleteData", "fn_deleteData", 2, 0, 1, 0, 0, 0, 0),
        ("insertData", "fn_insertData", 2, 0, 1, 0, 0, 0, 0),
        ("remove", "fn_remove", 0, 0, 1, 0, 0, 0, 0),
        ("replaceData", "fn_replaceData", 3, 0, 1, 0, 0, 0, 0),
        ("replaceWith", "fn_replaceWith", 0, 0, 1, 0, 0, 0, 0),
        ("substringData", "fn_substringData", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.data -> get attr')

    def set_data(self, val):
        self._attr['data'] = val

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.length -> get attr')

    def get_previousElementSibling(self):
        val = self._attr.get('previousElementSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.previousElementSibling -> get attr')

    def get_nextElementSibling(self):
        val = self._attr.get('nextElementSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.nextElementSibling -> get attr')

    def fn_after(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.after{tuple(args)} -> method')

    def fn_appendData(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.appendData{tuple(args)} -> method')

    def fn_before(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.before{tuple(args)} -> method')

    def fn_deleteData(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.deleteData{tuple(args)} -> method')

    def fn_insertData(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.insertData{tuple(args)} -> method')

    def fn_remove(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.remove{tuple(args)} -> method')

    def fn_replaceData(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.replaceData{tuple(args)} -> method')

    def fn_replaceWith(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.replaceWith{tuple(args)} -> method')

    def fn_substringData(self, *args):
        logger.debug(f'patch -> v8_character_data.py -> CharacterData.substringData{tuple(args)} -> method')
