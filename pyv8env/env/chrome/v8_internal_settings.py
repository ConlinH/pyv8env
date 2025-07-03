from .flags import *
from .v8_internal_settings_generated import InternalSettingsGenerated


@construct_000001
class InternalSettings(InternalSettingsGenerated):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(InternalSettings, self).__init__(*args, **kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setAutoplayPolicy", "fn_setAutoplayPolicy", 1, 0, 1, 0, 0, 0, 0),
        ("setAvailableHoverTypes", "fn_setAvailableHoverTypes", 1, 0, 1, 0, 0, 0, 0),
        ("setAvailablePointerTypes", "fn_setAvailablePointerTypes", 1, 0, 1, 0, 0, 0, 0),
        ("setCursiveFontFamily", "fn_setCursiveFontFamily", 2, 0, 1, 0, 0, 0, 0),
        ("setDisplayModeOverride", "fn_setDisplayModeOverride", 1, 0, 1, 0, 0, 0, 0),
        ("setEditingBehavior", "fn_setEditingBehavior", 1, 0, 1, 0, 0, 0, 0),
        ("setFantasyFontFamily", "fn_setFantasyFontFamily", 2, 0, 1, 0, 0, 0, 0),
        ("setFixedFontFamily", "fn_setFixedFontFamily", 2, 0, 1, 0, 0, 0, 0),
        ("setImageAnimationPolicy", "fn_setImageAnimationPolicy", 1, 0, 1, 0, 0, 0, 0),
        ("setMathFontFamily", "fn_setMathFontFamily", 2, 0, 1, 0, 0, 0, 0),
        ("setPreferCompositingToLCDTextEnabled", "fn_setPreferCompositingToLCDTextEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setPrimaryHoverType", "fn_setPrimaryHoverType", 1, 0, 1, 0, 0, 0, 0),
        ("setPrimaryPointerType", "fn_setPrimaryPointerType", 1, 0, 1, 0, 0, 0, 0),
        ("setSansSerifFontFamily", "fn_setSansSerifFontFamily", 2, 0, 1, 0, 0, 0, 0),
        ("setSerifFontFamily", "fn_setSerifFontFamily", 2, 0, 1, 0, 0, 0, 0),
        ("setStandardFontFamily", "fn_setStandardFontFamily", 2, 0, 1, 0, 0, 0, 0),
        ("setTextAutosizingWindowSizeOverride", "fn_setTextAutosizingWindowSizeOverride", 2, 0, 1, 0, 0, 0, 0),
        ("setTextTrackKindUserPreference", "fn_setTextTrackKindUserPreference", 1, 0, 1, 0, 0, 0, 0),
        ("setViewportStyle", "fn_setViewportStyle", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_setAutoplayPolicy(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setAutoplayPolicy{tuple(args)} -> method')

    def fn_setAvailableHoverTypes(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setAvailableHoverTypes{tuple(args)} -> method')

    def fn_setAvailablePointerTypes(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setAvailablePointerTypes{tuple(args)} -> method')

    def fn_setCursiveFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setCursiveFontFamily{tuple(args)} -> method')

    def fn_setDisplayModeOverride(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setDisplayModeOverride{tuple(args)} -> method')

    def fn_setEditingBehavior(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setEditingBehavior{tuple(args)} -> method')

    def fn_setFantasyFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setFantasyFontFamily{tuple(args)} -> method')

    def fn_setFixedFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setFixedFontFamily{tuple(args)} -> method')

    def fn_setImageAnimationPolicy(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setImageAnimationPolicy{tuple(args)} -> method')

    def fn_setMathFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setMathFontFamily{tuple(args)} -> method')

    def fn_setPreferCompositingToLCDTextEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setPreferCompositingToLCDTextEnabled{tuple(args)} -> method')

    def fn_setPrimaryHoverType(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setPrimaryHoverType{tuple(args)} -> method')

    def fn_setPrimaryPointerType(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setPrimaryPointerType{tuple(args)} -> method')

    def fn_setSansSerifFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setSansSerifFontFamily{tuple(args)} -> method')

    def fn_setSerifFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setSerifFontFamily{tuple(args)} -> method')

    def fn_setStandardFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setStandardFontFamily{tuple(args)} -> method')

    def fn_setTextAutosizingWindowSizeOverride(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setTextAutosizingWindowSizeOverride{tuple(args)} -> method')

    def fn_setTextTrackKindUserPreference(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setTextTrackKindUserPreference{tuple(args)} -> method')

    def fn_setViewportStyle(self, *args):
        logger.debug(f'patch -> v8_internal_settings.py -> InternalSettings.setViewportStyle{tuple(args)} -> method')
