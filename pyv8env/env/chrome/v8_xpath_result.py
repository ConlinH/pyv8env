from .flags import *


@construct_100001
class XPathResult:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    ANY_TYPE = 0
    NUMBER_TYPE = 1
    STRING_TYPE = 2
    BOOLEAN_TYPE = 3
    UNORDERED_NODE_ITERATOR_TYPE = 4
    ORDERED_NODE_ITERATOR_TYPE = 5
    UNORDERED_NODE_SNAPSHOT_TYPE = 6
    ORDERED_NODE_SNAPSHOT_TYPE = 7
    ANY_UNORDERED_NODE_TYPE = 8
    FIRST_ORDERED_NODE_TYPE = 9

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("resultType", "get_resultType", None, 0, 1, 0, 0, 0, 0, 1),
        ("numberValue", "get_numberValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("stringValue", "get_stringValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("booleanValue", "get_booleanValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("singleNodeValue", "get_singleNodeValue", None, 0, 1, 0, 0, 0, 0, 1),
        ("invalidIteratorState", "get_invalidIteratorState", None, 0, 1, 0, 0, 0, 0, 1),
        ("snapshotLength", "get_snapshotLength", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("iterateNext", "fn_iterateNext", 0, 0, 1, 0, 0, 0, 0),
        ("snapshotItem", "fn_snapshotItem", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_resultType(self):
        val = self._attr.get('resultType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.resultType -> get attr')

    def get_numberValue(self):
        val = self._attr.get('numberValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.numberValue -> get attr')

    def get_stringValue(self):
        val = self._attr.get('stringValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.stringValue -> get attr')

    def get_booleanValue(self):
        val = self._attr.get('booleanValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.booleanValue -> get attr')

    def get_singleNodeValue(self):
        val = self._attr.get('singleNodeValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.singleNodeValue -> get attr')

    def get_invalidIteratorState(self):
        val = self._attr.get('invalidIteratorState')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.invalidIteratorState -> get attr')

    def get_snapshotLength(self):
        val = self._attr.get('snapshotLength')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.snapshotLength -> get attr')

    def fn_iterateNext(self, *args):
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.iterateNext{tuple(args)} -> method')

    def fn_snapshotItem(self, *args):
        logger.debug(f'patch -> v8_xpath_result.py -> XPathResult.snapshotItem{tuple(args)} -> method')
