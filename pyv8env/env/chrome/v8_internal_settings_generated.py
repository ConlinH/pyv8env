from .flags import *


@construct_000001
class InternalSettingsGenerated:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("setAccelerated2dCanvasMSAASampleCount", "fn_setAccelerated2dCanvasMSAASampleCount", 1, 0, 1, 0, 0, 0, 0),
        ("setAcceleratedCompositingEnabled", "fn_setAcceleratedCompositingEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setAccessibilityAlwaysShowFocus", "fn_setAccessibilityAlwaysShowFocus", 1, 0, 1, 0, 0, 0, 0),
        ("setAccessibilityFontScaleFactor", "fn_setAccessibilityFontScaleFactor", 1, 0, 1, 0, 0, 0, 0),
        ("setAccessibilityFontWeightAdjustment", "fn_setAccessibilityFontWeightAdjustment", 1, 0, 1, 0, 0, 0, 0),
        ("setAccessibilityIncludeSvgGElement", "fn_setAccessibilityIncludeSvgGElement", 1, 0, 1, 0, 0, 0, 0),
        ("setAccessibilityPasswordValuesEnabled", "fn_setAccessibilityPasswordValuesEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setAccessibilityTextSizeContrastFactor", "fn_setAccessibilityTextSizeContrastFactor", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowCustomScrollbarInMainFrame", "fn_setAllowCustomScrollbarInMainFrame", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowFileAccessFromFileURLs", "fn_setAllowFileAccessFromFileURLs", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowGeolocationOnInsecureOrigins", "fn_setAllowGeolocationOnInsecureOrigins", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowNonEmptyNavigatorPlugins", "fn_setAllowNonEmptyNavigatorPlugins", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowRunningOfInsecureContent", "fn_setAllowRunningOfInsecureContent", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowScriptsToCloseWindows", "fn_setAllowScriptsToCloseWindows", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowUniversalAccessFromFileURLs", "fn_setAllowUniversalAccessFromFileURLs", 1, 0, 1, 0, 0, 0, 0),
        ("setAlwaysShowContextMenuOnTouch", "fn_setAlwaysShowContextMenuOnTouch", 1, 0, 1, 0, 0, 0, 0),
        ("setAntialiased2dCanvasEnabled", "fn_setAntialiased2dCanvasEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setAntialiasedClips2dCanvasEnabled", "fn_setAntialiasedClips2dCanvasEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setAriaModalPrunesAXTree", "fn_setAriaModalPrunesAXTree", 1, 0, 1, 0, 0, 0, 0),
        ("setAvailableHoverTypes", "fn_setAvailableHoverTypes", 1, 0, 1, 0, 0, 0, 0),
        ("setAvailablePointerTypes", "fn_setAvailablePointerTypes", 1, 0, 1, 0, 0, 0, 0),
        ("setBarrelButtonForDragEnabled", "fn_setBarrelButtonForDragEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setBypassCSP", "fn_setBypassCSP", 1, 0, 1, 0, 0, 0, 0),
        ("setCaretBrowsingEnabled", "fn_setCaretBrowsingEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setCookieEnabled", "fn_setCookieEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setDNSPrefetchingEnabled", "fn_setDNSPrefetchingEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setDOMPasteAllowed", "fn_setDOMPasteAllowed", 1, 0, 1, 0, 0, 0, 0),
        ("setDefaultFixedFontSize", "fn_setDefaultFixedFontSize", 1, 0, 1, 0, 0, 0, 0),
        ("setDefaultFontSize", "fn_setDefaultFontSize", 1, 0, 1, 0, 0, 0, 0),
        ("setDefaultTextEncodingName", "fn_setDefaultTextEncodingName", 1, 0, 1, 0, 0, 0, 0),
        ("setDefaultVideoPosterURL", "fn_setDefaultVideoPosterURL", 1, 0, 1, 0, 0, 0, 0),
        ("setDeviceScaleAdjustment", "fn_setDeviceScaleAdjustment", 1, 0, 1, 0, 0, 0, 0),
        ("setDisableReadingFromCanvas", "fn_setDisableReadingFromCanvas", 1, 0, 1, 0, 0, 0, 0),
        ("setDisallowFetchForDocWrittenScriptsInMainFrame", "fn_setDisallowFetchForDocWrittenScriptsInMainFrame", 1, 0, 1, 0, 0, 0, 0),
        ("setDisallowFetchForDocWrittenScriptsInMainFrameIfEffectively2G", "fn_setDisallowFetchForDocWrittenScriptsInMainFrameIfEffectively2G", 1, 0, 1, 0, 0, 0, 0),
        ("setDisallowFetchForDocWrittenScriptsInMainFrameOnSlowConnections", "fn_setDisallowFetchForDocWrittenScriptsInMainFrameOnSlowConnections", 1, 0, 1, 0, 0, 0, 0),
        ("setDoHtmlPreloadScanning", "fn_setDoHtmlPreloadScanning", 1, 0, 1, 0, 0, 0, 0),
        ("setDoNotUpdateSelectionOnMutatingSelectionRange", "fn_setDoNotUpdateSelectionOnMutatingSelectionRange", 1, 0, 1, 0, 0, 0, 0),
        ("setDontSendKeyEventsToJavascript", "fn_setDontSendKeyEventsToJavascript", 1, 0, 1, 0, 0, 0, 0),
        ("setDownloadableBinaryFontsEnabled", "fn_setDownloadableBinaryFontsEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setEmbeddedMediaExperienceEnabled", "fn_setEmbeddedMediaExperienceEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setForceAndroidOverlayScrollbar", "fn_setForceAndroidOverlayScrollbar", 1, 0, 1, 0, 0, 0, 0),
        ("setForceDarkModeEnabled", "fn_setForceDarkModeEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setForceMainWorldInitialization", "fn_setForceMainWorldInitialization", 1, 0, 1, 0, 0, 0, 0),
        ("setForceTouchEventFeatureDetectionForInspector", "fn_setForceTouchEventFeatureDetectionForInspector", 1, 0, 1, 0, 0, 0, 0),
        ("setForceZeroLayoutHeight", "fn_setForceZeroLayoutHeight", 1, 0, 1, 0, 0, 0, 0),
        ("setFullscreenSupported", "fn_setFullscreenSupported", 1, 0, 1, 0, 0, 0, 0),
        ("setHideDownloadUI", "fn_setHideDownloadUI", 1, 0, 1, 0, 0, 0, 0),
        ("setHideScrollbars", "fn_setHideScrollbars", 1, 0, 1, 0, 0, 0, 0),
        ("setHighlightAds", "fn_setHighlightAds", 1, 0, 1, 0, 0, 0, 0),
        ("setHyperlinkAuditingEnabled", "fn_setHyperlinkAuditingEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setIgnoreMainFrameOverflowHiddenQuirk", "fn_setIgnoreMainFrameOverflowHiddenQuirk", 1, 0, 1, 0, 0, 0, 0),
        ("setImagesEnabled", "fn_setImagesEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setImmersiveModeEnabled", "fn_setImmersiveModeEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setInForcedColors", "fn_setInForcedColors", 1, 0, 1, 0, 0, 0, 0),
        ("setInvertedColors", "fn_setInvertedColors", 1, 0, 1, 0, 0, 0, 0),
        ("setJavaScriptCanAccessClipboard", "fn_setJavaScriptCanAccessClipboard", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadEnabled", "fn_setLazyLoadEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingFrameMarginPx2G", "fn_setLazyLoadingFrameMarginPx2G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingFrameMarginPx3G", "fn_setLazyLoadingFrameMarginPx3G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingFrameMarginPx4G", "fn_setLazyLoadingFrameMarginPx4G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingFrameMarginPxOffline", "fn_setLazyLoadingFrameMarginPxOffline", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingFrameMarginPxSlow2G", "fn_setLazyLoadingFrameMarginPxSlow2G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingFrameMarginPxUnknown", "fn_setLazyLoadingFrameMarginPxUnknown", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingImageMarginPx2G", "fn_setLazyLoadingImageMarginPx2G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingImageMarginPx3G", "fn_setLazyLoadingImageMarginPx3G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingImageMarginPx4G", "fn_setLazyLoadingImageMarginPx4G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingImageMarginPxOffline", "fn_setLazyLoadingImageMarginPxOffline", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingImageMarginPxSlow2G", "fn_setLazyLoadingImageMarginPxSlow2G", 1, 0, 1, 0, 0, 0, 0),
        ("setLazyLoadingImageMarginPxUnknown", "fn_setLazyLoadingImageMarginPxUnknown", 1, 0, 1, 0, 0, 0, 0),
        ("setLoadWithOverviewMode", "fn_setLoadWithOverviewMode", 1, 0, 1, 0, 0, 0, 0),
        ("setLoadsImagesAutomatically", "fn_setLoadsImagesAutomatically", 1, 0, 1, 0, 0, 0, 0),
        ("setLocalStorageEnabled", "fn_setLocalStorageEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setLogDnsPrefetchAndPreconnect", "fn_setLogDnsPrefetchAndPreconnect", 1, 0, 1, 0, 0, 0, 0),
        ("setLogPreload", "fn_setLogPreload", 1, 0, 1, 0, 0, 0, 0),
        ("setMainFrameClipsContent", "fn_setMainFrameClipsContent", 1, 0, 1, 0, 0, 0, 0),
        ("setMainFrameResizesAreOrientationChanges", "fn_setMainFrameResizesAreOrientationChanges", 1, 0, 1, 0, 0, 0, 0),
        ("setMaxTouchPoints", "fn_setMaxTouchPoints", 1, 0, 1, 0, 0, 0, 0),
        ("setMediaControlsEnabled", "fn_setMediaControlsEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setMediaTypeOverride", "fn_setMediaTypeOverride", 1, 0, 1, 0, 0, 0, 0),
        ("setMinimumFontSize", "fn_setMinimumFontSize", 1, 0, 1, 0, 0, 0, 0),
        ("setMinimumLogicalFontSize", "fn_setMinimumLogicalFontSize", 1, 0, 1, 0, 0, 0, 0),
        ("setMockGestureTapHighlightsEnabled", "fn_setMockGestureTapHighlightsEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setModalContextMenu", "fn_setModalContextMenu", 1, 0, 1, 0, 0, 0, 0),
        ("setMultiTargetTapNotificationEnabled", "fn_setMultiTargetTapNotificationEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setNavigateOnDragDrop", "fn_setNavigateOnDragDrop", 1, 0, 1, 0, 0, 0, 0),
        ("setNavigatorPlatformOverride", "fn_setNavigatorPlatformOverride", 1, 0, 1, 0, 0, 0, 0),
        ("setNetworkQuietTimeout", "fn_setNetworkQuietTimeout", 1, 0, 1, 0, 0, 0, 0),
        ("setPasswordEchoDurationInSeconds", "fn_setPasswordEchoDurationInSeconds", 1, 0, 1, 0, 0, 0, 0),
        ("setPasswordEchoEnabled", "fn_setPasswordEchoEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setPictureInPictureEnabled", "fn_setPictureInPictureEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setPlaceRTLScrollbarsOnLeftSideInMainFrame", "fn_setPlaceRTLScrollbarsOnLeftSideInMainFrame", 1, 0, 1, 0, 0, 0, 0),
        ("setPluginsEnabled", "fn_setPluginsEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setPreferHiddenVolumeControls", "fn_setPreferHiddenVolumeControls", 1, 0, 1, 0, 0, 0, 0),
        ("setPrefersDefaultScrollbarStyles", "fn_setPrefersDefaultScrollbarStyles", 1, 0, 1, 0, 0, 0, 0),
        ("setPrefersReducedMotion", "fn_setPrefersReducedMotion", 1, 0, 1, 0, 0, 0, 0),
        ("setPrefersReducedTransparency", "fn_setPrefersReducedTransparency", 1, 0, 1, 0, 0, 0, 0),
        ("setPresentationReceiver", "fn_setPresentationReceiver", 1, 0, 1, 0, 0, 0, 0),
        ("setPresentationRequiresUserGesture", "fn_setPresentationRequiresUserGesture", 1, 0, 1, 0, 0, 0, 0),
        ("setReportScreenSizeInPhysicalPixelsQuirk", "fn_setReportScreenSizeInPhysicalPixelsQuirk", 1, 0, 1, 0, 0, 0, 0),
        ("setRequireTransientActivationAndAuthorizationForSubAppsAPI", "fn_setRequireTransientActivationAndAuthorizationForSubAppsAPI", 1, 0, 1, 0, 0, 0, 0),
        ("setRequireTransientActivationForGetDisplayMedia", "fn_setRequireTransientActivationForGetDisplayMedia", 1, 0, 1, 0, 0, 0, 0),
        ("setRequireTransientActivationForHtmlFullscreen", "fn_setRequireTransientActivationForHtmlFullscreen", 1, 0, 1, 0, 0, 0, 0),
        ("setRequireTransientActivationForShowFileOrDirectoryPicker", "fn_setRequireTransientActivationForShowFileOrDirectoryPicker", 1, 0, 1, 0, 0, 0, 0),
        ("setResizable", "fn_setResizable", 1, 0, 1, 0, 0, 0, 0),
        ("setRubberBandingOnCompositorThread", "fn_setRubberBandingOnCompositorThread", 1, 0, 1, 0, 0, 0, 0),
        ("setScriptEnabled", "fn_setScriptEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setScrollAnimatorEnabled", "fn_setScrollAnimatorEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setSelectTrailingWhitespaceEnabled", "fn_setSelectTrailingWhitespaceEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setSelectionClipboardBufferAvailable", "fn_setSelectionClipboardBufferAvailable", 1, 0, 1, 0, 0, 0, 0),
        ("setSelectionIncludesAltImageText", "fn_setSelectionIncludesAltImageText", 1, 0, 1, 0, 0, 0, 0),
        ("setShouldClearDocumentBackground", "fn_setShouldClearDocumentBackground", 1, 0, 1, 0, 0, 0, 0),
        ("setShouldPrintBackgrounds", "fn_setShouldPrintBackgrounds", 1, 0, 1, 0, 0, 0, 0),
        ("setShouldProtectAgainstIpcFlooding", "fn_setShouldProtectAgainstIpcFlooding", 1, 0, 1, 0, 0, 0, 0),
        ("setShouldReuseGlobalForUnownedMainFrame", "fn_setShouldReuseGlobalForUnownedMainFrame", 1, 0, 1, 0, 0, 0, 0),
        ("setShowContextMenuOnMouseUp", "fn_setShowContextMenuOnMouseUp", 1, 0, 1, 0, 0, 0, 0),
        ("setShrinksViewportContentToFit", "fn_setShrinksViewportContentToFit", 1, 0, 1, 0, 0, 0, 0),
        ("setSmartInsertDeleteEnabled", "fn_setSmartInsertDeleteEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setSmoothScrollForFindEnabled", "fn_setSmoothScrollForFindEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setSpatialNavigationEnabled", "fn_setSpatialNavigationEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setSpellCheckEnabledByDefault", "fn_setSpellCheckEnabledByDefault", 1, 0, 1, 0, 0, 0, 0),
        ("setStrictMixedContentChecking", "fn_setStrictMixedContentChecking", 1, 0, 1, 0, 0, 0, 0),
        ("setStrictMixedContentCheckingForPlugin", "fn_setStrictMixedContentCheckingForPlugin", 1, 0, 1, 0, 0, 0, 0),
        ("setStrictPowerfulFeatureRestrictions", "fn_setStrictPowerfulFeatureRestrictions", 1, 0, 1, 0, 0, 0, 0),
        ("setStrictlyBlockBlockableMixedContent", "fn_setStrictlyBlockBlockableMixedContent", 1, 0, 1, 0, 0, 0, 0),
        ("setSupportsMultipleWindows", "fn_setSupportsMultipleWindows", 1, 0, 1, 0, 0, 0, 0),
        ("setSyncXHRInDocumentsEnabled", "fn_setSyncXHRInDocumentsEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setTargetBlankImpliesNoOpenerEnabledWillBeRemoved", "fn_setTargetBlankImpliesNoOpenerEnabledWillBeRemoved", 1, 0, 1, 0, 0, 0, 0),
        ("setTextAreasAreResizable", "fn_setTextAreasAreResizable", 1, 0, 1, 0, 0, 0, 0),
        ("setTextAutosizingEnabled", "fn_setTextAutosizingEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackBackgroundColor", "fn_setTextTrackBackgroundColor", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackFontFamily", "fn_setTextTrackFontFamily", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackFontStyle", "fn_setTextTrackFontStyle", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackFontVariant", "fn_setTextTrackFontVariant", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackMarginPercentage", "fn_setTextTrackMarginPercentage", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackTextColor", "fn_setTextTrackTextColor", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackTextShadow", "fn_setTextTrackTextShadow", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackTextSize", "fn_setTextTrackTextSize", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackWindowColor", "fn_setTextTrackWindowColor", 1, 0, 1, 0, 0, 0, 0),
        ("setTextTrackWindowRadius", "fn_setTextTrackWindowRadius", 1, 0, 1, 0, 0, 0, 0),
        ("setTouchDragDropEnabled", "fn_setTouchDragDropEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setTouchDragEndContextMenu", "fn_setTouchDragEndContextMenu", 1, 0, 1, 0, 0, 0, 0),
        ("setTouchEditingEnabled", "fn_setTouchEditingEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setUseAXMenuList", "fn_setUseAXMenuList", 1, 0, 1, 0, 0, 0, 0),
        ("setUseWideViewport", "fn_setUseWideViewport", 1, 0, 1, 0, 0, 0, 0),
        ("setValidationMessageTimerMagnification", "fn_setValidationMessageTimerMagnification", 1, 0, 1, 0, 0, 0, 0),
        ("setViewportEnabled", "fn_setViewportEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setViewportMetaEnabled", "fn_setViewportMetaEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setViewportMetaMergeContentQuirk", "fn_setViewportMetaMergeContentQuirk", 1, 0, 1, 0, 0, 0, 0),
        ("setViewportMetaZeroValuesQuirk", "fn_setViewportMetaZeroValuesQuirk", 1, 0, 1, 0, 0, 0, 0),
        ("setWebAppScope", "fn_setWebAppScope", 1, 0, 1, 0, 0, 0, 0),
        ("setWebGL1Enabled", "fn_setWebGL1Enabled", 1, 0, 1, 0, 0, 0, 0),
        ("setWebGL2Enabled", "fn_setWebGL2Enabled", 1, 0, 1, 0, 0, 0, 0),
        ("setWebGLErrorsToConsoleEnabled", "fn_setWebGLErrorsToConsoleEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setWebSecurityEnabled", "fn_setWebSecurityEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setWebXRImmersiveArAllowed", "fn_setWebXRImmersiveArAllowed", 1, 0, 1, 0, 0, 0, 0),
        ("setWideViewportQuirkEnabled", "fn_setWideViewportQuirkEnabled", 1, 0, 1, 0, 0, 0, 0),

    )

    def fn_setAccelerated2dCanvasMSAASampleCount(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAccelerated2dCanvasMSAASampleCount{tuple(args)} -> method')

    def fn_setAcceleratedCompositingEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAcceleratedCompositingEnabled{tuple(args)} -> method')

    def fn_setAccessibilityAlwaysShowFocus(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAccessibilityAlwaysShowFocus{tuple(args)} -> method')

    def fn_setAccessibilityFontScaleFactor(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAccessibilityFontScaleFactor{tuple(args)} -> method')

    def fn_setAccessibilityFontWeightAdjustment(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAccessibilityFontWeightAdjustment{tuple(args)} -> method')

    def fn_setAccessibilityIncludeSvgGElement(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAccessibilityIncludeSvgGElement{tuple(args)} -> method')

    def fn_setAccessibilityPasswordValuesEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAccessibilityPasswordValuesEnabled{tuple(args)} -> method')

    def fn_setAccessibilityTextSizeContrastFactor(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAccessibilityTextSizeContrastFactor{tuple(args)} -> method')

    def fn_setAllowCustomScrollbarInMainFrame(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAllowCustomScrollbarInMainFrame{tuple(args)} -> method')

    def fn_setAllowFileAccessFromFileURLs(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAllowFileAccessFromFileURLs{tuple(args)} -> method')

    def fn_setAllowGeolocationOnInsecureOrigins(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAllowGeolocationOnInsecureOrigins{tuple(args)} -> method')

    def fn_setAllowNonEmptyNavigatorPlugins(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAllowNonEmptyNavigatorPlugins{tuple(args)} -> method')

    def fn_setAllowRunningOfInsecureContent(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAllowRunningOfInsecureContent{tuple(args)} -> method')

    def fn_setAllowScriptsToCloseWindows(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAllowScriptsToCloseWindows{tuple(args)} -> method')

    def fn_setAllowUniversalAccessFromFileURLs(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAllowUniversalAccessFromFileURLs{tuple(args)} -> method')

    def fn_setAlwaysShowContextMenuOnTouch(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAlwaysShowContextMenuOnTouch{tuple(args)} -> method')

    def fn_setAntialiased2dCanvasEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAntialiased2dCanvasEnabled{tuple(args)} -> method')

    def fn_setAntialiasedClips2dCanvasEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAntialiasedClips2dCanvasEnabled{tuple(args)} -> method')

    def fn_setAriaModalPrunesAXTree(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAriaModalPrunesAXTree{tuple(args)} -> method')

    def fn_setAvailableHoverTypes(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAvailableHoverTypes{tuple(args)} -> method')

    def fn_setAvailablePointerTypes(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setAvailablePointerTypes{tuple(args)} -> method')

    def fn_setBarrelButtonForDragEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setBarrelButtonForDragEnabled{tuple(args)} -> method')

    def fn_setBypassCSP(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setBypassCSP{tuple(args)} -> method')

    def fn_setCaretBrowsingEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setCaretBrowsingEnabled{tuple(args)} -> method')

    def fn_setCookieEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setCookieEnabled{tuple(args)} -> method')

    def fn_setDNSPrefetchingEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDNSPrefetchingEnabled{tuple(args)} -> method')

    def fn_setDOMPasteAllowed(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDOMPasteAllowed{tuple(args)} -> method')

    def fn_setDefaultFixedFontSize(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDefaultFixedFontSize{tuple(args)} -> method')

    def fn_setDefaultFontSize(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDefaultFontSize{tuple(args)} -> method')

    def fn_setDefaultTextEncodingName(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDefaultTextEncodingName{tuple(args)} -> method')

    def fn_setDefaultVideoPosterURL(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDefaultVideoPosterURL{tuple(args)} -> method')

    def fn_setDeviceScaleAdjustment(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDeviceScaleAdjustment{tuple(args)} -> method')

    def fn_setDisableReadingFromCanvas(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDisableReadingFromCanvas{tuple(args)} -> method')

    def fn_setDisallowFetchForDocWrittenScriptsInMainFrame(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDisallowFetchForDocWrittenScriptsInMainFrame{tuple(args)} -> method')

    def fn_setDisallowFetchForDocWrittenScriptsInMainFrameIfEffectively2G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDisallowFetchForDocWrittenScriptsInMainFrameIfEffectively2G{tuple(args)} -> method')

    def fn_setDisallowFetchForDocWrittenScriptsInMainFrameOnSlowConnections(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDisallowFetchForDocWrittenScriptsInMainFrameOnSlowConnections{tuple(args)} -> method')

    def fn_setDoHtmlPreloadScanning(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDoHtmlPreloadScanning{tuple(args)} -> method')

    def fn_setDoNotUpdateSelectionOnMutatingSelectionRange(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDoNotUpdateSelectionOnMutatingSelectionRange{tuple(args)} -> method')

    def fn_setDontSendKeyEventsToJavascript(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDontSendKeyEventsToJavascript{tuple(args)} -> method')

    def fn_setDownloadableBinaryFontsEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setDownloadableBinaryFontsEnabled{tuple(args)} -> method')

    def fn_setEmbeddedMediaExperienceEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setEmbeddedMediaExperienceEnabled{tuple(args)} -> method')

    def fn_setForceAndroidOverlayScrollbar(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setForceAndroidOverlayScrollbar{tuple(args)} -> method')

    def fn_setForceDarkModeEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setForceDarkModeEnabled{tuple(args)} -> method')

    def fn_setForceMainWorldInitialization(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setForceMainWorldInitialization{tuple(args)} -> method')

    def fn_setForceTouchEventFeatureDetectionForInspector(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setForceTouchEventFeatureDetectionForInspector{tuple(args)} -> method')

    def fn_setForceZeroLayoutHeight(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setForceZeroLayoutHeight{tuple(args)} -> method')

    def fn_setFullscreenSupported(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setFullscreenSupported{tuple(args)} -> method')

    def fn_setHideDownloadUI(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setHideDownloadUI{tuple(args)} -> method')

    def fn_setHideScrollbars(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setHideScrollbars{tuple(args)} -> method')

    def fn_setHighlightAds(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setHighlightAds{tuple(args)} -> method')

    def fn_setHyperlinkAuditingEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setHyperlinkAuditingEnabled{tuple(args)} -> method')

    def fn_setIgnoreMainFrameOverflowHiddenQuirk(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setIgnoreMainFrameOverflowHiddenQuirk{tuple(args)} -> method')

    def fn_setImagesEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setImagesEnabled{tuple(args)} -> method')

    def fn_setImmersiveModeEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setImmersiveModeEnabled{tuple(args)} -> method')

    def fn_setInForcedColors(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setInForcedColors{tuple(args)} -> method')

    def fn_setInvertedColors(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setInvertedColors{tuple(args)} -> method')

    def fn_setJavaScriptCanAccessClipboard(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setJavaScriptCanAccessClipboard{tuple(args)} -> method')

    def fn_setLazyLoadEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadEnabled{tuple(args)} -> method')

    def fn_setLazyLoadingFrameMarginPx2G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingFrameMarginPx2G{tuple(args)} -> method')

    def fn_setLazyLoadingFrameMarginPx3G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingFrameMarginPx3G{tuple(args)} -> method')

    def fn_setLazyLoadingFrameMarginPx4G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingFrameMarginPx4G{tuple(args)} -> method')

    def fn_setLazyLoadingFrameMarginPxOffline(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingFrameMarginPxOffline{tuple(args)} -> method')

    def fn_setLazyLoadingFrameMarginPxSlow2G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingFrameMarginPxSlow2G{tuple(args)} -> method')

    def fn_setLazyLoadingFrameMarginPxUnknown(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingFrameMarginPxUnknown{tuple(args)} -> method')

    def fn_setLazyLoadingImageMarginPx2G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingImageMarginPx2G{tuple(args)} -> method')

    def fn_setLazyLoadingImageMarginPx3G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingImageMarginPx3G{tuple(args)} -> method')

    def fn_setLazyLoadingImageMarginPx4G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingImageMarginPx4G{tuple(args)} -> method')

    def fn_setLazyLoadingImageMarginPxOffline(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingImageMarginPxOffline{tuple(args)} -> method')

    def fn_setLazyLoadingImageMarginPxSlow2G(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingImageMarginPxSlow2G{tuple(args)} -> method')

    def fn_setLazyLoadingImageMarginPxUnknown(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLazyLoadingImageMarginPxUnknown{tuple(args)} -> method')

    def fn_setLoadWithOverviewMode(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLoadWithOverviewMode{tuple(args)} -> method')

    def fn_setLoadsImagesAutomatically(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLoadsImagesAutomatically{tuple(args)} -> method')

    def fn_setLocalStorageEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLocalStorageEnabled{tuple(args)} -> method')

    def fn_setLogDnsPrefetchAndPreconnect(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLogDnsPrefetchAndPreconnect{tuple(args)} -> method')

    def fn_setLogPreload(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setLogPreload{tuple(args)} -> method')

    def fn_setMainFrameClipsContent(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMainFrameClipsContent{tuple(args)} -> method')

    def fn_setMainFrameResizesAreOrientationChanges(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMainFrameResizesAreOrientationChanges{tuple(args)} -> method')

    def fn_setMaxTouchPoints(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMaxTouchPoints{tuple(args)} -> method')

    def fn_setMediaControlsEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMediaControlsEnabled{tuple(args)} -> method')

    def fn_setMediaTypeOverride(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMediaTypeOverride{tuple(args)} -> method')

    def fn_setMinimumFontSize(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMinimumFontSize{tuple(args)} -> method')

    def fn_setMinimumLogicalFontSize(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMinimumLogicalFontSize{tuple(args)} -> method')

    def fn_setMockGestureTapHighlightsEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMockGestureTapHighlightsEnabled{tuple(args)} -> method')

    def fn_setModalContextMenu(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setModalContextMenu{tuple(args)} -> method')

    def fn_setMultiTargetTapNotificationEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setMultiTargetTapNotificationEnabled{tuple(args)} -> method')

    def fn_setNavigateOnDragDrop(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setNavigateOnDragDrop{tuple(args)} -> method')

    def fn_setNavigatorPlatformOverride(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setNavigatorPlatformOverride{tuple(args)} -> method')

    def fn_setNetworkQuietTimeout(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setNetworkQuietTimeout{tuple(args)} -> method')

    def fn_setPasswordEchoDurationInSeconds(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPasswordEchoDurationInSeconds{tuple(args)} -> method')

    def fn_setPasswordEchoEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPasswordEchoEnabled{tuple(args)} -> method')

    def fn_setPictureInPictureEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPictureInPictureEnabled{tuple(args)} -> method')

    def fn_setPlaceRTLScrollbarsOnLeftSideInMainFrame(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPlaceRTLScrollbarsOnLeftSideInMainFrame{tuple(args)} -> method')

    def fn_setPluginsEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPluginsEnabled{tuple(args)} -> method')

    def fn_setPreferHiddenVolumeControls(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPreferHiddenVolumeControls{tuple(args)} -> method')

    def fn_setPrefersDefaultScrollbarStyles(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPrefersDefaultScrollbarStyles{tuple(args)} -> method')

    def fn_setPrefersReducedMotion(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPrefersReducedMotion{tuple(args)} -> method')

    def fn_setPrefersReducedTransparency(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPrefersReducedTransparency{tuple(args)} -> method')

    def fn_setPresentationReceiver(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPresentationReceiver{tuple(args)} -> method')

    def fn_setPresentationRequiresUserGesture(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setPresentationRequiresUserGesture{tuple(args)} -> method')

    def fn_setReportScreenSizeInPhysicalPixelsQuirk(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setReportScreenSizeInPhysicalPixelsQuirk{tuple(args)} -> method')

    def fn_setRequireTransientActivationAndAuthorizationForSubAppsAPI(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setRequireTransientActivationAndAuthorizationForSubAppsAPI{tuple(args)} -> method')

    def fn_setRequireTransientActivationForGetDisplayMedia(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setRequireTransientActivationForGetDisplayMedia{tuple(args)} -> method')

    def fn_setRequireTransientActivationForHtmlFullscreen(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setRequireTransientActivationForHtmlFullscreen{tuple(args)} -> method')

    def fn_setRequireTransientActivationForShowFileOrDirectoryPicker(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setRequireTransientActivationForShowFileOrDirectoryPicker{tuple(args)} -> method')

    def fn_setResizable(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setResizable{tuple(args)} -> method')

    def fn_setRubberBandingOnCompositorThread(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setRubberBandingOnCompositorThread{tuple(args)} -> method')

    def fn_setScriptEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setScriptEnabled{tuple(args)} -> method')

    def fn_setScrollAnimatorEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setScrollAnimatorEnabled{tuple(args)} -> method')

    def fn_setSelectTrailingWhitespaceEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSelectTrailingWhitespaceEnabled{tuple(args)} -> method')

    def fn_setSelectionClipboardBufferAvailable(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSelectionClipboardBufferAvailable{tuple(args)} -> method')

    def fn_setSelectionIncludesAltImageText(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSelectionIncludesAltImageText{tuple(args)} -> method')

    def fn_setShouldClearDocumentBackground(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setShouldClearDocumentBackground{tuple(args)} -> method')

    def fn_setShouldPrintBackgrounds(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setShouldPrintBackgrounds{tuple(args)} -> method')

    def fn_setShouldProtectAgainstIpcFlooding(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setShouldProtectAgainstIpcFlooding{tuple(args)} -> method')

    def fn_setShouldReuseGlobalForUnownedMainFrame(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setShouldReuseGlobalForUnownedMainFrame{tuple(args)} -> method')

    def fn_setShowContextMenuOnMouseUp(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setShowContextMenuOnMouseUp{tuple(args)} -> method')

    def fn_setShrinksViewportContentToFit(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setShrinksViewportContentToFit{tuple(args)} -> method')

    def fn_setSmartInsertDeleteEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSmartInsertDeleteEnabled{tuple(args)} -> method')

    def fn_setSmoothScrollForFindEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSmoothScrollForFindEnabled{tuple(args)} -> method')

    def fn_setSpatialNavigationEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSpatialNavigationEnabled{tuple(args)} -> method')

    def fn_setSpellCheckEnabledByDefault(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSpellCheckEnabledByDefault{tuple(args)} -> method')

    def fn_setStrictMixedContentChecking(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setStrictMixedContentChecking{tuple(args)} -> method')

    def fn_setStrictMixedContentCheckingForPlugin(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setStrictMixedContentCheckingForPlugin{tuple(args)} -> method')

    def fn_setStrictPowerfulFeatureRestrictions(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setStrictPowerfulFeatureRestrictions{tuple(args)} -> method')

    def fn_setStrictlyBlockBlockableMixedContent(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setStrictlyBlockBlockableMixedContent{tuple(args)} -> method')

    def fn_setSupportsMultipleWindows(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSupportsMultipleWindows{tuple(args)} -> method')

    def fn_setSyncXHRInDocumentsEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setSyncXHRInDocumentsEnabled{tuple(args)} -> method')

    def fn_setTargetBlankImpliesNoOpenerEnabledWillBeRemoved(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTargetBlankImpliesNoOpenerEnabledWillBeRemoved{tuple(args)} -> method')

    def fn_setTextAreasAreResizable(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextAreasAreResizable{tuple(args)} -> method')

    def fn_setTextAutosizingEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextAutosizingEnabled{tuple(args)} -> method')

    def fn_setTextTrackBackgroundColor(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackBackgroundColor{tuple(args)} -> method')

    def fn_setTextTrackFontFamily(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackFontFamily{tuple(args)} -> method')

    def fn_setTextTrackFontStyle(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackFontStyle{tuple(args)} -> method')

    def fn_setTextTrackFontVariant(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackFontVariant{tuple(args)} -> method')

    def fn_setTextTrackMarginPercentage(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackMarginPercentage{tuple(args)} -> method')

    def fn_setTextTrackTextColor(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackTextColor{tuple(args)} -> method')

    def fn_setTextTrackTextShadow(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackTextShadow{tuple(args)} -> method')

    def fn_setTextTrackTextSize(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackTextSize{tuple(args)} -> method')

    def fn_setTextTrackWindowColor(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackWindowColor{tuple(args)} -> method')

    def fn_setTextTrackWindowRadius(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTextTrackWindowRadius{tuple(args)} -> method')

    def fn_setTouchDragDropEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTouchDragDropEnabled{tuple(args)} -> method')

    def fn_setTouchDragEndContextMenu(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTouchDragEndContextMenu{tuple(args)} -> method')

    def fn_setTouchEditingEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setTouchEditingEnabled{tuple(args)} -> method')

    def fn_setUseAXMenuList(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setUseAXMenuList{tuple(args)} -> method')

    def fn_setUseWideViewport(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setUseWideViewport{tuple(args)} -> method')

    def fn_setValidationMessageTimerMagnification(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setValidationMessageTimerMagnification{tuple(args)} -> method')

    def fn_setViewportEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setViewportEnabled{tuple(args)} -> method')

    def fn_setViewportMetaEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setViewportMetaEnabled{tuple(args)} -> method')

    def fn_setViewportMetaMergeContentQuirk(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setViewportMetaMergeContentQuirk{tuple(args)} -> method')

    def fn_setViewportMetaZeroValuesQuirk(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setViewportMetaZeroValuesQuirk{tuple(args)} -> method')

    def fn_setWebAppScope(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setWebAppScope{tuple(args)} -> method')

    def fn_setWebGL1Enabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setWebGL1Enabled{tuple(args)} -> method')

    def fn_setWebGL2Enabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setWebGL2Enabled{tuple(args)} -> method')

    def fn_setWebGLErrorsToConsoleEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setWebGLErrorsToConsoleEnabled{tuple(args)} -> method')

    def fn_setWebSecurityEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setWebSecurityEnabled{tuple(args)} -> method')

    def fn_setWebXRImmersiveArAllowed(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setWebXRImmersiveArAllowed{tuple(args)} -> method')

    def fn_setWideViewportQuirkEnabled(self, *args):
        logger.debug(f'patch -> v8_internal_settings_generated.py -> InternalSettingsGenerated.setWideViewportQuirkEnabled{tuple(args)} -> method')
