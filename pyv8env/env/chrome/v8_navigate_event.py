from .flags import *
from .v8_event import Event


@construct_112001
class NavigateEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NavigateEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("navigationType", "get_navigationType", None, 0, 1, 0, 0, 0, 0, 1),
        ("destination", "get_destination", None, 0, 1, 0, 0, 0, 0, 1),
        ("canTransition", "get_canTransition", None, 0, 1, 0, 0, 0, 0, 1),
        ("canIntercept", "get_canIntercept", None, 0, 1, 0, 0, 0, 0, 1),
        ("userInitiated", "get_userInitiated", None, 0, 1, 0, 0, 0, 0, 1),
        ("hashChange", "get_hashChange", None, 0, 1, 0, 0, 0, 0, 1),
        ("signal", "get_signal", None, 0, 1, 0, 0, 0, 0, 1),
        ("formData", "get_formData", None, 0, 1, 0, 0, 0, 0, 1),
        ("downloadRequest", "get_downloadRequest", None, 0, 1, 0, 0, 0, 0, 1),
        ("info", "get_info", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),
        ("hasUAVisualTransition", "get_hasUAVisualTransition", None, 0, 1, 0, 0, 0, 0, 1),
        ("sourceElement", "get_sourceElement", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("intercept", "fn_intercept", 0, 0, 1, 0, 0, 0, 0),
        ("scroll", "fn_scroll", 0, 0, 1, 0, 0, 0, 0),
        ("commit", "fn_commit", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_navigationType(self):
        val = self._attr.get('navigationType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.navigationType -> get attr')

    def get_destination(self):
        val = self._attr.get('destination')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.destination -> get attr')

    def get_canTransition(self):
        val = self._attr.get('canTransition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.canTransition -> get attr')

    def get_canIntercept(self):
        val = self._attr.get('canIntercept')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.canIntercept -> get attr')

    def get_userInitiated(self):
        val = self._attr.get('userInitiated')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.userInitiated -> get attr')

    def get_hashChange(self):
        val = self._attr.get('hashChange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.hashChange -> get attr')

    def get_signal(self):
        val = self._attr.get('signal')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.signal -> get attr')

    def get_formData(self):
        val = self._attr.get('formData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.formData -> get attr')

    def get_downloadRequest(self):
        val = self._attr.get('downloadRequest')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.downloadRequest -> get attr')

    def get_info(self):
        val = self._attr.get('info')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.info -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.isTrusted -> get attr')

    def get_hasUAVisualTransition(self):
        val = self._attr.get('hasUAVisualTransition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.hasUAVisualTransition -> get attr')

    def get_sourceElement(self):
        val = self._attr.get('sourceElement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.sourceElement -> get attr')

    def fn_intercept(self, *args):
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.intercept{tuple(args)} -> method')

    def fn_scroll(self, *args):
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.scroll{tuple(args)} -> method')

    def fn_commit(self, *args):
        logger.debug(f'patch -> v8_navigate_event.py -> NavigateEvent.commit{tuple(args)} -> method')
