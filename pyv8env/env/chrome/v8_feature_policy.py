from .flags import *


@construct_100001
class FeaturePolicy:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("allowedFeatures", "fn_allowedFeatures", 0, 0, 1, 0, 0, 0, 0),
        ("allowsFeature", "fn_allowsFeature", 1, 0, 1, 0, 0, 0, 0),
        ("features", "fn_features", 0, 0, 1, 0, 0, 0, 0),
        ("getAllowlistForFeature", "fn_getAllowlistForFeature", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_allowedFeatures(self, *args):
        logger.debug(f'patch -> v8_feature_policy.py -> FeaturePolicy.allowedFeatures{tuple(args)} -> method')

    def fn_allowsFeature(self, *args):
        logger.debug(f'patch -> v8_feature_policy.py -> FeaturePolicy.allowsFeature{tuple(args)} -> method')

    def fn_features(self, *args):
        logger.debug(f'patch -> v8_feature_policy.py -> FeaturePolicy.features{tuple(args)} -> method')

    def fn_getAllowlistForFeature(self, *args):
        logger.debug(f'patch -> v8_feature_policy.py -> FeaturePolicy.getAllowlistForFeature{tuple(args)} -> method')
