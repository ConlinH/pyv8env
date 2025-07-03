from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Node(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Node, self).__init__(*args, **kw)
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12
    DOCUMENT_POSITION_DISCONNECTED = 1
    DOCUMENT_POSITION_PRECEDING = 2
    DOCUMENT_POSITION_FOLLOWING = 4
    DOCUMENT_POSITION_CONTAINS = 8
    DOCUMENT_POSITION_CONTAINED_BY = 16
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = 32

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("nodeType", "get_nodeType", None, 0, 1, 0, 0, 0, 0, 1),
        ("nodeName", "get_nodeName", None, 0, 1, 0, 0, 0, 0, 1),
        ("baseURI", "get_baseURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("isConnected", "get_isConnected", None, 0, 1, 0, 0, 0, 0, 1),
        ("ownerDocument", "get_ownerDocument", None, 0, 1, 0, 0, 0, 0, 1),
        ("parentNode", "get_parentNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("parentElement", "get_parentElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("childNodes", "get_childNodes", None, 0, 1, 0, 0, 0, 0, 1),
        ("firstChild", "get_firstChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastChild", "get_lastChild", None, 0, 1, 0, 0, 0, 0, 1),
        ("previousSibling", "get_previousSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextSibling", "get_nextSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("nodeValue", "get_nodeValue", "set_nodeValue", 0, 1, 0, 0, 0, 0, 1),
        ("textContent", "get_textContent", "set_textContent", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("appendChild", "fn_appendChild", 1, 0, 1, 0, 0, 0, 0),
        ("cloneNode", "fn_cloneNode", 0, 0, 1, 0, 0, 0, 0),
        ("compareDocumentPosition", "fn_compareDocumentPosition", 1, 0, 1, 0, 0, 0, 0),
        ("contains", "fn_contains", 1, 0, 1, 0, 0, 0, 1),
        ("getRootNode", "fn_getRootNode", 0, 0, 1, 0, 0, 0, 0),
        ("hasChildNodes", "fn_hasChildNodes", 0, 0, 1, 0, 0, 0, 1),
        ("insertBefore", "fn_insertBefore", 2, 0, 1, 0, 0, 0, 0),
        ("isDefaultNamespace", "fn_isDefaultNamespace", 1, 0, 1, 0, 0, 0, 0),
        ("isEqualNode", "fn_isEqualNode", 1, 0, 1, 0, 0, 0, 0),
        ("isSameNode", "fn_isSameNode", 1, 0, 1, 0, 0, 0, 0),
        ("lookupNamespaceURI", "fn_lookupNamespaceURI", 1, 0, 1, 0, 0, 0, 0),
        ("lookupPrefix", "fn_lookupPrefix", 1, 0, 1, 0, 0, 0, 0),
        ("normalize", "fn_normalize", 0, 0, 1, 0, 0, 0, 0),
        ("removeChild", "fn_removeChild", 1, 0, 1, 0, 0, 0, 0),
        ("replaceChild", "fn_replaceChild", 2, 0, 1, 0, 0, 0, 0),
        ("moveBefore", "fn_moveBefore", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_nodeType(self):
        val = self._attr.get('nodeType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.nodeType -> get attr')

    def get_nodeName(self):
        val = self._attr.get('nodeName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.nodeName -> get attr')

    def get_baseURI(self):
        val = self._attr.get('baseURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.baseURI -> get attr')

    def get_isConnected(self):
        val = self._attr.get('isConnected')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.isConnected -> get attr')

    def get_ownerDocument(self):
        val = self._attr.get('ownerDocument')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.ownerDocument -> get attr')

    def get_parentNode(self):
        val = self._attr.get('parentNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.parentNode -> get attr')

    def get_parentElement(self):
        val = self._attr.get('parentElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.parentElement -> get attr')

    def get_childNodes(self):
        val = self._attr.get('childNodes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.childNodes -> get attr')

    def get_firstChild(self):
        val = self._attr.get('firstChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.firstChild -> get attr')

    def get_lastChild(self):
        val = self._attr.get('lastChild')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.lastChild -> get attr')

    def get_previousSibling(self):
        val = self._attr.get('previousSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.previousSibling -> get attr')

    def get_nextSibling(self):
        val = self._attr.get('nextSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.nextSibling -> get attr')

    def get_nodeValue(self):
        val = self._attr.get('nodeValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.nodeValue -> get attr')

    def set_nodeValue(self, val):
        self._attr['nodeValue'] = val

    def get_textContent(self):
        val = self._attr.get('textContent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node.py -> Node.textContent -> get attr')

    def set_textContent(self, val):
        self._attr['textContent'] = val

    def fn_appendChild(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.appendChild{tuple(args)} -> method')

    def fn_cloneNode(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.cloneNode{tuple(args)} -> method')

    def fn_compareDocumentPosition(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.compareDocumentPosition{tuple(args)} -> method')

    def fn_contains(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.contains{tuple(args)} -> method')

    def fn_getRootNode(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.getRootNode{tuple(args)} -> method')

    def fn_hasChildNodes(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.hasChildNodes{tuple(args)} -> method')

    def fn_insertBefore(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.insertBefore{tuple(args)} -> method')

    def fn_isDefaultNamespace(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.isDefaultNamespace{tuple(args)} -> method')

    def fn_isEqualNode(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.isEqualNode{tuple(args)} -> method')

    def fn_isSameNode(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.isSameNode{tuple(args)} -> method')

    def fn_lookupNamespaceURI(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.lookupNamespaceURI{tuple(args)} -> method')

    def fn_lookupPrefix(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.lookupPrefix{tuple(args)} -> method')

    def fn_normalize(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.normalize{tuple(args)} -> method')

    def fn_removeChild(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.removeChild{tuple(args)} -> method')

    def fn_replaceChild(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.replaceChild{tuple(args)} -> method')

    def fn_moveBefore(self, *args):
        logger.debug(f'patch -> v8_node.py -> Node.moveBefore{tuple(args)} -> method')
