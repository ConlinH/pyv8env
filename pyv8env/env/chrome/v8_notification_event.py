from .flags import *
from .v8_extendable_event import ExtendableEvent


@construct_112001
class NotificationEvent(ExtendableEvent):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(NotificationEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("notification", "get_notification", None, 0, 1, 0, 0, 0, 0, 1),
        ("action", "get_action", None, 0, 1, 0, 0, 0, 0, 1),
        ("reply", "get_reply", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_notification(self):
        val = self._attr.get('notification')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification_event.py -> NotificationEvent.notification -> get attr')

    def get_action(self):
        val = self._attr.get('action')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification_event.py -> NotificationEvent.action -> get attr')

    def get_reply(self):
        val = self._attr.get('reply')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification_event.py -> NotificationEvent.reply -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_notification_event.py -> NotificationEvent.isTrusted -> get attr')
