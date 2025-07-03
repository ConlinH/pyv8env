from .flags import *


@construct_100001
class NodeIterator:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("root", "get_root", None, 0, 1, 0, 0, 0, 0, 1),
        ("referenceNode", "get_referenceNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointerBeforeReferenceNode", "get_pointerBeforeReferenceNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("whatToShow", "get_whatToShow", None, 0, 1, 0, 0, 0, 0, 1),
        ("filter", "get_filter", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("detach", "fn_detach", 0, 0, 1, 0, 0, 0, 0),
        ("nextNode", "fn_nextNode", 0, 0, 1, 0, 0, 0, 0),
        ("previousNode", "fn_previousNode", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_root(self):
        val = self._attr.get('root')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.root -> get attr')

    def get_referenceNode(self):
        val = self._attr.get('referenceNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.referenceNode -> get attr')

    def get_pointerBeforeReferenceNode(self):
        val = self._attr.get('pointerBeforeReferenceNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.pointerBeforeReferenceNode -> get attr')

    def get_whatToShow(self):
        val = self._attr.get('whatToShow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.whatToShow -> get attr')

    def get_filter(self):
        val = self._attr.get('filter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.filter -> get attr')

    def fn_detach(self, *args):
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.detach{tuple(args)} -> method')

    def fn_nextNode(self, *args):
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.nextNode{tuple(args)} -> method')

    def fn_previousNode(self, *args):
        logger.debug(f'patch -> v8_node_iterator.py -> NodeIterator.previousNode{tuple(args)} -> method')
