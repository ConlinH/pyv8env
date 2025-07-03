from .flags import *
from .v8_event_target import EventTarget


@construct_100001
class DocumentPictureInPicture(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DocumentPictureInPicture, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("window", "get_window", None, 0, 1, 0, 0, 0, 0, 1),
        ("onenter", "get_onenter", "set_onenter", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("requestWindow", "fn_requestWindow", 0, 0, 1, 0, 1, 0, 0),

    )

    def get_window(self):
        val = self._attr.get('window')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_picture_in_picture.py -> DocumentPictureInPicture.window -> get attr')

    def get_onenter(self):
        val = self._attr.get('onenter')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_document_picture_in_picture.py -> DocumentPictureInPicture.onenter -> get attr')

    def set_onenter(self, val):
        self._attr['onenter'] = val

    def fn_requestWindow(self, *args):
        logger.debug(f'patch -> v8_document_picture_in_picture.py -> DocumentPictureInPicture.requestWindow{tuple(args)} -> method')
