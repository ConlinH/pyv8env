from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class PreferenceObject(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(PreferenceObject, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("override", "get_override", None, 0, 1, 0, 0, 0, 0, 1),
        ("value", "get_value", None, 0, 1, 0, 0, 0, 0, 1),
        ("validValues", "get_validValues", None, 0, 1, 0, 0, 0, 0, 1),
        ("onchange", "get_onchange", "set_onchange", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("clearOverride", "fn_clearOverride", 0, 0, 1, 0, 0, 0, 0),
        ("requestOverride", "fn_requestOverride", 1, 0, 1, 0, 1, 0, 0),

    )

    def get_override(self):
        val = self._attr.get('override')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_object.py -> PreferenceObject.override -> get attr')

    def get_value(self):
        val = self._attr.get('value')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_object.py -> PreferenceObject.value -> get attr')

    def get_validValues(self):
        val = self._attr.get('validValues')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_object.py -> PreferenceObject.validValues -> get attr')

    def get_onchange(self):
        val = self._attr.get('onchange')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_preference_object.py -> PreferenceObject.onchange -> get attr')

    def set_onchange(self, val):
        self._attr['onchange'] = val

    def fn_clearOverride(self, *args):
        logger.debug(f'patch -> v8_preference_object.py -> PreferenceObject.clearOverride{tuple(args)} -> method')

    def fn_requestOverride(self, *args):
        logger.debug(f'patch -> v8_preference_object.py -> PreferenceObject.requestOverride{tuple(args)} -> method')
