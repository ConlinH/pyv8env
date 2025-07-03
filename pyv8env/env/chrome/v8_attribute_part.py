from .flags import *
from .v8_node_part import NodePart


@construct_114001
class AttributePart(NodePart):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(AttributePart, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("localName", "get_localName", None, 0, 1, 0, 0, 0, 0, 1),
        ("automatic", "get_automatic", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_localName(self):
        val = self._attr.get('localName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attribute_part.py -> AttributePart.localName -> get attr')

    def get_automatic(self):
        val = self._attr.get('automatic')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_attribute_part.py -> AttributePart.automatic -> get attr')
