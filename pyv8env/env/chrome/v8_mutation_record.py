from .flags import *


@construct_100001
class MutationRecord:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),
        ("addedNodes", "get_addedNodes", None, 0, 1, 0, 0, 0, 0, 1),
        ("removedNodes", "get_removedNodes", None, 0, 1, 0, 0, 0, 0, 1),
        ("previousSibling", "get_previousSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextSibling", "get_nextSibling", None, 0, 1, 0, 0, 0, 0, 1),
        ("attributeName", "get_attributeName", None, 0, 1, 0, 0, 0, 0, 1),
        ("attributeNamespace", "get_attributeNamespace", None, 0, 1, 0, 0, 0, 0, 1),
        ("oldValue", "get_oldValue", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.type -> get attr')

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.target -> get attr')

    def get_addedNodes(self):
        val = self._attr.get('addedNodes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.addedNodes -> get attr')

    def get_removedNodes(self):
        val = self._attr.get('removedNodes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.removedNodes -> get attr')

    def get_previousSibling(self):
        val = self._attr.get('previousSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.previousSibling -> get attr')

    def get_nextSibling(self):
        val = self._attr.get('nextSibling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.nextSibling -> get attr')

    def get_attributeName(self):
        val = self._attr.get('attributeName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.attributeName -> get attr')

    def get_attributeNamespace(self):
        val = self._attr.get('attributeNamespace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.attributeNamespace -> get attr')

    def get_oldValue(self):
        val = self._attr.get('oldValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_mutation_record.py -> MutationRecord.oldValue -> get attr')
