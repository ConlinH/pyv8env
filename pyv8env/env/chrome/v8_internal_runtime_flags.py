from .flags import *


@construct_000001
class InternalRuntimeFlags:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("accelerated2dCanvasEnabled", "get_accelerated2dCanvasEnabled", "set_accelerated2dCanvasEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("acceleratedSmallCanvasesEnabled", "get_acceleratedSmallCanvasesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibilityAriaVirtualContentEnabled", "get_accessibilityAriaVirtualContentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibilityExposeDisplayNoneEnabled", "get_accessibilityExposeDisplayNoneEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibilityObjectModelEnabled", "get_accessibilityObjectModelEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibilityOSLevelBoldTextEnabled", "get_accessibilityOSLevelBoldTextEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibilityPageZoomEnabled", "get_accessibilityPageZoomEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibilitySerializationSizeMetricsEnabled", "get_accessibilitySerializationSizeMetricsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("accessibilityUseAXPositionForDocumentMarkersEnabled", "get_accessibilityUseAXPositionForDocumentMarkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("addressSpaceEnabled", "get_addressSpaceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("adInterestGroupAPIEnabled", "get_adInterestGroupAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("adjustEndOfNextParagraphIfMovedParagraphIsUpdatedEnabled", "get_adjustEndOfNextParagraphIfMovedParagraphIsUpdatedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("adTaggingEnabled", "get_adTaggingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("allowContentInitiatedDataUrlNavigationsEnabled", "get_allowContentInitiatedDataUrlNavigationsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("allowJavaScriptToResetAutofillStateEnabled", "get_allowJavaScriptToResetAutofillStateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("allowURNsInIframesEnabled", "get_allowURNsInIframesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("androidDownloadableFontsMatchingEnabled", "get_androidDownloadableFontsMatchingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("animationProgressAPIEnabled", "get_animationProgressAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("animationWorkletEnabled", "get_animationWorkletEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("anonymousIframeEnabled", "get_anonymousIframeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("aomAriaRelationshipPropertiesEnabled", "get_aomAriaRelationshipPropertiesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("appTitleEnabled", "get_appTitleEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("ariaNotifyEnabled", "get_ariaNotifyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("atomicMoveAPIEnabled", "get_atomicMoveAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("attributionReportingEnabled", "get_attributionReportingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("attributionReportingCrossAppWebEnabled", "get_attributionReportingCrossAppWebEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("attributionReportingInterfaceEnabled", "get_attributionReportingInterfaceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("audioContextOnErrorEnabled", "get_audioContextOnErrorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("audioContextPlayoutStatsEnabled", "get_audioContextPlayoutStatsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("audioContextSetSinkIdEnabled", "get_audioContextSetSinkIdEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("audioOutputDevicesEnabled", "get_audioOutputDevicesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("audioVideoTracksEnabled", "get_audioVideoTracksEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("autoDarkModeEnabled", "get_autoDarkModeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("automationControlledEnabled", "get_automationControlledEnabled", "set_automationControlledEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("autoPictureInPictureVideoHeuristicsEnabled", "get_autoPictureInPictureVideoHeuristicsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("autoSizeLazyLoadedImagesEnabled", "get_autoSizeLazyLoadedImagesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("avoidCaretVisibleSelectionAdjusterEnabled", "get_avoidCaretVisibleSelectionAdjusterEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("backdropInheritOriginatingEnabled", "get_backdropInheritOriginatingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("backfaceVisibilityInteropEnabled", "get_backfaceVisibilityInteropEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("backForwardCacheEnabled", "get_backForwardCacheEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("backForwardCacheExperimentHTTPHeaderEnabled", "get_backForwardCacheExperimentHTTPHeaderEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("backForwardCacheNotRestoredReasonsEnabled", "get_backForwardCacheNotRestoredReasonsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("backForwardTransitionsEnabled", "get_backForwardTransitionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("backgroundFetchEnabled", "get_backgroundFetchEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("barcodeDetectorEnabled", "get_barcodeDetectorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("beforeunloadEventCancelByPreventDefaultEnabled", "get_beforeunloadEventCancelByPreventDefaultEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("bidiCaretAffinityEnabled", "get_bidiCaretAffinityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blinkExtensionChromeOSEnabled", "get_blinkExtensionChromeOSEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blinkExtensionChromeOSKioskEnabled", "get_blinkExtensionChromeOSKioskEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blinkExtensionDiagnosticsEnabled", "get_blinkExtensionDiagnosticsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blinkExtensionWebViewEnabled", "get_blinkExtensionWebViewEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blinkExtensionWebViewMediaIntegrityEnabled", "get_blinkExtensionWebViewMediaIntegrityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blinkLifecycleScriptForbiddenEnabled", "get_blinkLifecycleScriptForbiddenEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blinkRuntimeCallStatsEnabled", "get_blinkRuntimeCallStatsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("blockingFocusWithoutUserActivationEnabled", "get_blockingFocusWithoutUserActivationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("boundaryEventDispatchTracksNodeRemovalEnabled", "get_boundaryEventDispatchTracksNodeRemovalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("breakIteratorDataGeneratorEnabled", "get_breakIteratorDataGeneratorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("browserVerifiedUserActivationKeyboardEnabled", "get_browserVerifiedUserActivationKeyboardEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("browserVerifiedUserActivationMouseEnabled", "get_browserVerifiedUserActivationMouseEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("bufferedBytesConsumerLimitSizeEnabled", "get_bufferedBytesConsumerLimitSizeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("bypassPepcSecurityForTestingEnabled", "get_bypassPepcSecurityForTestingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cacheStorageCodeCacheHintEnabled", "get_cacheStorageCodeCacheHintEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvas2dCanvasFilterEnabled", "get_canvas2dCanvasFilterEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvas2dGPUTransferEnabled", "get_canvas2dGPUTransferEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvas2dImageChromiumEnabled", "get_canvas2dImageChromiumEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvas2dLayersEnabled", "get_canvas2dLayersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvas2dMeshEnabled", "get_canvas2dMeshEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvas2dScrollPathIntoViewEnabled", "get_canvas2dScrollPathIntoViewEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvasFloatingPointEnabled", "get_canvasFloatingPointEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvasHDREnabled", "get_canvasHDREnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvasImageSmoothingEnabled", "get_canvasImageSmoothingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("canvasUsesArcPaintOpEnabled", "get_canvasUsesArcPaintOpEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("capabilityDelegationDisplayCaptureRequestEnabled", "get_capabilityDelegationDisplayCaptureRequestEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("captureControllerEnabled", "get_captureControllerEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("capturedMouseEventsEnabled", "get_capturedMouseEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("capturedSurfaceControlEnabled", "get_capturedSurfaceControlEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("captureHandleEnabled", "get_captureHandleEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("caretPositionFromPointEnabled", "get_caretPositionFromPointEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cctNewRFMPushBehaviorEnabled", "get_cctNewRFMPushBehaviorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("checkVisibilityExtraPropertiesEnabled", "get_checkVisibilityExtraPropertiesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("clickToCapturedPointerEnabled", "get_clickToCapturedPointerEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("clipboardSvgEnabled", "get_clipboardSvgEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("clipPathRejectEmptyPathsEnabled", "get_clipPathRejectEmptyPathsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("closeWatcherEnabled", "get_closeWatcherEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("coepReflectionEnabled", "get_coepReflectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("compositeBGColorAnimationEnabled", "get_compositeBGColorAnimationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("compositeBoxShadowAnimationEnabled", "get_compositeBoxShadowAnimationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("compositeClipPathAnimationEnabled", "get_compositeClipPathAnimationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("compositedSelectionUpdateEnabled", "get_compositedSelectionUpdateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("compositionForegroundMarkersEnabled", "get_compositionForegroundMarkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("compressionDictionaryTransportEnabled", "get_compressionDictionaryTransportEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("compressionDictionaryTransportBackendEnabled", "get_compressionDictionaryTransportBackendEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("computedAccessibilityInfoEnabled", "get_computedAccessibilityInfoEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("computePressureEnabled", "get_computePressureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("concurrentViewTransitionsSPAEnabled", "get_concurrentViewTransitionsSPAEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("contactsManagerEnabled", "get_contactsManagerEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("contactsManagerExtraPropertiesEnabled", "get_contactsManagerExtraPropertiesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentIndexEnabled", "get_contentIndexEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("contextMenuEnabled", "get_contextMenuEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("continueEventTimingRecordingWhenBufferIsFullEnabled", "get_continueEventTimingRecordingWhenBufferIsFullEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cookieDeprecationFacilitatedTestingEnabled", "get_cookieDeprecationFacilitatedTestingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cooperativeSchedulingEnabled", "get_cooperativeSchedulingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("coopRestrictPropertiesEnabled", "get_coopRestrictPropertiesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("corsRFC1918Enabled", "get_corsRFC1918Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("createInputShadowTreeDuringLayoutEnabled", "get_createInputShadowTreeDuringLayoutEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("credentialManagerReportEnabled", "get_credentialManagerReportEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("crossFramePerformanceTimelineEnabled", "get_crossFramePerformanceTimelineEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssAnchorPositioningEnabled", "get_cssAnchorPositioningEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssAnchorScopeEnabled", "get_cssAnchorScopeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssAtRuleCounterStyleImageSymbolsEnabled", "get_cssAtRuleCounterStyleImageSymbolsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssAtRuleCounterStyleSpeakAsDescriptorEnabled", "get_cssAtRuleCounterStyleSpeakAsDescriptorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssBackgroundClipUnprefixEnabled", "get_cssBackgroundClipUnprefixEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssCalcSimplificationAndSerializationEnabled", "get_cssCalcSimplificationAndSerializationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssCalcSizeFunctionEnabled", "get_cssCalcSizeFunctionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssCapFontUnitsEnabled", "get_cssCapFontUnitsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssCaseSensitiveSelectorEnabled", "get_cssCaseSensitiveSelectorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssColorContrastEnabled", "get_cssColorContrastEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssColorTypedOMEnabled", "get_cssColorTypedOMEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssComputedStyleFullPseudoElementParserEnabled", "get_cssComputedStyleFullPseudoElementParserEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssContentMultiArgAltTextEnabled", "get_cssContentMultiArgAltTextEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssContentVisibilityImpliesContainIntrinsicSizeAutoEnabled", "get_cssContentVisibilityImpliesContainIntrinsicSizeAutoEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssCrossFadeEnabled", "get_cssCrossFadeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssCustomStateDeprecatedSyntaxEnabled", "get_cssCustomStateDeprecatedSyntaxEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssCustomStateNewSyntaxEnabled", "get_cssCustomStateNewSyntaxEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssDisplayModePictureInPictureEnabled", "get_cssDisplayModePictureInPictureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssDynamicRangeLimitEnabled", "get_cssDynamicRangeLimitEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssEnumeratedCustomPropertiesEnabled", "get_cssEnumeratedCustomPropertiesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssExponentialFunctionsEnabled", "get_cssExponentialFunctionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssFontSizeAdjustEnabled", "get_cssFontSizeAdjustEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssFunctionsEnabled", "get_cssFunctionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssHexAlphaColorEnabled", "get_cssHexAlphaColorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssKeyframesRuleLengthEnabled", "get_cssKeyframesRuleLengthEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssLayoutAPIEnabled", "get_cssLayoutAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssLazyParsingFastPathEnabled", "get_cssLazyParsingFastPathEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssLightDarkColorsEnabled", "get_cssLightDarkColorsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssLineClampEnabled", "get_cssLineClampEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssLogicalOverflowEnabled", "get_cssLogicalOverflowEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssMarkerNestedPseudoElementEnabled", "get_cssMarkerNestedPseudoElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssNumericFactoryCompletenessEnabled", "get_cssNumericFactoryCompletenessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssPaintAPIArgumentsEnabled", "get_cssPaintAPIArgumentsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssParserIgnoreCharsetForURLsEnabled", "get_cssParserIgnoreCharsetForURLsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssPositionStickyStaticScrollPositionEnabled", "get_cssPositionStickyStaticScrollPositionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssPositionTryOrderEnabled", "get_cssPositionTryOrderEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssPositionVisibilityEnabled", "get_cssPositionVisibilityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssProgressNotationEnabled", "get_cssProgressNotationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssPseudoOpenClosedEnabled", "get_cssPseudoOpenClosedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssPseudoPlayingPausedEnabled", "get_cssPseudoPlayingPausedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssPseudoScrollMarkersEnabled", "get_cssPseudoScrollMarkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssReadingOrderItemsEnabled", "get_cssReadingOrderItemsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssRelativeColorEnabled", "get_cssRelativeColorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssResizeAutoEnabled", "get_cssResizeAutoEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssRubyAlignEnabled", "get_cssRubyAlignEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssScrollSnapChangeEventEnabled", "get_cssScrollSnapChangeEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssScrollSnapChangingEventEnabled", "get_cssScrollSnapChangingEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssScrollSnapEventsEnabled", "get_cssScrollSnapEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssScrollStartEnabled", "get_cssScrollStartEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssScrollStartTargetEnabled", "get_cssScrollStartTargetEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssScrollStateContainerQueriesEnabled", "get_cssScrollStateContainerQueriesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssSelectorFragmentAnchorEnabled", "get_cssSelectorFragmentAnchorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssSignRelatedFunctionsEnabled", "get_cssSignRelatedFunctionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssSizingKeywordAnimationEnabled", "get_cssSizingKeywordAnimationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssSnapContainerQueriesEnabled", "get_cssSnapContainerQueriesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssSteppedValueFunctionsEnabled", "get_cssSteppedValueFunctionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssStickyContainerQueriesEnabled", "get_cssStickyContainerQueriesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssSupportsForImportRulesEnabled", "get_cssSupportsForImportRulesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssSystemAccentColorEnabled", "get_cssSystemAccentColorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssTextAutoSpaceEnabled", "get_cssTextAutoSpaceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssTextBoxTrimEnabled", "get_cssTextBoxTrimEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssTextSpacingEnabled", "get_cssTextSpacingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssTransitionShorterSerializationEnabled", "get_cssTransitionShorterSerializationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssTreeScopedTimelinesEnabled", "get_cssTreeScopedTimelinesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssUnknownContainerQueriesNoSelectionEnabled", "get_cssUnknownContainerQueriesNoSelectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssUserSelectContainEnabled", "get_cssUserSelectContainEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssVideoDynamicRangeMediaQueriesEnabled", "get_cssVideoDynamicRangeMediaQueriesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cssViewTransitionClassEnabled", "get_cssViewTransitionClassEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("cursorAnchorInfoMojoPipeEnabled", "get_cursorAnchorInfoMojoPipeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("customElementsGetNameEnabled", "get_customElementsGetNameEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("databaseEnabled", "get_databaseEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("deprecateUnloadOptOutEnabled", "get_deprecateUnloadOptOutEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("desktopCaptureDisableLocalEchoControlEnabled", "get_desktopCaptureDisableLocalEchoControlEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("desktopPWAsAdditionalWindowingControlsEnabled", "get_desktopPWAsAdditionalWindowingControlsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("desktopPWAsSubAppsEnabled", "get_desktopPWAsSubAppsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("detailsStylingEnabled", "get_detailsStylingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceAttributesEnabled", "get_deviceAttributesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceOrientationRequestPermissionEnabled", "get_deviceOrientationRequestPermissionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("devicePostureEnabled", "get_devicePostureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dialogCloseWhenOpenRemovedEnabled", "get_dialogCloseWhenOpenRemovedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dialogNewFocusBehaviorEnabled", "get_dialogNewFocusBehaviorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("digitalGoodsEnabled", "get_digitalGoodsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("digitalGoodsV21Enabled", "get_digitalGoodsV21Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("directSocketsEnabled", "get_directSocketsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dirnameMoreInputTypesEnabled", "get_dirnameMoreInputTypesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("disableAhemAntialiasEnabled", "get_disableAhemAntialiasEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("disableDifferentOriginSubframeDialogSuppressionEnabled", "get_disableDifferentOriginSubframeDialogSuppressionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("disableHardwareNoiseSuppressionEnabled", "get_disableHardwareNoiseSuppressionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("disableSelectAllForEmptyTextEnabled", "get_disableSelectAllForEmptyTextEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("disableThirdPartyStoragePartitioning2Enabled", "get_disableThirdPartyStoragePartitioning2Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dispatchBeforeInputForSpinButtonInteractionsEnabled", "get_dispatchBeforeInputForSpinButtonInteractionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dispatchHiddenVisibilityTransitionsEnabled", "get_dispatchHiddenVisibilityTransitionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dispatchSelectionchangeEventPerElementEnabled", "get_dispatchSelectionchangeEventPerElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("displayContentsFocusableEnabled", "get_displayContentsFocusableEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("displayCutoutAPIEnabled", "get_displayCutoutAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentBaseURIFixEnabled", "get_documentBaseURIFixEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentCookieEnabled", "get_documentCookieEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentDomainEnabled", "get_documentDomainEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentOpenOriginAliasRemovalEnabled", "get_documentOpenOriginAliasRemovalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentOpenSandboxInheritanceRemovalEnabled", "get_documentOpenSandboxInheritanceRemovalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentPictureInPictureAPIEnabled", "get_documentPictureInPictureAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentPictureInPictureUserActivationEnabled", "get_documentPictureInPictureUserActivationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentPolicyDocumentDomainEnabled", "get_documentPolicyDocumentDomainEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentPolicyIncludeJSCallStacksInCrashReportsEnabled", "get_documentPolicyIncludeJSCallStacksInCrashReportsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentPolicyNegotiationEnabled", "get_documentPolicyNegotiationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentPolicySyncXHREnabled", "get_documentPolicySyncXHREnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentRenderBlockingEnabled", "get_documentRenderBlockingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("documentWriteEnabled", "get_documentWriteEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("domParserIncludeShadowRootsEnabled", "get_domParserIncludeShadowRootsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("domParserUsesHTMLFastPathParserEnabled", "get_domParserUsesHTMLFastPathParserEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("domPartsAPIEnabled", "get_domPartsAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dontFireDblclickOnDisabledFormControlsEnabled", "get_dontFireDblclickOnDisabledFormControlsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("dynamicScrollCullRectExpansionEnabled", "get_dynamicScrollCullRectExpansionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("elementCaptureEnabled", "get_elementCaptureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("elementGetInnerHTMLEnabled", "get_elementGetInnerHTMLEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("enforceAnonymityExposureEnabled", "get_enforceAnonymityExposureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("escapeLtGtInAttributesEnabled", "get_escapeLtGtInAttributesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("eventTimingInteractionCountEnabled", "get_eventTimingInteractionCountEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("excludeTransparentTextsFromBeingLcpEligibleEnabled", "get_excludeTransparentTextsFromBeingLcpEligibleEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("experimentalContentSecurityPolicyFeaturesEnabled", "get_experimentalContentSecurityPolicyFeaturesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("experimentalJSProfilerMarkersEnabled", "get_experimentalJSProfilerMarkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("experimentalPoliciesEnabled", "get_experimentalPoliciesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("exposeRenderTimeNonTaoDelayedImageEnabled", "get_exposeRenderTimeNonTaoDelayedImageEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("extendedTextMetricsEnabled", "get_extendedTextMetricsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("eyeDropperAPIEnabled", "get_eyeDropperAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("faceDetectorEnabled", "get_faceDetectorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fasterMinContentEnabled", "get_fasterMinContentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fastPathSingleSelectorExactMatchEnabled", "get_fastPathSingleSelectorExactMatchEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fastPositionIteratorEnabled", "get_fastPositionIteratorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmEnabled", "get_fedCmEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmAuthzEnabled", "get_fedCmAuthzEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmAutoSelectedFlagEnabled", "get_fedCmAutoSelectedFlagEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmButtonModeEnabled", "get_fedCmButtonModeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmDisconnectEnabled", "get_fedCmDisconnectEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmDomainHintEnabled", "get_fedCmDomainHintEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmErrorEnabled", "get_fedCmErrorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmIdPRegistrationEnabled", "get_fedCmIdPRegistrationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmIdpSigninStatusEnabled", "get_fedCmIdpSigninStatusEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmMultipleIdentityProvidersEnabled", "get_fedCmMultipleIdentityProvidersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmSelectiveDisclosureEnabled", "get_fedCmSelectiveDisclosureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fedCmWithStorageAccessAPIEnabled", "get_fedCmWithStorageAccessAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fencedFramesEnabled", "get_fencedFramesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fencedFramesAPIChangesEnabled", "get_fencedFramesAPIChangesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fencedFramesDefaultModeEnabled", "get_fencedFramesDefaultModeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fencedFramesLocalUnpartitionedDataAccessEnabled", "get_fencedFramesLocalUnpartitionedDataAccessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fetchLaterAPIEnabled", "get_fetchLaterAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fetchUploadStreamingEnabled", "get_fetchUploadStreamingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileHandlingEnabled", "get_fileHandlingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileHandlingIconsEnabled", "get_fileHandlingIconsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemEnabled", "get_fileSystemEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemAccessEnabled", "get_fileSystemAccessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemAccessAPIExperimentalEnabled", "get_fileSystemAccessAPIExperimentalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemAccessGetCloudIdentifiersEnabled", "get_fileSystemAccessGetCloudIdentifiersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemAccessLocalEnabled", "get_fileSystemAccessLocalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemAccessLockingSchemeEnabled", "get_fileSystemAccessLockingSchemeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemAccessOriginPrivateEnabled", "get_fileSystemAccessOriginPrivateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fileSystemObserverEnabled", "get_fileSystemObserverEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("findTextInReadonlyTextInputEnabled", "get_findTextInReadonlyTextInputEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeEnabled", "get_fledgeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeBiddingAndAuctionServerAPIEnabled", "get_fledgeBiddingAndAuctionServerAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeClearOriginJoinedAdInterestGroupsEnabled", "get_fledgeClearOriginJoinedAdInterestGroupsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeCreateAuctionNonceSynchronousResolutionEnabled", "get_fledgeCreateAuctionNonceSynchronousResolutionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeCustomMaxAuctionAdComponentsEnabled", "get_fledgeCustomMaxAuctionAdComponentsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeDeprecatedRenderURLReplacementsEnabled", "get_fledgeDeprecatedRenderURLReplacementsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeDirectFromSellerSignalsHeaderAdSlotEnabled", "get_fledgeDirectFromSellerSignalsHeaderAdSlotEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeFeatureDetectAllEnabled", "get_fledgeFeatureDetectAllEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeFeatureDetectionEnabled", "get_fledgeFeatureDetectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeMultiBidEnabled", "get_fledgeMultiBidEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeNegativeTargetingEnabled", "get_fledgeNegativeTargetingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgePermitCrossOriginTrustedSignalsEnabled", "get_fledgePermitCrossOriginTrustedSignalsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeRealTimeReportingEnabled", "get_fledgeRealTimeReportingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeReportingTimeoutEnabled", "get_fledgeReportingTimeoutEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fledgeTrustedBiddingSignalsSlotSizeEnabled", "get_fledgeTrustedBiddingSignalsSlotSizeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fluentOverlayScrollbarsEnabled", "get_fluentOverlayScrollbarsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fluentScrollbarsEnabled", "get_fluentScrollbarsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("flushParserBeforeCreatingCustomElementsEnabled", "get_flushParserBeforeCreatingCustomElementsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("focusgroupEnabled", "get_focusgroupEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontAccessEnabled", "get_fontAccessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontationsFontBackendEnabled", "get_fontationsFontBackendEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontFamilyPostscriptMatchingCTMigrationEnabled", "get_fontFamilyPostscriptMatchingCTMigrationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontFamilyStyleMatchingCTMigrationEnabled", "get_fontFamilyStyleMatchingCTMigrationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontMatchingCTMigrationEnabled", "get_fontMatchingCTMigrationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontPaletteAnimationEnabled", "get_fontPaletteAnimationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontSrcLocalMatchingEnabled", "get_fontSrcLocalMatchingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontVariantEmojiEnabled", "get_fontVariantEmojiEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fontVariationSequencesEnabled", "get_fontVariationSequencesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("forcedColorsEnabled", "get_forcedColorsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("forcedColorsPreserveParentColorEnabled", "get_forcedColorsPreserveParentColorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("forceEagerMeasureMemoryEnabled", "get_forceEagerMeasureMemoryEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("forceReduceMotionEnabled", "get_forceReduceMotionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("forceTallerSelectPopupEnabled", "get_forceTallerSelectPopupEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("formattedTextEnabled", "get_formattedTextEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("formControlRestoreStateIfAutocompleteOffEnabled", "get_formControlRestoreStateIfAutocompleteOffEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("formControlsVerticalWritingModeDirectionSupportEnabled", "get_formControlsVerticalWritingModeDirectionSupportEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("formStateRestoreCallbackCallWithStateEnabled", "get_formStateRestoreCallbackCallWithStateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fractionalScrollOffsetsEnabled", "get_fractionalScrollOffsetsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("freezeFramesOnVisibilityEnabled", "get_freezeFramesOnVisibilityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("fullscreenPopupWindowsEnabled", "get_fullscreenPopupWindowsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("gamepadButtonAxisEventsEnabled", "get_gamepadButtonAxisEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("gamepadMultitouchEnabled", "get_gamepadMultitouchEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("getAllScreensMediaEnabled", "get_getAllScreensMediaEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("getDisplayMediaEnabled", "get_getDisplayMediaEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("getDisplayMediaRequiresUserActivationEnabled", "get_getDisplayMediaRequiresUserActivationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("getNextSiblingPositionWhenLastChildEnabled", "get_getNextSiblingPositionWhenLastChildEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("groupEffectEnabled", "get_groupEffectEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("handwritingRecognitionEnabled", "get_handwritingRecognitionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("hangingWhitespaceDoesNotDependOnAlignmentEnabled", "get_hangingWhitespaceDoesNotDependOnAlignmentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("hasUAVisualTransitionEnabled", "get_hasUAVisualTransitionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("highlightInheritanceEnabled", "get_highlightInheritanceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("highlightPointerEventsEnabled", "get_highlightPointerEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("hitTestOpaquenessEnabled", "get_hitTestOpaquenessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("hrefTranslateEnabled", "get_hrefTranslateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlAnchorAttributeEnabled", "get_htmlAnchorAttributeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlInterestTargetAttributeEnabled", "get_htmlInterestTargetAttributeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlInvokeActionsV2Enabled", "get_htmlInvokeActionsV2Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlInvokeTargetAttributeEnabled", "get_htmlInvokeTargetAttributeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlParserYieldAndDelayOftenForTestingEnabled", "get_htmlParserYieldAndDelayOftenForTestingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlPopoverActionHoverEnabled", "get_htmlPopoverActionHoverEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlPopoverHintEnabled", "get_htmlPopoverHintEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlSearchElementEnabled", "get_htmlSearchElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlSelectElementShowPickerEnabled", "get_htmlSelectElementShowPickerEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlSelectListElementEnabled", "get_htmlSelectListElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("htmlUnsafeMethodsEnabled", "get_htmlUnsafeMethodsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("ignoresCSSTextTransformsForPlainTextCopyEnabled", "get_ignoresCSSTextTransformsForPlainTextCopyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("implicitRootScrollerEnabled", "get_implicitRootScrollerEnabled", "set_implicitRootScrollerEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("importAttributesDisallowUnknownKeysEnabled", "get_importAttributesDisallowUnknownKeysEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("importMapIntegrityEnabled", "get_importMapIntegrityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("improvedXMLErrorsEnabled", "get_improvedXMLErrorsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("incomingCallNotificationsEnabled", "get_incomingCallNotificationsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("incrementLocalSurfaceIdForMainframeSameDocNavigationEnabled", "get_incrementLocalSurfaceIdForMainframeSameDocNavigationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inertDisplayTransitionEnabled", "get_inertDisplayTransitionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inertElementNonEditableEnabled", "get_inertElementNonEditableEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inertElementNonSearchableEnabled", "get_inertElementNonSearchableEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("infiniteCullRectEnabled", "get_infiniteCullRectEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inheritUserModifyWithoutContenteditableEnabled", "get_inheritUserModifyWithoutContenteditableEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inlineBlockInSameLineEnabled", "get_inlineBlockInSameLineEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("innerHTMLParserFastpathLogFailureEnabled", "get_innerHTMLParserFastpathLogFailureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputClipRulesCssEnabled", "get_inputClipRulesCssEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputMultipleFieldsUIEnabled", "get_inputMultipleFieldsUIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputStepCurrentValueValidationEnabled", "get_inputStepCurrentValueValidationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("inputTypeSupportInsertLinkEnabled", "get_inputTypeSupportInsertLinkEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("insertBlockquoteBeforeOuterBlockEnabled", "get_insertBlockquoteBeforeOuterBlockEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("insertLineBreakIfPhrasingContentEnabled", "get_insertLineBreakIfPhrasingContentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("installedAppEnabled", "get_installedAppEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("interoperablePrivateAttributionEnabled", "get_interoperablePrivateAttributionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("interruptComposedScrollbarDisappearanceEnabled", "get_interruptComposedScrollbarDisappearanceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("intersectionObserverScrollMarginEnabled", "get_intersectionObserverScrollMarginEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("intersectionOptimizationEnabled", "get_intersectionOptimizationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("invertedColorsEnabled", "get_invertedColorsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("invisibleSVGAnimationThrottlingEnabled", "get_invisibleSVGAnimationThrottlingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("javaScriptCompileHintsMagicRuntimeEnabled", "get_javaScriptCompileHintsMagicRuntimeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("keyboardAccessibleTooltipEnabled", "get_keyboardAccessibleTooltipEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("keyboardFocusableScrollersEnabled", "get_keyboardFocusableScrollersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("keyboardFocusableScrollersOptOutEnabled", "get_keyboardFocusableScrollersOptOutEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("labelEventHandlerCallSuperEnabled", "get_labelEventHandlerCallSuperEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("langAttributeAwareFormControlUIEnabled", "get_langAttributeAwareFormControlUIEnabled", "set_langAttributeAwareFormControlUIEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("lastSuccessfulPositionOptionEnabled", "get_lastSuccessfulPositionOptionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("layoutBaselineFixEnabled", "get_layoutBaselineFixEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("layoutBlockButtonEnabled", "get_layoutBlockButtonEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("layoutFlexNewRowAlgorithmV3Enabled", "get_layoutFlexNewRowAlgorithmV3Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("layoutFlexUnderInvalidationFixEnabled", "get_layoutFlexUnderInvalidationFixEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("layoutIgnoreMarginsForStickyEnabled", "get_layoutIgnoreMarginsForStickyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("layoutNGShapeCacheEnabled", "get_layoutNGShapeCacheEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("layoutSegmentationFastPathForObjectReplacementEnabled", "get_layoutSegmentationFastPathForObjectReplacementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("lazyInitializeMediaControlsEnabled", "get_lazyInitializeMediaControlsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("lazyLoadScrollMarginEnabled", "get_lazyLoadScrollMarginEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("lazyLoadScrollMarginIframeEnabled", "get_lazyLoadScrollMarginIframeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("lcpAnimatedImagesWebExposedEnabled", "get_lcpAnimatedImagesWebExposedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("lcpMouseoverHeuristicsEnabled", "get_lcpMouseoverHeuristicsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("lcpMultipleUpdatesPerElementEnabled", "get_lcpMultipleUpdatesPerElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("legacyWindowsDWriteFontFallbackEnabled", "get_legacyWindowsDWriteFontFallbackEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("limitThirdPartyCookiesEnabled", "get_limitThirdPartyCookiesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("lockedModeEnabled", "get_lockedModeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("longAnimationFrameTimingEnabled", "get_longAnimationFrameTimingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("longTaskFromLongAnimationFrameEnabled", "get_longTaskFromLongAnimationFrameEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("macFontsDeprecateFontTraitsWorkaroundEnabled", "get_macFontsDeprecateFontTraitsWorkaroundEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("machineLearningCommonEnabled", "get_machineLearningCommonEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("machineLearningModelLoaderEnabled", "get_machineLearningModelLoaderEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("machineLearningNeuralNetworkEnabled", "get_machineLearningNeuralNetworkEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("managedConfigurationEnabled", "get_managedConfigurationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("measureMemoryEnabled", "get_measureMemoryEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCapabilitiesDynamicRangeEnabled", "get_mediaCapabilitiesDynamicRangeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCapabilitiesEncodingInfoEnabled", "get_mediaCapabilitiesEncodingInfoEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCapabilitiesSpatialAudioEnabled", "get_mediaCapabilitiesSpatialAudioEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCaptureEnabled", "get_mediaCaptureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCaptureBackgroundBlurEnabled", "get_mediaCaptureBackgroundBlurEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCaptureCameraControlsEnabled", "get_mediaCaptureCameraControlsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCaptureConfigurationChangeEnabled", "get_mediaCaptureConfigurationChangeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCaptureVoiceIsolationEnabled", "get_mediaCaptureVoiceIsolationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCastOverlayButtonEnabled", "get_mediaCastOverlayButtonEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaControlsExpandGestureEnabled", "get_mediaControlsExpandGestureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaControlsOverlayPlayButtonEnabled", "get_mediaControlsOverlayPlayButtonEnabled", "set_mediaControlsOverlayPlayButtonEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("mediaElementVolumeGreaterThanOneEnabled", "get_mediaElementVolumeGreaterThanOneEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaEngagementBypassAutoplayPoliciesEnabled", "get_mediaEngagementBypassAutoplayPoliciesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaLatencyHintEnabled", "get_mediaLatencyHintEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaPreviewsOptOutEnabled", "get_mediaPreviewsOptOutEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaQueryNavigationControlsEnabled", "get_mediaQueryNavigationControlsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaRecorderUseMediaVideoEncoderEnabled", "get_mediaRecorderUseMediaVideoEncoderEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaSessionEnabled", "get_mediaSessionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaSessionChapterInformationEnabled", "get_mediaSessionChapterInformationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaSessionEnterPictureInPictureEnabled", "get_mediaSessionEnterPictureInPictureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaSourceExperimentalEnabled", "get_mediaSourceExperimentalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaSourceExtensionsForWebCodecsEnabled", "get_mediaSourceExtensionsForWebCodecsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaSourceNewAbortAndDurationEnabled", "get_mediaSourceNewAbortAndDurationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaStreamTrackTransferEnabled", "get_mediaStreamTrackTransferEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("messagePortCloseEventEnabled", "get_messagePortCloseEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("metaRefreshNoFractionalEnabled", "get_metaRefreshNoFractionalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("middleClickAutoscrollEnabled", "get_middleClickAutoscrollEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mobileLayoutThemeEnabled", "get_mobileLayoutThemeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("modelExecutionAPIEnabled", "get_modelExecutionAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mojoJSEnabled", "get_mojoJSEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mojoJSTestEnabled", "get_mojoJSTestEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mouseDragFromIframeOnCancelledMouseDownEnabled", "get_mouseDragFromIframeOnCancelledMouseDownEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mouseDragOnCancelledMouseMoveEnabled", "get_mouseDragOnCancelledMouseMoveEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("moveEndingSelectionToListChildEnabled", "get_moveEndingSelectionToListChildEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("multiSelectDeselectWhenOnlyOptionEnabled", "get_multiSelectDeselectWhenOnlyOptionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mutationEventsEnabled", "get_mutationEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("mutationEventsSpecialTrialMessageEnabled", "get_mutationEventsSpecialTrialMessageEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigateEventCommitBehaviorEnabled", "get_navigateEventCommitBehaviorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigateEventSourceElementEnabled", "get_navigateEventSourceElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigationActivationEnabled", "get_navigationActivationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigationIdEnabled", "get_navigationIdEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("navigatorContentUtilsEnabled", "get_navigatorContentUtilsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("netInfoConstantTypeEnabled", "get_netInfoConstantTypeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("netInfoDownlinkMaxEnabled", "get_netInfoDownlinkMaxEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("newFilterMapRectEnabled", "get_newFilterMapRectEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("newGetFocusableAreaBehaviorEnabled", "get_newGetFocusableAreaBehaviorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("nextSiblingPositionUseNextCandidateEnabled", "get_nextSiblingPositionUseNextCandidateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("noIdleEncodingForWebTestsEnabled", "get_noIdleEncodingForWebTestsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("noIncreasingEndOffsetOnSplittingTextNodesEnabled", "get_noIncreasingEndOffsetOnSplittingTextNodesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("noIntrinsicSizeOverrideEnabled", "get_noIntrinsicSizeOverrideEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("nonComposedEnterLeaveEventsEnabled", "get_nonComposedEnterLeaveEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("nonEmptyBlockquotesOnOutdentingEnabled", "get_nonEmptyBlockquotesOnOutdentingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("nonStandardAppearanceValuesHighUsageEnabled", "get_nonStandardAppearanceValuesHighUsageEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("nonStandardAppearanceValueSliderVerticalEnabled", "get_nonStandardAppearanceValueSliderVerticalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("notificationConstructorEnabled", "get_notificationConstructorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("notificationContentImageEnabled", "get_notificationContentImageEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("notificationsEnabled", "get_notificationsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("notificationTriggersEnabled", "get_notificationTriggersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("noVarySearchPrefetchEnabled", "get_noVarySearchPrefetchEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("observableAPIEnabled", "get_observableAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("offMainThreadCSSPaintEnabled", "get_offMainThreadCSSPaintEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("offscreenCanvasCommitEnabled", "get_offscreenCanvasCommitEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("omitBlurEventOnElementRemovalEnabled", "get_omitBlurEventOnElementRemovalEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("onDeviceChangeEnabled", "get_onDeviceChangeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("optionElementAlwaysUseLabelEnabled", "get_optionElementAlwaysUseLabelEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("orientationEventEnabled", "get_orientationEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originIsolationHeaderEnabled", "get_originIsolationHeaderEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originPolicyEnabled", "get_originPolicyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIEnabled", "get_originTrialsSampleAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIBrowserReadWriteEnabled", "get_originTrialsSampleAPIBrowserReadWriteEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIDependentEnabled", "get_originTrialsSampleAPIDependentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIDeprecationEnabled", "get_originTrialsSampleAPIDeprecationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIExpiryGracePeriodEnabled", "get_originTrialsSampleAPIExpiryGracePeriodEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIExpiryGracePeriodThirdPartyEnabled", "get_originTrialsSampleAPIExpiryGracePeriodThirdPartyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIImpliedEnabled", "get_originTrialsSampleAPIImpliedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIInvalidOSEnabled", "get_originTrialsSampleAPIInvalidOSEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPINavigationEnabled", "get_originTrialsSampleAPINavigationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIPersistentExpiryGracePeriodEnabled", "get_originTrialsSampleAPIPersistentExpiryGracePeriodEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIPersistentFeatureEnabled", "get_originTrialsSampleAPIPersistentFeatureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIPersistentInvalidOSEnabled", "get_originTrialsSampleAPIPersistentInvalidOSEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIPersistentThirdPartyDeprecationFeatureEnabled", "get_originTrialsSampleAPIPersistentThirdPartyDeprecationFeatureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("originTrialsSampleAPIThirdPartyEnabled", "get_originTrialsSampleAPIThirdPartyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("overscrollCustomizationEnabled", "get_overscrollCustomizationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageFreezeOptInEnabled", "get_pageFreezeOptInEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageFreezeOptOutEnabled", "get_pageFreezeOptOutEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageMarginBoxesEnabled", "get_pageMarginBoxesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pagePopupEnabled", "get_pagePopupEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageRevealEventEnabled", "get_pageRevealEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pageSwapEventEnabled", "get_pageSwapEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paintHoldingForIframesEnabled", "get_paintHoldingForIframesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paintHoldingForLocalIframesEnabled", "get_paintHoldingForLocalIframesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paintUnderInvalidationCheckingEnabled", "get_paintUnderInvalidationCheckingEnabled", "set_paintUnderInvalidationCheckingEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("parakeetEnabled", "get_parakeetEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("passwordRevealEnabled", "get_passwordRevealEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("passwordStrongLabelEnabled", "get_passwordStrongLabelEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentAppEnabled", "get_paymentAppEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentInstrumentsEnabled", "get_paymentInstrumentsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentLinkDetectionEnabled", "get_paymentLinkDetectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentMethodChangeEventEnabled", "get_paymentMethodChangeEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("paymentRequestEnabled", "get_paymentRequestEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("percentBasedScrollingEnabled", "get_percentBasedScrollingEnabled", "set_percentBasedScrollingEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("performanceManagerInstrumentationEnabled", "get_performanceManagerInstrumentationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("performanceMarkFeatureUsageEnabled", "get_performanceMarkFeatureUsageEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("performanceNavigateSystemEntropyEnabled", "get_performanceNavigateSystemEntropyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("periodicBackgroundSyncEnabled", "get_periodicBackgroundSyncEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("perMethodCanMakePaymentQuotaEnabled", "get_perMethodCanMakePaymentQuotaEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("permissionElementEnabled", "get_permissionElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("permissionsEnabled", "get_permissionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("permissionsRequestRevokeEnabled", "get_permissionsRequestRevokeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pNaClEnabled", "get_pNaClEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointerCaptureLostOnRemovalDuringCaptureEnabled", "get_pointerCaptureLostOnRemovalDuringCaptureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pointerEventDeviceIdEnabled", "get_pointerEventDeviceIdEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("positionOutsideTabSpanCheckSiblingNodeEnabled", "get_positionOutsideTabSpanCheckSiblingNodeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("preciseMemoryInfoEnabled", "get_preciseMemoryInfoEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("preferDefaultScrollbarStylesEnabled", "get_preferDefaultScrollbarStylesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("preferNonCompositedScrollingEnabled", "get_preferNonCompositedScrollingEnabled", "set_preferNonCompositedScrollingEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("prefersReducedDataEnabled", "get_prefersReducedDataEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("prefixedVideoFullscreenEnabled", "get_prefixedVideoFullscreenEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("prePaintAncestorsOfMissedOOFEnabled", "get_prePaintAncestorsOfMissedOOFEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("prerender2Enabled", "get_prerender2Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("presentationEnabled", "get_presentationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("prettyPrintJSONDocumentEnabled", "get_prettyPrintJSONDocumentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("preventReadingSystemAccentColorEnabled", "get_preventReadingSystemAccentColorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privacySandboxAdsAPISEnabled", "get_privacySandboxAdsAPISEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privateAggregationApiFilteringIdsEnabled", "get_privateAggregationApiFilteringIdsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privateAggregationAuctionReportBuyerDebugModeConfigEnabled", "get_privateAggregationAuctionReportBuyerDebugModeConfigEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privateNetworkAccessNonSecureContextsAllowedEnabled", "get_privateNetworkAccessNonSecureContextsAllowedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privateNetworkAccessNullIpAddressEnabled", "get_privateNetworkAccessNullIpAddressEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privateNetworkAccessPermissionPromptEnabled", "get_privateNetworkAccessPermissionPromptEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privateStateTokensEnabled", "get_privateStateTokensEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("privateStateTokensAlwaysAllowIssuanceEnabled", "get_privateStateTokensAlwaysAllowIssuanceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("protectedOriginTrialsSampleAPIEnabled", "get_protectedOriginTrialsSampleAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("protectedOriginTrialsSampleAPIDependentEnabled", "get_protectedOriginTrialsSampleAPIDependentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("protectedOriginTrialsSampleAPIImpliedEnabled", "get_protectedOriginTrialsSampleAPIImpliedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pushMessagingEnabled", "get_pushMessagingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("pushMessagingSubscriptionChangeEnabled", "get_pushMessagingSubscriptionChangeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("quickIntensiveWakeUpThrottlingAfterLoadingEnabled", "get_quickIntensiveWakeUpThrottlingAfterLoadingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("quotaChangeEnabled", "get_quotaChangeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rasterInducingScrollEnabled", "get_rasterInducingScrollEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("readableStreamAsyncIterableEnabled", "get_readableStreamAsyncIterableEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("recollectInlinesReserveCapacityEnabled", "get_recollectInlinesReserveCapacityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("reduceAcceptLanguageEnabled", "get_reduceAcceptLanguageEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("reduceCookieIPCsEnabled", "get_reduceCookieIPCsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("reduceUserAgentAndroidVersionDeviceModelEnabled", "get_reduceUserAgentAndroidVersionDeviceModelEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("reduceUserAgentMinorVersionEnabled", "get_reduceUserAgentMinorVersionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("reduceUserAgentPlatformOsCpuEnabled", "get_reduceUserAgentPlatformOsCpuEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("regionCaptureEnabled", "get_regionCaptureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("remotePlaybackEnabled", "get_remotePlaybackEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("remotePlaybackBackendEnabled", "get_remotePlaybackBackendEnabled", "set_remotePlaybackBackendEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("removeDanglingMarkupInTargetEnabled", "get_removeDanglingMarkupInTargetEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("removeDataUrlInSvgUseEnabled", "get_removeDataUrlInSvgUseEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("removeMobileViewportDoubleTapEnabled", "get_removeMobileViewportDoubleTapEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("removeNodeHavingChildrenIfFullySelectedEnabled", "get_removeNodeHavingChildrenIfFullySelectedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("removeVisibleSelectionInDOMSelectionEnabled", "get_removeVisibleSelectionInDOMSelectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("renderBlockingInlineModuleScriptEnabled", "get_renderBlockingInlineModuleScriptEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("renderBlockingStatusEnabled", "get_renderBlockingStatusEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("renderPriorityAttributeEnabled", "get_renderPriorityAttributeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("reportVisibleLineBoundsEnabled", "get_reportVisibleLineBoundsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("resourceTimingContentTypeEnabled", "get_resourceTimingContentTypeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("resourceTimingUseCORSForBodySizesEnabled", "get_resourceTimingUseCORSForBodySizesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("restrictGamepadAccessEnabled", "get_restrictGamepadAccessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rewindFloatsEnabled", "get_rewindFloatsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcAudioJitterBufferMaxPacketsEnabled", "get_rtcAudioJitterBufferMaxPacketsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcEncodedAudioFrameAbsCaptureTimeEnabled", "get_rtcEncodedAudioFrameAbsCaptureTimeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcEncodedFrameSetMetadataEnabled", "get_rtcEncodedFrameSetMetadataEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcEncodedVideoFrameAdditionalMetadataEnabled", "get_rtcEncodedVideoFrameAdditionalMetadataEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcJitterBufferTargetEnabled", "get_rtcJitterBufferTargetEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcLegacyCallbackBasedGetStatsEnabled", "get_rtcLegacyCallbackBasedGetStatsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcRtpEncodingParametersCodecEnabled", "get_rtcRtpEncodingParametersCodecEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcRtpHeaderExtensionControlEnabled", "get_rtcRtpHeaderExtensionControlEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcRtpTransportEnabled", "get_rtcRtpTransportEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcStatsRelativePacketArrivalDelayEnabled", "get_rtcStatsRelativePacketArrivalDelayEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rtcSvcScalabilityModeEnabled", "get_rtcSvcScalabilityModeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rubyAnnotationSpaceFixEnabled", "get_rubyAnnotationSpaceFixEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rubyLineBreakableEnabled", "get_rubyLineBreakableEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rubyLineEdgeAlignmentEnabled", "get_rubyLineEdgeAlignmentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("rubyShortHeuristicsEnabled", "get_rubyShortHeuristicsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("runMicrotaskBeforeXmlCustomElementEnabled", "get_runMicrotaskBeforeXmlCustomElementEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sanitizerAPIEnabled", "get_sanitizerAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("schedulerYieldEnabled", "get_schedulerYieldEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scopedCustomElementRegistryEnabled", "get_scopedCustomElementRegistryEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scriptedSpeechRecognitionEnabled", "get_scriptedSpeechRecognitionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scriptedSpeechSynthesisEnabled", "get_scriptedSpeechSynthesisEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollbarColorEnabled", "get_scrollbarColorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollbarWidthEnabled", "get_scrollbarWidthEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollEndEventsEnabled", "get_scrollEndEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollNodeForOverflowHiddenEnabled", "get_scrollNodeForOverflowHiddenEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollTimelineEnabled", "get_scrollTimelineEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollTimelineAlwaysOnCompositorEnabled", "get_scrollTimelineAlwaysOnCompositorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollTimelineCurrentTimeEnabled", "get_scrollTimelineCurrentTimeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollTimelineOnCompositorEnabled", "get_scrollTimelineOnCompositorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("scrollTopLeftInteropEnabled", "get_scrollTopLeftInteropEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("searchTextHighlightPseudoEnabled", "get_searchTextHighlightPseudoEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("securePaymentConfirmationEnabled", "get_securePaymentConfirmationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("securePaymentConfirmationDebugEnabled", "get_securePaymentConfirmationDebugEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("securePaymentConfirmationNetworkAndIssuerIconsEnabled", "get_securePaymentConfirmationNetworkAndIssuerIconsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("securePaymentConfirmationOptOutEnabled", "get_securePaymentConfirmationOptOutEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("selectionRespectsColorsEnabled", "get_selectionRespectsColorsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sendBeaconThrowForBlobWithNonSimpleTypeEnabled", "get_sendBeaconThrowForBlobWithNonSimpleTypeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sensorExtraClassesEnabled", "get_sensorExtraClassesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("serialEnabled", "get_serialEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("serializeViewTransitionStateInSPAEnabled", "get_serializeViewTransitionStateInSPAEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("serialPortConnectedEnabled", "get_serialPortConnectedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("serviceWorkerClientLifecycleStateEnabled", "get_serviceWorkerClientLifecycleStateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("serviceWorkerStaticRouterEnabled", "get_serviceWorkerStaticRouterEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("serviceWorkerStaticRouterTimingInfoEnabled", "get_serviceWorkerStaticRouterTimingInfoEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("setSequentialFocusStartingPointEnabled", "get_setSequentialFocusStartingPointEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("shapeResultCachedPreviousSafeToBreakOffsetEnabled", "get_shapeResultCachedPreviousSafeToBreakOffsetEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedArrayBufferEnabled", "get_sharedArrayBufferEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedArrayBufferOnDesktopEnabled", "get_sharedArrayBufferOnDesktopEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedArrayBufferUnrestrictedAccessAllowedEnabled", "get_sharedArrayBufferUnrestrictedAccessAllowedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedAutofillEnabled", "get_sharedAutofillEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedStorageAPIEnabled", "get_sharedStorageAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedStorageAPIM118Enabled", "get_sharedStorageAPIM118Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedStorageAPIM125Enabled", "get_sharedStorageAPIM125Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("sharedWorkerEnabled", "get_sharedWorkerEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("showPickerConsumeUserActivationEnabled", "get_showPickerConsumeUserActivationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("signatureBasedIntegrityEnabled", "get_signatureBasedIntegrityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("siteInitiatedMirroringEnabled", "get_siteInitiatedMirroringEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("skipAdEnabled", "get_skipAdEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("skipPreloadScanningEnabled", "get_skipPreloadScanningEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("skipTouchEventFilterEnabled", "get_skipTouchEventFilterEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("skipUpdateTypeForHTMLInputElementCreatedByParserEnabled", "get_skipUpdateTypeForHTMLInputElementCreatedByParserEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("smartCardEnabled", "get_smartCardEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("smartZoomEnabled", "get_smartZoomEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("smilAutoSuspendOnLagEnabled", "get_smilAutoSuspendOnLagEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("softNavigationDetectionEnabled", "get_softNavigationDetectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("softNavigationHeuristicsEnabled", "get_softNavigationHeuristicsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("softNavigationHeuristicsExposeFPAndFCPEnabled", "get_softNavigationHeuristicsExposeFPAndFCPEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speakerSelectionEnabled", "get_speakerSelectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesDocumentRulesEnabled", "get_speculationRulesDocumentRulesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesDocumentRulesSelectorMatchesEnabled", "get_speculationRulesDocumentRulesSelectorMatchesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesEagernessEnabled", "get_speculationRulesEagernessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesFetchFromHeaderEnabled", "get_speculationRulesFetchFromHeaderEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesImplicitSourceEnabled", "get_speculationRulesImplicitSourceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesNoVarySearchHintEnabled", "get_speculationRulesNoVarySearchHintEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesNoVarySearchHintShippedByDefaultEnabled", "get_speculationRulesNoVarySearchHintShippedByDefaultEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesPointerDownHeuristicsEnabled", "get_speculationRulesPointerDownHeuristicsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesPointerHoverHeuristicsEnabled", "get_speculationRulesPointerHoverHeuristicsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesPrefetchFutureEnabled", "get_speculationRulesPrefetchFutureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesPrefetchWithSubresourcesEnabled", "get_speculationRulesPrefetchWithSubresourcesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("speculationRulesRelativeToDocumentEnabled", "get_speculationRulesRelativeToDocumentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("spellCheckerReplaceRangeUseInsertTextEnabled", "get_spellCheckerReplaceRangeUseInsertTextEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("srcsetMaxDensityEnabled", "get_srcsetMaxDensityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("stableBlinkFeaturesEnabled", "get_stableBlinkFeaturesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("standardizedBrowserZoomEnabled", "get_standardizedBrowserZoomEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("staticAnimationOptimizationEnabled", "get_staticAnimationOptimizationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("storageBucketsEnabled", "get_storageBucketsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("storageBucketsDurabilityEnabled", "get_storageBucketsDurabilityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("storageBucketsLocksEnabled", "get_storageBucketsLocksEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("strictMimeTypesForWorkersEnabled", "get_strictMimeTypesForWorkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("stylableSelectEnabled", "get_stylableSelectEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("stylusHandwritingEnabled", "get_stylusHandwritingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("svgContextPaintEnabled", "get_svgContextPaintEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("svgCrossOriginAttributeEnabled", "get_svgCrossOriginAttributeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("svgFilterUserSpaceViewportForNonSvgEnabled", "get_svgFilterUserSpaceViewportForNonSvgEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("svgNoPixelSnappingScaleAdjustmentEnabled", "get_svgNoPixelSnappingScaleAdjustmentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("synthesizedKeyboardEventsForAccessibilityActionsEnabled", "get_synthesizedKeyboardEventsForAccessibilityActionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("systemWakeLockEnabled", "get_systemWakeLockEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testBlinkFeatureDefaultEnabled", "get_testBlinkFeatureDefaultEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testFeatureEnabled", "get_testFeatureEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testFeatureDependentEnabled", "get_testFeatureDependentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testFeatureImpliedEnabled", "get_testFeatureImpliedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testFeatureProtectedEnabled", "get_testFeatureProtectedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testFeatureProtectedDependentEnabled", "get_testFeatureProtectedDependentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testFeatureProtectedImpliedEnabled", "get_testFeatureProtectedImpliedEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("testFeatureStableEnabled", "get_testFeatureStableEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textAlignJustifyBidiIsolateEnabled", "get_textAlignJustifyBidiIsolateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textAlignLastJustifyNewLineEnabled", "get_textAlignLastJustifyNewLineEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textAreaChildrenChangedStillValidatesEnabled", "get_textAreaChildrenChangedStillValidatesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textDecoratingBoxEnabled", "get_textDecoratingBoxEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textDetectorEnabled", "get_textDetectorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textDiffSplitFixEnabled", "get_textDiffSplitFixEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textFragmentAPIEnabled", "get_textFragmentAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textFragmentIdentifiersEnabled", "get_textFragmentIdentifiersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textFragmentTapOpensContextMenuEnabled", "get_textFragmentTapOpensContextMenuEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textMetricsBaselinesEnabled", "get_textMetricsBaselinesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("textSizeAdjustImprovementsEnabled", "get_textSizeAdjustImprovementsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("timelineScopeEnabled", "get_timelineScopeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("timerThrottlingForBackgroundTabsEnabled", "get_timerThrottlingForBackgroundTabsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("timeZoneChangeEventEnabled", "get_timeZoneChangeEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("topicsAPIEnabled", "get_topicsAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("topicsDocumentAPIEnabled", "get_topicsDocumentAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("topLevelTpcdEnabled", "get_topLevelTpcdEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("touchDragAndContextMenuEnabled", "get_touchDragAndContextMenuEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("touchDragOnShortPressEnabled", "get_touchDragOnShortPressEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("touchEventFeatureDetectionEnabled", "get_touchEventFeatureDetectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("touchTextEditingRedesignEnabled", "get_touchTextEditingRedesignEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("tpcdEnabled", "get_tpcdEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("translateServiceEnabled", "get_translateServiceEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("translationAPIEnabled", "get_translationAPIEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("trustedTypeBeforePolicyCreationEventEnabled", "get_trustedTypeBeforePolicyCreationEventEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("trustedTypesFromLiteralEnabled", "get_trustedTypesFromLiteralEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("trustedTypesUseCodeLikeEnabled", "get_trustedTypesUseCodeLikeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("unblockTouchMoveEarlierEnabled", "get_unblockTouchMoveEarlierEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("unclosedFormControlIsInvalidEnabled", "get_unclosedFormControlIsInvalidEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("unexposedTaskIdsEnabled", "get_unexposedTaskIdsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("unownedAnimationsSkipCSSEventsEnabled", "get_unownedAnimationsSkipCSSEventsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("unrestrictedMeasureUserAgentSpecificMemoryEnabled", "get_unrestrictedMeasureUserAgentSpecificMemoryEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("unrestrictedSharedArrayBufferEnabled", "get_unrestrictedSharedArrayBufferEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("unrestrictedUsbEnabled", "get_unrestrictedUsbEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("urlAttributeFixEnabled", "get_urlAttributeFixEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("urlParseEnabled", "get_urlParseEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("urlPatternCompareComponentEnabled", "get_urlPatternCompareComponentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("urlPatternHasRegExpGroupsEnabled", "get_urlPatternHasRegExpGroupsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("urlPatternRegexpUnicodeSetsModeEnabled", "get_urlPatternRegexpUnicodeSetsModeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("urlPatternWildcardMoreOftenEnabled", "get_urlPatternWildcardMoreOftenEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("urlSearchParamsHasAndDeleteMultipleArgsEnabled", "get_urlSearchParamsHasAndDeleteMultipleArgsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("useBeginFramePresentationFeedbackEnabled", "get_useBeginFramePresentationFeedbackEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("usedColorSchemeRootScrollbarsEnabled", "get_usedColorSchemeRootScrollbarsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("userActivationSameOriginVisibilityEnabled", "get_userActivationSameOriginVisibilityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("useUndoStepElementDispatchBeforeInputEnabled", "get_useUndoStepElementDispatchBeforeInputEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("v8IdleTasksEnabled", "get_v8IdleTasksEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoAutoFullscreenEnabled", "get_videoAutoFullscreenEnabled", "set_videoAutoFullscreenEnabled", 0, 1, 0, 0, 0, 0, 1),
        ("videoFullscreenOrientationLockEnabled", "get_videoFullscreenOrientationLockEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoRotateToFullscreenEnabled", "get_videoRotateToFullscreenEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoTrackGeneratorEnabled", "get_videoTrackGeneratorEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoTrackGeneratorInWindowEnabled", "get_videoTrackGeneratorInWindowEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("videoTrackGeneratorInWorkerEnabled", "get_videoTrackGeneratorInWorkerEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewportHeightClientHintHeaderEnabled", "get_viewportHeightClientHintHeaderEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewportSegmentsEnabled", "get_viewportSegmentsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewTransitionOnNavigationEnabled", "get_viewTransitionOnNavigationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewTransitionOnNavigationForIframesEnabled", "get_viewTransitionOnNavigationForIframesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("viewTransitionTypesEnabled", "get_viewTransitionTypesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibilityCollapseColumnEnabled", "get_visibilityCollapseColumnEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("visualViewportOnScrollEndEnabled", "get_visualViewportOnScrollEndEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("vttCueDisplayRubyEnabled", "get_vttCueDisplayRubyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("wakeLockEnabled", "get_wakeLockEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("warnOnContentVisibilityRenderAccessEnabled", "get_warnOnContentVisibilityRenderAccessEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAnimationsSVGEnabled", "get_webAnimationsSVGEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAppLaunchQueueEnabled", "get_webAppLaunchQueueEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAppScopeExtensionsEnabled", "get_webAppScopeExtensionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAppsLockScreenEnabled", "get_webAppsLockScreenEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAppTabStripEnabled", "get_webAppTabStripEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAppTabStripCustomizationsEnabled", "get_webAppTabStripCustomizationsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAppTranslationsEnabled", "get_webAppTranslationsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAppUrlHandlingEnabled", "get_webAppUrlHandlingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAssemblyJSPromiseIntegrationEnabled", "get_webAssemblyJSPromiseIntegrationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAssemblyJSStringBuiltinsEnabled", "get_webAssemblyJSStringBuiltinsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthEnabled", "get_webAuthEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthAuthenticatorAttachmentEnabled", "get_webAuthAuthenticatorAttachmentEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthenticationHintsEnabled", "get_webAuthenticationHintsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthenticationJSONSerializationEnabled", "get_webAuthenticationJSONSerializationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthenticationLargeBlobExtensionEnabled", "get_webAuthenticationLargeBlobExtensionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthenticationPRFEnabled", "get_webAuthenticationPRFEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthenticationRemoteDesktopSupportEnabled", "get_webAuthenticationRemoteDesktopSupportEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webAuthenticationSupplementalPubKeysEnabled", "get_webAuthenticationSupplementalPubKeysEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webBluetoothEnabled", "get_webBluetoothEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webBluetoothGetDevicesEnabled", "get_webBluetoothGetDevicesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webBluetoothScanningEnabled", "get_webBluetoothScanningEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webBluetoothWatchAdvertisementsEnabled", "get_webBluetoothWatchAdvertisementsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webcodecsCopyToRGBEnabled", "get_webcodecsCopyToRGBEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webcodecsHBDFormatsEnabled", "get_webcodecsHBDFormatsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webCryptoCurve25519Enabled", "get_webCryptoCurve25519Enabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webExposedScrollOffsetEnabled", "get_webExposedScrollOffsetEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webFontResizeLCPEnabled", "get_webFontResizeLCPEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webglDeveloperExtensionsEnabled", "get_webglDeveloperExtensionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webglDraftExtensionsEnabled", "get_webglDraftExtensionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webglDrawingBufferStorageEnabled", "get_webglDrawingBufferStorageEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webglImageChromiumEnabled", "get_webglImageChromiumEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webgpuAdapterInfoAttributeEnabled", "get_webgpuAdapterInfoAttributeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webgpuDeveloperFeaturesEnabled", "get_webgpuDeveloperFeaturesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webgpuExperimentalFeaturesEnabled", "get_webgpuExperimentalFeaturesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webHIDEnabled", "get_webHIDEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webHIDOnServiceWorkersEnabled", "get_webHIDOnServiceWorkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webIdentityDigitalCredentialsEnabled", "get_webIdentityDigitalCredentialsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webIDLBigIntUsesToBigIntEnabled", "get_webIDLBigIntUsesToBigIntEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webNFCEnabled", "get_webNFCEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webOTPEnabled", "get_webOTPEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webOTPAssertionFeaturePolicyEnabled", "get_webOTPAssertionFeaturePolicyEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webPreferencesEnabled", "get_webPreferencesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webPrintingEnabled", "get_webPrintingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webSerialBluetoothEnabled", "get_webSerialBluetoothEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webShareEnabled", "get_webShareEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("websocketHTTPURLEnabled", "get_websocketHTTPURLEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("websocketStreamEnabled", "get_websocketStreamEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webTransportCustomCertificatesEnabled", "get_webTransportCustomCertificatesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webTransportStatsEnabled", "get_webTransportStatsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webUSBEnabled", "get_webUSBEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webUSBOnDedicatedWorkersEnabled", "get_webUSBOnDedicatedWorkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webUSBOnServiceWorkersEnabled", "get_webUSBOnServiceWorkersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webViewXREquestedWithDeprecationEnabled", "get_webViewXREquestedWithDeprecationEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webVTTRegionsEnabled", "get_webVTTRegionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXREnabled", "get_webXREnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXREnabledFeaturesEnabled", "get_webXREnabledFeaturesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRFrameRateEnabled", "get_webXRFrameRateEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRFrontFacingEnabled", "get_webXRFrontFacingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRHandInputEnabled", "get_webXRHandInputEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRHitTestEntityTypesEnabled", "get_webXRHitTestEntityTypesEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRImageTrackingEnabled", "get_webXRImageTrackingEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRLayersEnabled", "get_webXRLayersEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRPlaneDetectionEnabled", "get_webXRPlaneDetectionEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRPoseMotionDataEnabled", "get_webXRPoseMotionDataEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webXRSpecParityEnabled", "get_webXRSpecParityEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("wgiGamepadTriggerRumbleEnabled", "get_wgiGamepadTriggerRumbleEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("windowDefaultStatusEnabled", "get_windowDefaultStatusEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("windowPlacementFullscreenOnScreensChangeEnabled", "get_windowPlacementFullscreenOnScreensChangeEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("writingSuggestionsEnabled", "get_writingSuggestionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("xmlParserMergeAdjacentCDataSectionsEnabled", "get_xmlParserMergeAdjacentCDataSectionsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("xpathLangUseAsciiCaseEnabled", "get_xpathLangUseAsciiCaseEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("zeroCopyTabCaptureEnabled", "get_zeroCopyTabCaptureEnabled", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_accelerated2dCanvasEnabled(self):
        val = self._attr.get('accelerated2dCanvasEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accelerated2dCanvasEnabled -> get attr')

    def set_accelerated2dCanvasEnabled(self, val):
        self._attr['accelerated2dCanvasEnabled'] = val

    def get_acceleratedSmallCanvasesEnabled(self):
        val = self._attr.get('acceleratedSmallCanvasesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.acceleratedSmallCanvasesEnabled -> get attr')

    def get_accessibilityAriaVirtualContentEnabled(self):
        val = self._attr.get('accessibilityAriaVirtualContentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accessibilityAriaVirtualContentEnabled -> get attr')

    def get_accessibilityExposeDisplayNoneEnabled(self):
        val = self._attr.get('accessibilityExposeDisplayNoneEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accessibilityExposeDisplayNoneEnabled -> get attr')

    def get_accessibilityObjectModelEnabled(self):
        val = self._attr.get('accessibilityObjectModelEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accessibilityObjectModelEnabled -> get attr')

    def get_accessibilityOSLevelBoldTextEnabled(self):
        val = self._attr.get('accessibilityOSLevelBoldTextEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accessibilityOSLevelBoldTextEnabled -> get attr')

    def get_accessibilityPageZoomEnabled(self):
        val = self._attr.get('accessibilityPageZoomEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accessibilityPageZoomEnabled -> get attr')

    def get_accessibilitySerializationSizeMetricsEnabled(self):
        val = self._attr.get('accessibilitySerializationSizeMetricsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accessibilitySerializationSizeMetricsEnabled -> get attr')

    def get_accessibilityUseAXPositionForDocumentMarkersEnabled(self):
        val = self._attr.get('accessibilityUseAXPositionForDocumentMarkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.accessibilityUseAXPositionForDocumentMarkersEnabled -> get attr')

    def get_addressSpaceEnabled(self):
        val = self._attr.get('addressSpaceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.addressSpaceEnabled -> get attr')

    def get_adInterestGroupAPIEnabled(self):
        val = self._attr.get('adInterestGroupAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.adInterestGroupAPIEnabled -> get attr')

    def get_adjustEndOfNextParagraphIfMovedParagraphIsUpdatedEnabled(self):
        val = self._attr.get('adjustEndOfNextParagraphIfMovedParagraphIsUpdatedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.adjustEndOfNextParagraphIfMovedParagraphIsUpdatedEnabled -> get attr')

    def get_adTaggingEnabled(self):
        val = self._attr.get('adTaggingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.adTaggingEnabled -> get attr')

    def get_allowContentInitiatedDataUrlNavigationsEnabled(self):
        val = self._attr.get('allowContentInitiatedDataUrlNavigationsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.allowContentInitiatedDataUrlNavigationsEnabled -> get attr')

    def get_allowJavaScriptToResetAutofillStateEnabled(self):
        val = self._attr.get('allowJavaScriptToResetAutofillStateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.allowJavaScriptToResetAutofillStateEnabled -> get attr')

    def get_allowURNsInIframesEnabled(self):
        val = self._attr.get('allowURNsInIframesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.allowURNsInIframesEnabled -> get attr')

    def get_androidDownloadableFontsMatchingEnabled(self):
        val = self._attr.get('androidDownloadableFontsMatchingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.androidDownloadableFontsMatchingEnabled -> get attr')

    def get_animationProgressAPIEnabled(self):
        val = self._attr.get('animationProgressAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.animationProgressAPIEnabled -> get attr')

    def get_animationWorkletEnabled(self):
        val = self._attr.get('animationWorkletEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.animationWorkletEnabled -> get attr')

    def get_anonymousIframeEnabled(self):
        val = self._attr.get('anonymousIframeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.anonymousIframeEnabled -> get attr')

    def get_aomAriaRelationshipPropertiesEnabled(self):
        val = self._attr.get('aomAriaRelationshipPropertiesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.aomAriaRelationshipPropertiesEnabled -> get attr')

    def get_appTitleEnabled(self):
        val = self._attr.get('appTitleEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.appTitleEnabled -> get attr')

    def get_ariaNotifyEnabled(self):
        val = self._attr.get('ariaNotifyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.ariaNotifyEnabled -> get attr')

    def get_atomicMoveAPIEnabled(self):
        val = self._attr.get('atomicMoveAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.atomicMoveAPIEnabled -> get attr')

    def get_attributionReportingEnabled(self):
        val = self._attr.get('attributionReportingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.attributionReportingEnabled -> get attr')

    def get_attributionReportingCrossAppWebEnabled(self):
        val = self._attr.get('attributionReportingCrossAppWebEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.attributionReportingCrossAppWebEnabled -> get attr')

    def get_attributionReportingInterfaceEnabled(self):
        val = self._attr.get('attributionReportingInterfaceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.attributionReportingInterfaceEnabled -> get attr')

    def get_audioContextOnErrorEnabled(self):
        val = self._attr.get('audioContextOnErrorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.audioContextOnErrorEnabled -> get attr')

    def get_audioContextPlayoutStatsEnabled(self):
        val = self._attr.get('audioContextPlayoutStatsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.audioContextPlayoutStatsEnabled -> get attr')

    def get_audioContextSetSinkIdEnabled(self):
        val = self._attr.get('audioContextSetSinkIdEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.audioContextSetSinkIdEnabled -> get attr')

    def get_audioOutputDevicesEnabled(self):
        val = self._attr.get('audioOutputDevicesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.audioOutputDevicesEnabled -> get attr')

    def get_audioVideoTracksEnabled(self):
        val = self._attr.get('audioVideoTracksEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.audioVideoTracksEnabled -> get attr')

    def get_autoDarkModeEnabled(self):
        val = self._attr.get('autoDarkModeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.autoDarkModeEnabled -> get attr')

    def get_automationControlledEnabled(self):
        val = self._attr.get('automationControlledEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.automationControlledEnabled -> get attr')

    def set_automationControlledEnabled(self, val):
        self._attr['automationControlledEnabled'] = val

    def get_autoPictureInPictureVideoHeuristicsEnabled(self):
        val = self._attr.get('autoPictureInPictureVideoHeuristicsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.autoPictureInPictureVideoHeuristicsEnabled -> get attr')

    def get_autoSizeLazyLoadedImagesEnabled(self):
        val = self._attr.get('autoSizeLazyLoadedImagesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.autoSizeLazyLoadedImagesEnabled -> get attr')

    def get_avoidCaretVisibleSelectionAdjusterEnabled(self):
        val = self._attr.get('avoidCaretVisibleSelectionAdjusterEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.avoidCaretVisibleSelectionAdjusterEnabled -> get attr')

    def get_backdropInheritOriginatingEnabled(self):
        val = self._attr.get('backdropInheritOriginatingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.backdropInheritOriginatingEnabled -> get attr')

    def get_backfaceVisibilityInteropEnabled(self):
        val = self._attr.get('backfaceVisibilityInteropEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.backfaceVisibilityInteropEnabled -> get attr')

    def get_backForwardCacheEnabled(self):
        val = self._attr.get('backForwardCacheEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.backForwardCacheEnabled -> get attr')

    def get_backForwardCacheExperimentHTTPHeaderEnabled(self):
        val = self._attr.get('backForwardCacheExperimentHTTPHeaderEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.backForwardCacheExperimentHTTPHeaderEnabled -> get attr')

    def get_backForwardCacheNotRestoredReasonsEnabled(self):
        val = self._attr.get('backForwardCacheNotRestoredReasonsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.backForwardCacheNotRestoredReasonsEnabled -> get attr')

    def get_backForwardTransitionsEnabled(self):
        val = self._attr.get('backForwardTransitionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.backForwardTransitionsEnabled -> get attr')

    def get_backgroundFetchEnabled(self):
        val = self._attr.get('backgroundFetchEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.backgroundFetchEnabled -> get attr')

    def get_barcodeDetectorEnabled(self):
        val = self._attr.get('barcodeDetectorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.barcodeDetectorEnabled -> get attr')

    def get_beforeunloadEventCancelByPreventDefaultEnabled(self):
        val = self._attr.get('beforeunloadEventCancelByPreventDefaultEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.beforeunloadEventCancelByPreventDefaultEnabled -> get attr')

    def get_bidiCaretAffinityEnabled(self):
        val = self._attr.get('bidiCaretAffinityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.bidiCaretAffinityEnabled -> get attr')

    def get_blinkExtensionChromeOSEnabled(self):
        val = self._attr.get('blinkExtensionChromeOSEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blinkExtensionChromeOSEnabled -> get attr')

    def get_blinkExtensionChromeOSKioskEnabled(self):
        val = self._attr.get('blinkExtensionChromeOSKioskEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blinkExtensionChromeOSKioskEnabled -> get attr')

    def get_blinkExtensionDiagnosticsEnabled(self):
        val = self._attr.get('blinkExtensionDiagnosticsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blinkExtensionDiagnosticsEnabled -> get attr')

    def get_blinkExtensionWebViewEnabled(self):
        val = self._attr.get('blinkExtensionWebViewEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blinkExtensionWebViewEnabled -> get attr')

    def get_blinkExtensionWebViewMediaIntegrityEnabled(self):
        val = self._attr.get('blinkExtensionWebViewMediaIntegrityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blinkExtensionWebViewMediaIntegrityEnabled -> get attr')

    def get_blinkLifecycleScriptForbiddenEnabled(self):
        val = self._attr.get('blinkLifecycleScriptForbiddenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blinkLifecycleScriptForbiddenEnabled -> get attr')

    def get_blinkRuntimeCallStatsEnabled(self):
        val = self._attr.get('blinkRuntimeCallStatsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blinkRuntimeCallStatsEnabled -> get attr')

    def get_blockingFocusWithoutUserActivationEnabled(self):
        val = self._attr.get('blockingFocusWithoutUserActivationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.blockingFocusWithoutUserActivationEnabled -> get attr')

    def get_boundaryEventDispatchTracksNodeRemovalEnabled(self):
        val = self._attr.get('boundaryEventDispatchTracksNodeRemovalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.boundaryEventDispatchTracksNodeRemovalEnabled -> get attr')

    def get_breakIteratorDataGeneratorEnabled(self):
        val = self._attr.get('breakIteratorDataGeneratorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.breakIteratorDataGeneratorEnabled -> get attr')

    def get_browserVerifiedUserActivationKeyboardEnabled(self):
        val = self._attr.get('browserVerifiedUserActivationKeyboardEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.browserVerifiedUserActivationKeyboardEnabled -> get attr')

    def get_browserVerifiedUserActivationMouseEnabled(self):
        val = self._attr.get('browserVerifiedUserActivationMouseEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.browserVerifiedUserActivationMouseEnabled -> get attr')

    def get_bufferedBytesConsumerLimitSizeEnabled(self):
        val = self._attr.get('bufferedBytesConsumerLimitSizeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.bufferedBytesConsumerLimitSizeEnabled -> get attr')

    def get_bypassPepcSecurityForTestingEnabled(self):
        val = self._attr.get('bypassPepcSecurityForTestingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.bypassPepcSecurityForTestingEnabled -> get attr')

    def get_cacheStorageCodeCacheHintEnabled(self):
        val = self._attr.get('cacheStorageCodeCacheHintEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cacheStorageCodeCacheHintEnabled -> get attr')

    def get_canvas2dCanvasFilterEnabled(self):
        val = self._attr.get('canvas2dCanvasFilterEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvas2dCanvasFilterEnabled -> get attr')

    def get_canvas2dGPUTransferEnabled(self):
        val = self._attr.get('canvas2dGPUTransferEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvas2dGPUTransferEnabled -> get attr')

    def get_canvas2dImageChromiumEnabled(self):
        val = self._attr.get('canvas2dImageChromiumEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvas2dImageChromiumEnabled -> get attr')

    def get_canvas2dLayersEnabled(self):
        val = self._attr.get('canvas2dLayersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvas2dLayersEnabled -> get attr')

    def get_canvas2dMeshEnabled(self):
        val = self._attr.get('canvas2dMeshEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvas2dMeshEnabled -> get attr')

    def get_canvas2dScrollPathIntoViewEnabled(self):
        val = self._attr.get('canvas2dScrollPathIntoViewEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvas2dScrollPathIntoViewEnabled -> get attr')

    def get_canvasFloatingPointEnabled(self):
        val = self._attr.get('canvasFloatingPointEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvasFloatingPointEnabled -> get attr')

    def get_canvasHDREnabled(self):
        val = self._attr.get('canvasHDREnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvasHDREnabled -> get attr')

    def get_canvasImageSmoothingEnabled(self):
        val = self._attr.get('canvasImageSmoothingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvasImageSmoothingEnabled -> get attr')

    def get_canvasUsesArcPaintOpEnabled(self):
        val = self._attr.get('canvasUsesArcPaintOpEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.canvasUsesArcPaintOpEnabled -> get attr')

    def get_capabilityDelegationDisplayCaptureRequestEnabled(self):
        val = self._attr.get('capabilityDelegationDisplayCaptureRequestEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.capabilityDelegationDisplayCaptureRequestEnabled -> get attr')

    def get_captureControllerEnabled(self):
        val = self._attr.get('captureControllerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.captureControllerEnabled -> get attr')

    def get_capturedMouseEventsEnabled(self):
        val = self._attr.get('capturedMouseEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.capturedMouseEventsEnabled -> get attr')

    def get_capturedSurfaceControlEnabled(self):
        val = self._attr.get('capturedSurfaceControlEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.capturedSurfaceControlEnabled -> get attr')

    def get_captureHandleEnabled(self):
        val = self._attr.get('captureHandleEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.captureHandleEnabled -> get attr')

    def get_caretPositionFromPointEnabled(self):
        val = self._attr.get('caretPositionFromPointEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.caretPositionFromPointEnabled -> get attr')

    def get_cctNewRFMPushBehaviorEnabled(self):
        val = self._attr.get('cctNewRFMPushBehaviorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cctNewRFMPushBehaviorEnabled -> get attr')

    def get_checkVisibilityExtraPropertiesEnabled(self):
        val = self._attr.get('checkVisibilityExtraPropertiesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.checkVisibilityExtraPropertiesEnabled -> get attr')

    def get_clickToCapturedPointerEnabled(self):
        val = self._attr.get('clickToCapturedPointerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.clickToCapturedPointerEnabled -> get attr')

    def get_clipboardSvgEnabled(self):
        val = self._attr.get('clipboardSvgEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.clipboardSvgEnabled -> get attr')

    def get_clipPathRejectEmptyPathsEnabled(self):
        val = self._attr.get('clipPathRejectEmptyPathsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.clipPathRejectEmptyPathsEnabled -> get attr')

    def get_closeWatcherEnabled(self):
        val = self._attr.get('closeWatcherEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.closeWatcherEnabled -> get attr')

    def get_coepReflectionEnabled(self):
        val = self._attr.get('coepReflectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.coepReflectionEnabled -> get attr')

    def get_compositeBGColorAnimationEnabled(self):
        val = self._attr.get('compositeBGColorAnimationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.compositeBGColorAnimationEnabled -> get attr')

    def get_compositeBoxShadowAnimationEnabled(self):
        val = self._attr.get('compositeBoxShadowAnimationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.compositeBoxShadowAnimationEnabled -> get attr')

    def get_compositeClipPathAnimationEnabled(self):
        val = self._attr.get('compositeClipPathAnimationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.compositeClipPathAnimationEnabled -> get attr')

    def get_compositedSelectionUpdateEnabled(self):
        val = self._attr.get('compositedSelectionUpdateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.compositedSelectionUpdateEnabled -> get attr')

    def get_compositionForegroundMarkersEnabled(self):
        val = self._attr.get('compositionForegroundMarkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.compositionForegroundMarkersEnabled -> get attr')

    def get_compressionDictionaryTransportEnabled(self):
        val = self._attr.get('compressionDictionaryTransportEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.compressionDictionaryTransportEnabled -> get attr')

    def get_compressionDictionaryTransportBackendEnabled(self):
        val = self._attr.get('compressionDictionaryTransportBackendEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.compressionDictionaryTransportBackendEnabled -> get attr')

    def get_computedAccessibilityInfoEnabled(self):
        val = self._attr.get('computedAccessibilityInfoEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.computedAccessibilityInfoEnabled -> get attr')

    def get_computePressureEnabled(self):
        val = self._attr.get('computePressureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.computePressureEnabled -> get attr')

    def get_concurrentViewTransitionsSPAEnabled(self):
        val = self._attr.get('concurrentViewTransitionsSPAEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.concurrentViewTransitionsSPAEnabled -> get attr')

    def get_contactsManagerEnabled(self):
        val = self._attr.get('contactsManagerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.contactsManagerEnabled -> get attr')

    def get_contactsManagerExtraPropertiesEnabled(self):
        val = self._attr.get('contactsManagerExtraPropertiesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.contactsManagerExtraPropertiesEnabled -> get attr')

    def get_contentIndexEnabled(self):
        val = self._attr.get('contentIndexEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.contentIndexEnabled -> get attr')

    def get_contextMenuEnabled(self):
        val = self._attr.get('contextMenuEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.contextMenuEnabled -> get attr')

    def get_continueEventTimingRecordingWhenBufferIsFullEnabled(self):
        val = self._attr.get('continueEventTimingRecordingWhenBufferIsFullEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.continueEventTimingRecordingWhenBufferIsFullEnabled -> get attr')

    def get_cookieDeprecationFacilitatedTestingEnabled(self):
        val = self._attr.get('cookieDeprecationFacilitatedTestingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cookieDeprecationFacilitatedTestingEnabled -> get attr')

    def get_cooperativeSchedulingEnabled(self):
        val = self._attr.get('cooperativeSchedulingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cooperativeSchedulingEnabled -> get attr')

    def get_coopRestrictPropertiesEnabled(self):
        val = self._attr.get('coopRestrictPropertiesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.coopRestrictPropertiesEnabled -> get attr')

    def get_corsRFC1918Enabled(self):
        val = self._attr.get('corsRFC1918Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.corsRFC1918Enabled -> get attr')

    def get_createInputShadowTreeDuringLayoutEnabled(self):
        val = self._attr.get('createInputShadowTreeDuringLayoutEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.createInputShadowTreeDuringLayoutEnabled -> get attr')

    def get_credentialManagerReportEnabled(self):
        val = self._attr.get('credentialManagerReportEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.credentialManagerReportEnabled -> get attr')

    def get_crossFramePerformanceTimelineEnabled(self):
        val = self._attr.get('crossFramePerformanceTimelineEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.crossFramePerformanceTimelineEnabled -> get attr')

    def get_cssAnchorPositioningEnabled(self):
        val = self._attr.get('cssAnchorPositioningEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssAnchorPositioningEnabled -> get attr')

    def get_cssAnchorScopeEnabled(self):
        val = self._attr.get('cssAnchorScopeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssAnchorScopeEnabled -> get attr')

    def get_cssAtRuleCounterStyleImageSymbolsEnabled(self):
        val = self._attr.get('cssAtRuleCounterStyleImageSymbolsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssAtRuleCounterStyleImageSymbolsEnabled -> get attr')

    def get_cssAtRuleCounterStyleSpeakAsDescriptorEnabled(self):
        val = self._attr.get('cssAtRuleCounterStyleSpeakAsDescriptorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssAtRuleCounterStyleSpeakAsDescriptorEnabled -> get attr')

    def get_cssBackgroundClipUnprefixEnabled(self):
        val = self._attr.get('cssBackgroundClipUnprefixEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssBackgroundClipUnprefixEnabled -> get attr')

    def get_cssCalcSimplificationAndSerializationEnabled(self):
        val = self._attr.get('cssCalcSimplificationAndSerializationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssCalcSimplificationAndSerializationEnabled -> get attr')

    def get_cssCalcSizeFunctionEnabled(self):
        val = self._attr.get('cssCalcSizeFunctionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssCalcSizeFunctionEnabled -> get attr')

    def get_cssCapFontUnitsEnabled(self):
        val = self._attr.get('cssCapFontUnitsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssCapFontUnitsEnabled -> get attr')

    def get_cssCaseSensitiveSelectorEnabled(self):
        val = self._attr.get('cssCaseSensitiveSelectorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssCaseSensitiveSelectorEnabled -> get attr')

    def get_cssColorContrastEnabled(self):
        val = self._attr.get('cssColorContrastEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssColorContrastEnabled -> get attr')

    def get_cssColorTypedOMEnabled(self):
        val = self._attr.get('cssColorTypedOMEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssColorTypedOMEnabled -> get attr')

    def get_cssComputedStyleFullPseudoElementParserEnabled(self):
        val = self._attr.get('cssComputedStyleFullPseudoElementParserEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssComputedStyleFullPseudoElementParserEnabled -> get attr')

    def get_cssContentMultiArgAltTextEnabled(self):
        val = self._attr.get('cssContentMultiArgAltTextEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssContentMultiArgAltTextEnabled -> get attr')

    def get_cssContentVisibilityImpliesContainIntrinsicSizeAutoEnabled(self):
        val = self._attr.get('cssContentVisibilityImpliesContainIntrinsicSizeAutoEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssContentVisibilityImpliesContainIntrinsicSizeAutoEnabled -> get attr')

    def get_cssCrossFadeEnabled(self):
        val = self._attr.get('cssCrossFadeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssCrossFadeEnabled -> get attr')

    def get_cssCustomStateDeprecatedSyntaxEnabled(self):
        val = self._attr.get('cssCustomStateDeprecatedSyntaxEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssCustomStateDeprecatedSyntaxEnabled -> get attr')

    def get_cssCustomStateNewSyntaxEnabled(self):
        val = self._attr.get('cssCustomStateNewSyntaxEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssCustomStateNewSyntaxEnabled -> get attr')

    def get_cssDisplayModePictureInPictureEnabled(self):
        val = self._attr.get('cssDisplayModePictureInPictureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssDisplayModePictureInPictureEnabled -> get attr')

    def get_cssDynamicRangeLimitEnabled(self):
        val = self._attr.get('cssDynamicRangeLimitEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssDynamicRangeLimitEnabled -> get attr')

    def get_cssEnumeratedCustomPropertiesEnabled(self):
        val = self._attr.get('cssEnumeratedCustomPropertiesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssEnumeratedCustomPropertiesEnabled -> get attr')

    def get_cssExponentialFunctionsEnabled(self):
        val = self._attr.get('cssExponentialFunctionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssExponentialFunctionsEnabled -> get attr')

    def get_cssFontSizeAdjustEnabled(self):
        val = self._attr.get('cssFontSizeAdjustEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssFontSizeAdjustEnabled -> get attr')

    def get_cssFunctionsEnabled(self):
        val = self._attr.get('cssFunctionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssFunctionsEnabled -> get attr')

    def get_cssHexAlphaColorEnabled(self):
        val = self._attr.get('cssHexAlphaColorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssHexAlphaColorEnabled -> get attr')

    def get_cssKeyframesRuleLengthEnabled(self):
        val = self._attr.get('cssKeyframesRuleLengthEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssKeyframesRuleLengthEnabled -> get attr')

    def get_cssLayoutAPIEnabled(self):
        val = self._attr.get('cssLayoutAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssLayoutAPIEnabled -> get attr')

    def get_cssLazyParsingFastPathEnabled(self):
        val = self._attr.get('cssLazyParsingFastPathEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssLazyParsingFastPathEnabled -> get attr')

    def get_cssLightDarkColorsEnabled(self):
        val = self._attr.get('cssLightDarkColorsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssLightDarkColorsEnabled -> get attr')

    def get_cssLineClampEnabled(self):
        val = self._attr.get('cssLineClampEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssLineClampEnabled -> get attr')

    def get_cssLogicalOverflowEnabled(self):
        val = self._attr.get('cssLogicalOverflowEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssLogicalOverflowEnabled -> get attr')

    def get_cssMarkerNestedPseudoElementEnabled(self):
        val = self._attr.get('cssMarkerNestedPseudoElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssMarkerNestedPseudoElementEnabled -> get attr')

    def get_cssNumericFactoryCompletenessEnabled(self):
        val = self._attr.get('cssNumericFactoryCompletenessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssNumericFactoryCompletenessEnabled -> get attr')

    def get_cssPaintAPIArgumentsEnabled(self):
        val = self._attr.get('cssPaintAPIArgumentsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssPaintAPIArgumentsEnabled -> get attr')

    def get_cssParserIgnoreCharsetForURLsEnabled(self):
        val = self._attr.get('cssParserIgnoreCharsetForURLsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssParserIgnoreCharsetForURLsEnabled -> get attr')

    def get_cssPositionStickyStaticScrollPositionEnabled(self):
        val = self._attr.get('cssPositionStickyStaticScrollPositionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssPositionStickyStaticScrollPositionEnabled -> get attr')

    def get_cssPositionTryOrderEnabled(self):
        val = self._attr.get('cssPositionTryOrderEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssPositionTryOrderEnabled -> get attr')

    def get_cssPositionVisibilityEnabled(self):
        val = self._attr.get('cssPositionVisibilityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssPositionVisibilityEnabled -> get attr')

    def get_cssProgressNotationEnabled(self):
        val = self._attr.get('cssProgressNotationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssProgressNotationEnabled -> get attr')

    def get_cssPseudoOpenClosedEnabled(self):
        val = self._attr.get('cssPseudoOpenClosedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssPseudoOpenClosedEnabled -> get attr')

    def get_cssPseudoPlayingPausedEnabled(self):
        val = self._attr.get('cssPseudoPlayingPausedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssPseudoPlayingPausedEnabled -> get attr')

    def get_cssPseudoScrollMarkersEnabled(self):
        val = self._attr.get('cssPseudoScrollMarkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssPseudoScrollMarkersEnabled -> get attr')

    def get_cssReadingOrderItemsEnabled(self):
        val = self._attr.get('cssReadingOrderItemsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssReadingOrderItemsEnabled -> get attr')

    def get_cssRelativeColorEnabled(self):
        val = self._attr.get('cssRelativeColorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssRelativeColorEnabled -> get attr')

    def get_cssResizeAutoEnabled(self):
        val = self._attr.get('cssResizeAutoEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssResizeAutoEnabled -> get attr')

    def get_cssRubyAlignEnabled(self):
        val = self._attr.get('cssRubyAlignEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssRubyAlignEnabled -> get attr')

    def get_cssScrollSnapChangeEventEnabled(self):
        val = self._attr.get('cssScrollSnapChangeEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssScrollSnapChangeEventEnabled -> get attr')

    def get_cssScrollSnapChangingEventEnabled(self):
        val = self._attr.get('cssScrollSnapChangingEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssScrollSnapChangingEventEnabled -> get attr')

    def get_cssScrollSnapEventsEnabled(self):
        val = self._attr.get('cssScrollSnapEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssScrollSnapEventsEnabled -> get attr')

    def get_cssScrollStartEnabled(self):
        val = self._attr.get('cssScrollStartEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssScrollStartEnabled -> get attr')

    def get_cssScrollStartTargetEnabled(self):
        val = self._attr.get('cssScrollStartTargetEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssScrollStartTargetEnabled -> get attr')

    def get_cssScrollStateContainerQueriesEnabled(self):
        val = self._attr.get('cssScrollStateContainerQueriesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssScrollStateContainerQueriesEnabled -> get attr')

    def get_cssSelectorFragmentAnchorEnabled(self):
        val = self._attr.get('cssSelectorFragmentAnchorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssSelectorFragmentAnchorEnabled -> get attr')

    def get_cssSignRelatedFunctionsEnabled(self):
        val = self._attr.get('cssSignRelatedFunctionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssSignRelatedFunctionsEnabled -> get attr')

    def get_cssSizingKeywordAnimationEnabled(self):
        val = self._attr.get('cssSizingKeywordAnimationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssSizingKeywordAnimationEnabled -> get attr')

    def get_cssSnapContainerQueriesEnabled(self):
        val = self._attr.get('cssSnapContainerQueriesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssSnapContainerQueriesEnabled -> get attr')

    def get_cssSteppedValueFunctionsEnabled(self):
        val = self._attr.get('cssSteppedValueFunctionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssSteppedValueFunctionsEnabled -> get attr')

    def get_cssStickyContainerQueriesEnabled(self):
        val = self._attr.get('cssStickyContainerQueriesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssStickyContainerQueriesEnabled -> get attr')

    def get_cssSupportsForImportRulesEnabled(self):
        val = self._attr.get('cssSupportsForImportRulesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssSupportsForImportRulesEnabled -> get attr')

    def get_cssSystemAccentColorEnabled(self):
        val = self._attr.get('cssSystemAccentColorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssSystemAccentColorEnabled -> get attr')

    def get_cssTextAutoSpaceEnabled(self):
        val = self._attr.get('cssTextAutoSpaceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssTextAutoSpaceEnabled -> get attr')

    def get_cssTextBoxTrimEnabled(self):
        val = self._attr.get('cssTextBoxTrimEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssTextBoxTrimEnabled -> get attr')

    def get_cssTextSpacingEnabled(self):
        val = self._attr.get('cssTextSpacingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssTextSpacingEnabled -> get attr')

    def get_cssTransitionShorterSerializationEnabled(self):
        val = self._attr.get('cssTransitionShorterSerializationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssTransitionShorterSerializationEnabled -> get attr')

    def get_cssTreeScopedTimelinesEnabled(self):
        val = self._attr.get('cssTreeScopedTimelinesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssTreeScopedTimelinesEnabled -> get attr')

    def get_cssUnknownContainerQueriesNoSelectionEnabled(self):
        val = self._attr.get('cssUnknownContainerQueriesNoSelectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssUnknownContainerQueriesNoSelectionEnabled -> get attr')

    def get_cssUserSelectContainEnabled(self):
        val = self._attr.get('cssUserSelectContainEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssUserSelectContainEnabled -> get attr')

    def get_cssVideoDynamicRangeMediaQueriesEnabled(self):
        val = self._attr.get('cssVideoDynamicRangeMediaQueriesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssVideoDynamicRangeMediaQueriesEnabled -> get attr')

    def get_cssViewTransitionClassEnabled(self):
        val = self._attr.get('cssViewTransitionClassEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cssViewTransitionClassEnabled -> get attr')

    def get_cursorAnchorInfoMojoPipeEnabled(self):
        val = self._attr.get('cursorAnchorInfoMojoPipeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.cursorAnchorInfoMojoPipeEnabled -> get attr')

    def get_customElementsGetNameEnabled(self):
        val = self._attr.get('customElementsGetNameEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.customElementsGetNameEnabled -> get attr')

    def get_databaseEnabled(self):
        val = self._attr.get('databaseEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.databaseEnabled -> get attr')

    def get_deprecateUnloadOptOutEnabled(self):
        val = self._attr.get('deprecateUnloadOptOutEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.deprecateUnloadOptOutEnabled -> get attr')

    def get_desktopCaptureDisableLocalEchoControlEnabled(self):
        val = self._attr.get('desktopCaptureDisableLocalEchoControlEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.desktopCaptureDisableLocalEchoControlEnabled -> get attr')

    def get_desktopPWAsAdditionalWindowingControlsEnabled(self):
        val = self._attr.get('desktopPWAsAdditionalWindowingControlsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.desktopPWAsAdditionalWindowingControlsEnabled -> get attr')

    def get_desktopPWAsSubAppsEnabled(self):
        val = self._attr.get('desktopPWAsSubAppsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.desktopPWAsSubAppsEnabled -> get attr')

    def get_detailsStylingEnabled(self):
        val = self._attr.get('detailsStylingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.detailsStylingEnabled -> get attr')

    def get_deviceAttributesEnabled(self):
        val = self._attr.get('deviceAttributesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.deviceAttributesEnabled -> get attr')

    def get_deviceOrientationRequestPermissionEnabled(self):
        val = self._attr.get('deviceOrientationRequestPermissionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.deviceOrientationRequestPermissionEnabled -> get attr')

    def get_devicePostureEnabled(self):
        val = self._attr.get('devicePostureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.devicePostureEnabled -> get attr')

    def get_dialogCloseWhenOpenRemovedEnabled(self):
        val = self._attr.get('dialogCloseWhenOpenRemovedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dialogCloseWhenOpenRemovedEnabled -> get attr')

    def get_dialogNewFocusBehaviorEnabled(self):
        val = self._attr.get('dialogNewFocusBehaviorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dialogNewFocusBehaviorEnabled -> get attr')

    def get_digitalGoodsEnabled(self):
        val = self._attr.get('digitalGoodsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.digitalGoodsEnabled -> get attr')

    def get_digitalGoodsV21Enabled(self):
        val = self._attr.get('digitalGoodsV21Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.digitalGoodsV21Enabled -> get attr')

    def get_directSocketsEnabled(self):
        val = self._attr.get('directSocketsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.directSocketsEnabled -> get attr')

    def get_dirnameMoreInputTypesEnabled(self):
        val = self._attr.get('dirnameMoreInputTypesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dirnameMoreInputTypesEnabled -> get attr')

    def get_disableAhemAntialiasEnabled(self):
        val = self._attr.get('disableAhemAntialiasEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.disableAhemAntialiasEnabled -> get attr')

    def get_disableDifferentOriginSubframeDialogSuppressionEnabled(self):
        val = self._attr.get('disableDifferentOriginSubframeDialogSuppressionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.disableDifferentOriginSubframeDialogSuppressionEnabled -> get attr')

    def get_disableHardwareNoiseSuppressionEnabled(self):
        val = self._attr.get('disableHardwareNoiseSuppressionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.disableHardwareNoiseSuppressionEnabled -> get attr')

    def get_disableSelectAllForEmptyTextEnabled(self):
        val = self._attr.get('disableSelectAllForEmptyTextEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.disableSelectAllForEmptyTextEnabled -> get attr')

    def get_disableThirdPartyStoragePartitioning2Enabled(self):
        val = self._attr.get('disableThirdPartyStoragePartitioning2Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.disableThirdPartyStoragePartitioning2Enabled -> get attr')

    def get_dispatchBeforeInputForSpinButtonInteractionsEnabled(self):
        val = self._attr.get('dispatchBeforeInputForSpinButtonInteractionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dispatchBeforeInputForSpinButtonInteractionsEnabled -> get attr')

    def get_dispatchHiddenVisibilityTransitionsEnabled(self):
        val = self._attr.get('dispatchHiddenVisibilityTransitionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dispatchHiddenVisibilityTransitionsEnabled -> get attr')

    def get_dispatchSelectionchangeEventPerElementEnabled(self):
        val = self._attr.get('dispatchSelectionchangeEventPerElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dispatchSelectionchangeEventPerElementEnabled -> get attr')

    def get_displayContentsFocusableEnabled(self):
        val = self._attr.get('displayContentsFocusableEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.displayContentsFocusableEnabled -> get attr')

    def get_displayCutoutAPIEnabled(self):
        val = self._attr.get('displayCutoutAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.displayCutoutAPIEnabled -> get attr')

    def get_documentBaseURIFixEnabled(self):
        val = self._attr.get('documentBaseURIFixEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentBaseURIFixEnabled -> get attr')

    def get_documentCookieEnabled(self):
        val = self._attr.get('documentCookieEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentCookieEnabled -> get attr')

    def get_documentDomainEnabled(self):
        val = self._attr.get('documentDomainEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentDomainEnabled -> get attr')

    def get_documentOpenOriginAliasRemovalEnabled(self):
        val = self._attr.get('documentOpenOriginAliasRemovalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentOpenOriginAliasRemovalEnabled -> get attr')

    def get_documentOpenSandboxInheritanceRemovalEnabled(self):
        val = self._attr.get('documentOpenSandboxInheritanceRemovalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentOpenSandboxInheritanceRemovalEnabled -> get attr')

    def get_documentPictureInPictureAPIEnabled(self):
        val = self._attr.get('documentPictureInPictureAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentPictureInPictureAPIEnabled -> get attr')

    def get_documentPictureInPictureUserActivationEnabled(self):
        val = self._attr.get('documentPictureInPictureUserActivationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentPictureInPictureUserActivationEnabled -> get attr')

    def get_documentPolicyDocumentDomainEnabled(self):
        val = self._attr.get('documentPolicyDocumentDomainEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentPolicyDocumentDomainEnabled -> get attr')

    def get_documentPolicyIncludeJSCallStacksInCrashReportsEnabled(self):
        val = self._attr.get('documentPolicyIncludeJSCallStacksInCrashReportsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentPolicyIncludeJSCallStacksInCrashReportsEnabled -> get attr')

    def get_documentPolicyNegotiationEnabled(self):
        val = self._attr.get('documentPolicyNegotiationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentPolicyNegotiationEnabled -> get attr')

    def get_documentPolicySyncXHREnabled(self):
        val = self._attr.get('documentPolicySyncXHREnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentPolicySyncXHREnabled -> get attr')

    def get_documentRenderBlockingEnabled(self):
        val = self._attr.get('documentRenderBlockingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentRenderBlockingEnabled -> get attr')

    def get_documentWriteEnabled(self):
        val = self._attr.get('documentWriteEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.documentWriteEnabled -> get attr')

    def get_domParserIncludeShadowRootsEnabled(self):
        val = self._attr.get('domParserIncludeShadowRootsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.domParserIncludeShadowRootsEnabled -> get attr')

    def get_domParserUsesHTMLFastPathParserEnabled(self):
        val = self._attr.get('domParserUsesHTMLFastPathParserEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.domParserUsesHTMLFastPathParserEnabled -> get attr')

    def get_domPartsAPIEnabled(self):
        val = self._attr.get('domPartsAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.domPartsAPIEnabled -> get attr')

    def get_dontFireDblclickOnDisabledFormControlsEnabled(self):
        val = self._attr.get('dontFireDblclickOnDisabledFormControlsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dontFireDblclickOnDisabledFormControlsEnabled -> get attr')

    def get_dynamicScrollCullRectExpansionEnabled(self):
        val = self._attr.get('dynamicScrollCullRectExpansionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.dynamicScrollCullRectExpansionEnabled -> get attr')

    def get_elementCaptureEnabled(self):
        val = self._attr.get('elementCaptureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.elementCaptureEnabled -> get attr')

    def get_elementGetInnerHTMLEnabled(self):
        val = self._attr.get('elementGetInnerHTMLEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.elementGetInnerHTMLEnabled -> get attr')

    def get_enforceAnonymityExposureEnabled(self):
        val = self._attr.get('enforceAnonymityExposureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.enforceAnonymityExposureEnabled -> get attr')

    def get_escapeLtGtInAttributesEnabled(self):
        val = self._attr.get('escapeLtGtInAttributesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.escapeLtGtInAttributesEnabled -> get attr')

    def get_eventTimingInteractionCountEnabled(self):
        val = self._attr.get('eventTimingInteractionCountEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.eventTimingInteractionCountEnabled -> get attr')

    def get_excludeTransparentTextsFromBeingLcpEligibleEnabled(self):
        val = self._attr.get('excludeTransparentTextsFromBeingLcpEligibleEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.excludeTransparentTextsFromBeingLcpEligibleEnabled -> get attr')

    def get_experimentalContentSecurityPolicyFeaturesEnabled(self):
        val = self._attr.get('experimentalContentSecurityPolicyFeaturesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.experimentalContentSecurityPolicyFeaturesEnabled -> get attr')

    def get_experimentalJSProfilerMarkersEnabled(self):
        val = self._attr.get('experimentalJSProfilerMarkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.experimentalJSProfilerMarkersEnabled -> get attr')

    def get_experimentalPoliciesEnabled(self):
        val = self._attr.get('experimentalPoliciesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.experimentalPoliciesEnabled -> get attr')

    def get_exposeRenderTimeNonTaoDelayedImageEnabled(self):
        val = self._attr.get('exposeRenderTimeNonTaoDelayedImageEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.exposeRenderTimeNonTaoDelayedImageEnabled -> get attr')

    def get_extendedTextMetricsEnabled(self):
        val = self._attr.get('extendedTextMetricsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.extendedTextMetricsEnabled -> get attr')

    def get_eyeDropperAPIEnabled(self):
        val = self._attr.get('eyeDropperAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.eyeDropperAPIEnabled -> get attr')

    def get_faceDetectorEnabled(self):
        val = self._attr.get('faceDetectorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.faceDetectorEnabled -> get attr')

    def get_fasterMinContentEnabled(self):
        val = self._attr.get('fasterMinContentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fasterMinContentEnabled -> get attr')

    def get_fastPathSingleSelectorExactMatchEnabled(self):
        val = self._attr.get('fastPathSingleSelectorExactMatchEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fastPathSingleSelectorExactMatchEnabled -> get attr')

    def get_fastPositionIteratorEnabled(self):
        val = self._attr.get('fastPositionIteratorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fastPositionIteratorEnabled -> get attr')

    def get_fedCmEnabled(self):
        val = self._attr.get('fedCmEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmEnabled -> get attr')

    def get_fedCmAuthzEnabled(self):
        val = self._attr.get('fedCmAuthzEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmAuthzEnabled -> get attr')

    def get_fedCmAutoSelectedFlagEnabled(self):
        val = self._attr.get('fedCmAutoSelectedFlagEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmAutoSelectedFlagEnabled -> get attr')

    def get_fedCmButtonModeEnabled(self):
        val = self._attr.get('fedCmButtonModeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmButtonModeEnabled -> get attr')

    def get_fedCmDisconnectEnabled(self):
        val = self._attr.get('fedCmDisconnectEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmDisconnectEnabled -> get attr')

    def get_fedCmDomainHintEnabled(self):
        val = self._attr.get('fedCmDomainHintEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmDomainHintEnabled -> get attr')

    def get_fedCmErrorEnabled(self):
        val = self._attr.get('fedCmErrorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmErrorEnabled -> get attr')

    def get_fedCmIdPRegistrationEnabled(self):
        val = self._attr.get('fedCmIdPRegistrationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmIdPRegistrationEnabled -> get attr')

    def get_fedCmIdpSigninStatusEnabled(self):
        val = self._attr.get('fedCmIdpSigninStatusEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmIdpSigninStatusEnabled -> get attr')

    def get_fedCmMultipleIdentityProvidersEnabled(self):
        val = self._attr.get('fedCmMultipleIdentityProvidersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmMultipleIdentityProvidersEnabled -> get attr')

    def get_fedCmSelectiveDisclosureEnabled(self):
        val = self._attr.get('fedCmSelectiveDisclosureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmSelectiveDisclosureEnabled -> get attr')

    def get_fedCmWithStorageAccessAPIEnabled(self):
        val = self._attr.get('fedCmWithStorageAccessAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fedCmWithStorageAccessAPIEnabled -> get attr')

    def get_fencedFramesEnabled(self):
        val = self._attr.get('fencedFramesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fencedFramesEnabled -> get attr')

    def get_fencedFramesAPIChangesEnabled(self):
        val = self._attr.get('fencedFramesAPIChangesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fencedFramesAPIChangesEnabled -> get attr')

    def get_fencedFramesDefaultModeEnabled(self):
        val = self._attr.get('fencedFramesDefaultModeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fencedFramesDefaultModeEnabled -> get attr')

    def get_fencedFramesLocalUnpartitionedDataAccessEnabled(self):
        val = self._attr.get('fencedFramesLocalUnpartitionedDataAccessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fencedFramesLocalUnpartitionedDataAccessEnabled -> get attr')

    def get_fetchLaterAPIEnabled(self):
        val = self._attr.get('fetchLaterAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fetchLaterAPIEnabled -> get attr')

    def get_fetchUploadStreamingEnabled(self):
        val = self._attr.get('fetchUploadStreamingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fetchUploadStreamingEnabled -> get attr')

    def get_fileHandlingEnabled(self):
        val = self._attr.get('fileHandlingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileHandlingEnabled -> get attr')

    def get_fileHandlingIconsEnabled(self):
        val = self._attr.get('fileHandlingIconsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileHandlingIconsEnabled -> get attr')

    def get_fileSystemEnabled(self):
        val = self._attr.get('fileSystemEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemEnabled -> get attr')

    def get_fileSystemAccessEnabled(self):
        val = self._attr.get('fileSystemAccessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemAccessEnabled -> get attr')

    def get_fileSystemAccessAPIExperimentalEnabled(self):
        val = self._attr.get('fileSystemAccessAPIExperimentalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemAccessAPIExperimentalEnabled -> get attr')

    def get_fileSystemAccessGetCloudIdentifiersEnabled(self):
        val = self._attr.get('fileSystemAccessGetCloudIdentifiersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemAccessGetCloudIdentifiersEnabled -> get attr')

    def get_fileSystemAccessLocalEnabled(self):
        val = self._attr.get('fileSystemAccessLocalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemAccessLocalEnabled -> get attr')

    def get_fileSystemAccessLockingSchemeEnabled(self):
        val = self._attr.get('fileSystemAccessLockingSchemeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemAccessLockingSchemeEnabled -> get attr')

    def get_fileSystemAccessOriginPrivateEnabled(self):
        val = self._attr.get('fileSystemAccessOriginPrivateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemAccessOriginPrivateEnabled -> get attr')

    def get_fileSystemObserverEnabled(self):
        val = self._attr.get('fileSystemObserverEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fileSystemObserverEnabled -> get attr')

    def get_findTextInReadonlyTextInputEnabled(self):
        val = self._attr.get('findTextInReadonlyTextInputEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.findTextInReadonlyTextInputEnabled -> get attr')

    def get_fledgeEnabled(self):
        val = self._attr.get('fledgeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeEnabled -> get attr')

    def get_fledgeBiddingAndAuctionServerAPIEnabled(self):
        val = self._attr.get('fledgeBiddingAndAuctionServerAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeBiddingAndAuctionServerAPIEnabled -> get attr')

    def get_fledgeClearOriginJoinedAdInterestGroupsEnabled(self):
        val = self._attr.get('fledgeClearOriginJoinedAdInterestGroupsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeClearOriginJoinedAdInterestGroupsEnabled -> get attr')

    def get_fledgeCreateAuctionNonceSynchronousResolutionEnabled(self):
        val = self._attr.get('fledgeCreateAuctionNonceSynchronousResolutionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeCreateAuctionNonceSynchronousResolutionEnabled -> get attr')

    def get_fledgeCustomMaxAuctionAdComponentsEnabled(self):
        val = self._attr.get('fledgeCustomMaxAuctionAdComponentsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeCustomMaxAuctionAdComponentsEnabled -> get attr')

    def get_fledgeDeprecatedRenderURLReplacementsEnabled(self):
        val = self._attr.get('fledgeDeprecatedRenderURLReplacementsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeDeprecatedRenderURLReplacementsEnabled -> get attr')

    def get_fledgeDirectFromSellerSignalsHeaderAdSlotEnabled(self):
        val = self._attr.get('fledgeDirectFromSellerSignalsHeaderAdSlotEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeDirectFromSellerSignalsHeaderAdSlotEnabled -> get attr')

    def get_fledgeFeatureDetectAllEnabled(self):
        val = self._attr.get('fledgeFeatureDetectAllEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeFeatureDetectAllEnabled -> get attr')

    def get_fledgeFeatureDetectionEnabled(self):
        val = self._attr.get('fledgeFeatureDetectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeFeatureDetectionEnabled -> get attr')

    def get_fledgeMultiBidEnabled(self):
        val = self._attr.get('fledgeMultiBidEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeMultiBidEnabled -> get attr')

    def get_fledgeNegativeTargetingEnabled(self):
        val = self._attr.get('fledgeNegativeTargetingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeNegativeTargetingEnabled -> get attr')

    def get_fledgePermitCrossOriginTrustedSignalsEnabled(self):
        val = self._attr.get('fledgePermitCrossOriginTrustedSignalsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgePermitCrossOriginTrustedSignalsEnabled -> get attr')

    def get_fledgeRealTimeReportingEnabled(self):
        val = self._attr.get('fledgeRealTimeReportingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeRealTimeReportingEnabled -> get attr')

    def get_fledgeReportingTimeoutEnabled(self):
        val = self._attr.get('fledgeReportingTimeoutEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeReportingTimeoutEnabled -> get attr')

    def get_fledgeTrustedBiddingSignalsSlotSizeEnabled(self):
        val = self._attr.get('fledgeTrustedBiddingSignalsSlotSizeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fledgeTrustedBiddingSignalsSlotSizeEnabled -> get attr')

    def get_fluentOverlayScrollbarsEnabled(self):
        val = self._attr.get('fluentOverlayScrollbarsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fluentOverlayScrollbarsEnabled -> get attr')

    def get_fluentScrollbarsEnabled(self):
        val = self._attr.get('fluentScrollbarsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fluentScrollbarsEnabled -> get attr')

    def get_flushParserBeforeCreatingCustomElementsEnabled(self):
        val = self._attr.get('flushParserBeforeCreatingCustomElementsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.flushParserBeforeCreatingCustomElementsEnabled -> get attr')

    def get_focusgroupEnabled(self):
        val = self._attr.get('focusgroupEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.focusgroupEnabled -> get attr')

    def get_fontAccessEnabled(self):
        val = self._attr.get('fontAccessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontAccessEnabled -> get attr')

    def get_fontationsFontBackendEnabled(self):
        val = self._attr.get('fontationsFontBackendEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontationsFontBackendEnabled -> get attr')

    def get_fontFamilyPostscriptMatchingCTMigrationEnabled(self):
        val = self._attr.get('fontFamilyPostscriptMatchingCTMigrationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontFamilyPostscriptMatchingCTMigrationEnabled -> get attr')

    def get_fontFamilyStyleMatchingCTMigrationEnabled(self):
        val = self._attr.get('fontFamilyStyleMatchingCTMigrationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontFamilyStyleMatchingCTMigrationEnabled -> get attr')

    def get_fontMatchingCTMigrationEnabled(self):
        val = self._attr.get('fontMatchingCTMigrationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontMatchingCTMigrationEnabled -> get attr')

    def get_fontPaletteAnimationEnabled(self):
        val = self._attr.get('fontPaletteAnimationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontPaletteAnimationEnabled -> get attr')

    def get_fontSrcLocalMatchingEnabled(self):
        val = self._attr.get('fontSrcLocalMatchingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontSrcLocalMatchingEnabled -> get attr')

    def get_fontVariantEmojiEnabled(self):
        val = self._attr.get('fontVariantEmojiEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontVariantEmojiEnabled -> get attr')

    def get_fontVariationSequencesEnabled(self):
        val = self._attr.get('fontVariationSequencesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fontVariationSequencesEnabled -> get attr')

    def get_forcedColorsEnabled(self):
        val = self._attr.get('forcedColorsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.forcedColorsEnabled -> get attr')

    def get_forcedColorsPreserveParentColorEnabled(self):
        val = self._attr.get('forcedColorsPreserveParentColorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.forcedColorsPreserveParentColorEnabled -> get attr')

    def get_forceEagerMeasureMemoryEnabled(self):
        val = self._attr.get('forceEagerMeasureMemoryEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.forceEagerMeasureMemoryEnabled -> get attr')

    def get_forceReduceMotionEnabled(self):
        val = self._attr.get('forceReduceMotionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.forceReduceMotionEnabled -> get attr')

    def get_forceTallerSelectPopupEnabled(self):
        val = self._attr.get('forceTallerSelectPopupEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.forceTallerSelectPopupEnabled -> get attr')

    def get_formattedTextEnabled(self):
        val = self._attr.get('formattedTextEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.formattedTextEnabled -> get attr')

    def get_formControlRestoreStateIfAutocompleteOffEnabled(self):
        val = self._attr.get('formControlRestoreStateIfAutocompleteOffEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.formControlRestoreStateIfAutocompleteOffEnabled -> get attr')

    def get_formControlsVerticalWritingModeDirectionSupportEnabled(self):
        val = self._attr.get('formControlsVerticalWritingModeDirectionSupportEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.formControlsVerticalWritingModeDirectionSupportEnabled -> get attr')

    def get_formStateRestoreCallbackCallWithStateEnabled(self):
        val = self._attr.get('formStateRestoreCallbackCallWithStateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.formStateRestoreCallbackCallWithStateEnabled -> get attr')

    def get_fractionalScrollOffsetsEnabled(self):
        val = self._attr.get('fractionalScrollOffsetsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fractionalScrollOffsetsEnabled -> get attr')

    def get_freezeFramesOnVisibilityEnabled(self):
        val = self._attr.get('freezeFramesOnVisibilityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.freezeFramesOnVisibilityEnabled -> get attr')

    def get_fullscreenPopupWindowsEnabled(self):
        val = self._attr.get('fullscreenPopupWindowsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.fullscreenPopupWindowsEnabled -> get attr')

    def get_gamepadButtonAxisEventsEnabled(self):
        val = self._attr.get('gamepadButtonAxisEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.gamepadButtonAxisEventsEnabled -> get attr')

    def get_gamepadMultitouchEnabled(self):
        val = self._attr.get('gamepadMultitouchEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.gamepadMultitouchEnabled -> get attr')

    def get_getAllScreensMediaEnabled(self):
        val = self._attr.get('getAllScreensMediaEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.getAllScreensMediaEnabled -> get attr')

    def get_getDisplayMediaEnabled(self):
        val = self._attr.get('getDisplayMediaEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.getDisplayMediaEnabled -> get attr')

    def get_getDisplayMediaRequiresUserActivationEnabled(self):
        val = self._attr.get('getDisplayMediaRequiresUserActivationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.getDisplayMediaRequiresUserActivationEnabled -> get attr')

    def get_getNextSiblingPositionWhenLastChildEnabled(self):
        val = self._attr.get('getNextSiblingPositionWhenLastChildEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.getNextSiblingPositionWhenLastChildEnabled -> get attr')

    def get_groupEffectEnabled(self):
        val = self._attr.get('groupEffectEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.groupEffectEnabled -> get attr')

    def get_handwritingRecognitionEnabled(self):
        val = self._attr.get('handwritingRecognitionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.handwritingRecognitionEnabled -> get attr')

    def get_hangingWhitespaceDoesNotDependOnAlignmentEnabled(self):
        val = self._attr.get('hangingWhitespaceDoesNotDependOnAlignmentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.hangingWhitespaceDoesNotDependOnAlignmentEnabled -> get attr')

    def get_hasUAVisualTransitionEnabled(self):
        val = self._attr.get('hasUAVisualTransitionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.hasUAVisualTransitionEnabled -> get attr')

    def get_highlightInheritanceEnabled(self):
        val = self._attr.get('highlightInheritanceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.highlightInheritanceEnabled -> get attr')

    def get_highlightPointerEventsEnabled(self):
        val = self._attr.get('highlightPointerEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.highlightPointerEventsEnabled -> get attr')

    def get_hitTestOpaquenessEnabled(self):
        val = self._attr.get('hitTestOpaquenessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.hitTestOpaquenessEnabled -> get attr')

    def get_hrefTranslateEnabled(self):
        val = self._attr.get('hrefTranslateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.hrefTranslateEnabled -> get attr')

    def get_htmlAnchorAttributeEnabled(self):
        val = self._attr.get('htmlAnchorAttributeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlAnchorAttributeEnabled -> get attr')

    def get_htmlInterestTargetAttributeEnabled(self):
        val = self._attr.get('htmlInterestTargetAttributeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlInterestTargetAttributeEnabled -> get attr')

    def get_htmlInvokeActionsV2Enabled(self):
        val = self._attr.get('htmlInvokeActionsV2Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlInvokeActionsV2Enabled -> get attr')

    def get_htmlInvokeTargetAttributeEnabled(self):
        val = self._attr.get('htmlInvokeTargetAttributeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlInvokeTargetAttributeEnabled -> get attr')

    def get_htmlParserYieldAndDelayOftenForTestingEnabled(self):
        val = self._attr.get('htmlParserYieldAndDelayOftenForTestingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlParserYieldAndDelayOftenForTestingEnabled -> get attr')

    def get_htmlPopoverActionHoverEnabled(self):
        val = self._attr.get('htmlPopoverActionHoverEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlPopoverActionHoverEnabled -> get attr')

    def get_htmlPopoverHintEnabled(self):
        val = self._attr.get('htmlPopoverHintEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlPopoverHintEnabled -> get attr')

    def get_htmlSearchElementEnabled(self):
        val = self._attr.get('htmlSearchElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlSearchElementEnabled -> get attr')

    def get_htmlSelectElementShowPickerEnabled(self):
        val = self._attr.get('htmlSelectElementShowPickerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlSelectElementShowPickerEnabled -> get attr')

    def get_htmlSelectListElementEnabled(self):
        val = self._attr.get('htmlSelectListElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlSelectListElementEnabled -> get attr')

    def get_htmlUnsafeMethodsEnabled(self):
        val = self._attr.get('htmlUnsafeMethodsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.htmlUnsafeMethodsEnabled -> get attr')

    def get_ignoresCSSTextTransformsForPlainTextCopyEnabled(self):
        val = self._attr.get('ignoresCSSTextTransformsForPlainTextCopyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.ignoresCSSTextTransformsForPlainTextCopyEnabled -> get attr')

    def get_implicitRootScrollerEnabled(self):
        val = self._attr.get('implicitRootScrollerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.implicitRootScrollerEnabled -> get attr')

    def set_implicitRootScrollerEnabled(self, val):
        self._attr['implicitRootScrollerEnabled'] = val

    def get_importAttributesDisallowUnknownKeysEnabled(self):
        val = self._attr.get('importAttributesDisallowUnknownKeysEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.importAttributesDisallowUnknownKeysEnabled -> get attr')

    def get_importMapIntegrityEnabled(self):
        val = self._attr.get('importMapIntegrityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.importMapIntegrityEnabled -> get attr')

    def get_improvedXMLErrorsEnabled(self):
        val = self._attr.get('improvedXMLErrorsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.improvedXMLErrorsEnabled -> get attr')

    def get_incomingCallNotificationsEnabled(self):
        val = self._attr.get('incomingCallNotificationsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.incomingCallNotificationsEnabled -> get attr')

    def get_incrementLocalSurfaceIdForMainframeSameDocNavigationEnabled(self):
        val = self._attr.get('incrementLocalSurfaceIdForMainframeSameDocNavigationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.incrementLocalSurfaceIdForMainframeSameDocNavigationEnabled -> get attr')

    def get_inertDisplayTransitionEnabled(self):
        val = self._attr.get('inertDisplayTransitionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inertDisplayTransitionEnabled -> get attr')

    def get_inertElementNonEditableEnabled(self):
        val = self._attr.get('inertElementNonEditableEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inertElementNonEditableEnabled -> get attr')

    def get_inertElementNonSearchableEnabled(self):
        val = self._attr.get('inertElementNonSearchableEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inertElementNonSearchableEnabled -> get attr')

    def get_infiniteCullRectEnabled(self):
        val = self._attr.get('infiniteCullRectEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.infiniteCullRectEnabled -> get attr')

    def get_inheritUserModifyWithoutContenteditableEnabled(self):
        val = self._attr.get('inheritUserModifyWithoutContenteditableEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inheritUserModifyWithoutContenteditableEnabled -> get attr')

    def get_inlineBlockInSameLineEnabled(self):
        val = self._attr.get('inlineBlockInSameLineEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inlineBlockInSameLineEnabled -> get attr')

    def get_innerHTMLParserFastpathLogFailureEnabled(self):
        val = self._attr.get('innerHTMLParserFastpathLogFailureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.innerHTMLParserFastpathLogFailureEnabled -> get attr')

    def get_inputClipRulesCssEnabled(self):
        val = self._attr.get('inputClipRulesCssEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inputClipRulesCssEnabled -> get attr')

    def get_inputMultipleFieldsUIEnabled(self):
        val = self._attr.get('inputMultipleFieldsUIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inputMultipleFieldsUIEnabled -> get attr')

    def get_inputStepCurrentValueValidationEnabled(self):
        val = self._attr.get('inputStepCurrentValueValidationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inputStepCurrentValueValidationEnabled -> get attr')

    def get_inputTypeSupportInsertLinkEnabled(self):
        val = self._attr.get('inputTypeSupportInsertLinkEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.inputTypeSupportInsertLinkEnabled -> get attr')

    def get_insertBlockquoteBeforeOuterBlockEnabled(self):
        val = self._attr.get('insertBlockquoteBeforeOuterBlockEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.insertBlockquoteBeforeOuterBlockEnabled -> get attr')

    def get_insertLineBreakIfPhrasingContentEnabled(self):
        val = self._attr.get('insertLineBreakIfPhrasingContentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.insertLineBreakIfPhrasingContentEnabled -> get attr')

    def get_installedAppEnabled(self):
        val = self._attr.get('installedAppEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.installedAppEnabled -> get attr')

    def get_interoperablePrivateAttributionEnabled(self):
        val = self._attr.get('interoperablePrivateAttributionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.interoperablePrivateAttributionEnabled -> get attr')

    def get_interruptComposedScrollbarDisappearanceEnabled(self):
        val = self._attr.get('interruptComposedScrollbarDisappearanceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.interruptComposedScrollbarDisappearanceEnabled -> get attr')

    def get_intersectionObserverScrollMarginEnabled(self):
        val = self._attr.get('intersectionObserverScrollMarginEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.intersectionObserverScrollMarginEnabled -> get attr')

    def get_intersectionOptimizationEnabled(self):
        val = self._attr.get('intersectionOptimizationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.intersectionOptimizationEnabled -> get attr')

    def get_invertedColorsEnabled(self):
        val = self._attr.get('invertedColorsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.invertedColorsEnabled -> get attr')

    def get_invisibleSVGAnimationThrottlingEnabled(self):
        val = self._attr.get('invisibleSVGAnimationThrottlingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.invisibleSVGAnimationThrottlingEnabled -> get attr')

    def get_javaScriptCompileHintsMagicRuntimeEnabled(self):
        val = self._attr.get('javaScriptCompileHintsMagicRuntimeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.javaScriptCompileHintsMagicRuntimeEnabled -> get attr')

    def get_keyboardAccessibleTooltipEnabled(self):
        val = self._attr.get('keyboardAccessibleTooltipEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.keyboardAccessibleTooltipEnabled -> get attr')

    def get_keyboardFocusableScrollersEnabled(self):
        val = self._attr.get('keyboardFocusableScrollersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.keyboardFocusableScrollersEnabled -> get attr')

    def get_keyboardFocusableScrollersOptOutEnabled(self):
        val = self._attr.get('keyboardFocusableScrollersOptOutEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.keyboardFocusableScrollersOptOutEnabled -> get attr')

    def get_labelEventHandlerCallSuperEnabled(self):
        val = self._attr.get('labelEventHandlerCallSuperEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.labelEventHandlerCallSuperEnabled -> get attr')

    def get_langAttributeAwareFormControlUIEnabled(self):
        val = self._attr.get('langAttributeAwareFormControlUIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.langAttributeAwareFormControlUIEnabled -> get attr')

    def set_langAttributeAwareFormControlUIEnabled(self, val):
        self._attr['langAttributeAwareFormControlUIEnabled'] = val

    def get_lastSuccessfulPositionOptionEnabled(self):
        val = self._attr.get('lastSuccessfulPositionOptionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lastSuccessfulPositionOptionEnabled -> get attr')

    def get_layoutBaselineFixEnabled(self):
        val = self._attr.get('layoutBaselineFixEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.layoutBaselineFixEnabled -> get attr')

    def get_layoutBlockButtonEnabled(self):
        val = self._attr.get('layoutBlockButtonEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.layoutBlockButtonEnabled -> get attr')

    def get_layoutFlexNewRowAlgorithmV3Enabled(self):
        val = self._attr.get('layoutFlexNewRowAlgorithmV3Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.layoutFlexNewRowAlgorithmV3Enabled -> get attr')

    def get_layoutFlexUnderInvalidationFixEnabled(self):
        val = self._attr.get('layoutFlexUnderInvalidationFixEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.layoutFlexUnderInvalidationFixEnabled -> get attr')

    def get_layoutIgnoreMarginsForStickyEnabled(self):
        val = self._attr.get('layoutIgnoreMarginsForStickyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.layoutIgnoreMarginsForStickyEnabled -> get attr')

    def get_layoutNGShapeCacheEnabled(self):
        val = self._attr.get('layoutNGShapeCacheEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.layoutNGShapeCacheEnabled -> get attr')

    def get_layoutSegmentationFastPathForObjectReplacementEnabled(self):
        val = self._attr.get('layoutSegmentationFastPathForObjectReplacementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.layoutSegmentationFastPathForObjectReplacementEnabled -> get attr')

    def get_lazyInitializeMediaControlsEnabled(self):
        val = self._attr.get('lazyInitializeMediaControlsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lazyInitializeMediaControlsEnabled -> get attr')

    def get_lazyLoadScrollMarginEnabled(self):
        val = self._attr.get('lazyLoadScrollMarginEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lazyLoadScrollMarginEnabled -> get attr')

    def get_lazyLoadScrollMarginIframeEnabled(self):
        val = self._attr.get('lazyLoadScrollMarginIframeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lazyLoadScrollMarginIframeEnabled -> get attr')

    def get_lcpAnimatedImagesWebExposedEnabled(self):
        val = self._attr.get('lcpAnimatedImagesWebExposedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lcpAnimatedImagesWebExposedEnabled -> get attr')

    def get_lcpMouseoverHeuristicsEnabled(self):
        val = self._attr.get('lcpMouseoverHeuristicsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lcpMouseoverHeuristicsEnabled -> get attr')

    def get_lcpMultipleUpdatesPerElementEnabled(self):
        val = self._attr.get('lcpMultipleUpdatesPerElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lcpMultipleUpdatesPerElementEnabled -> get attr')

    def get_legacyWindowsDWriteFontFallbackEnabled(self):
        val = self._attr.get('legacyWindowsDWriteFontFallbackEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.legacyWindowsDWriteFontFallbackEnabled -> get attr')

    def get_limitThirdPartyCookiesEnabled(self):
        val = self._attr.get('limitThirdPartyCookiesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.limitThirdPartyCookiesEnabled -> get attr')

    def get_lockedModeEnabled(self):
        val = self._attr.get('lockedModeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.lockedModeEnabled -> get attr')

    def get_longAnimationFrameTimingEnabled(self):
        val = self._attr.get('longAnimationFrameTimingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.longAnimationFrameTimingEnabled -> get attr')

    def get_longTaskFromLongAnimationFrameEnabled(self):
        val = self._attr.get('longTaskFromLongAnimationFrameEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.longTaskFromLongAnimationFrameEnabled -> get attr')

    def get_macFontsDeprecateFontTraitsWorkaroundEnabled(self):
        val = self._attr.get('macFontsDeprecateFontTraitsWorkaroundEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.macFontsDeprecateFontTraitsWorkaroundEnabled -> get attr')

    def get_machineLearningCommonEnabled(self):
        val = self._attr.get('machineLearningCommonEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.machineLearningCommonEnabled -> get attr')

    def get_machineLearningModelLoaderEnabled(self):
        val = self._attr.get('machineLearningModelLoaderEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.machineLearningModelLoaderEnabled -> get attr')

    def get_machineLearningNeuralNetworkEnabled(self):
        val = self._attr.get('machineLearningNeuralNetworkEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.machineLearningNeuralNetworkEnabled -> get attr')

    def get_managedConfigurationEnabled(self):
        val = self._attr.get('managedConfigurationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.managedConfigurationEnabled -> get attr')

    def get_measureMemoryEnabled(self):
        val = self._attr.get('measureMemoryEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.measureMemoryEnabled -> get attr')

    def get_mediaCapabilitiesDynamicRangeEnabled(self):
        val = self._attr.get('mediaCapabilitiesDynamicRangeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCapabilitiesDynamicRangeEnabled -> get attr')

    def get_mediaCapabilitiesEncodingInfoEnabled(self):
        val = self._attr.get('mediaCapabilitiesEncodingInfoEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCapabilitiesEncodingInfoEnabled -> get attr')

    def get_mediaCapabilitiesSpatialAudioEnabled(self):
        val = self._attr.get('mediaCapabilitiesSpatialAudioEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCapabilitiesSpatialAudioEnabled -> get attr')

    def get_mediaCaptureEnabled(self):
        val = self._attr.get('mediaCaptureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCaptureEnabled -> get attr')

    def get_mediaCaptureBackgroundBlurEnabled(self):
        val = self._attr.get('mediaCaptureBackgroundBlurEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCaptureBackgroundBlurEnabled -> get attr')

    def get_mediaCaptureCameraControlsEnabled(self):
        val = self._attr.get('mediaCaptureCameraControlsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCaptureCameraControlsEnabled -> get attr')

    def get_mediaCaptureConfigurationChangeEnabled(self):
        val = self._attr.get('mediaCaptureConfigurationChangeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCaptureConfigurationChangeEnabled -> get attr')

    def get_mediaCaptureVoiceIsolationEnabled(self):
        val = self._attr.get('mediaCaptureVoiceIsolationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCaptureVoiceIsolationEnabled -> get attr')

    def get_mediaCastOverlayButtonEnabled(self):
        val = self._attr.get('mediaCastOverlayButtonEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaCastOverlayButtonEnabled -> get attr')

    def get_mediaControlsExpandGestureEnabled(self):
        val = self._attr.get('mediaControlsExpandGestureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaControlsExpandGestureEnabled -> get attr')

    def get_mediaControlsOverlayPlayButtonEnabled(self):
        val = self._attr.get('mediaControlsOverlayPlayButtonEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaControlsOverlayPlayButtonEnabled -> get attr')

    def set_mediaControlsOverlayPlayButtonEnabled(self, val):
        self._attr['mediaControlsOverlayPlayButtonEnabled'] = val

    def get_mediaElementVolumeGreaterThanOneEnabled(self):
        val = self._attr.get('mediaElementVolumeGreaterThanOneEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaElementVolumeGreaterThanOneEnabled -> get attr')

    def get_mediaEngagementBypassAutoplayPoliciesEnabled(self):
        val = self._attr.get('mediaEngagementBypassAutoplayPoliciesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaEngagementBypassAutoplayPoliciesEnabled -> get attr')

    def get_mediaLatencyHintEnabled(self):
        val = self._attr.get('mediaLatencyHintEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaLatencyHintEnabled -> get attr')

    def get_mediaPreviewsOptOutEnabled(self):
        val = self._attr.get('mediaPreviewsOptOutEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaPreviewsOptOutEnabled -> get attr')

    def get_mediaQueryNavigationControlsEnabled(self):
        val = self._attr.get('mediaQueryNavigationControlsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaQueryNavigationControlsEnabled -> get attr')

    def get_mediaRecorderUseMediaVideoEncoderEnabled(self):
        val = self._attr.get('mediaRecorderUseMediaVideoEncoderEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaRecorderUseMediaVideoEncoderEnabled -> get attr')

    def get_mediaSessionEnabled(self):
        val = self._attr.get('mediaSessionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaSessionEnabled -> get attr')

    def get_mediaSessionChapterInformationEnabled(self):
        val = self._attr.get('mediaSessionChapterInformationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaSessionChapterInformationEnabled -> get attr')

    def get_mediaSessionEnterPictureInPictureEnabled(self):
        val = self._attr.get('mediaSessionEnterPictureInPictureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaSessionEnterPictureInPictureEnabled -> get attr')

    def get_mediaSourceExperimentalEnabled(self):
        val = self._attr.get('mediaSourceExperimentalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaSourceExperimentalEnabled -> get attr')

    def get_mediaSourceExtensionsForWebCodecsEnabled(self):
        val = self._attr.get('mediaSourceExtensionsForWebCodecsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaSourceExtensionsForWebCodecsEnabled -> get attr')

    def get_mediaSourceNewAbortAndDurationEnabled(self):
        val = self._attr.get('mediaSourceNewAbortAndDurationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaSourceNewAbortAndDurationEnabled -> get attr')

    def get_mediaStreamTrackTransferEnabled(self):
        val = self._attr.get('mediaStreamTrackTransferEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mediaStreamTrackTransferEnabled -> get attr')

    def get_messagePortCloseEventEnabled(self):
        val = self._attr.get('messagePortCloseEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.messagePortCloseEventEnabled -> get attr')

    def get_metaRefreshNoFractionalEnabled(self):
        val = self._attr.get('metaRefreshNoFractionalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.metaRefreshNoFractionalEnabled -> get attr')

    def get_middleClickAutoscrollEnabled(self):
        val = self._attr.get('middleClickAutoscrollEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.middleClickAutoscrollEnabled -> get attr')

    def get_mobileLayoutThemeEnabled(self):
        val = self._attr.get('mobileLayoutThemeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mobileLayoutThemeEnabled -> get attr')

    def get_modelExecutionAPIEnabled(self):
        val = self._attr.get('modelExecutionAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.modelExecutionAPIEnabled -> get attr')

    def get_mojoJSEnabled(self):
        val = self._attr.get('mojoJSEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mojoJSEnabled -> get attr')

    def get_mojoJSTestEnabled(self):
        val = self._attr.get('mojoJSTestEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mojoJSTestEnabled -> get attr')

    def get_mouseDragFromIframeOnCancelledMouseDownEnabled(self):
        val = self._attr.get('mouseDragFromIframeOnCancelledMouseDownEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mouseDragFromIframeOnCancelledMouseDownEnabled -> get attr')

    def get_mouseDragOnCancelledMouseMoveEnabled(self):
        val = self._attr.get('mouseDragOnCancelledMouseMoveEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mouseDragOnCancelledMouseMoveEnabled -> get attr')

    def get_moveEndingSelectionToListChildEnabled(self):
        val = self._attr.get('moveEndingSelectionToListChildEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.moveEndingSelectionToListChildEnabled -> get attr')

    def get_multiSelectDeselectWhenOnlyOptionEnabled(self):
        val = self._attr.get('multiSelectDeselectWhenOnlyOptionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.multiSelectDeselectWhenOnlyOptionEnabled -> get attr')

    def get_mutationEventsEnabled(self):
        val = self._attr.get('mutationEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mutationEventsEnabled -> get attr')

    def get_mutationEventsSpecialTrialMessageEnabled(self):
        val = self._attr.get('mutationEventsSpecialTrialMessageEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.mutationEventsSpecialTrialMessageEnabled -> get attr')

    def get_navigateEventCommitBehaviorEnabled(self):
        val = self._attr.get('navigateEventCommitBehaviorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.navigateEventCommitBehaviorEnabled -> get attr')

    def get_navigateEventSourceElementEnabled(self):
        val = self._attr.get('navigateEventSourceElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.navigateEventSourceElementEnabled -> get attr')

    def get_navigationActivationEnabled(self):
        val = self._attr.get('navigationActivationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.navigationActivationEnabled -> get attr')

    def get_navigationIdEnabled(self):
        val = self._attr.get('navigationIdEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.navigationIdEnabled -> get attr')

    def get_navigatorContentUtilsEnabled(self):
        val = self._attr.get('navigatorContentUtilsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.navigatorContentUtilsEnabled -> get attr')

    def get_netInfoConstantTypeEnabled(self):
        val = self._attr.get('netInfoConstantTypeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.netInfoConstantTypeEnabled -> get attr')

    def get_netInfoDownlinkMaxEnabled(self):
        val = self._attr.get('netInfoDownlinkMaxEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.netInfoDownlinkMaxEnabled -> get attr')

    def get_newFilterMapRectEnabled(self):
        val = self._attr.get('newFilterMapRectEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.newFilterMapRectEnabled -> get attr')

    def get_newGetFocusableAreaBehaviorEnabled(self):
        val = self._attr.get('newGetFocusableAreaBehaviorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.newGetFocusableAreaBehaviorEnabled -> get attr')

    def get_nextSiblingPositionUseNextCandidateEnabled(self):
        val = self._attr.get('nextSiblingPositionUseNextCandidateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.nextSiblingPositionUseNextCandidateEnabled -> get attr')

    def get_noIdleEncodingForWebTestsEnabled(self):
        val = self._attr.get('noIdleEncodingForWebTestsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.noIdleEncodingForWebTestsEnabled -> get attr')

    def get_noIncreasingEndOffsetOnSplittingTextNodesEnabled(self):
        val = self._attr.get('noIncreasingEndOffsetOnSplittingTextNodesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.noIncreasingEndOffsetOnSplittingTextNodesEnabled -> get attr')

    def get_noIntrinsicSizeOverrideEnabled(self):
        val = self._attr.get('noIntrinsicSizeOverrideEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.noIntrinsicSizeOverrideEnabled -> get attr')

    def get_nonComposedEnterLeaveEventsEnabled(self):
        val = self._attr.get('nonComposedEnterLeaveEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.nonComposedEnterLeaveEventsEnabled -> get attr')

    def get_nonEmptyBlockquotesOnOutdentingEnabled(self):
        val = self._attr.get('nonEmptyBlockquotesOnOutdentingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.nonEmptyBlockquotesOnOutdentingEnabled -> get attr')

    def get_nonStandardAppearanceValuesHighUsageEnabled(self):
        val = self._attr.get('nonStandardAppearanceValuesHighUsageEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.nonStandardAppearanceValuesHighUsageEnabled -> get attr')

    def get_nonStandardAppearanceValueSliderVerticalEnabled(self):
        val = self._attr.get('nonStandardAppearanceValueSliderVerticalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.nonStandardAppearanceValueSliderVerticalEnabled -> get attr')

    def get_notificationConstructorEnabled(self):
        val = self._attr.get('notificationConstructorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.notificationConstructorEnabled -> get attr')

    def get_notificationContentImageEnabled(self):
        val = self._attr.get('notificationContentImageEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.notificationContentImageEnabled -> get attr')

    def get_notificationsEnabled(self):
        val = self._attr.get('notificationsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.notificationsEnabled -> get attr')

    def get_notificationTriggersEnabled(self):
        val = self._attr.get('notificationTriggersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.notificationTriggersEnabled -> get attr')

    def get_noVarySearchPrefetchEnabled(self):
        val = self._attr.get('noVarySearchPrefetchEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.noVarySearchPrefetchEnabled -> get attr')

    def get_observableAPIEnabled(self):
        val = self._attr.get('observableAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.observableAPIEnabled -> get attr')

    def get_offMainThreadCSSPaintEnabled(self):
        val = self._attr.get('offMainThreadCSSPaintEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.offMainThreadCSSPaintEnabled -> get attr')

    def get_offscreenCanvasCommitEnabled(self):
        val = self._attr.get('offscreenCanvasCommitEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.offscreenCanvasCommitEnabled -> get attr')

    def get_omitBlurEventOnElementRemovalEnabled(self):
        val = self._attr.get('omitBlurEventOnElementRemovalEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.omitBlurEventOnElementRemovalEnabled -> get attr')

    def get_onDeviceChangeEnabled(self):
        val = self._attr.get('onDeviceChangeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.onDeviceChangeEnabled -> get attr')

    def get_optionElementAlwaysUseLabelEnabled(self):
        val = self._attr.get('optionElementAlwaysUseLabelEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.optionElementAlwaysUseLabelEnabled -> get attr')

    def get_orientationEventEnabled(self):
        val = self._attr.get('orientationEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.orientationEventEnabled -> get attr')

    def get_originIsolationHeaderEnabled(self):
        val = self._attr.get('originIsolationHeaderEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originIsolationHeaderEnabled -> get attr')

    def get_originPolicyEnabled(self):
        val = self._attr.get('originPolicyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originPolicyEnabled -> get attr')

    def get_originTrialsSampleAPIEnabled(self):
        val = self._attr.get('originTrialsSampleAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIEnabled -> get attr')

    def get_originTrialsSampleAPIBrowserReadWriteEnabled(self):
        val = self._attr.get('originTrialsSampleAPIBrowserReadWriteEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIBrowserReadWriteEnabled -> get attr')

    def get_originTrialsSampleAPIDependentEnabled(self):
        val = self._attr.get('originTrialsSampleAPIDependentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIDependentEnabled -> get attr')

    def get_originTrialsSampleAPIDeprecationEnabled(self):
        val = self._attr.get('originTrialsSampleAPIDeprecationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIDeprecationEnabled -> get attr')

    def get_originTrialsSampleAPIExpiryGracePeriodEnabled(self):
        val = self._attr.get('originTrialsSampleAPIExpiryGracePeriodEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIExpiryGracePeriodEnabled -> get attr')

    def get_originTrialsSampleAPIExpiryGracePeriodThirdPartyEnabled(self):
        val = self._attr.get('originTrialsSampleAPIExpiryGracePeriodThirdPartyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIExpiryGracePeriodThirdPartyEnabled -> get attr')

    def get_originTrialsSampleAPIImpliedEnabled(self):
        val = self._attr.get('originTrialsSampleAPIImpliedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIImpliedEnabled -> get attr')

    def get_originTrialsSampleAPIInvalidOSEnabled(self):
        val = self._attr.get('originTrialsSampleAPIInvalidOSEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIInvalidOSEnabled -> get attr')

    def get_originTrialsSampleAPINavigationEnabled(self):
        val = self._attr.get('originTrialsSampleAPINavigationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPINavigationEnabled -> get attr')

    def get_originTrialsSampleAPIPersistentExpiryGracePeriodEnabled(self):
        val = self._attr.get('originTrialsSampleAPIPersistentExpiryGracePeriodEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIPersistentExpiryGracePeriodEnabled -> get attr')

    def get_originTrialsSampleAPIPersistentFeatureEnabled(self):
        val = self._attr.get('originTrialsSampleAPIPersistentFeatureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIPersistentFeatureEnabled -> get attr')

    def get_originTrialsSampleAPIPersistentInvalidOSEnabled(self):
        val = self._attr.get('originTrialsSampleAPIPersistentInvalidOSEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIPersistentInvalidOSEnabled -> get attr')

    def get_originTrialsSampleAPIPersistentThirdPartyDeprecationFeatureEnabled(self):
        val = self._attr.get('originTrialsSampleAPIPersistentThirdPartyDeprecationFeatureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIPersistentThirdPartyDeprecationFeatureEnabled -> get attr')

    def get_originTrialsSampleAPIThirdPartyEnabled(self):
        val = self._attr.get('originTrialsSampleAPIThirdPartyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.originTrialsSampleAPIThirdPartyEnabled -> get attr')

    def get_overscrollCustomizationEnabled(self):
        val = self._attr.get('overscrollCustomizationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.overscrollCustomizationEnabled -> get attr')

    def get_pageFreezeOptInEnabled(self):
        val = self._attr.get('pageFreezeOptInEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pageFreezeOptInEnabled -> get attr')

    def get_pageFreezeOptOutEnabled(self):
        val = self._attr.get('pageFreezeOptOutEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pageFreezeOptOutEnabled -> get attr')

    def get_pageMarginBoxesEnabled(self):
        val = self._attr.get('pageMarginBoxesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pageMarginBoxesEnabled -> get attr')

    def get_pagePopupEnabled(self):
        val = self._attr.get('pagePopupEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pagePopupEnabled -> get attr')

    def get_pageRevealEventEnabled(self):
        val = self._attr.get('pageRevealEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pageRevealEventEnabled -> get attr')

    def get_pageSwapEventEnabled(self):
        val = self._attr.get('pageSwapEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pageSwapEventEnabled -> get attr')

    def get_paintHoldingForIframesEnabled(self):
        val = self._attr.get('paintHoldingForIframesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paintHoldingForIframesEnabled -> get attr')

    def get_paintHoldingForLocalIframesEnabled(self):
        val = self._attr.get('paintHoldingForLocalIframesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paintHoldingForLocalIframesEnabled -> get attr')

    def get_paintUnderInvalidationCheckingEnabled(self):
        val = self._attr.get('paintUnderInvalidationCheckingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paintUnderInvalidationCheckingEnabled -> get attr')

    def set_paintUnderInvalidationCheckingEnabled(self, val):
        self._attr['paintUnderInvalidationCheckingEnabled'] = val

    def get_parakeetEnabled(self):
        val = self._attr.get('parakeetEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.parakeetEnabled -> get attr')

    def get_passwordRevealEnabled(self):
        val = self._attr.get('passwordRevealEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.passwordRevealEnabled -> get attr')

    def get_passwordStrongLabelEnabled(self):
        val = self._attr.get('passwordStrongLabelEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.passwordStrongLabelEnabled -> get attr')

    def get_paymentAppEnabled(self):
        val = self._attr.get('paymentAppEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paymentAppEnabled -> get attr')

    def get_paymentInstrumentsEnabled(self):
        val = self._attr.get('paymentInstrumentsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paymentInstrumentsEnabled -> get attr')

    def get_paymentLinkDetectionEnabled(self):
        val = self._attr.get('paymentLinkDetectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paymentLinkDetectionEnabled -> get attr')

    def get_paymentMethodChangeEventEnabled(self):
        val = self._attr.get('paymentMethodChangeEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paymentMethodChangeEventEnabled -> get attr')

    def get_paymentRequestEnabled(self):
        val = self._attr.get('paymentRequestEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.paymentRequestEnabled -> get attr')

    def get_percentBasedScrollingEnabled(self):
        val = self._attr.get('percentBasedScrollingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.percentBasedScrollingEnabled -> get attr')

    def set_percentBasedScrollingEnabled(self, val):
        self._attr['percentBasedScrollingEnabled'] = val

    def get_performanceManagerInstrumentationEnabled(self):
        val = self._attr.get('performanceManagerInstrumentationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.performanceManagerInstrumentationEnabled -> get attr')

    def get_performanceMarkFeatureUsageEnabled(self):
        val = self._attr.get('performanceMarkFeatureUsageEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.performanceMarkFeatureUsageEnabled -> get attr')

    def get_performanceNavigateSystemEntropyEnabled(self):
        val = self._attr.get('performanceNavigateSystemEntropyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.performanceNavigateSystemEntropyEnabled -> get attr')

    def get_periodicBackgroundSyncEnabled(self):
        val = self._attr.get('periodicBackgroundSyncEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.periodicBackgroundSyncEnabled -> get attr')

    def get_perMethodCanMakePaymentQuotaEnabled(self):
        val = self._attr.get('perMethodCanMakePaymentQuotaEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.perMethodCanMakePaymentQuotaEnabled -> get attr')

    def get_permissionElementEnabled(self):
        val = self._attr.get('permissionElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.permissionElementEnabled -> get attr')

    def get_permissionsEnabled(self):
        val = self._attr.get('permissionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.permissionsEnabled -> get attr')

    def get_permissionsRequestRevokeEnabled(self):
        val = self._attr.get('permissionsRequestRevokeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.permissionsRequestRevokeEnabled -> get attr')

    def get_pNaClEnabled(self):
        val = self._attr.get('pNaClEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pNaClEnabled -> get attr')

    def get_pointerCaptureLostOnRemovalDuringCaptureEnabled(self):
        val = self._attr.get('pointerCaptureLostOnRemovalDuringCaptureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pointerCaptureLostOnRemovalDuringCaptureEnabled -> get attr')

    def get_pointerEventDeviceIdEnabled(self):
        val = self._attr.get('pointerEventDeviceIdEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pointerEventDeviceIdEnabled -> get attr')

    def get_positionOutsideTabSpanCheckSiblingNodeEnabled(self):
        val = self._attr.get('positionOutsideTabSpanCheckSiblingNodeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.positionOutsideTabSpanCheckSiblingNodeEnabled -> get attr')

    def get_preciseMemoryInfoEnabled(self):
        val = self._attr.get('preciseMemoryInfoEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.preciseMemoryInfoEnabled -> get attr')

    def get_preferDefaultScrollbarStylesEnabled(self):
        val = self._attr.get('preferDefaultScrollbarStylesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.preferDefaultScrollbarStylesEnabled -> get attr')

    def get_preferNonCompositedScrollingEnabled(self):
        val = self._attr.get('preferNonCompositedScrollingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.preferNonCompositedScrollingEnabled -> get attr')

    def set_preferNonCompositedScrollingEnabled(self, val):
        self._attr['preferNonCompositedScrollingEnabled'] = val

    def get_prefersReducedDataEnabled(self):
        val = self._attr.get('prefersReducedDataEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.prefersReducedDataEnabled -> get attr')

    def get_prefixedVideoFullscreenEnabled(self):
        val = self._attr.get('prefixedVideoFullscreenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.prefixedVideoFullscreenEnabled -> get attr')

    def get_prePaintAncestorsOfMissedOOFEnabled(self):
        val = self._attr.get('prePaintAncestorsOfMissedOOFEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.prePaintAncestorsOfMissedOOFEnabled -> get attr')

    def get_prerender2Enabled(self):
        val = self._attr.get('prerender2Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.prerender2Enabled -> get attr')

    def get_presentationEnabled(self):
        val = self._attr.get('presentationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.presentationEnabled -> get attr')

    def get_prettyPrintJSONDocumentEnabled(self):
        val = self._attr.get('prettyPrintJSONDocumentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.prettyPrintJSONDocumentEnabled -> get attr')

    def get_preventReadingSystemAccentColorEnabled(self):
        val = self._attr.get('preventReadingSystemAccentColorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.preventReadingSystemAccentColorEnabled -> get attr')

    def get_privacySandboxAdsAPISEnabled(self):
        val = self._attr.get('privacySandboxAdsAPISEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privacySandboxAdsAPISEnabled -> get attr')

    def get_privateAggregationApiFilteringIdsEnabled(self):
        val = self._attr.get('privateAggregationApiFilteringIdsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privateAggregationApiFilteringIdsEnabled -> get attr')

    def get_privateAggregationAuctionReportBuyerDebugModeConfigEnabled(self):
        val = self._attr.get('privateAggregationAuctionReportBuyerDebugModeConfigEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privateAggregationAuctionReportBuyerDebugModeConfigEnabled -> get attr')

    def get_privateNetworkAccessNonSecureContextsAllowedEnabled(self):
        val = self._attr.get('privateNetworkAccessNonSecureContextsAllowedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privateNetworkAccessNonSecureContextsAllowedEnabled -> get attr')

    def get_privateNetworkAccessNullIpAddressEnabled(self):
        val = self._attr.get('privateNetworkAccessNullIpAddressEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privateNetworkAccessNullIpAddressEnabled -> get attr')

    def get_privateNetworkAccessPermissionPromptEnabled(self):
        val = self._attr.get('privateNetworkAccessPermissionPromptEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privateNetworkAccessPermissionPromptEnabled -> get attr')

    def get_privateStateTokensEnabled(self):
        val = self._attr.get('privateStateTokensEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privateStateTokensEnabled -> get attr')

    def get_privateStateTokensAlwaysAllowIssuanceEnabled(self):
        val = self._attr.get('privateStateTokensAlwaysAllowIssuanceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.privateStateTokensAlwaysAllowIssuanceEnabled -> get attr')

    def get_protectedOriginTrialsSampleAPIEnabled(self):
        val = self._attr.get('protectedOriginTrialsSampleAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.protectedOriginTrialsSampleAPIEnabled -> get attr')

    def get_protectedOriginTrialsSampleAPIDependentEnabled(self):
        val = self._attr.get('protectedOriginTrialsSampleAPIDependentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.protectedOriginTrialsSampleAPIDependentEnabled -> get attr')

    def get_protectedOriginTrialsSampleAPIImpliedEnabled(self):
        val = self._attr.get('protectedOriginTrialsSampleAPIImpliedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.protectedOriginTrialsSampleAPIImpliedEnabled -> get attr')

    def get_pushMessagingEnabled(self):
        val = self._attr.get('pushMessagingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pushMessagingEnabled -> get attr')

    def get_pushMessagingSubscriptionChangeEnabled(self):
        val = self._attr.get('pushMessagingSubscriptionChangeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.pushMessagingSubscriptionChangeEnabled -> get attr')

    def get_quickIntensiveWakeUpThrottlingAfterLoadingEnabled(self):
        val = self._attr.get('quickIntensiveWakeUpThrottlingAfterLoadingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.quickIntensiveWakeUpThrottlingAfterLoadingEnabled -> get attr')

    def get_quotaChangeEnabled(self):
        val = self._attr.get('quotaChangeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.quotaChangeEnabled -> get attr')

    def get_rasterInducingScrollEnabled(self):
        val = self._attr.get('rasterInducingScrollEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rasterInducingScrollEnabled -> get attr')

    def get_readableStreamAsyncIterableEnabled(self):
        val = self._attr.get('readableStreamAsyncIterableEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.readableStreamAsyncIterableEnabled -> get attr')

    def get_recollectInlinesReserveCapacityEnabled(self):
        val = self._attr.get('recollectInlinesReserveCapacityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.recollectInlinesReserveCapacityEnabled -> get attr')

    def get_reduceAcceptLanguageEnabled(self):
        val = self._attr.get('reduceAcceptLanguageEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.reduceAcceptLanguageEnabled -> get attr')

    def get_reduceCookieIPCsEnabled(self):
        val = self._attr.get('reduceCookieIPCsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.reduceCookieIPCsEnabled -> get attr')

    def get_reduceUserAgentAndroidVersionDeviceModelEnabled(self):
        val = self._attr.get('reduceUserAgentAndroidVersionDeviceModelEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.reduceUserAgentAndroidVersionDeviceModelEnabled -> get attr')

    def get_reduceUserAgentMinorVersionEnabled(self):
        val = self._attr.get('reduceUserAgentMinorVersionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.reduceUserAgentMinorVersionEnabled -> get attr')

    def get_reduceUserAgentPlatformOsCpuEnabled(self):
        val = self._attr.get('reduceUserAgentPlatformOsCpuEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.reduceUserAgentPlatformOsCpuEnabled -> get attr')

    def get_regionCaptureEnabled(self):
        val = self._attr.get('regionCaptureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.regionCaptureEnabled -> get attr')

    def get_remotePlaybackEnabled(self):
        val = self._attr.get('remotePlaybackEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.remotePlaybackEnabled -> get attr')

    def get_remotePlaybackBackendEnabled(self):
        val = self._attr.get('remotePlaybackBackendEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.remotePlaybackBackendEnabled -> get attr')

    def set_remotePlaybackBackendEnabled(self, val):
        self._attr['remotePlaybackBackendEnabled'] = val

    def get_removeDanglingMarkupInTargetEnabled(self):
        val = self._attr.get('removeDanglingMarkupInTargetEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.removeDanglingMarkupInTargetEnabled -> get attr')

    def get_removeDataUrlInSvgUseEnabled(self):
        val = self._attr.get('removeDataUrlInSvgUseEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.removeDataUrlInSvgUseEnabled -> get attr')

    def get_removeMobileViewportDoubleTapEnabled(self):
        val = self._attr.get('removeMobileViewportDoubleTapEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.removeMobileViewportDoubleTapEnabled -> get attr')

    def get_removeNodeHavingChildrenIfFullySelectedEnabled(self):
        val = self._attr.get('removeNodeHavingChildrenIfFullySelectedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.removeNodeHavingChildrenIfFullySelectedEnabled -> get attr')

    def get_removeVisibleSelectionInDOMSelectionEnabled(self):
        val = self._attr.get('removeVisibleSelectionInDOMSelectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.removeVisibleSelectionInDOMSelectionEnabled -> get attr')

    def get_renderBlockingInlineModuleScriptEnabled(self):
        val = self._attr.get('renderBlockingInlineModuleScriptEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.renderBlockingInlineModuleScriptEnabled -> get attr')

    def get_renderBlockingStatusEnabled(self):
        val = self._attr.get('renderBlockingStatusEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.renderBlockingStatusEnabled -> get attr')

    def get_renderPriorityAttributeEnabled(self):
        val = self._attr.get('renderPriorityAttributeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.renderPriorityAttributeEnabled -> get attr')

    def get_reportVisibleLineBoundsEnabled(self):
        val = self._attr.get('reportVisibleLineBoundsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.reportVisibleLineBoundsEnabled -> get attr')

    def get_resourceTimingContentTypeEnabled(self):
        val = self._attr.get('resourceTimingContentTypeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.resourceTimingContentTypeEnabled -> get attr')

    def get_resourceTimingUseCORSForBodySizesEnabled(self):
        val = self._attr.get('resourceTimingUseCORSForBodySizesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.resourceTimingUseCORSForBodySizesEnabled -> get attr')

    def get_restrictGamepadAccessEnabled(self):
        val = self._attr.get('restrictGamepadAccessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.restrictGamepadAccessEnabled -> get attr')

    def get_rewindFloatsEnabled(self):
        val = self._attr.get('rewindFloatsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rewindFloatsEnabled -> get attr')

    def get_rtcAudioJitterBufferMaxPacketsEnabled(self):
        val = self._attr.get('rtcAudioJitterBufferMaxPacketsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcAudioJitterBufferMaxPacketsEnabled -> get attr')

    def get_rtcEncodedAudioFrameAbsCaptureTimeEnabled(self):
        val = self._attr.get('rtcEncodedAudioFrameAbsCaptureTimeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcEncodedAudioFrameAbsCaptureTimeEnabled -> get attr')

    def get_rtcEncodedFrameSetMetadataEnabled(self):
        val = self._attr.get('rtcEncodedFrameSetMetadataEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcEncodedFrameSetMetadataEnabled -> get attr')

    def get_rtcEncodedVideoFrameAdditionalMetadataEnabled(self):
        val = self._attr.get('rtcEncodedVideoFrameAdditionalMetadataEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcEncodedVideoFrameAdditionalMetadataEnabled -> get attr')

    def get_rtcJitterBufferTargetEnabled(self):
        val = self._attr.get('rtcJitterBufferTargetEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcJitterBufferTargetEnabled -> get attr')

    def get_rtcLegacyCallbackBasedGetStatsEnabled(self):
        val = self._attr.get('rtcLegacyCallbackBasedGetStatsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcLegacyCallbackBasedGetStatsEnabled -> get attr')

    def get_rtcRtpEncodingParametersCodecEnabled(self):
        val = self._attr.get('rtcRtpEncodingParametersCodecEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcRtpEncodingParametersCodecEnabled -> get attr')

    def get_rtcRtpHeaderExtensionControlEnabled(self):
        val = self._attr.get('rtcRtpHeaderExtensionControlEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcRtpHeaderExtensionControlEnabled -> get attr')

    def get_rtcRtpTransportEnabled(self):
        val = self._attr.get('rtcRtpTransportEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcRtpTransportEnabled -> get attr')

    def get_rtcStatsRelativePacketArrivalDelayEnabled(self):
        val = self._attr.get('rtcStatsRelativePacketArrivalDelayEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcStatsRelativePacketArrivalDelayEnabled -> get attr')

    def get_rtcSvcScalabilityModeEnabled(self):
        val = self._attr.get('rtcSvcScalabilityModeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rtcSvcScalabilityModeEnabled -> get attr')

    def get_rubyAnnotationSpaceFixEnabled(self):
        val = self._attr.get('rubyAnnotationSpaceFixEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rubyAnnotationSpaceFixEnabled -> get attr')

    def get_rubyLineBreakableEnabled(self):
        val = self._attr.get('rubyLineBreakableEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rubyLineBreakableEnabled -> get attr')

    def get_rubyLineEdgeAlignmentEnabled(self):
        val = self._attr.get('rubyLineEdgeAlignmentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rubyLineEdgeAlignmentEnabled -> get attr')

    def get_rubyShortHeuristicsEnabled(self):
        val = self._attr.get('rubyShortHeuristicsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.rubyShortHeuristicsEnabled -> get attr')

    def get_runMicrotaskBeforeXmlCustomElementEnabled(self):
        val = self._attr.get('runMicrotaskBeforeXmlCustomElementEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.runMicrotaskBeforeXmlCustomElementEnabled -> get attr')

    def get_sanitizerAPIEnabled(self):
        val = self._attr.get('sanitizerAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sanitizerAPIEnabled -> get attr')

    def get_schedulerYieldEnabled(self):
        val = self._attr.get('schedulerYieldEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.schedulerYieldEnabled -> get attr')

    def get_scopedCustomElementRegistryEnabled(self):
        val = self._attr.get('scopedCustomElementRegistryEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scopedCustomElementRegistryEnabled -> get attr')

    def get_scriptedSpeechRecognitionEnabled(self):
        val = self._attr.get('scriptedSpeechRecognitionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scriptedSpeechRecognitionEnabled -> get attr')

    def get_scriptedSpeechSynthesisEnabled(self):
        val = self._attr.get('scriptedSpeechSynthesisEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scriptedSpeechSynthesisEnabled -> get attr')

    def get_scrollbarColorEnabled(self):
        val = self._attr.get('scrollbarColorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollbarColorEnabled -> get attr')

    def get_scrollbarWidthEnabled(self):
        val = self._attr.get('scrollbarWidthEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollbarWidthEnabled -> get attr')

    def get_scrollEndEventsEnabled(self):
        val = self._attr.get('scrollEndEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollEndEventsEnabled -> get attr')

    def get_scrollNodeForOverflowHiddenEnabled(self):
        val = self._attr.get('scrollNodeForOverflowHiddenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollNodeForOverflowHiddenEnabled -> get attr')

    def get_scrollTimelineEnabled(self):
        val = self._attr.get('scrollTimelineEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollTimelineEnabled -> get attr')

    def get_scrollTimelineAlwaysOnCompositorEnabled(self):
        val = self._attr.get('scrollTimelineAlwaysOnCompositorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollTimelineAlwaysOnCompositorEnabled -> get attr')

    def get_scrollTimelineCurrentTimeEnabled(self):
        val = self._attr.get('scrollTimelineCurrentTimeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollTimelineCurrentTimeEnabled -> get attr')

    def get_scrollTimelineOnCompositorEnabled(self):
        val = self._attr.get('scrollTimelineOnCompositorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollTimelineOnCompositorEnabled -> get attr')

    def get_scrollTopLeftInteropEnabled(self):
        val = self._attr.get('scrollTopLeftInteropEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.scrollTopLeftInteropEnabled -> get attr')

    def get_searchTextHighlightPseudoEnabled(self):
        val = self._attr.get('searchTextHighlightPseudoEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.searchTextHighlightPseudoEnabled -> get attr')

    def get_securePaymentConfirmationEnabled(self):
        val = self._attr.get('securePaymentConfirmationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.securePaymentConfirmationEnabled -> get attr')

    def get_securePaymentConfirmationDebugEnabled(self):
        val = self._attr.get('securePaymentConfirmationDebugEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.securePaymentConfirmationDebugEnabled -> get attr')

    def get_securePaymentConfirmationNetworkAndIssuerIconsEnabled(self):
        val = self._attr.get('securePaymentConfirmationNetworkAndIssuerIconsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.securePaymentConfirmationNetworkAndIssuerIconsEnabled -> get attr')

    def get_securePaymentConfirmationOptOutEnabled(self):
        val = self._attr.get('securePaymentConfirmationOptOutEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.securePaymentConfirmationOptOutEnabled -> get attr')

    def get_selectionRespectsColorsEnabled(self):
        val = self._attr.get('selectionRespectsColorsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.selectionRespectsColorsEnabled -> get attr')

    def get_sendBeaconThrowForBlobWithNonSimpleTypeEnabled(self):
        val = self._attr.get('sendBeaconThrowForBlobWithNonSimpleTypeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sendBeaconThrowForBlobWithNonSimpleTypeEnabled -> get attr')

    def get_sensorExtraClassesEnabled(self):
        val = self._attr.get('sensorExtraClassesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sensorExtraClassesEnabled -> get attr')

    def get_serialEnabled(self):
        val = self._attr.get('serialEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.serialEnabled -> get attr')

    def get_serializeViewTransitionStateInSPAEnabled(self):
        val = self._attr.get('serializeViewTransitionStateInSPAEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.serializeViewTransitionStateInSPAEnabled -> get attr')

    def get_serialPortConnectedEnabled(self):
        val = self._attr.get('serialPortConnectedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.serialPortConnectedEnabled -> get attr')

    def get_serviceWorkerClientLifecycleStateEnabled(self):
        val = self._attr.get('serviceWorkerClientLifecycleStateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.serviceWorkerClientLifecycleStateEnabled -> get attr')

    def get_serviceWorkerStaticRouterEnabled(self):
        val = self._attr.get('serviceWorkerStaticRouterEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.serviceWorkerStaticRouterEnabled -> get attr')

    def get_serviceWorkerStaticRouterTimingInfoEnabled(self):
        val = self._attr.get('serviceWorkerStaticRouterTimingInfoEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.serviceWorkerStaticRouterTimingInfoEnabled -> get attr')

    def get_setSequentialFocusStartingPointEnabled(self):
        val = self._attr.get('setSequentialFocusStartingPointEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.setSequentialFocusStartingPointEnabled -> get attr')

    def get_shapeResultCachedPreviousSafeToBreakOffsetEnabled(self):
        val = self._attr.get('shapeResultCachedPreviousSafeToBreakOffsetEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.shapeResultCachedPreviousSafeToBreakOffsetEnabled -> get attr')

    def get_sharedArrayBufferEnabled(self):
        val = self._attr.get('sharedArrayBufferEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedArrayBufferEnabled -> get attr')

    def get_sharedArrayBufferOnDesktopEnabled(self):
        val = self._attr.get('sharedArrayBufferOnDesktopEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedArrayBufferOnDesktopEnabled -> get attr')

    def get_sharedArrayBufferUnrestrictedAccessAllowedEnabled(self):
        val = self._attr.get('sharedArrayBufferUnrestrictedAccessAllowedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedArrayBufferUnrestrictedAccessAllowedEnabled -> get attr')

    def get_sharedAutofillEnabled(self):
        val = self._attr.get('sharedAutofillEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedAutofillEnabled -> get attr')

    def get_sharedStorageAPIEnabled(self):
        val = self._attr.get('sharedStorageAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedStorageAPIEnabled -> get attr')

    def get_sharedStorageAPIM118Enabled(self):
        val = self._attr.get('sharedStorageAPIM118Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedStorageAPIM118Enabled -> get attr')

    def get_sharedStorageAPIM125Enabled(self):
        val = self._attr.get('sharedStorageAPIM125Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedStorageAPIM125Enabled -> get attr')

    def get_sharedWorkerEnabled(self):
        val = self._attr.get('sharedWorkerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.sharedWorkerEnabled -> get attr')

    def get_showPickerConsumeUserActivationEnabled(self):
        val = self._attr.get('showPickerConsumeUserActivationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.showPickerConsumeUserActivationEnabled -> get attr')

    def get_signatureBasedIntegrityEnabled(self):
        val = self._attr.get('signatureBasedIntegrityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.signatureBasedIntegrityEnabled -> get attr')

    def get_siteInitiatedMirroringEnabled(self):
        val = self._attr.get('siteInitiatedMirroringEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.siteInitiatedMirroringEnabled -> get attr')

    def get_skipAdEnabled(self):
        val = self._attr.get('skipAdEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.skipAdEnabled -> get attr')

    def get_skipPreloadScanningEnabled(self):
        val = self._attr.get('skipPreloadScanningEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.skipPreloadScanningEnabled -> get attr')

    def get_skipTouchEventFilterEnabled(self):
        val = self._attr.get('skipTouchEventFilterEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.skipTouchEventFilterEnabled -> get attr')

    def get_skipUpdateTypeForHTMLInputElementCreatedByParserEnabled(self):
        val = self._attr.get('skipUpdateTypeForHTMLInputElementCreatedByParserEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.skipUpdateTypeForHTMLInputElementCreatedByParserEnabled -> get attr')

    def get_smartCardEnabled(self):
        val = self._attr.get('smartCardEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.smartCardEnabled -> get attr')

    def get_smartZoomEnabled(self):
        val = self._attr.get('smartZoomEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.smartZoomEnabled -> get attr')

    def get_smilAutoSuspendOnLagEnabled(self):
        val = self._attr.get('smilAutoSuspendOnLagEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.smilAutoSuspendOnLagEnabled -> get attr')

    def get_softNavigationDetectionEnabled(self):
        val = self._attr.get('softNavigationDetectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.softNavigationDetectionEnabled -> get attr')

    def get_softNavigationHeuristicsEnabled(self):
        val = self._attr.get('softNavigationHeuristicsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.softNavigationHeuristicsEnabled -> get attr')

    def get_softNavigationHeuristicsExposeFPAndFCPEnabled(self):
        val = self._attr.get('softNavigationHeuristicsExposeFPAndFCPEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.softNavigationHeuristicsExposeFPAndFCPEnabled -> get attr')

    def get_speakerSelectionEnabled(self):
        val = self._attr.get('speakerSelectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speakerSelectionEnabled -> get attr')

    def get_speculationRulesDocumentRulesEnabled(self):
        val = self._attr.get('speculationRulesDocumentRulesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesDocumentRulesEnabled -> get attr')

    def get_speculationRulesDocumentRulesSelectorMatchesEnabled(self):
        val = self._attr.get('speculationRulesDocumentRulesSelectorMatchesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesDocumentRulesSelectorMatchesEnabled -> get attr')

    def get_speculationRulesEagernessEnabled(self):
        val = self._attr.get('speculationRulesEagernessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesEagernessEnabled -> get attr')

    def get_speculationRulesFetchFromHeaderEnabled(self):
        val = self._attr.get('speculationRulesFetchFromHeaderEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesFetchFromHeaderEnabled -> get attr')

    def get_speculationRulesImplicitSourceEnabled(self):
        val = self._attr.get('speculationRulesImplicitSourceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesImplicitSourceEnabled -> get attr')

    def get_speculationRulesNoVarySearchHintEnabled(self):
        val = self._attr.get('speculationRulesNoVarySearchHintEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesNoVarySearchHintEnabled -> get attr')

    def get_speculationRulesNoVarySearchHintShippedByDefaultEnabled(self):
        val = self._attr.get('speculationRulesNoVarySearchHintShippedByDefaultEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesNoVarySearchHintShippedByDefaultEnabled -> get attr')

    def get_speculationRulesPointerDownHeuristicsEnabled(self):
        val = self._attr.get('speculationRulesPointerDownHeuristicsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesPointerDownHeuristicsEnabled -> get attr')

    def get_speculationRulesPointerHoverHeuristicsEnabled(self):
        val = self._attr.get('speculationRulesPointerHoverHeuristicsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesPointerHoverHeuristicsEnabled -> get attr')

    def get_speculationRulesPrefetchFutureEnabled(self):
        val = self._attr.get('speculationRulesPrefetchFutureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesPrefetchFutureEnabled -> get attr')

    def get_speculationRulesPrefetchWithSubresourcesEnabled(self):
        val = self._attr.get('speculationRulesPrefetchWithSubresourcesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesPrefetchWithSubresourcesEnabled -> get attr')

    def get_speculationRulesRelativeToDocumentEnabled(self):
        val = self._attr.get('speculationRulesRelativeToDocumentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.speculationRulesRelativeToDocumentEnabled -> get attr')

    def get_spellCheckerReplaceRangeUseInsertTextEnabled(self):
        val = self._attr.get('spellCheckerReplaceRangeUseInsertTextEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.spellCheckerReplaceRangeUseInsertTextEnabled -> get attr')

    def get_srcsetMaxDensityEnabled(self):
        val = self._attr.get('srcsetMaxDensityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.srcsetMaxDensityEnabled -> get attr')

    def get_stableBlinkFeaturesEnabled(self):
        val = self._attr.get('stableBlinkFeaturesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.stableBlinkFeaturesEnabled -> get attr')

    def get_standardizedBrowserZoomEnabled(self):
        val = self._attr.get('standardizedBrowserZoomEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.standardizedBrowserZoomEnabled -> get attr')

    def get_staticAnimationOptimizationEnabled(self):
        val = self._attr.get('staticAnimationOptimizationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.staticAnimationOptimizationEnabled -> get attr')

    def get_storageBucketsEnabled(self):
        val = self._attr.get('storageBucketsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.storageBucketsEnabled -> get attr')

    def get_storageBucketsDurabilityEnabled(self):
        val = self._attr.get('storageBucketsDurabilityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.storageBucketsDurabilityEnabled -> get attr')

    def get_storageBucketsLocksEnabled(self):
        val = self._attr.get('storageBucketsLocksEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.storageBucketsLocksEnabled -> get attr')

    def get_strictMimeTypesForWorkersEnabled(self):
        val = self._attr.get('strictMimeTypesForWorkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.strictMimeTypesForWorkersEnabled -> get attr')

    def get_stylableSelectEnabled(self):
        val = self._attr.get('stylableSelectEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.stylableSelectEnabled -> get attr')

    def get_stylusHandwritingEnabled(self):
        val = self._attr.get('stylusHandwritingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.stylusHandwritingEnabled -> get attr')

    def get_svgContextPaintEnabled(self):
        val = self._attr.get('svgContextPaintEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.svgContextPaintEnabled -> get attr')

    def get_svgCrossOriginAttributeEnabled(self):
        val = self._attr.get('svgCrossOriginAttributeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.svgCrossOriginAttributeEnabled -> get attr')

    def get_svgFilterUserSpaceViewportForNonSvgEnabled(self):
        val = self._attr.get('svgFilterUserSpaceViewportForNonSvgEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.svgFilterUserSpaceViewportForNonSvgEnabled -> get attr')

    def get_svgNoPixelSnappingScaleAdjustmentEnabled(self):
        val = self._attr.get('svgNoPixelSnappingScaleAdjustmentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.svgNoPixelSnappingScaleAdjustmentEnabled -> get attr')

    def get_synthesizedKeyboardEventsForAccessibilityActionsEnabled(self):
        val = self._attr.get('synthesizedKeyboardEventsForAccessibilityActionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.synthesizedKeyboardEventsForAccessibilityActionsEnabled -> get attr')

    def get_systemWakeLockEnabled(self):
        val = self._attr.get('systemWakeLockEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.systemWakeLockEnabled -> get attr')

    def get_testBlinkFeatureDefaultEnabled(self):
        val = self._attr.get('testBlinkFeatureDefaultEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testBlinkFeatureDefaultEnabled -> get attr')

    def get_testFeatureEnabled(self):
        val = self._attr.get('testFeatureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testFeatureEnabled -> get attr')

    def get_testFeatureDependentEnabled(self):
        val = self._attr.get('testFeatureDependentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testFeatureDependentEnabled -> get attr')

    def get_testFeatureImpliedEnabled(self):
        val = self._attr.get('testFeatureImpliedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testFeatureImpliedEnabled -> get attr')

    def get_testFeatureProtectedEnabled(self):
        val = self._attr.get('testFeatureProtectedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testFeatureProtectedEnabled -> get attr')

    def get_testFeatureProtectedDependentEnabled(self):
        val = self._attr.get('testFeatureProtectedDependentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testFeatureProtectedDependentEnabled -> get attr')

    def get_testFeatureProtectedImpliedEnabled(self):
        val = self._attr.get('testFeatureProtectedImpliedEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testFeatureProtectedImpliedEnabled -> get attr')

    def get_testFeatureStableEnabled(self):
        val = self._attr.get('testFeatureStableEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.testFeatureStableEnabled -> get attr')

    def get_textAlignJustifyBidiIsolateEnabled(self):
        val = self._attr.get('textAlignJustifyBidiIsolateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textAlignJustifyBidiIsolateEnabled -> get attr')

    def get_textAlignLastJustifyNewLineEnabled(self):
        val = self._attr.get('textAlignLastJustifyNewLineEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textAlignLastJustifyNewLineEnabled -> get attr')

    def get_textAreaChildrenChangedStillValidatesEnabled(self):
        val = self._attr.get('textAreaChildrenChangedStillValidatesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textAreaChildrenChangedStillValidatesEnabled -> get attr')

    def get_textDecoratingBoxEnabled(self):
        val = self._attr.get('textDecoratingBoxEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textDecoratingBoxEnabled -> get attr')

    def get_textDetectorEnabled(self):
        val = self._attr.get('textDetectorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textDetectorEnabled -> get attr')

    def get_textDiffSplitFixEnabled(self):
        val = self._attr.get('textDiffSplitFixEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textDiffSplitFixEnabled -> get attr')

    def get_textFragmentAPIEnabled(self):
        val = self._attr.get('textFragmentAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textFragmentAPIEnabled -> get attr')

    def get_textFragmentIdentifiersEnabled(self):
        val = self._attr.get('textFragmentIdentifiersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textFragmentIdentifiersEnabled -> get attr')

    def get_textFragmentTapOpensContextMenuEnabled(self):
        val = self._attr.get('textFragmentTapOpensContextMenuEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textFragmentTapOpensContextMenuEnabled -> get attr')

    def get_textMetricsBaselinesEnabled(self):
        val = self._attr.get('textMetricsBaselinesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textMetricsBaselinesEnabled -> get attr')

    def get_textSizeAdjustImprovementsEnabled(self):
        val = self._attr.get('textSizeAdjustImprovementsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.textSizeAdjustImprovementsEnabled -> get attr')

    def get_timelineScopeEnabled(self):
        val = self._attr.get('timelineScopeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.timelineScopeEnabled -> get attr')

    def get_timerThrottlingForBackgroundTabsEnabled(self):
        val = self._attr.get('timerThrottlingForBackgroundTabsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.timerThrottlingForBackgroundTabsEnabled -> get attr')

    def get_timeZoneChangeEventEnabled(self):
        val = self._attr.get('timeZoneChangeEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.timeZoneChangeEventEnabled -> get attr')

    def get_topicsAPIEnabled(self):
        val = self._attr.get('topicsAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.topicsAPIEnabled -> get attr')

    def get_topicsDocumentAPIEnabled(self):
        val = self._attr.get('topicsDocumentAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.topicsDocumentAPIEnabled -> get attr')

    def get_topLevelTpcdEnabled(self):
        val = self._attr.get('topLevelTpcdEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.topLevelTpcdEnabled -> get attr')

    def get_touchDragAndContextMenuEnabled(self):
        val = self._attr.get('touchDragAndContextMenuEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.touchDragAndContextMenuEnabled -> get attr')

    def get_touchDragOnShortPressEnabled(self):
        val = self._attr.get('touchDragOnShortPressEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.touchDragOnShortPressEnabled -> get attr')

    def get_touchEventFeatureDetectionEnabled(self):
        val = self._attr.get('touchEventFeatureDetectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.touchEventFeatureDetectionEnabled -> get attr')

    def get_touchTextEditingRedesignEnabled(self):
        val = self._attr.get('touchTextEditingRedesignEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.touchTextEditingRedesignEnabled -> get attr')

    def get_tpcdEnabled(self):
        val = self._attr.get('tpcdEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.tpcdEnabled -> get attr')

    def get_translateServiceEnabled(self):
        val = self._attr.get('translateServiceEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.translateServiceEnabled -> get attr')

    def get_translationAPIEnabled(self):
        val = self._attr.get('translationAPIEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.translationAPIEnabled -> get attr')

    def get_trustedTypeBeforePolicyCreationEventEnabled(self):
        val = self._attr.get('trustedTypeBeforePolicyCreationEventEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.trustedTypeBeforePolicyCreationEventEnabled -> get attr')

    def get_trustedTypesFromLiteralEnabled(self):
        val = self._attr.get('trustedTypesFromLiteralEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.trustedTypesFromLiteralEnabled -> get attr')

    def get_trustedTypesUseCodeLikeEnabled(self):
        val = self._attr.get('trustedTypesUseCodeLikeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.trustedTypesUseCodeLikeEnabled -> get attr')

    def get_unblockTouchMoveEarlierEnabled(self):
        val = self._attr.get('unblockTouchMoveEarlierEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.unblockTouchMoveEarlierEnabled -> get attr')

    def get_unclosedFormControlIsInvalidEnabled(self):
        val = self._attr.get('unclosedFormControlIsInvalidEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.unclosedFormControlIsInvalidEnabled -> get attr')

    def get_unexposedTaskIdsEnabled(self):
        val = self._attr.get('unexposedTaskIdsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.unexposedTaskIdsEnabled -> get attr')

    def get_unownedAnimationsSkipCSSEventsEnabled(self):
        val = self._attr.get('unownedAnimationsSkipCSSEventsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.unownedAnimationsSkipCSSEventsEnabled -> get attr')

    def get_unrestrictedMeasureUserAgentSpecificMemoryEnabled(self):
        val = self._attr.get('unrestrictedMeasureUserAgentSpecificMemoryEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.unrestrictedMeasureUserAgentSpecificMemoryEnabled -> get attr')

    def get_unrestrictedSharedArrayBufferEnabled(self):
        val = self._attr.get('unrestrictedSharedArrayBufferEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.unrestrictedSharedArrayBufferEnabled -> get attr')

    def get_unrestrictedUsbEnabled(self):
        val = self._attr.get('unrestrictedUsbEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.unrestrictedUsbEnabled -> get attr')

    def get_urlAttributeFixEnabled(self):
        val = self._attr.get('urlAttributeFixEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.urlAttributeFixEnabled -> get attr')

    def get_urlParseEnabled(self):
        val = self._attr.get('urlParseEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.urlParseEnabled -> get attr')

    def get_urlPatternCompareComponentEnabled(self):
        val = self._attr.get('urlPatternCompareComponentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.urlPatternCompareComponentEnabled -> get attr')

    def get_urlPatternHasRegExpGroupsEnabled(self):
        val = self._attr.get('urlPatternHasRegExpGroupsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.urlPatternHasRegExpGroupsEnabled -> get attr')

    def get_urlPatternRegexpUnicodeSetsModeEnabled(self):
        val = self._attr.get('urlPatternRegexpUnicodeSetsModeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.urlPatternRegexpUnicodeSetsModeEnabled -> get attr')

    def get_urlPatternWildcardMoreOftenEnabled(self):
        val = self._attr.get('urlPatternWildcardMoreOftenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.urlPatternWildcardMoreOftenEnabled -> get attr')

    def get_urlSearchParamsHasAndDeleteMultipleArgsEnabled(self):
        val = self._attr.get('urlSearchParamsHasAndDeleteMultipleArgsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.urlSearchParamsHasAndDeleteMultipleArgsEnabled -> get attr')

    def get_useBeginFramePresentationFeedbackEnabled(self):
        val = self._attr.get('useBeginFramePresentationFeedbackEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.useBeginFramePresentationFeedbackEnabled -> get attr')

    def get_usedColorSchemeRootScrollbarsEnabled(self):
        val = self._attr.get('usedColorSchemeRootScrollbarsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.usedColorSchemeRootScrollbarsEnabled -> get attr')

    def get_userActivationSameOriginVisibilityEnabled(self):
        val = self._attr.get('userActivationSameOriginVisibilityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.userActivationSameOriginVisibilityEnabled -> get attr')

    def get_useUndoStepElementDispatchBeforeInputEnabled(self):
        val = self._attr.get('useUndoStepElementDispatchBeforeInputEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.useUndoStepElementDispatchBeforeInputEnabled -> get attr')

    def get_v8IdleTasksEnabled(self):
        val = self._attr.get('v8IdleTasksEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.v8IdleTasksEnabled -> get attr')

    def get_videoAutoFullscreenEnabled(self):
        val = self._attr.get('videoAutoFullscreenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.videoAutoFullscreenEnabled -> get attr')

    def set_videoAutoFullscreenEnabled(self, val):
        self._attr['videoAutoFullscreenEnabled'] = val

    def get_videoFullscreenOrientationLockEnabled(self):
        val = self._attr.get('videoFullscreenOrientationLockEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.videoFullscreenOrientationLockEnabled -> get attr')

    def get_videoRotateToFullscreenEnabled(self):
        val = self._attr.get('videoRotateToFullscreenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.videoRotateToFullscreenEnabled -> get attr')

    def get_videoTrackGeneratorEnabled(self):
        val = self._attr.get('videoTrackGeneratorEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.videoTrackGeneratorEnabled -> get attr')

    def get_videoTrackGeneratorInWindowEnabled(self):
        val = self._attr.get('videoTrackGeneratorInWindowEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.videoTrackGeneratorInWindowEnabled -> get attr')

    def get_videoTrackGeneratorInWorkerEnabled(self):
        val = self._attr.get('videoTrackGeneratorInWorkerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.videoTrackGeneratorInWorkerEnabled -> get attr')

    def get_viewportHeightClientHintHeaderEnabled(self):
        val = self._attr.get('viewportHeightClientHintHeaderEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.viewportHeightClientHintHeaderEnabled -> get attr')

    def get_viewportSegmentsEnabled(self):
        val = self._attr.get('viewportSegmentsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.viewportSegmentsEnabled -> get attr')

    def get_viewTransitionOnNavigationEnabled(self):
        val = self._attr.get('viewTransitionOnNavigationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.viewTransitionOnNavigationEnabled -> get attr')

    def get_viewTransitionOnNavigationForIframesEnabled(self):
        val = self._attr.get('viewTransitionOnNavigationForIframesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.viewTransitionOnNavigationForIframesEnabled -> get attr')

    def get_viewTransitionTypesEnabled(self):
        val = self._attr.get('viewTransitionTypesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.viewTransitionTypesEnabled -> get attr')

    def get_visibilityCollapseColumnEnabled(self):
        val = self._attr.get('visibilityCollapseColumnEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.visibilityCollapseColumnEnabled -> get attr')

    def get_visualViewportOnScrollEndEnabled(self):
        val = self._attr.get('visualViewportOnScrollEndEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.visualViewportOnScrollEndEnabled -> get attr')

    def get_vttCueDisplayRubyEnabled(self):
        val = self._attr.get('vttCueDisplayRubyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.vttCueDisplayRubyEnabled -> get attr')

    def get_wakeLockEnabled(self):
        val = self._attr.get('wakeLockEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.wakeLockEnabled -> get attr')

    def get_warnOnContentVisibilityRenderAccessEnabled(self):
        val = self._attr.get('warnOnContentVisibilityRenderAccessEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.warnOnContentVisibilityRenderAccessEnabled -> get attr')

    def get_webAnimationsSVGEnabled(self):
        val = self._attr.get('webAnimationsSVGEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAnimationsSVGEnabled -> get attr')

    def get_webAppLaunchQueueEnabled(self):
        val = self._attr.get('webAppLaunchQueueEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAppLaunchQueueEnabled -> get attr')

    def get_webAppScopeExtensionsEnabled(self):
        val = self._attr.get('webAppScopeExtensionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAppScopeExtensionsEnabled -> get attr')

    def get_webAppsLockScreenEnabled(self):
        val = self._attr.get('webAppsLockScreenEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAppsLockScreenEnabled -> get attr')

    def get_webAppTabStripEnabled(self):
        val = self._attr.get('webAppTabStripEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAppTabStripEnabled -> get attr')

    def get_webAppTabStripCustomizationsEnabled(self):
        val = self._attr.get('webAppTabStripCustomizationsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAppTabStripCustomizationsEnabled -> get attr')

    def get_webAppTranslationsEnabled(self):
        val = self._attr.get('webAppTranslationsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAppTranslationsEnabled -> get attr')

    def get_webAppUrlHandlingEnabled(self):
        val = self._attr.get('webAppUrlHandlingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAppUrlHandlingEnabled -> get attr')

    def get_webAssemblyJSPromiseIntegrationEnabled(self):
        val = self._attr.get('webAssemblyJSPromiseIntegrationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAssemblyJSPromiseIntegrationEnabled -> get attr')

    def get_webAssemblyJSStringBuiltinsEnabled(self):
        val = self._attr.get('webAssemblyJSStringBuiltinsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAssemblyJSStringBuiltinsEnabled -> get attr')

    def get_webAuthEnabled(self):
        val = self._attr.get('webAuthEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthEnabled -> get attr')

    def get_webAuthAuthenticatorAttachmentEnabled(self):
        val = self._attr.get('webAuthAuthenticatorAttachmentEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthAuthenticatorAttachmentEnabled -> get attr')

    def get_webAuthenticationHintsEnabled(self):
        val = self._attr.get('webAuthenticationHintsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthenticationHintsEnabled -> get attr')

    def get_webAuthenticationJSONSerializationEnabled(self):
        val = self._attr.get('webAuthenticationJSONSerializationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthenticationJSONSerializationEnabled -> get attr')

    def get_webAuthenticationLargeBlobExtensionEnabled(self):
        val = self._attr.get('webAuthenticationLargeBlobExtensionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthenticationLargeBlobExtensionEnabled -> get attr')

    def get_webAuthenticationPRFEnabled(self):
        val = self._attr.get('webAuthenticationPRFEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthenticationPRFEnabled -> get attr')

    def get_webAuthenticationRemoteDesktopSupportEnabled(self):
        val = self._attr.get('webAuthenticationRemoteDesktopSupportEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthenticationRemoteDesktopSupportEnabled -> get attr')

    def get_webAuthenticationSupplementalPubKeysEnabled(self):
        val = self._attr.get('webAuthenticationSupplementalPubKeysEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webAuthenticationSupplementalPubKeysEnabled -> get attr')

    def get_webBluetoothEnabled(self):
        val = self._attr.get('webBluetoothEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webBluetoothEnabled -> get attr')

    def get_webBluetoothGetDevicesEnabled(self):
        val = self._attr.get('webBluetoothGetDevicesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webBluetoothGetDevicesEnabled -> get attr')

    def get_webBluetoothScanningEnabled(self):
        val = self._attr.get('webBluetoothScanningEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webBluetoothScanningEnabled -> get attr')

    def get_webBluetoothWatchAdvertisementsEnabled(self):
        val = self._attr.get('webBluetoothWatchAdvertisementsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webBluetoothWatchAdvertisementsEnabled -> get attr')

    def get_webcodecsCopyToRGBEnabled(self):
        val = self._attr.get('webcodecsCopyToRGBEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webcodecsCopyToRGBEnabled -> get attr')

    def get_webcodecsHBDFormatsEnabled(self):
        val = self._attr.get('webcodecsHBDFormatsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webcodecsHBDFormatsEnabled -> get attr')

    def get_webCryptoCurve25519Enabled(self):
        val = self._attr.get('webCryptoCurve25519Enabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webCryptoCurve25519Enabled -> get attr')

    def get_webExposedScrollOffsetEnabled(self):
        val = self._attr.get('webExposedScrollOffsetEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webExposedScrollOffsetEnabled -> get attr')

    def get_webFontResizeLCPEnabled(self):
        val = self._attr.get('webFontResizeLCPEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webFontResizeLCPEnabled -> get attr')

    def get_webglDeveloperExtensionsEnabled(self):
        val = self._attr.get('webglDeveloperExtensionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webglDeveloperExtensionsEnabled -> get attr')

    def get_webglDraftExtensionsEnabled(self):
        val = self._attr.get('webglDraftExtensionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webglDraftExtensionsEnabled -> get attr')

    def get_webglDrawingBufferStorageEnabled(self):
        val = self._attr.get('webglDrawingBufferStorageEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webglDrawingBufferStorageEnabled -> get attr')

    def get_webglImageChromiumEnabled(self):
        val = self._attr.get('webglImageChromiumEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webglImageChromiumEnabled -> get attr')

    def get_webgpuAdapterInfoAttributeEnabled(self):
        val = self._attr.get('webgpuAdapterInfoAttributeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webgpuAdapterInfoAttributeEnabled -> get attr')

    def get_webgpuDeveloperFeaturesEnabled(self):
        val = self._attr.get('webgpuDeveloperFeaturesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webgpuDeveloperFeaturesEnabled -> get attr')

    def get_webgpuExperimentalFeaturesEnabled(self):
        val = self._attr.get('webgpuExperimentalFeaturesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webgpuExperimentalFeaturesEnabled -> get attr')

    def get_webHIDEnabled(self):
        val = self._attr.get('webHIDEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webHIDEnabled -> get attr')

    def get_webHIDOnServiceWorkersEnabled(self):
        val = self._attr.get('webHIDOnServiceWorkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webHIDOnServiceWorkersEnabled -> get attr')

    def get_webIdentityDigitalCredentialsEnabled(self):
        val = self._attr.get('webIdentityDigitalCredentialsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webIdentityDigitalCredentialsEnabled -> get attr')

    def get_webIDLBigIntUsesToBigIntEnabled(self):
        val = self._attr.get('webIDLBigIntUsesToBigIntEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webIDLBigIntUsesToBigIntEnabled -> get attr')

    def get_webNFCEnabled(self):
        val = self._attr.get('webNFCEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webNFCEnabled -> get attr')

    def get_webOTPEnabled(self):
        val = self._attr.get('webOTPEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webOTPEnabled -> get attr')

    def get_webOTPAssertionFeaturePolicyEnabled(self):
        val = self._attr.get('webOTPAssertionFeaturePolicyEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webOTPAssertionFeaturePolicyEnabled -> get attr')

    def get_webPreferencesEnabled(self):
        val = self._attr.get('webPreferencesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webPreferencesEnabled -> get attr')

    def get_webPrintingEnabled(self):
        val = self._attr.get('webPrintingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webPrintingEnabled -> get attr')

    def get_webSerialBluetoothEnabled(self):
        val = self._attr.get('webSerialBluetoothEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webSerialBluetoothEnabled -> get attr')

    def get_webShareEnabled(self):
        val = self._attr.get('webShareEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webShareEnabled -> get attr')

    def get_websocketHTTPURLEnabled(self):
        val = self._attr.get('websocketHTTPURLEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.websocketHTTPURLEnabled -> get attr')

    def get_websocketStreamEnabled(self):
        val = self._attr.get('websocketStreamEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.websocketStreamEnabled -> get attr')

    def get_webTransportCustomCertificatesEnabled(self):
        val = self._attr.get('webTransportCustomCertificatesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webTransportCustomCertificatesEnabled -> get attr')

    def get_webTransportStatsEnabled(self):
        val = self._attr.get('webTransportStatsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webTransportStatsEnabled -> get attr')

    def get_webUSBEnabled(self):
        val = self._attr.get('webUSBEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webUSBEnabled -> get attr')

    def get_webUSBOnDedicatedWorkersEnabled(self):
        val = self._attr.get('webUSBOnDedicatedWorkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webUSBOnDedicatedWorkersEnabled -> get attr')

    def get_webUSBOnServiceWorkersEnabled(self):
        val = self._attr.get('webUSBOnServiceWorkersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webUSBOnServiceWorkersEnabled -> get attr')

    def get_webViewXREquestedWithDeprecationEnabled(self):
        val = self._attr.get('webViewXREquestedWithDeprecationEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webViewXREquestedWithDeprecationEnabled -> get attr')

    def get_webVTTRegionsEnabled(self):
        val = self._attr.get('webVTTRegionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webVTTRegionsEnabled -> get attr')

    def get_webXREnabled(self):
        val = self._attr.get('webXREnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXREnabled -> get attr')

    def get_webXREnabledFeaturesEnabled(self):
        val = self._attr.get('webXREnabledFeaturesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXREnabledFeaturesEnabled -> get attr')

    def get_webXRFrameRateEnabled(self):
        val = self._attr.get('webXRFrameRateEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRFrameRateEnabled -> get attr')

    def get_webXRFrontFacingEnabled(self):
        val = self._attr.get('webXRFrontFacingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRFrontFacingEnabled -> get attr')

    def get_webXRHandInputEnabled(self):
        val = self._attr.get('webXRHandInputEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRHandInputEnabled -> get attr')

    def get_webXRHitTestEntityTypesEnabled(self):
        val = self._attr.get('webXRHitTestEntityTypesEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRHitTestEntityTypesEnabled -> get attr')

    def get_webXRImageTrackingEnabled(self):
        val = self._attr.get('webXRImageTrackingEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRImageTrackingEnabled -> get attr')

    def get_webXRLayersEnabled(self):
        val = self._attr.get('webXRLayersEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRLayersEnabled -> get attr')

    def get_webXRPlaneDetectionEnabled(self):
        val = self._attr.get('webXRPlaneDetectionEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRPlaneDetectionEnabled -> get attr')

    def get_webXRPoseMotionDataEnabled(self):
        val = self._attr.get('webXRPoseMotionDataEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRPoseMotionDataEnabled -> get attr')

    def get_webXRSpecParityEnabled(self):
        val = self._attr.get('webXRSpecParityEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.webXRSpecParityEnabled -> get attr')

    def get_wgiGamepadTriggerRumbleEnabled(self):
        val = self._attr.get('wgiGamepadTriggerRumbleEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.wgiGamepadTriggerRumbleEnabled -> get attr')

    def get_windowDefaultStatusEnabled(self):
        val = self._attr.get('windowDefaultStatusEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.windowDefaultStatusEnabled -> get attr')

    def get_windowPlacementFullscreenOnScreensChangeEnabled(self):
        val = self._attr.get('windowPlacementFullscreenOnScreensChangeEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.windowPlacementFullscreenOnScreensChangeEnabled -> get attr')

    def get_writingSuggestionsEnabled(self):
        val = self._attr.get('writingSuggestionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.writingSuggestionsEnabled -> get attr')

    def get_xmlParserMergeAdjacentCDataSectionsEnabled(self):
        val = self._attr.get('xmlParserMergeAdjacentCDataSectionsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.xmlParserMergeAdjacentCDataSectionsEnabled -> get attr')

    def get_xpathLangUseAsciiCaseEnabled(self):
        val = self._attr.get('xpathLangUseAsciiCaseEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.xpathLangUseAsciiCaseEnabled -> get attr')

    def get_zeroCopyTabCaptureEnabled(self):
        val = self._attr.get('zeroCopyTabCaptureEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internal_runtime_flags.py -> InternalRuntimeFlags.zeroCopyTabCaptureEnabled -> get attr')
