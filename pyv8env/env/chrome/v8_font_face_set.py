from .flags import *
from .v8_event_target import EventTarget


@construct_000000
class FontFaceSet(EventTarget):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(FontFaceSet, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("onloading", "get_onloading", "set_onloading", 0, 1, 0, 0, 0, 0, 1),
        ("onloadingdone", "get_onloadingdone", "set_onloadingdone", 0, 1, 0, 0, 0, 0, 1),
        ("onloadingerror", "get_onloadingerror", "set_onloadingerror", 0, 1, 0, 0, 0, 0, 1),
        ("ready", "get_ready", None, 0, 1, 0, 1, 0, 0, 1),
        ("status", "get_status", None, 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("check", "fn_check", 1, 0, 1, 0, 0, 0, 0),
        ("load", "fn_load", 1, 0, 1, 0, 1, 0, 0),
        ("add", "fn_add", 1, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 0, 0, 1, 0, 0, 0, 0),
        ("delete", "fn_delete", 1, 0, 1, 0, 0, 0, 0),
        ("entries", "fn_entries", 0, 0, 1, 0, 0, 0, 0),
        ("forEach", "fn_forEach", 1, 0, 1, 0, 0, 0, 0),
        ("has", "fn_has", 1, 0, 1, 0, 0, 0, 0),
        ("keys", "fn_keys", 0, 0, 1, 0, 0, 0, 0),
        ("values", "fn_values", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_onloading(self):
        val = self._attr.get('onloading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.onloading -> get attr')

    def set_onloading(self, val):
        self._attr['onloading'] = val

    def get_onloadingdone(self):
        val = self._attr.get('onloadingdone')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.onloadingdone -> get attr')

    def set_onloadingdone(self, val):
        self._attr['onloadingdone'] = val

    def get_onloadingerror(self):
        val = self._attr.get('onloadingerror')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.onloadingerror -> get attr')

    def set_onloadingerror(self, val):
        self._attr['onloadingerror'] = val

    def get_ready(self):
        val = self._attr.get('ready')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.ready -> get attr')

    def get_status(self):
        val = self._attr.get('status')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.status -> get attr')

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.size -> get attr')

    def fn_check(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.check{tuple(args)} -> method')

    def fn_load(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.load{tuple(args)} -> method')

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.add{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.clear{tuple(args)} -> method')

    def fn_delete(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.delete{tuple(args)} -> method')

    def fn_entries(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.entries{tuple(args)} -> method')

    def fn_forEach(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.forEach{tuple(args)} -> method')

    def fn_has(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.has{tuple(args)} -> method')

    def fn_keys(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.keys{tuple(args)} -> method')

    def fn_values(self, *args):
        logger.debug(f'patch -> v8_font_face_set.py -> FontFaceSet.values{tuple(args)} -> method')
