from .flags import *


@construct_111001
class Event:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    NONE = 0
    CAPTURING_PHASE = 1
    AT_TARGET = 2
    BUBBLING_PHASE = 3

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("type", "get_type", None, 0, 1, 0, 0, 0, 0, 1),
        ("target", "get_target", None, 0, 1, 0, 0, 0, 0, 1),
        ("currentTarget", "get_currentTarget", None, 0, 1, 0, 0, 0, 0, 1),
        ("eventPhase", "get_eventPhase", None, 0, 1, 0, 0, 0, 0, 1),
        ("bubbles", "get_bubbles", None, 0, 1, 0, 0, 0, 0, 1),
        ("cancelable", "get_cancelable", None, 0, 1, 0, 0, 0, 0, 1),
        ("defaultPrevented", "get_defaultPrevented", None, 0, 1, 0, 0, 0, 0, 1),
        ("composed", "get_composed", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),
        ("timeStamp", "get_timeStamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("srcElement", "get_srcElement", None, 0, 1, 0, 0, 0, 0, 1),
        ("returnValue", "get_returnValue", "set_returnValue", 0, 1, 0, 0, 0, 0, 1),
        ("cancelBubble", "get_cancelBubble", "set_cancelBubble", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("composedPath", "fn_composedPath", 0, 0, 1, 0, 0, 0, 0),
        ("initEvent", "fn_initEvent", 1, 0, 1, 0, 0, 0, 0),
        ("preventDefault", "fn_preventDefault", 0, 0, 1, 0, 0, 0, 0),
        ("stopImmediatePropagation", "fn_stopImmediatePropagation", 0, 0, 1, 0, 0, 0, 0),
        ("stopPropagation", "fn_stopPropagation", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.type -> get attr')

    def get_target(self):
        val = self._attr.get('target')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.target -> get attr')

    def get_currentTarget(self):
        val = self._attr.get('currentTarget')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.currentTarget -> get attr')

    def get_eventPhase(self):
        val = self._attr.get('eventPhase')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.eventPhase -> get attr')

    def get_bubbles(self):
        val = self._attr.get('bubbles')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.bubbles -> get attr')

    def get_cancelable(self):
        val = self._attr.get('cancelable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.cancelable -> get attr')

    def get_defaultPrevented(self):
        val = self._attr.get('defaultPrevented')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.defaultPrevented -> get attr')

    def get_composed(self):
        val = self._attr.get('composed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.composed -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.isTrusted -> get attr')

    def get_timeStamp(self):
        val = self._attr.get('timeStamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.timeStamp -> get attr')

    def get_srcElement(self):
        val = self._attr.get('srcElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.srcElement -> get attr')

    def get_returnValue(self):
        val = self._attr.get('returnValue')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.returnValue -> get attr')

    def set_returnValue(self, val):
        self._attr['returnValue'] = val

    def get_cancelBubble(self):
        val = self._attr.get('cancelBubble')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_event.py -> Event.cancelBubble -> get attr')

    def set_cancelBubble(self, val):
        self._attr['cancelBubble'] = val

    def fn_composedPath(self, *args):
        logger.debug(f'patch -> v8_event.py -> Event.composedPath{tuple(args)} -> method')

    def fn_initEvent(self, *args):
        logger.debug(f'patch -> v8_event.py -> Event.initEvent{tuple(args)} -> method')

    def fn_preventDefault(self, *args):
        logger.debug(f'patch -> v8_event.py -> Event.preventDefault{tuple(args)} -> method')

    def fn_stopImmediatePropagation(self, *args):
        logger.debug(f'patch -> v8_event.py -> Event.stopImmediatePropagation{tuple(args)} -> method')

    def fn_stopPropagation(self, *args):
        logger.debug(f'patch -> v8_event.py -> Event.stopPropagation{tuple(args)} -> method')
