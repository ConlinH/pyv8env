from .flags import *


@construct_100001
class TextMetrics:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("actualBoundingBoxLeft", "get_actualBoundingBoxLeft", None, 0, 1, 0, 0, 0, 0, 1),
        ("actualBoundingBoxRight", "get_actualBoundingBoxRight", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontBoundingBoxAscent", "get_fontBoundingBoxAscent", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontBoundingBoxDescent", "get_fontBoundingBoxDescent", None, 0, 1, 0, 0, 0, 0, 1),
        ("actualBoundingBoxAscent", "get_actualBoundingBoxAscent", None, 0, 1, 0, 0, 0, 0, 1),
        ("actualBoundingBoxDescent", "get_actualBoundingBoxDescent", None, 0, 1, 0, 0, 0, 0, 1),
        ("hangingBaseline", "get_hangingBaseline", None, 0, 1, 0, 0, 0, 0, 1),
        ("alphabeticBaseline", "get_alphabeticBaseline", None, 0, 1, 0, 0, 0, 0, 1),
        ("ideographicBaseline", "get_ideographicBaseline", None, 0, 1, 0, 0, 0, 0, 1),
        ("emHeightAscent", "get_emHeightAscent", None, 0, 1, 0, 0, 0, 0, 1),
        ("emHeightDescent", "get_emHeightDescent", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getSelectionRects", "fn_getSelectionRects", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.width -> get attr')

    def get_actualBoundingBoxLeft(self):
        val = self._attr.get('actualBoundingBoxLeft')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.actualBoundingBoxLeft -> get attr')

    def get_actualBoundingBoxRight(self):
        val = self._attr.get('actualBoundingBoxRight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.actualBoundingBoxRight -> get attr')

    def get_fontBoundingBoxAscent(self):
        val = self._attr.get('fontBoundingBoxAscent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.fontBoundingBoxAscent -> get attr')

    def get_fontBoundingBoxDescent(self):
        val = self._attr.get('fontBoundingBoxDescent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.fontBoundingBoxDescent -> get attr')

    def get_actualBoundingBoxAscent(self):
        val = self._attr.get('actualBoundingBoxAscent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.actualBoundingBoxAscent -> get attr')

    def get_actualBoundingBoxDescent(self):
        val = self._attr.get('actualBoundingBoxDescent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.actualBoundingBoxDescent -> get attr')

    def get_hangingBaseline(self):
        val = self._attr.get('hangingBaseline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.hangingBaseline -> get attr')

    def get_alphabeticBaseline(self):
        val = self._attr.get('alphabeticBaseline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.alphabeticBaseline -> get attr')

    def get_ideographicBaseline(self):
        val = self._attr.get('ideographicBaseline')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.ideographicBaseline -> get attr')

    def get_emHeightAscent(self):
        val = self._attr.get('emHeightAscent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.emHeightAscent -> get attr')

    def get_emHeightDescent(self):
        val = self._attr.get('emHeightDescent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.emHeightDescent -> get attr')

    def fn_getSelectionRects(self, *args):
        logger.debug(f'patch -> v8_text_metrics.py -> TextMetrics.getSelectionRects{tuple(args)} -> method')
