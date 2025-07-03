from .flags import *


@construct_100001
class TreeWalker:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("root", "get_root", None, 0, 1, 0, 0, 0, 0, 1),
        ("whatToShow", "get_whatToShow", None, 0, 1, 0, 0, 0, 0, 1),
        ("filter", "get_filter", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentNode", "get_currentNode", "set_currentNode", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("firstChild", "fn_firstChild", 0, 0, 1, 0, 0, 0, 0),
        ("lastChild", "fn_lastChild", 0, 0, 1, 0, 0, 0, 0),
        ("nextNode", "fn_nextNode", 0, 0, 1, 0, 0, 0, 0),
        ("nextSibling", "fn_nextSibling", 0, 0, 1, 0, 0, 0, 0),
        ("parentNode", "fn_parentNode", 0, 0, 1, 0, 0, 0, 0),
        ("previousNode", "fn_previousNode", 0, 0, 1, 0, 0, 0, 0),
        ("previousSibling", "fn_previousSibling", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_root(self):
        val = self._attr.get('root')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.root -> get attr')

    def get_whatToShow(self):
        val = self._attr.get('whatToShow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.whatToShow -> get attr')

    def get_filter(self):
        val = self._attr.get('filter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.filter -> get attr')

    def get_currentNode(self):
        val = self._attr.get('currentNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.currentNode -> get attr')

    def set_currentNode(self, val):
        self._attr['currentNode'] = val

    def fn_firstChild(self, *args):
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.firstChild{tuple(args)} -> method')

    def fn_lastChild(self, *args):
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.lastChild{tuple(args)} -> method')

    def fn_nextNode(self, *args):
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.nextNode{tuple(args)} -> method')

    def fn_nextSibling(self, *args):
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.nextSibling{tuple(args)} -> method')

    def fn_parentNode(self, *args):
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.parentNode{tuple(args)} -> method')

    def fn_previousNode(self, *args):
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.previousNode{tuple(args)} -> method')

    def fn_previousSibling(self, *args):
        logger.debug(f'patch -> v8_tree_walker.py -> TreeWalker.previousSibling{tuple(args)} -> method')
