from .flags import *


@construct_100001
class DelegatedInkTrailPresenter:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("presentationArea", "get_presentationArea", None, 0, 1, 0, 0, 0, 0, 1),
        ("expectedImprovement", "get_expectedImprovement", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("updateInkTrailStartPoint", "fn_updateInkTrailStartPoint", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_presentationArea(self):
        val = self._attr.get('presentationArea')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_delegated_ink_trail_presenter.py -> DelegatedInkTrailPresenter.presentationArea -> get attr')

    def get_expectedImprovement(self):
        val = self._attr.get('expectedImprovement')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_delegated_ink_trail_presenter.py -> DelegatedInkTrailPresenter.expectedImprovement -> get attr')

    def fn_updateInkTrailStartPoint(self, *args):
        logger.debug(f'patch -> v8_delegated_ink_trail_presenter.py -> DelegatedInkTrailPresenter.updateInkTrailStartPoint{tuple(args)} -> method')
