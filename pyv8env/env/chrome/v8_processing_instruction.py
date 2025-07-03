from .flags import *
from .v8_character_data import CharacterData


@construct_100001
class ProcessingInstruction(CharacterData):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ProcessingInstruction, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),
        ("sheet", "get_sheet", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_processing_instruction.py -> ProcessingInstruction.target -> get attr')

    def get_sheet(self):
        val = self._attr.get('sheet')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_processing_instruction.py -> ProcessingInstruction.sheet -> get attr')
