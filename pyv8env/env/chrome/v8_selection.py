from .flags import *


@construct_100001
class Selection:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("anchorNode", "get_anchorNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("anchorOffset", "get_anchorOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("focusNode", "get_focusNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("focusOffset", "get_focusOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("isCollapsed", "get_isCollapsed", None, 0, 1, 0, 0, 0, 0, 1),
        ("rangeCount", "get_rangeCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("baseNode", "get_baseNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("baseOffset", "get_baseOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("extentNode", "get_extentNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("extentOffset", "get_extentOffset", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("addRange", "fn_addRange", 1, 0, 1, 0, 0, 0, 0),
        ("collapse", "fn_collapse", 1, 0, 1, 0, 0, 0, 0),
        ("collapseToEnd", "fn_collapseToEnd", 0, 0, 1, 0, 0, 0, 0),
        ("collapseToStart", "fn_collapseToStart", 0, 0, 1, 0, 0, 0, 0),
        ("containsNode", "fn_containsNode", 1, 0, 1, 0, 0, 0, 0),
        ("deleteFromDocument", "fn_deleteFromDocument", 0, 0, 1, 0, 0, 0, 0),
        ("empty", "fn_empty", 0, 0, 1, 0, 0, 0, 0),
        ("extend", "fn_extend", 1, 0, 1, 0, 0, 0, 0),
        ("getRangeAt", "fn_getRangeAt", 1, 0, 1, 0, 0, 0, 0),
        ("modify", "fn_modify", 0, 0, 1, 0, 0, 0, 0),
        ("removeAllRanges", "fn_removeAllRanges", 0, 0, 1, 0, 0, 0, 0),
        ("removeRange", "fn_removeRange", 1, 0, 1, 0, 0, 0, 0),
        ("selectAllChildren", "fn_selectAllChildren", 1, 0, 1, 0, 0, 0, 0),
        ("setBaseAndExtent", "fn_setBaseAndExtent", 4, 0, 1, 0, 0, 0, 0),
        ("setPosition", "fn_setPosition", 1, 0, 1, 0, 0, 0, 0),
        ("toString", "fn_toString", 0, 0, 1, 0, 0, 0, 1),

    )

    def get_anchorNode(self):
        val = self._attr.get('anchorNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.anchorNode -> get attr')

    def get_anchorOffset(self):
        val = self._attr.get('anchorOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.anchorOffset -> get attr')

    def get_focusNode(self):
        val = self._attr.get('focusNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.focusNode -> get attr')

    def get_focusOffset(self):
        val = self._attr.get('focusOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.focusOffset -> get attr')

    def get_isCollapsed(self):
        val = self._attr.get('isCollapsed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.isCollapsed -> get attr')

    def get_rangeCount(self):
        val = self._attr.get('rangeCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.rangeCount -> get attr')

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.type -> get attr')

    def get_baseNode(self):
        val = self._attr.get('baseNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.baseNode -> get attr')

    def get_baseOffset(self):
        val = self._attr.get('baseOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.baseOffset -> get attr')

    def get_extentNode(self):
        val = self._attr.get('extentNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.extentNode -> get attr')

    def get_extentOffset(self):
        val = self._attr.get('extentOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_selection.py -> Selection.extentOffset -> get attr')

    def fn_addRange(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.addRange{tuple(args)} -> method')

    def fn_collapse(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.collapse{tuple(args)} -> method')

    def fn_collapseToEnd(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.collapseToEnd{tuple(args)} -> method')

    def fn_collapseToStart(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.collapseToStart{tuple(args)} -> method')

    def fn_containsNode(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.containsNode{tuple(args)} -> method')

    def fn_deleteFromDocument(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.deleteFromDocument{tuple(args)} -> method')

    def fn_empty(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.empty{tuple(args)} -> method')

    def fn_extend(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.extend{tuple(args)} -> method')

    def fn_getRangeAt(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.getRangeAt{tuple(args)} -> method')

    def fn_modify(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.modify{tuple(args)} -> method')

    def fn_removeAllRanges(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.removeAllRanges{tuple(args)} -> method')

    def fn_removeRange(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.removeRange{tuple(args)} -> method')

    def fn_selectAllChildren(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.selectAllChildren{tuple(args)} -> method')

    def fn_setBaseAndExtent(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.setBaseAndExtent{tuple(args)} -> method')

    def fn_setPosition(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.setPosition{tuple(args)} -> method')

    def fn_toString(self, *args):
        logger.debug(f'patch -> v8_selection.py -> Selection.toString{tuple(args)} -> method')
