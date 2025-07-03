from .flags import *
from .v8_abstract_range import AbstractRange


@construct_110001
class Range(AbstractRange):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Range, self).__init__(*args, **kw)
    START_TO_START = 0
    START_TO_END = 1
    END_TO_END = 2
    END_TO_START = 3

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("commonAncestorContainer", "get_commonAncestorContainer", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("cloneContents", "fn_cloneContents", 0, 0, 1, 0, 0, 0, 0),
        ("cloneRange", "fn_cloneRange", 0, 0, 1, 0, 0, 0, 0),
        ("collapse", "fn_collapse", 0, 0, 1, 0, 0, 0, 0),
        ("compareBoundaryPoints", "fn_compareBoundaryPoints", 2, 0, 1, 0, 0, 0, 0),
        ("comparePoint", "fn_comparePoint", 2, 0, 1, 0, 0, 0, 0),
        ("createContextualFragment", "fn_createContextualFragment", 1, 0, 1, 0, 0, 0, 0),
        ("deleteContents", "fn_deleteContents", 0, 0, 1, 0, 0, 0, 0),
        ("detach", "fn_detach", 0, 0, 1, 0, 0, 0, 0),
        ("expand", "fn_expand", 0, 0, 1, 0, 0, 0, 0),
        ("extractContents", "fn_extractContents", 0, 0, 1, 0, 0, 0, 0),
        ("getBoundingClientRect", "fn_getBoundingClientRect", 0, 0, 1, 0, 0, 0, 0),
        ("getClientRects", "fn_getClientRects", 0, 0, 1, 0, 0, 0, 0),
        ("insertNode", "fn_insertNode", 1, 0, 1, 0, 0, 0, 0),
        ("intersectsNode", "fn_intersectsNode", 1, 0, 1, 0, 0, 0, 0),
        ("isPointInRange", "fn_isPointInRange", 2, 0, 1, 0, 0, 0, 0),
        ("selectNode", "fn_selectNode", 1, 0, 1, 0, 0, 0, 0),
        ("selectNodeContents", "fn_selectNodeContents", 1, 0, 1, 0, 0, 0, 0),
        ("setEnd", "fn_setEnd", 2, 0, 1, 0, 0, 0, 0),
        ("setEndAfter", "fn_setEndAfter", 1, 0, 1, 0, 0, 0, 0),
        ("setEndBefore", "fn_setEndBefore", 1, 0, 1, 0, 0, 0, 0),
        ("setStart", "fn_setStart", 2, 0, 1, 0, 0, 0, 0),
        ("setStartAfter", "fn_setStartAfter", 1, 0, 1, 0, 0, 0, 0),
        ("setStartBefore", "fn_setStartBefore", 1, 0, 1, 0, 0, 0, 0),
        ("surroundContents", "fn_surroundContents", 1, 0, 1, 0, 0, 0, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_commonAncestorContainer(self):
        val = self._attr.get('commonAncestorContainer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_range.py -> Range.commonAncestorContainer -> get attr')

    def fn_cloneContents(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.cloneContents{tuple(args)} -> method')

    def fn_cloneRange(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.cloneRange{tuple(args)} -> method')

    def fn_collapse(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.collapse{tuple(args)} -> method')

    def fn_compareBoundaryPoints(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.compareBoundaryPoints{tuple(args)} -> method')

    def fn_comparePoint(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.comparePoint{tuple(args)} -> method')

    def fn_createContextualFragment(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.createContextualFragment{tuple(args)} -> method')

    def fn_deleteContents(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.deleteContents{tuple(args)} -> method')

    def fn_detach(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.detach{tuple(args)} -> method')

    def fn_expand(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.expand{tuple(args)} -> method')

    def fn_extractContents(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.extractContents{tuple(args)} -> method')

    def fn_getBoundingClientRect(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.getBoundingClientRect{tuple(args)} -> method')

    def fn_getClientRects(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.getClientRects{tuple(args)} -> method')

    def fn_insertNode(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.insertNode{tuple(args)} -> method')

    def fn_intersectsNode(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.intersectsNode{tuple(args)} -> method')

    def fn_isPointInRange(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.isPointInRange{tuple(args)} -> method')

    def fn_selectNode(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.selectNode{tuple(args)} -> method')

    def fn_selectNodeContents(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.selectNodeContents{tuple(args)} -> method')

    def fn_setEnd(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.setEnd{tuple(args)} -> method')

    def fn_setEndAfter(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.setEndAfter{tuple(args)} -> method')

    def fn_setEndBefore(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.setEndBefore{tuple(args)} -> method')

    def fn_setStart(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.setStart{tuple(args)} -> method')

    def fn_setStartAfter(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.setStartAfter{tuple(args)} -> method')

    def fn_setStartBefore(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.setStartBefore{tuple(args)} -> method')

    def fn_surroundContents(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.surroundContents{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_range.py -> Range.toString{tuple(args)} -> method')
