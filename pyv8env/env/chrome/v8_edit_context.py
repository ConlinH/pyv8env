from .flags import *
from .v8_event_target import EventTarget


@construct_110001
class EditContext(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(EditContext, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("text", "get_text", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectionStart", "get_selectionStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectionEnd", "get_selectionEnd", None, 0, 1, 0, 0, 0, 0, 1),
        ("characterBoundsRangeStart", "get_characterBoundsRangeStart", None, 0, 1, 0, 0, 0, 0, 1),
        ("ontextupdate", "get_ontextupdate", "set_ontextupdate", 0, 1, 0, 0, 0, 0, 1),
        ("ontextformatupdate", "get_ontextformatupdate", "set_ontextformatupdate", 0, 1, 0, 0, 0, 0, 1),
        ("oncharacterboundsupdate", "get_oncharacterboundsupdate", "set_oncharacterboundsupdate", 0, 1, 0, 0, 0, 0, 1),
        ("oncompositionstart", "get_oncompositionstart", "set_oncompositionstart", 0, 1, 0, 0, 0, 0, 1),
        ("oncompositionend", "get_oncompositionend", "set_oncompositionend", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("attachedElements", "fn_attachedElements", 0, 0, 1, 0, 0, 0, 0),
        ("characterBounds", "fn_characterBounds", 0, 0, 1, 0, 0, 0, 0),
        ("updateCharacterBounds", "fn_updateCharacterBounds", 2, 0, 1, 0, 0, 0, 0),
        ("updateControlBounds", "fn_updateControlBounds", 1, 0, 1, 0, 0, 0, 0),
        ("updateSelection", "fn_updateSelection", 2, 0, 1, 0, 0, 0, 0),
        ("updateSelectionBounds", "fn_updateSelectionBounds", 1, 0, 1, 0, 0, 0, 0),
        ("updateText", "fn_updateText", 3, 0, 1, 0, 0, 0, 0),

    )

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.text -> get attr')

    def get_selectionStart(self):
        val = self._attr.get('selectionStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.selectionStart -> get attr')

    def get_selectionEnd(self):
        val = self._attr.get('selectionEnd')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.selectionEnd -> get attr')

    def get_characterBoundsRangeStart(self):
        val = self._attr.get('characterBoundsRangeStart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.characterBoundsRangeStart -> get attr')

    def get_ontextupdate(self):
        val = self._attr.get('ontextupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.ontextupdate -> get attr')

    def set_ontextupdate(self, val):
        self._attr['ontextupdate'] = val

    def get_ontextformatupdate(self):
        val = self._attr.get('ontextformatupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.ontextformatupdate -> get attr')

    def set_ontextformatupdate(self, val):
        self._attr['ontextformatupdate'] = val

    def get_oncharacterboundsupdate(self):
        val = self._attr.get('oncharacterboundsupdate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.oncharacterboundsupdate -> get attr')

    def set_oncharacterboundsupdate(self, val):
        self._attr['oncharacterboundsupdate'] = val

    def get_oncompositionstart(self):
        val = self._attr.get('oncompositionstart')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.oncompositionstart -> get attr')

    def set_oncompositionstart(self, val):
        self._attr['oncompositionstart'] = val

    def get_oncompositionend(self):
        val = self._attr.get('oncompositionend')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.oncompositionend -> get attr')

    def set_oncompositionend(self, val):
        self._attr['oncompositionend'] = val

    def fn_attachedElements(self, *args):
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.attachedElements{tuple(args)} -> method')

    def fn_characterBounds(self, *args):
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.characterBounds{tuple(args)} -> method')

    def fn_updateCharacterBounds(self, *args):
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.updateCharacterBounds{tuple(args)} -> method')

    def fn_updateControlBounds(self, *args):
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.updateControlBounds{tuple(args)} -> method')

    def fn_updateSelection(self, *args):
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.updateSelection{tuple(args)} -> method')

    def fn_updateSelectionBounds(self, *args):
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.updateSelectionBounds{tuple(args)} -> method')

    def fn_updateText(self, *args):
        logger.debug(f'patch -> v8_edit_context.py -> EditContext.updateText{tuple(args)} -> method')
