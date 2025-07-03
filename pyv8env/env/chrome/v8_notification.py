from .flags import *
from .v8_event_target import EventTarget


@construct_111001
class Notification(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(Notification, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("permission", "get_permission", None, 0, 2, 0, 1, 1, 1, 1),
        ("maxActions", "get_maxActions", None, 0, 2, 0, 1, 1, 1, 1),
        ("onclick", "get_onclick", "set_onclick", 0, 1, 0, 0, 0, 0, 1),
        ("onshow", "get_onshow", "set_onshow", 0, 1, 0, 0, 0, 0, 1),
        ("onerror", "get_onerror", "set_onerror", 0, 1, 0, 0, 0, 0, 1),
        ("onclose", "get_onclose", "set_onclose", 0, 1, 0, 0, 0, 0, 1),
        ("title", "get_title", None, 0, 1, 0, 0, 0, 0, 1),
        ("dir", "get_dir", None, 0, 1, 0, 0, 0, 0, 1),
        ("lang", "get_lang", None, 0, 1, 0, 0, 0, 0, 1),
        ("body", "get_body", None, 0, 1, 0, 0, 0, 0, 1),
        ("tag", "get_tag", None, 0, 1, 0, 0, 0, 0, 1),
        ("icon", "get_icon", None, 0, 1, 0, 0, 0, 0, 1),
        ("badge", "get_badge", None, 0, 1, 0, 0, 0, 0, 1),
        ("vibrate", "get_vibrate", None, 0, 1, 0, 0, 0, 0, 1),
        ("timestamp", "get_timestamp", None, 0, 1, 0, 0, 0, 0, 1),
        ("renotify", "get_renotify", None, 0, 1, 0, 0, 0, 0, 1),
        ("silent", "get_silent", None, 0, 1, 0, 0, 0, 0, 1),
        ("requireInteraction", "get_requireInteraction", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("actions", "get_actions", None, 0, 1, 0, 0, 0, 0, 1),
        ("image", "get_image", None, 0, 1, 0, 0, 0, 0, 1),
        ("scenario", "get_scenario", None, 0, 1, 0, 0, 0, 0, 1),
        ("showTrigger", "get_showTrigger", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("close", "fn_close", 0, 0, 1, 0, 0, 0, 0),
        ("requestPermission", "fn_requestPermission", 0, 0, 2, 0, 1, 1, 0),

    )

    @classmethod
    def get_permission(cls):
        logger.debug(f'patch -> v8_notification.py -> Notification.permission -> get attr')

    @classmethod
    def get_maxActions(cls):
        logger.debug(f'patch -> v8_notification.py -> Notification.maxActions -> get attr')

    def get_onclick(self):
        val = self._attr.get('onclick')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.onclick -> get attr')

    def set_onclick(self, val):
        self._attr['onclick'] = val

    def get_onshow(self):
        val = self._attr.get('onshow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.onshow -> get attr')

    def set_onshow(self, val):
        self._attr['onshow'] = val

    def get_onerror(self):
        val = self._attr.get('onerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.onerror -> get attr')

    def set_onerror(self, val):
        self._attr['onerror'] = val

    def get_onclose(self):
        val = self._attr.get('onclose')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.onclose -> get attr')

    def set_onclose(self, val):
        self._attr['onclose'] = val

    def get_title(self):
        val = self._attr.get('title')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.title -> get attr')

    def get_dir(self):
        val = self._attr.get('dir')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.dir -> get attr')

    def get_lang(self):
        val = self._attr.get('lang')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.lang -> get attr')

    def get_body(self):
        val = self._attr.get('body')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.body -> get attr')

    def get_tag(self):
        val = self._attr.get('tag')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.tag -> get attr')

    def get_icon(self):
        val = self._attr.get('icon')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.icon -> get attr')

    def get_badge(self):
        val = self._attr.get('badge')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.badge -> get attr')

    def get_vibrate(self):
        val = self._attr.get('vibrate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.vibrate -> get attr')

    def get_timestamp(self):
        val = self._attr.get('timestamp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.timestamp -> get attr')

    def get_renotify(self):
        val = self._attr.get('renotify')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.renotify -> get attr')

    def get_silent(self):
        val = self._attr.get('silent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.silent -> get attr')

    def get_requireInteraction(self):
        val = self._attr.get('requireInteraction')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.requireInteraction -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.data -> get attr')

    def get_actions(self):
        val = self._attr.get('actions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.actions -> get attr')

    def get_image(self):
        val = self._attr.get('image')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.image -> get attr')

    def get_scenario(self):
        val = self._attr.get('scenario')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.scenario -> get attr')

    def get_showTrigger(self):
        val = self._attr.get('showTrigger')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification.py -> Notification.showTrigger -> get attr')

    def fn_close(self, *args):
        logger.debug(f'patch -> v8_notification.py -> Notification.close{tuple(args)} -> method')

    @classmethod
    def fn_requestPermission(cls, *args):
        logger.debug(f'patch -> v8_notification.py -> Notification.requestPermission{tuple(args)} -> method')
