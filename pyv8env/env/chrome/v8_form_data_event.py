from .flags import *
from .v8_event import Event


@construct_112001
class FormDataEvent(Event):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FormDataEvent, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("formData", "get_formData", None, 0, 1, 0, 0, 0, 0, 1),
        ("isTrusted", "get_isTrusted", None, 0, 0, 4, 0, 0, 0, 1),

    )

    def get_formData(self):
        val = self._attr.get('formData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_form_data_event.py -> FormDataEvent.formData -> get attr')

    def get_isTrusted(self):
        val = self._attr.get('isTrusted')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_form_data_event.py -> FormDataEvent.isTrusted -> get attr')
