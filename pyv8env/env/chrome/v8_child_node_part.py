from .flags import *
from .v8_part import Part


@construct_113001
class ChildNodePart(Part):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(ChildNodePart, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("previousSibling", "get_previousSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextSibling", "get_nextSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("children", "get_children", None, 0, 1, 0, 0, 0, 0, 1),
        ("rootContainer", "get_rootContainer", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("replaceChildren", "fn_replaceChildren", 0, 0, 1, 0, 0, 0, 0),
        ("clone", "fn_clone", 0, 0, 1, 0, 0, 0, 0),
        ("getPartNode", "fn_getPartNode", 1, 0, 1, 0, 0, 0, 0),
        ("getParts", "fn_getParts", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_previousSibling(self):
        val = self._attr.get('previousSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.previousSibling -> get attr')

    def get_nextSibling(self):
        val = self._attr.get('nextSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.nextSibling -> get attr')

    def get_children(self):
        val = self._attr.get('children')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.children -> get attr')

    def get_rootContainer(self):
        val = self._attr.get('rootContainer')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.rootContainer -> get attr')

    def fn_replaceChildren(self, *args):
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.replaceChildren{tuple(args)} -> method')

    def fn_clone(self, *args):
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.clone{tuple(args)} -> method')

    def fn_getPartNode(self, *args):
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.getPartNode{tuple(args)} -> method')

    def fn_getParts(self, *args):
        logger.debug(f'patch -> v8_child_node_part.py -> ChildNodePart.getParts{tuple(args)} -> method')
