from .flags import *
from .v8_event import Event


@construct_100001
class MutationEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(MutationEvent, self).__init__(*args, **kw)
    MODIFICATION = 1
    ADDITION = 2
    REMOVAL = 3

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("relatedNode", "get_relatedNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("prevValue", "get_prevValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("newValue", "get_newValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("attrName", "get_attrName", None, 0, 1, 0, 0, 0, 0, 1),
        ("attrChange", "get_attrChange", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("initMutationEvent", "fn_initMutationEvent", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_relatedNode(self):
        val = self._attr.get('relatedNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_event.py -> MutationEvent.relatedNode -> get attr')

    def get_prevValue(self):
        val = self._attr.get('prevValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_event.py -> MutationEvent.prevValue -> get attr')

    def get_newValue(self):
        val = self._attr.get('newValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_event.py -> MutationEvent.newValue -> get attr')

    def get_attrName(self):
        val = self._attr.get('attrName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_event.py -> MutationEvent.attrName -> get attr')

    def get_attrChange(self):
        val = self._attr.get('attrChange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_event.py -> MutationEvent.attrChange -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_event.py -> MutationEvent.isTrusted -> get attr')

    def fn_initMutationEvent(self, *args):
        logger.debug(f'patch -> v8_mutation_event.py -> MutationEvent.initMutationEvent{tuple(args)} -> method')
