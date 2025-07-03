from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class Navigation(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Navigation, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("currentEntry", "get_currentEntry", None, 0, 1, 0, 0, 0, 0, 1),
        ("transition", "get_transition", None, 0, 1, 0, 0, 0, 0, 1),
        ("canGoBack", "get_canGoBack", None, 0, 1, 0, 0, 0, 0, 1),
        ("canGoForward", "get_canGoForward", None, 0, 1, 0, 0, 0, 0, 1),
        ("onnavigate", "get_onnavigate", "set_onnavigate", 0, 1, 0, 0, 0, 0, 1),
        ("onnavigatesuccess", "get_onnavigatesuccess", "set_onnavigatesuccess", 0, 1, 0, 0, 0, 0, 1),
        ("onnavigateerror", "get_onnavigateerror", "set_onnavigateerror", 0, 1, 0, 0, 0, 0, 1),
        ("oncurrententrychange", "get_oncurrententrychange", "set_oncurrententrychange", 0, 1, 0, 0, 0, 0, 1),
        ("activation", "get_activation", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("back", "fn_back", 0, 0, 1, 0, 0, 0, 0),
        ("entries", "fn_entries", 0, 0, 1, 0, 0, 0, 0),
        ("forward", "fn_forward", 0, 0, 1, 0, 0, 0, 0),
        ("navigate", "fn_navigate", 1, 0, 1, 0, 0, 0, 0),
        ("reload", "fn_reload", 0, 0, 1, 0, 0, 0, 0),
        ("traverseTo", "fn_traverseTo", 1, 0, 1, 0, 0, 0, 0),
        ("updateCurrentEntry", "fn_updateCurrentEntry", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_currentEntry(self):
        val = self._attr.get('currentEntry')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.currentEntry -> get attr')

    def get_transition(self):
        val = self._attr.get('transition')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.transition -> get attr')

    def get_canGoBack(self):
        val = self._attr.get('canGoBack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.canGoBack -> get attr')

    def get_canGoForward(self):
        val = self._attr.get('canGoForward')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.canGoForward -> get attr')

    def get_onnavigate(self):
        val = self._attr.get('onnavigate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.onnavigate -> get attr')

    def set_onnavigate(self, val):
        self._attr['onnavigate'] = val

    def get_onnavigatesuccess(self):
        val = self._attr.get('onnavigatesuccess')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.onnavigatesuccess -> get attr')

    def set_onnavigatesuccess(self, val):
        self._attr['onnavigatesuccess'] = val

    def get_onnavigateerror(self):
        val = self._attr.get('onnavigateerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.onnavigateerror -> get attr')

    def set_onnavigateerror(self, val):
        self._attr['onnavigateerror'] = val

    def get_oncurrententrychange(self):
        val = self._attr.get('oncurrententrychange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.oncurrententrychange -> get attr')

    def set_oncurrententrychange(self, val):
        self._attr['oncurrententrychange'] = val

    def get_activation(self):
        val = self._attr.get('activation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigation.py -> Navigation.activation -> get attr')

    def fn_back(self, *args):
        logger.debug(f'patch -> v8_navigation.py -> Navigation.back{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_navigation.py -> Navigation.entries{tuple(args)} -> method')

    def fn_forward(self, *args):
        logger.debug(f'patch -> v8_navigation.py -> Navigation.forward{tuple(args)} -> method')

    def fn_navigate(self, *args):
        logger.debug(f'patch -> v8_navigation.py -> Navigation.navigate{tuple(args)} -> method')

    def fn_reload(self, *args):
        logger.debug(f'patch -> v8_navigation.py -> Navigation.reload{tuple(args)} -> method')

    def fn_traverseTo(self, *args):
        logger.debug(f'patch -> v8_navigation.py -> Navigation.traverseTo{tuple(args)} -> method')

    def fn_updateCurrentEntry(self, *args):
        logger.debug(f'patch -> v8_navigation.py -> Navigation.updateCurrentEntry{tuple(args)} -> method')
