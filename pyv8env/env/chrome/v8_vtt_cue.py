from .flags import *
from .v8_text_track_cue import TextTrackCue


@construct_113001
class VTTCue(TextTrackCue):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(VTTCue, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("vertical", "get_vertical", "set_vertical", 0, 1, 0, 0, 0, 0, 1),
        ("snapToLines", "get_snapToLines", "set_snapToLines", 0, 1, 0, 0, 0, 0, 1),
        ("line", "get_line", "set_line", 0, 1, 0, 0, 0, 0, 1),
        ("position", "get_position", "set_position", 0, 1, 0, 0, 0, 0, 1),
        ("size", "get_size", "set_size", 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("text", "get_text", "set_text", 0, 1, 0, 0, 0, 0, 1),
        ("region", "get_region", "set_region", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getCueAsHTML", "fn_getCueAsHTML", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_vertical(self):
        val = self._attr.get('vertical')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.vertical -> get attr')

    def set_vertical(self, val):
        self._attr['vertical'] = val

    def get_snapToLines(self):
        val = self._attr.get('snapToLines')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.snapToLines -> get attr')

    def set_snapToLines(self, val):
        self._attr['snapToLines'] = val

    def get_line(self):
        val = self._attr.get('line')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.line -> get attr')

    def set_line(self, val):
        self._attr['line'] = val

    def get_position(self):
        val = self._attr.get('position')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.position -> get attr')

    def set_position(self, val):
        self._attr['position'] = val

    def get_size(self):
        val = self._attr.get('size')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.size -> get attr')

    def set_size(self, val):
        self._attr['size'] = val

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_text(self):
        val = self._attr.get('text')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.text -> get attr')

    def set_text(self, val):
        self._attr['text'] = val

    def get_region(self):
        val = self._attr.get('region')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.region -> get attr')

    def set_region(self, val):
        self._attr['region'] = val

    def fn_getCueAsHTML(self, *args):
        logger.debug(f'patch -> v8_vtt_cue.py -> VTTCue.getCueAsHTML{tuple(args)} -> method')
