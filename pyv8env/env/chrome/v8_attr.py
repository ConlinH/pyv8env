from .flags import *
from .v8_node import Node


@construct_100001
class Attr(Node):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Attr, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("namespaceURI", "get_namespaceURI", None, 0, 1, 0, 0, 0, 0, 1),
        ("prefix", "get_prefix", None, 0, 1, 0, 0, 0, 0, 1),
        ("localName", "get_localName", None, 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", "set_value", 0, 1, 0, 0, 0, 0, 1),
        ("ownerElement", "get_ownerElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("specified", "get_specified", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_namespaceURI(self):
        val = self._attr.get('namespaceURI')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attr.py -> Attr.namespaceURI -> get attr')

    def get_prefix(self):
        val = self._attr.get('prefix')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attr.py -> Attr.prefix -> get attr')

    def get_localName(self):
        val = self._attr.get('localName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attr.py -> Attr.localName -> get attr')

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attr.py -> Attr.name -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attr.py -> Attr.value -> get attr')

    def set_value(self, val):
        self._attr['value'] = val

    def get_ownerElement(self):
        val = self._attr.get('ownerElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attr.py -> Attr.ownerElement -> get attr')

    def get_specified(self):
        val = self._attr.get('specified')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attr.py -> Attr.specified -> get attr')
