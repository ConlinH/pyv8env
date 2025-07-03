from .flags import *
from .v8_part import Part


@construct_112001
class NodePart(Part):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NodePart, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("node", "get_node", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_node(self):
        val = self._attr.get('node')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_node_part.py -> NodePart.node -> get attr')
