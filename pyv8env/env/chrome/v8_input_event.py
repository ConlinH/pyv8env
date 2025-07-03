from .flags import *
from .v8_ui_event import UIEvent


@construct_111001
class InputEvent(UIEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(InputEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("isComposing", "get_isComposing", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputType", "get_inputType", None, 0, 1, 0, 0, 0, 0, 1),
        ("dataTransfer", "get_dataTransfer", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getTargetRanges", "fn_getTargetRanges", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_input_event.py -> InputEvent.data -> get attr')

    def get_isComposing(self):
        val = self._attr.get('isComposing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_input_event.py -> InputEvent.isComposing -> get attr')

    def get_inputType(self):
        val = self._attr.get('inputType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_input_event.py -> InputEvent.inputType -> get attr')

    def get_dataTransfer(self):
        val = self._attr.get('dataTransfer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_input_event.py -> InputEvent.dataTransfer -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_input_event.py -> InputEvent.isTrusted -> get attr')

    def fn_getTargetRanges(self, *args):
        logger.debug(f'patch -> v8_input_event.py -> InputEvent.getTargetRanges{tuple(args)} -> method')
