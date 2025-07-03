from .flags import *


@construct_0003101
class Internals:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    LAYER_TREE_INCLUDES_INVALIDATIONS = 2
    LAYER_TREE_INCLUDES_DETAILED_INVALIDATIONS = 4

    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_internals.py -> Internals.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_internals.py -> Internals.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_internals.py -> Internals.__v8_index_del__')
            
    def __v8_index_enum__(self, *args):
        logger.debug('patch -> v8_internals.py -> Internals.__v8_index_enum__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_internals.py -> Internals.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_internals.py -> Internals.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("pagePopupWindow", "get_pagePopupWindow", None, 0, 1, 0, 0, 0, 0, 1),
        ("settings", "get_settings", None, 0, 1, 0, 0, 0, 0, 1),
        ("runtimeFlags", "get_runtimeFlags", None, 0, 1, 0, 0, 0, 0, 1),
        ("workerThreadCount", "get_workerThreadCount", None, 0, 1, 0, 0, 0, 0, 1),
        ("cursorUpdatePending", "get_cursorUpdatePending", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibleSelectionAnchorNode", "get_visibleSelectionAnchorNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibleSelectionAnchorOffset", "get_visibleSelectionAnchorOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibleSelectionFocusNode", "get_visibleSelectionFocusNode", None, 0, 1, 0, 0, 0, 0, 1),
        ("visibleSelectionFocusOffset", "get_visibleSelectionFocusOffset", None, 0, 1, 0, 0, 0, 0, 1),
        ("textAffinity", "get_textAffinity", None, 0, 1, 0, 0, 0, 0, 1),
        ("length", "get_length", None, 0, 1, 0, 0, 0, 0, 1),
        ("unscopableAttribute", "get_unscopableAttribute", None, 0, 1, 0, 0, 0, 0, 1),
        ("overlayScrollbarsEnabled", "get_overlayScrollbarsEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("peerConnectionCountLimit", "get_peerConnectionCountLimit", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("DisableIntersectionObserverThrottleDelay", "fn_DisableIntersectionObserverThrottleDelay", 0, 0, 1, 0, 0, 0, 0),
        ("LCPPrediction", "fn_LCPPrediction", 1, 0, 1, 0, 1, 0, 0),
        ("SetSupportsDraggableRegions", "fn_SetSupportsDraggableRegions", 1, 0, 1, 0, 0, 0, 0),
        ("ShadowRootMode", "fn_ShadowRootMode", 1, 0, 1, 0, 0, 0, 0),
        ("absoluteCaretBounds", "fn_absoluteCaretBounds", 0, 0, 1, 0, 0, 0, 0),
        ("activeMarkerCountForNode", "fn_activeMarkerCountForNode", 1, 0, 1, 0, 0, 0, 0),
        ("addActiveSuggestionMarker", "fn_addActiveSuggestionMarker", 4, 0, 1, 0, 0, 0, 0),
        ("addCompositionMarker", "fn_addCompositionMarker", 6, 0, 1, 0, 0, 0, 0),
        ("addEmbedderCustomElementName", "fn_addEmbedderCustomElementName", 1, 0, 1, 0, 0, 0, 0),
        ("addFakeDevice", "fn_addFakeDevice", 3, 0, 1, 0, 1, 0, 0),
        ("addOneToPromise", "fn_addOneToPromise", 1, 0, 1, 0, 1, 0, 0),
        ("addSuggestionMarker", "fn_addSuggestionMarker", 6, 0, 1, 0, 0, 0, 0),
        ("addTextMatchMarker", "fn_addTextMatchMarker", 2, 0, 1, 0, 0, 0, 0),
        ("advanceImageAnimation", "fn_advanceImageAnimation", 1, 0, 1, 0, 0, 0, 0),
        ("allIconURLs", "fn_allIconURLs", 1, 0, 1, 0, 0, 0, 0),
        ("audioHandlerCount", "fn_audioHandlerCount", 0, 0, 1, 0, 0, 0, 0),
        ("audioWorkletProcessorCount", "fn_audioWorkletProcessorCount", 0, 0, 1, 0, 0, 0, 0),
        ("boundingBox", "fn_boundingBox", 1, 0, 1, 0, 0, 0, 0),
        ("callbackFunctionTest", "fn_callbackFunctionTest", 0, 0, 1, 0, 0, 0, 0),
        ("canHyphenate", "fn_canHyphenate", 1, 0, 1, 0, 0, 0, 0),
        ("cancelCurrentSpellCheckRequest", "fn_cancelCurrentSpellCheckRequest", 1, 0, 1, 0, 0, 0, 0),
        ("canvasFontCacheMaxFonts", "fn_canvasFontCacheMaxFonts", 0, 0, 1, 0, 0, 0, 0),
        ("clearDevicePostureOverride", "fn_clearDevicePostureOverride", 0, 0, 1, 0, 1, 0, 0),
        ("clearHitTestCache", "fn_clearHitTestCache", 1, 0, 1, 0, 0, 0, 0),
        ("clearNetworkConnectionInfoOverride", "fn_clearNetworkConnectionInfoOverride", 0, 0, 1, 0, 0, 0, 0),
        ("clearUseCounter", "fn_clearUseCounter", 2, 0, 1, 0, 0, 0, 0),
        ("clickFedCmDialogButton", "fn_clickFedCmDialogButton", 1, 0, 1, 0, 1, 0, 0),
        ("collectSample", "fn_collectSample", 0, 0, 1, 0, 0, 0, 0),
        ("compareTreeScopePosition", "fn_compareTreeScopePosition", 2, 0, 1, 0, 0, 0, 0),
        ("computedStyleIncludingVisitedInfo", "fn_computedStyleIncludingVisitedInfo", 1, 0, 1, 0, 0, 0, 0),
        ("countElementShadow", "fn_countElementShadow", 1, 0, 1, 0, 0, 0, 0),
        ("counterValue", "fn_counterValue", 1, 0, 1, 0, 0, 0, 0),
        ("crash", "fn_crash", 0, 0, 1, 0, 0, 0, 0),
        ("createReadableStream", "fn_createReadableStream", 2, 0, 1, 0, 0, 0, 0),
        ("createRejectedPromise", "fn_createRejectedPromise", 1, 0, 1, 0, 1, 0, 0),
        ("createResolvedPromise", "fn_createResolvedPromise", 1, 0, 1, 0, 1, 0, 0),
        ("createUserAgentShadowRoot", "fn_createUserAgentShadowRoot", 1, 0, 1, 0, 0, 0, 0),
        ("createVirtualSensor", "fn_createVirtualSensor", 2, 0, 1, 0, 1, 0, 0),
        ("createWritableStreamAndSink", "fn_createWritableStreamAndSink", 2, 0, 1, 0, 0, 0, 0),
        ("currentTimeTicks", "fn_currentTimeTicks", 0, 0, 1, 0, 0, 0, 0),
        ("deleteAllCookies", "fn_deleteAllCookies", 0, 0, 1, 0, 1, 0, 0),
        ("deserializeBuffer", "fn_deserializeBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("dictionaryTest", "fn_dictionaryTest", 0, 0, 1, 0, 0, 0, 0),
        ("disableCanvasAcceleration", "fn_disableCanvasAcceleration", 1, 0, 1, 0, 0, 0, 0),
        ("disableCompositedAnimation", "fn_disableCompositedAnimation", 1, 0, 1, 0, 0, 0, 0),
        ("disableReferencedFilePathsVerification", "fn_disableReferencedFilePathsVerification", 0, 0, 1, 0, 0, 0, 0),
        ("dismissFedCmDialog", "fn_dismissFedCmDialog", 0, 0, 1, 0, 1, 0, 0),
        ("doesWindowHaveUrlFragment", "fn_doesWindowHaveUrlFragment", 1, 0, 1, 0, 0, 0, 0),
        ("draggableRegions", "fn_draggableRegions", 1, 0, 1, 0, 0, 0, 0),
        ("effectivePreload", "fn_effectivePreload", 1, 0, 1, 0, 0, 0, 0),
        ("effectiveRootScroller", "fn_effectiveRootScroller", 1, 0, 1, 0, 0, 0, 0),
        ("elementFromPoint", "fn_elementFromPoint", 5, 0, 1, 0, 0, 0, 0),
        ("elementLayoutTreeAsText", "fn_elementLayoutTreeAsText", 1, 0, 1, 0, 0, 0, 0),
        ("elementShouldAutoComplete", "fn_elementShouldAutoComplete", 1, 0, 1, 0, 0, 0, 0),
        ("enableMockSpeechSynthesizer", "fn_enableMockSpeechSynthesizer", 1, 0, 1, 0, 0, 0, 0),
        ("endColorChooser", "fn_endColorChooser", 1, 0, 1, 0, 0, 0, 0),
        ("evaluateInInspectorOverlay", "fn_evaluateInInspectorOverlay", 1, 0, 1, 0, 0, 0, 0),
        ("evictAllResources", "fn_evictAllResources", 0, 0, 1, 0, 0, 0, 0),
        ("executeCommand", "fn_executeCommand", 3, 0, 1, 0, 0, 0, 0),
        ("exemptUrlFromNetworkRevocation", "fn_exemptUrlFromNetworkRevocation", 1, 0, 1, 0, 1, 0, 0),
        ("fakeCaptureConfigurationChanged", "fn_fakeCaptureConfigurationChanged", 1, 0, 1, 0, 0, 0, 0),
        ("firstChildInFlatTree", "fn_firstChildInFlatTree", 1, 0, 1, 0, 0, 0, 0),
        ("forceCompositingUpdate", "fn_forceCompositingUpdate", 1, 0, 1, 0, 0, 0, 0),
        ("forceFullRepaint", "fn_forceFullRepaint", 1, 0, 1, 0, 0, 0, 0),
        ("forceImageReload", "fn_forceImageReload", 1, 0, 1, 0, 0, 0, 0),
        ("forceLoseCanvasContext", "fn_forceLoseCanvasContext", 2, 0, 1, 0, 0, 0, 0),
        ("forceReload", "fn_forceReload", 1, 0, 1, 0, 0, 0, 0),
        ("forceStaleStateForMediaElement", "fn_forceStaleStateForMediaElement", 2, 0, 1, 0, 0, 0, 0),
        ("formControlStateOfHistoryItem", "fn_formControlStateOfHistoryItem", 0, 0, 1, 0, 0, 0, 0),
        ("generateTestReport", "fn_generateTestReport", 1, 0, 1, 0, 0, 0, 0),
        ("getAgentId", "fn_getAgentId", 1, 0, 1, 0, 0, 0, 0),
        ("getAllCookies", "fn_getAllCookies", 0, 0, 1, 0, 1, 0, 0),
        ("getCSSPropertyAliases", "fn_getCSSPropertyAliases", 0, 0, 1, 0, 0, 0, 0),
        ("getCSSPropertyLonghands", "fn_getCSSPropertyLonghands", 0, 0, 1, 0, 0, 0, 0),
        ("getCSSPropertyShorthands", "fn_getCSSPropertyShorthands", 0, 0, 1, 0, 0, 0, 0),
        ("getComputedLabel", "fn_getComputedLabel", 1, 0, 1, 0, 0, 0, 0),
        ("getComputedRole", "fn_getComputedRole", 1, 0, 1, 0, 0, 0, 0),
        ("getCreatorScripts", "fn_getCreatorScripts", 1, 0, 1, 0, 0, 0, 0),
        ("getCurrentCursorInfo", "fn_getCurrentCursorInfo", 0, 0, 1, 0, 0, 0, 0),
        ("getDragCaret", "fn_getDragCaret", 0, 0, 1, 0, 0, 0, 0),
        ("getFedCmDialogType", "fn_getFedCmDialogType", 0, 0, 1, 0, 1, 0, 0),
        ("getFedCmTitle", "fn_getFedCmTitle", 0, 0, 1, 0, 1, 0, 0),
        ("getImageSourceURL", "fn_getImageSourceURL", 1, 0, 1, 0, 0, 0, 0),
        ("getInitialResourcePriority", "fn_getInitialResourcePriority", 2, 0, 1, 0, 1, 0, 0),
        ("getInitialResourcePriorityOfNewLoad", "fn_getInitialResourcePriorityOfNewLoad", 2, 0, 1, 0, 1, 0, 0),
        ("getInternalResponseURLList", "fn_getInternalResponseURLList", 1, 0, 1, 0, 0, 0, 0),
        ("getNamedCookie", "fn_getNamedCookie", 1, 0, 1, 0, 1, 0, 0),
        ("getParsedImportMap", "fn_getParsedImportMap", 1, 0, 1, 0, 0, 0, 0),
        ("getProgrammaticScrollAnimationState", "fn_getProgrammaticScrollAnimationState", 1, 0, 1, 0, 0, 0, 0),
        ("getReferencedFilePaths", "fn_getReferencedFilePaths", 0, 0, 1, 0, 0, 0, 0),
        ("getResourceHeader", "fn_getResourceHeader", 3, 0, 1, 0, 0, 0, 0),
        ("getScrollAnimationState", "fn_getScrollAnimationState", 1, 0, 1, 0, 0, 0, 0),
        ("getSelectionInFlatTree", "fn_getSelectionInFlatTree", 1, 0, 1, 0, 0, 0, 0),
        ("getVirtualSensorInformation", "fn_getVirtualSensorInformation", 1, 0, 1, 0, 1, 0, 0),
        ("hasAutofocusRequest", "fn_hasAutofocusRequest", 0, 0, 1, 0, 0, 0, 0),
        ("hasGrammarMarker", "fn_hasGrammarMarker", 3, 0, 1, 0, 0, 0, 0),
        ("hasLastEditCommand", "fn_hasLastEditCommand", 1, 0, 1, 0, 0, 0, 0),
        ("hasSpellingMarker", "fn_hasSpellingMarker", 3, 0, 1, 0, 0, 0, 0),
        ("hitTestCacheHits", "fn_hitTestCacheHits", 1, 0, 1, 0, 0, 0, 0),
        ("hitTestCount", "fn_hitTestCount", 1, 0, 1, 0, 0, 0, 0),
        ("htmlNamespace", "fn_htmlNamespace", 0, 0, 1, 0, 0, 0, 0),
        ("htmlTags", "fn_htmlTags", 0, 0, 1, 0, 0, 0, 0),
        ("idleTimeSpellCheckerState", "fn_idleTimeSpellCheckerState", 1, 0, 1, 0, 0, 0, 0),
        ("initializeUKMRecorder", "fn_initializeUKMRecorder", 0, 0, 1, 0, 0, 0, 0),
        ("innerEditorElement", "fn_innerEditorElement", 1, 0, 1, 0, 0, 0, 0),
        ("isActivated", "fn_isActivated", 0, 0, 1, 0, 0, 0, 0),
        ("isAnimatedCSSPropertyUseCounted", "fn_isAnimatedCSSPropertyUseCounted", 2, 0, 1, 0, 0, 0, 0),
        ("isCSSPropertyUseCounted", "fn_isCSSPropertyUseCounted", 2, 0, 1, 0, 0, 0, 0),
        ("isCompositedAnimation", "fn_isCompositedAnimation", 1, 0, 1, 0, 0, 0, 0),
        ("isInCanvasFontCache", "fn_isInCanvasFontCache", 2, 0, 1, 0, 0, 0, 0),
        ("isLoading", "fn_isLoading", 1, 0, 1, 0, 0, 0, 0),
        ("isLoadingFromMemoryCache", "fn_isLoadingFromMemoryCache", 1, 0, 1, 0, 0, 0, 0),
        ("isLowEndDevice", "fn_isLowEndDevice", 0, 0, 1, 0, 0, 0, 0),
        ("isMediaElementSuspended", "fn_isMediaElementSuspended", 1, 0, 1, 0, 0, 0, 0),
        ("isPreloaded", "fn_isPreloaded", 1, 0, 1, 0, 0, 0, 0),
        ("isPreloadedBy", "fn_isPreloadedBy", 2, 0, 1, 0, 0, 0, 0),
        ("isSelectPopupVisible", "fn_isSelectPopupVisible", 1, 0, 1, 0, 0, 0, 0),
        ("isSiteIsolated", "fn_isSiteIsolated", 1, 0, 1, 0, 0, 0, 0),
        ("isTrackingOcclusionForIFrame", "fn_isTrackingOcclusionForIFrame", 1, 0, 1, 0, 0, 0, 0),
        ("isUseCounted", "fn_isUseCounted", 2, 0, 1, 0, 0, 0, 0),
        ("isValidationMessageVisible", "fn_isValidationMessageVisible", 1, 0, 1, 0, 0, 0, 0),
        ("isVibrating", "fn_isVibrating", 1, 0, 1, 0, 0, 0, 0),
        ("isWebDXFeatureUseCounted", "fn_isWebDXFeatureUseCounted", 2, 0, 1, 0, 0, 0, 0),
        ("lastChildInFlatTree", "fn_lastChildInFlatTree", 1, 0, 1, 0, 0, 0, 0),
        ("lastSpellCheckProcessedSequence", "fn_lastSpellCheckProcessedSequence", 1, 0, 1, 0, 0, 0, 0),
        ("lastSpellCheckRequestSequence", "fn_lastSpellCheckRequestSequence", 1, 0, 1, 0, 0, 0, 0),
        ("layerTreeAsText", "fn_layerTreeAsText", 1, 0, 1, 0, 0, 0, 0),
        ("layoutCountForTesting", "fn_layoutCountForTesting", 0, 0, 1, 0, 0, 0, 0),
        ("lengthFromRange", "fn_lengthFromRange", 2, 0, 1, 0, 0, 0, 0),
        ("locationFromRange", "fn_locationFromRange", 2, 0, 1, 0, 0, 0, 0),
        ("mainThreadScrollingReasons", "fn_mainThreadScrollingReasons", 1, 0, 1, 0, 0, 0, 0),
        ("markerBackgroundColorForNode", "fn_markerBackgroundColorForNode", 3, 0, 1, 0, 0, 0, 0),
        ("markerCountForNode", "fn_markerCountForNode", 2, 0, 1, 0, 0, 0, 0),
        ("markerDescriptionForNode", "fn_markerDescriptionForNode", 3, 0, 1, 0, 0, 0, 0),
        ("markerRangeForNode", "fn_markerRangeForNode", 3, 0, 1, 0, 0, 0, 0),
        ("markerTextForListItem", "fn_markerTextForListItem", 1, 0, 1, 0, 0, 0, 0),
        ("markerUnderlineColorForNode", "fn_markerUnderlineColorForNode", 3, 0, 1, 0, 0, 0, 0),
        ("mediaKeySessionCount", "fn_mediaKeySessionCount", 0, 0, 1, 0, 0, 0, 0),
        ("mediaKeysCount", "fn_mediaKeysCount", 0, 0, 1, 0, 0, 0, 0),
        ("mediaPlayerPlayingRemotelyChanged", "fn_mediaPlayerPlayingRemotelyChanged", 2, 0, 1, 0, 0, 0, 0),
        ("mediaPlayerRemoteRouteAvailabilityChanged", "fn_mediaPlayerRemoteRouteAvailabilityChanged", 2, 0, 1, 0, 0, 0, 0),
        ("monotonicTimeToZeroBasedDocumentTime", "fn_monotonicTimeToZeroBasedDocumentTime", 1, 0, 1, 0, 0, 0, 0),
        ("needsLayoutCount", "fn_needsLayoutCount", 0, 0, 1, 0, 0, 0, 0),
        ("nextInFlatTree", "fn_nextInFlatTree", 1, 0, 1, 0, 0, 0, 0),
        ("nextSiblingInFlatTree", "fn_nextSiblingInFlatTree", 1, 0, 1, 0, 0, 0, 0),
        ("nodeNeedsStyleRecalc", "fn_nodeNeedsStyleRecalc", 1, 0, 1, 0, 0, 0, 0),
        ("nodesFromRect", "fn_nodesFromRect", 7, 0, 1, 0, 0, 0, 0),
        ("nonDraggableRegions", "fn_nonDraggableRegions", 1, 0, 1, 0, 0, 0, 0),
        ("nonFastScrollableRects", "fn_nonFastScrollableRects", 1, 0, 1, 0, 0, 0, 0),
        ("numberOfLiveAXObjects", "fn_numberOfLiveAXObjects", 0, 0, 1, 0, 0, 0, 0),
        ("numberOfLiveDocuments", "fn_numberOfLiveDocuments", 0, 0, 1, 0, 0, 0, 0),
        ("numberOfLiveNodes", "fn_numberOfLiveNodes", 0, 0, 1, 0, 0, 0, 0),
        ("numberOfPages", "fn_numberOfPages", 0, 0, 1, 0, 0, 0, 0),
        ("numberOfScrollableAreas", "fn_numberOfScrollableAreas", 1, 0, 1, 0, 0, 0, 0),
        ("observeGC", "fn_observeGC", 1, 0, 1, 0, 0, 0, 0),
        ("observeUseCounter", "fn_observeUseCounter", 2, 0, 1, 0, 1, 0, 0),
        ("originTrialsTest", "fn_originTrialsTest", 0, 0, 1, 0, 0, 0, 0),
        ("pageNumber", "fn_pageNumber", 1, 0, 1, 0, 0, 0, 0),
        ("pageScaleFactor", "fn_pageScaleFactor", 0, 0, 1, 0, 0, 0, 0),
        ("pageZoomFactor", "fn_pageZoomFactor", 0, 0, 1, 0, 0, 0, 0),
        ("parentTreeScope", "fn_parentTreeScope", 1, 0, 1, 0, 0, 0, 0),
        ("pauseAnimations", "fn_pauseAnimations", 1, 0, 1, 0, 0, 0, 0),
        ("peerConnectionCount", "fn_peerConnectionCount", 0, 0, 1, 0, 0, 0, 0),
        ("pendingVibrationPattern", "fn_pendingVibrationPattern", 1, 0, 1, 0, 0, 0, 0),
        ("pointerEventHandlerCount", "fn_pointerEventHandlerCount", 1, 0, 1, 0, 0, 0, 0),
        ("previousInFlatTree", "fn_previousInFlatTree", 1, 0, 1, 0, 0, 0, 0),
        ("promiseCheck", "fn_promiseCheck", 5, 0, 1, 0, 1, 0, 0),
        ("promiseCheckOverload", "fn_promiseCheckOverload", 1, 0, 1, 0, 1, 0, 0),
        ("promiseCheckRange", "fn_promiseCheckRange", 1, 0, 1, 0, 1, 0, 0),
        ("promiseCheckWithoutExceptionState", "fn_promiseCheckWithoutExceptionState", 2, 0, 1, 0, 1, 0, 0),
        ("rangeAsText", "fn_rangeAsText", 1, 0, 1, 0, 0, 0, 0),
        ("rangeFromLocationAndLength", "fn_rangeFromLocationAndLength", 3, 0, 1, 0, 0, 0, 0),
        ("recordTest", "fn_recordTest", 0, 0, 1, 0, 0, 0, 0),
        ("registerURLSchemeAsBypassingContentSecurityPolicy", "fn_registerURLSchemeAsBypassingContentSecurityPolicy", 1, 0, 1, 0, 0, 0, 0),
        ("removeMarker", "fn_removeMarker", 3, 0, 1, 0, 0, 0, 0),
        ("removeURLSchemeRegisteredAsBypassingContentSecurityPolicy", "fn_removeURLSchemeRegisteredAsBypassingContentSecurityPolicy", 1, 0, 1, 0, 0, 0, 0),
        ("removeVirtualSensor", "fn_removeVirtualSensor", 1, 0, 1, 0, 1, 0, 0),
        ("replaceMisspelled", "fn_replaceMisspelled", 2, 0, 1, 0, 0, 0, 0),
        ("resetSelectListTypeAheadSession", "fn_resetSelectListTypeAheadSession", 1, 0, 1, 0, 0, 0, 0),
        ("resetTypeAheadSession", "fn_resetTypeAheadSession", 1, 0, 1, 0, 0, 0, 0),
        ("rtcCertificateEquals", "fn_rtcCertificateEquals", 2, 0, 1, 0, 0, 0, 0),
        ("runFuzzer", "fn_runFuzzer", 2, 0, 1, 0, 1, 0, 0),
        ("runIdleTimeSpellChecker", "fn_runIdleTimeSpellChecker", 1, 0, 1, 0, 0, 0, 0),
        ("scrollEventHandlerCount", "fn_scrollEventHandlerCount", 1, 0, 1, 0, 0, 0, 0),
        ("scrollingStateTreeAsText", "fn_scrollingStateTreeAsText", 1, 0, 1, 0, 0, 0, 0),
        ("selectColorInColorChooser", "fn_selectColorInColorChooser", 2, 0, 1, 0, 0, 0, 0),
        ("selectFedCmAccount", "fn_selectFedCmAccount", 1, 0, 1, 0, 1, 0, 0),
        ("selectMenuListText", "fn_selectMenuListText", 1, 0, 1, 0, 0, 0, 0),
        ("selectPopupItemStyleFontHeight", "fn_selectPopupItemStyleFontHeight", 2, 0, 1, 0, 0, 0, 0),
        ("selectPopupItemStyleIsRtl", "fn_selectPopupItemStyleIsRtl", 2, 0, 1, 0, 0, 0, 0),
        ("selectedHTMLForClipboard", "fn_selectedHTMLForClipboard", 0, 0, 1, 0, 0, 0, 0),
        ("selectedTextForClipboard", "fn_selectedTextForClipboard", 0, 0, 1, 0, 0, 0, 0),
        ("selectionBounds", "fn_selectionBounds", 0, 0, 1, 0, 0, 0, 0),
        ("sequenceTest", "fn_sequenceTest", 0, 0, 1, 0, 0, 0, 0),
        ("serializeObject", "fn_serializeObject", 1, 0, 1, 0, 0, 0, 0),
        ("setAllowPerChunkTransferring", "fn_setAllowPerChunkTransferring", 1, 0, 1, 0, 0, 0, 0),
        ("setAutofilled", "fn_setAutofilled", 2, 0, 1, 0, 0, 0, 0),
        ("setAutofilledValue", "fn_setAutofilledValue", 2, 0, 1, 0, 0, 0, 0),
        ("setBackForwardCacheRestorationBufferSize", "fn_setBackForwardCacheRestorationBufferSize", 1, 0, 1, 0, 0, 0, 0),
        ("setBrowserControlsShownRatio", "fn_setBrowserControlsShownRatio", 2, 0, 1, 0, 0, 0, 0),
        ("setBrowserControlsState", "fn_setBrowserControlsState", 3, 0, 1, 0, 0, 0, 0),
        ("setCapsLockState", "fn_setCapsLockState", 1, 0, 1, 0, 0, 0, 0),
        ("setDarkPreferredColorScheme", "fn_setDarkPreferredColorScheme", 1, 0, 1, 0, 0, 0, 0),
        ("setDarkPreferredRootScrollbarColorScheme", "fn_setDarkPreferredRootScrollbarColorScheme", 1, 0, 1, 0, 0, 0, 0),
        ("setDeviceEmulationScale", "fn_setDeviceEmulationScale", 1, 0, 1, 0, 0, 0, 0),
        ("setDevicePostureOverride", "fn_setDevicePostureOverride", 1, 0, 1, 0, 1, 0, 0),
        ("setEventTimingBufferSize", "fn_setEventTimingBufferSize", 1, 0, 1, 0, 0, 0, 0),
        ("setFocused", "fn_setFocused", 1, 0, 1, 0, 0, 0, 0),
        ("setForcedColorsAndDarkPreferredColorScheme", "fn_setForcedColorsAndDarkPreferredColorScheme", 1, 0, 1, 0, 0, 0, 0),
        ("setFormControlStateOfHistoryItem", "fn_setFormControlStateOfHistoryItem", 1, 0, 1, 0, 0, 0, 0),
        ("setInitialFocus", "fn_setInitialFocus", 1, 0, 1, 0, 0, 0, 0),
        ("setIsAdFrame", "fn_setIsAdFrame", 1, 0, 1, 0, 0, 0, 0),
        ("setIsCursorVisible", "fn_setIsCursorVisible", 2, 0, 1, 0, 0, 0, 0),
        ("setIsLowEndDevice", "fn_setIsLowEndDevice", 1, 0, 1, 0, 0, 0, 0),
        ("setMarkedTextMatchesAreHighlighted", "fn_setMarkedTextMatchesAreHighlighted", 2, 0, 1, 0, 0, 0, 0),
        ("setMarker", "fn_setMarker", 3, 0, 1, 0, 0, 0, 0),
        ("setMaxNumberOfFramesToTen", "fn_setMaxNumberOfFramesToTen", 1, 0, 1, 0, 0, 0, 0),
        ("setMediaControlsTestMode", "fn_setMediaControlsTestMode", 2, 0, 1, 0, 0, 0, 0),
        ("setMockHyphenation", "fn_setMockHyphenation", 1, 0, 1, 0, 0, 0, 0),
        ("setNetworkConnectionInfoOverride", "fn_setNetworkConnectionInfoOverride", 5, 0, 1, 0, 0, 0, 0),
        ("setPageScaleFactor", "fn_setPageScaleFactor", 1, 0, 1, 0, 0, 0, 0),
        ("setPageScaleFactorLimits", "fn_setPageScaleFactorLimits", 2, 0, 1, 0, 0, 0, 0),
        ("setPermission", "fn_setPermission", 2, 0, 1, 0, 1, 0, 0),
        ("setPersistent", "fn_setPersistent", 2, 0, 1, 0, 0, 0, 0),
        ("setPseudoClassState", "fn_setPseudoClassState", 3, 0, 1, 0, 0, 0, 0),
        ("setSaveDataEnabled", "fn_setSaveDataEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("setScrollbarVisibilityInScrollableArea", "fn_setScrollbarVisibilityInScrollableArea", 2, 0, 1, 0, 0, 0, 0),
        ("setSelectionRangeForNumberType", "fn_setSelectionRangeForNumberType", 3, 0, 1, 0, 0, 0, 0),
        ("setShouldRevealPassword", "fn_setShouldRevealPassword", 2, 0, 1, 0, 0, 0, 0),
        ("setStorageAccess", "fn_setStorageAccess", 3, 0, 1, 0, 1, 0, 0),
        ("setSuggestedValue", "fn_setSuggestedValue", 2, 0, 1, 0, 0, 0, 0),
        ("setSystemTimeZone", "fn_setSystemTimeZone", 1, 0, 1, 0, 0, 0, 0),
        ("setTextMatchMarkersActive", "fn_setTextMatchMarkersActive", 4, 0, 1, 0, 0, 0, 0),
        ("setUserPreferredLanguages", "fn_setUserPreferredLanguages", 1, 0, 1, 0, 0, 0, 0),
        ("setValueForUser", "fn_setValueForUser", 2, 0, 1, 0, 0, 0, 0),
        ("setVisualViewportOffset", "fn_setVisualViewportOffset", 2, 0, 1, 0, 0, 0, 0),
        ("shadowPseudoId", "fn_shadowPseudoId", 1, 0, 1, 0, 0, 0, 0),
        ("shadowRoot", "fn_shadowRoot", 1, 0, 1, 0, 0, 0, 0),
        ("shortcutIconURLs", "fn_shortcutIconURLs", 1, 0, 1, 0, 0, 0, 0),
        ("simulateRasterUnderInvalidations", "fn_simulateRasterUnderInvalidations", 1, 0, 1, 0, 0, 0, 0),
        ("spellCheckedTextLength", "fn_spellCheckedTextLength", 1, 0, 1, 0, 0, 0, 0),
        ("startTrackingRepaints", "fn_startTrackingRepaints", 1, 0, 1, 0, 0, 0, 0),
        ("stopResponsivenessMetricsUkmSampling", "fn_stopResponsivenessMetricsUkmSampling", 0, 0, 1, 0, 0, 0, 0),
        ("stopTrackingRepaints", "fn_stopTrackingRepaints", 1, 0, 1, 0, 0, 0, 0),
        ("styleForElementCount", "fn_styleForElementCount", 0, 0, 1, 0, 0, 0, 0),
        ("suggestedValue", "fn_suggestedValue", 1, 0, 1, 0, 0, 0, 0),
        ("supportedTextEncodingLabels", "fn_supportedTextEncodingLabels", 0, 0, 1, 0, 0, 0, 0),
        ("svgNamespace", "fn_svgNamespace", 0, 0, 1, 0, 0, 0, 0),
        ("svgTags", "fn_svgTags", 0, 0, 1, 0, 0, 0, 0),
        ("terminateServiceWorker", "fn_terminateServiceWorker", 1, 0, 1, 0, 1, 0, 0),
        ("touchEndOrCancelEventHandlerCount", "fn_touchEndOrCancelEventHandlerCount", 1, 0, 1, 0, 0, 0, 0),
        ("touchEventTargetLayerRects", "fn_touchEventTargetLayerRects", 1, 0, 1, 0, 0, 0, 0),
        ("touchNodeAdjustedToBestClickableNode", "fn_touchNodeAdjustedToBestClickableNode", 5, 0, 1, 0, 0, 0, 0),
        ("touchNodeAdjustedToBestContextMenuNode", "fn_touchNodeAdjustedToBestContextMenuNode", 5, 0, 1, 0, 0, 0, 0),
        ("touchNodeAdjustedToBestStylusWritableNode", "fn_touchNodeAdjustedToBestStylusWritableNode", 5, 0, 1, 0, 0, 0, 0),
        ("touchPositionAdjustedToBestClickableNode", "fn_touchPositionAdjustedToBestClickableNode", 5, 0, 1, 0, 0, 0, 0),
        ("touchPositionAdjustedToBestContextMenuNode", "fn_touchPositionAdjustedToBestContextMenuNode", 5, 0, 1, 0, 0, 0, 0),
        ("touchStartOrMoveEventHandlerCount", "fn_touchStartOrMoveEventHandlerCount", 1, 0, 1, 0, 0, 0, 0),
        ("treeScopeRootNode", "fn_treeScopeRootNode", 1, 0, 1, 0, 0, 0, 0),
        ("triggerTestInspectorIssue", "fn_triggerTestInspectorIssue", 1, 0, 1, 0, 0, 0, 0),
        ("typeConversions", "fn_typeConversions", 0, 0, 1, 0, 0, 0, 0),
        ("unionTypesTest", "fn_unionTypesTest", 0, 0, 1, 0, 0, 0, 0),
        ("unscopableMethod", "fn_unscopableMethod", 0, 0, 1, 0, 0, 0, 0),
        ("updateLayoutAndRunPostLayoutTasks", "fn_updateLayoutAndRunPostLayoutTasks", 0, 0, 1, 0, 0, 0, 0),
        ("updateStyleAndReturnAffectedElementCount", "fn_updateStyleAndReturnAffectedElementCount", 0, 0, 1, 0, 0, 0, 0),
        ("updateVirtualSensor", "fn_updateVirtualSensor", 2, 0, 1, 0, 1, 0, 0),
        ("useMockOverlayScrollbars", "fn_useMockOverlayScrollbars", 0, 0, 1, 0, 0, 0, 0),
        ("userPreferredLanguages", "fn_userPreferredLanguages", 0, 0, 1, 0, 0, 0, 0),
        ("viewportAsText", "fn_viewportAsText", 4, 0, 1, 0, 0, 0, 0),
        ("waitForPeerConnectionDispatchEventsTaskCreated", "fn_waitForPeerConnectionDispatchEventsTaskCreated", 1, 0, 1, 0, 1, 0, 0),
        ("wheelEventHandlerCount", "fn_wheelEventHandlerCount", 1, 0, 1, 0, 0, 0, 0),
        ("zeroBasedDocumentTimeToMonotonicTime", "fn_zeroBasedDocumentTimeToMonotonicTime", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_pagePopupWindow(self):
        val = self._attr.get('pagePopupWindow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.pagePopupWindow -> get attr')

    def get_settings(self):
        val = self._attr.get('settings')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.settings -> get attr')

    def get_runtimeFlags(self):
        val = self._attr.get('runtimeFlags')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.runtimeFlags -> get attr')

    def get_workerThreadCount(self):
        val = self._attr.get('workerThreadCount')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.workerThreadCount -> get attr')

    def get_cursorUpdatePending(self):
        val = self._attr.get('cursorUpdatePending')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.cursorUpdatePending -> get attr')

    def get_visibleSelectionAnchorNode(self):
        val = self._attr.get('visibleSelectionAnchorNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.visibleSelectionAnchorNode -> get attr')

    def get_visibleSelectionAnchorOffset(self):
        val = self._attr.get('visibleSelectionAnchorOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.visibleSelectionAnchorOffset -> get attr')

    def get_visibleSelectionFocusNode(self):
        val = self._attr.get('visibleSelectionFocusNode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.visibleSelectionFocusNode -> get attr')

    def get_visibleSelectionFocusOffset(self):
        val = self._attr.get('visibleSelectionFocusOffset')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.visibleSelectionFocusOffset -> get attr')

    def get_textAffinity(self):
        val = self._attr.get('textAffinity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.textAffinity -> get attr')

    def get_length(self):
        val = self._attr.get('length')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.length -> get attr')

    def get_unscopableAttribute(self):
        val = self._attr.get('unscopableAttribute')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.unscopableAttribute -> get attr')

    def get_overlayScrollbarsEnabled(self):
        val = self._attr.get('overlayScrollbarsEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.overlayScrollbarsEnabled -> get attr')

    def get_peerConnectionCountLimit(self):
        val = self._attr.get('peerConnectionCountLimit')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_internals.py -> Internals.peerConnectionCountLimit -> get attr')

    def fn_DisableIntersectionObserverThrottleDelay(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.DisableIntersectionObserverThrottleDelay{tuple(args)} -> method')

    def fn_LCPPrediction(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.LCPPrediction{tuple(args)} -> method')

    def fn_SetSupportsDraggableRegions(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.SetSupportsDraggableRegions{tuple(args)} -> method')

    def fn_ShadowRootMode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.ShadowRootMode{tuple(args)} -> method')

    def fn_absoluteCaretBounds(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.absoluteCaretBounds{tuple(args)} -> method')

    def fn_activeMarkerCountForNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.activeMarkerCountForNode{tuple(args)} -> method')

    def fn_addActiveSuggestionMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.addActiveSuggestionMarker{tuple(args)} -> method')

    def fn_addCompositionMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.addCompositionMarker{tuple(args)} -> method')

    def fn_addEmbedderCustomElementName(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.addEmbedderCustomElementName{tuple(args)} -> method')

    def fn_addFakeDevice(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.addFakeDevice{tuple(args)} -> method')

    def fn_addOneToPromise(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.addOneToPromise{tuple(args)} -> method')

    def fn_addSuggestionMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.addSuggestionMarker{tuple(args)} -> method')

    def fn_addTextMatchMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.addTextMatchMarker{tuple(args)} -> method')

    def fn_advanceImageAnimation(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.advanceImageAnimation{tuple(args)} -> method')

    def fn_allIconURLs(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.allIconURLs{tuple(args)} -> method')

    def fn_audioHandlerCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.audioHandlerCount{tuple(args)} -> method')

    def fn_audioWorkletProcessorCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.audioWorkletProcessorCount{tuple(args)} -> method')

    def fn_boundingBox(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.boundingBox{tuple(args)} -> method')

    def fn_callbackFunctionTest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.callbackFunctionTest{tuple(args)} -> method')

    def fn_canHyphenate(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.canHyphenate{tuple(args)} -> method')

    def fn_cancelCurrentSpellCheckRequest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.cancelCurrentSpellCheckRequest{tuple(args)} -> method')

    def fn_canvasFontCacheMaxFonts(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.canvasFontCacheMaxFonts{tuple(args)} -> method')

    def fn_clearDevicePostureOverride(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.clearDevicePostureOverride{tuple(args)} -> method')

    def fn_clearHitTestCache(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.clearHitTestCache{tuple(args)} -> method')

    def fn_clearNetworkConnectionInfoOverride(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.clearNetworkConnectionInfoOverride{tuple(args)} -> method')

    def fn_clearUseCounter(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.clearUseCounter{tuple(args)} -> method')

    def fn_clickFedCmDialogButton(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.clickFedCmDialogButton{tuple(args)} -> method')

    def fn_collectSample(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.collectSample{tuple(args)} -> method')

    def fn_compareTreeScopePosition(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.compareTreeScopePosition{tuple(args)} -> method')

    def fn_computedStyleIncludingVisitedInfo(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.computedStyleIncludingVisitedInfo{tuple(args)} -> method')

    def fn_countElementShadow(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.countElementShadow{tuple(args)} -> method')

    def fn_counterValue(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.counterValue{tuple(args)} -> method')

    def fn_crash(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.crash{tuple(args)} -> method')

    def fn_createReadableStream(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.createReadableStream{tuple(args)} -> method')

    def fn_createRejectedPromise(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.createRejectedPromise{tuple(args)} -> method')

    def fn_createResolvedPromise(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.createResolvedPromise{tuple(args)} -> method')

    def fn_createUserAgentShadowRoot(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.createUserAgentShadowRoot{tuple(args)} -> method')

    def fn_createVirtualSensor(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.createVirtualSensor{tuple(args)} -> method')

    def fn_createWritableStreamAndSink(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.createWritableStreamAndSink{tuple(args)} -> method')

    def fn_currentTimeTicks(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.currentTimeTicks{tuple(args)} -> method')

    def fn_deleteAllCookies(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.deleteAllCookies{tuple(args)} -> method')

    def fn_deserializeBuffer(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.deserializeBuffer{tuple(args)} -> method')

    def fn_dictionaryTest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.dictionaryTest{tuple(args)} -> method')

    def fn_disableCanvasAcceleration(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.disableCanvasAcceleration{tuple(args)} -> method')

    def fn_disableCompositedAnimation(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.disableCompositedAnimation{tuple(args)} -> method')

    def fn_disableReferencedFilePathsVerification(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.disableReferencedFilePathsVerification{tuple(args)} -> method')

    def fn_dismissFedCmDialog(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.dismissFedCmDialog{tuple(args)} -> method')

    def fn_doesWindowHaveUrlFragment(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.doesWindowHaveUrlFragment{tuple(args)} -> method')

    def fn_draggableRegions(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.draggableRegions{tuple(args)} -> method')

    def fn_effectivePreload(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.effectivePreload{tuple(args)} -> method')

    def fn_effectiveRootScroller(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.effectiveRootScroller{tuple(args)} -> method')

    def fn_elementFromPoint(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.elementFromPoint{tuple(args)} -> method')

    def fn_elementLayoutTreeAsText(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.elementLayoutTreeAsText{tuple(args)} -> method')

    def fn_elementShouldAutoComplete(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.elementShouldAutoComplete{tuple(args)} -> method')

    def fn_enableMockSpeechSynthesizer(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.enableMockSpeechSynthesizer{tuple(args)} -> method')

    def fn_endColorChooser(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.endColorChooser{tuple(args)} -> method')

    def fn_evaluateInInspectorOverlay(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.evaluateInInspectorOverlay{tuple(args)} -> method')

    def fn_evictAllResources(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.evictAllResources{tuple(args)} -> method')

    def fn_executeCommand(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.executeCommand{tuple(args)} -> method')

    def fn_exemptUrlFromNetworkRevocation(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.exemptUrlFromNetworkRevocation{tuple(args)} -> method')

    def fn_fakeCaptureConfigurationChanged(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.fakeCaptureConfigurationChanged{tuple(args)} -> method')

    def fn_firstChildInFlatTree(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.firstChildInFlatTree{tuple(args)} -> method')

    def fn_forceCompositingUpdate(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.forceCompositingUpdate{tuple(args)} -> method')

    def fn_forceFullRepaint(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.forceFullRepaint{tuple(args)} -> method')

    def fn_forceImageReload(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.forceImageReload{tuple(args)} -> method')

    def fn_forceLoseCanvasContext(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.forceLoseCanvasContext{tuple(args)} -> method')

    def fn_forceReload(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.forceReload{tuple(args)} -> method')

    def fn_forceStaleStateForMediaElement(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.forceStaleStateForMediaElement{tuple(args)} -> method')

    def fn_formControlStateOfHistoryItem(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.formControlStateOfHistoryItem{tuple(args)} -> method')

    def fn_generateTestReport(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.generateTestReport{tuple(args)} -> method')

    def fn_getAgentId(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getAgentId{tuple(args)} -> method')

    def fn_getAllCookies(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getAllCookies{tuple(args)} -> method')

    def fn_getCSSPropertyAliases(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getCSSPropertyAliases{tuple(args)} -> method')

    def fn_getCSSPropertyLonghands(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getCSSPropertyLonghands{tuple(args)} -> method')

    def fn_getCSSPropertyShorthands(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getCSSPropertyShorthands{tuple(args)} -> method')

    def fn_getComputedLabel(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getComputedLabel{tuple(args)} -> method')

    def fn_getComputedRole(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getComputedRole{tuple(args)} -> method')

    def fn_getCreatorScripts(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getCreatorScripts{tuple(args)} -> method')

    def fn_getCurrentCursorInfo(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getCurrentCursorInfo{tuple(args)} -> method')

    def fn_getDragCaret(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getDragCaret{tuple(args)} -> method')

    def fn_getFedCmDialogType(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getFedCmDialogType{tuple(args)} -> method')

    def fn_getFedCmTitle(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getFedCmTitle{tuple(args)} -> method')

    def fn_getImageSourceURL(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getImageSourceURL{tuple(args)} -> method')

    def fn_getInitialResourcePriority(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getInitialResourcePriority{tuple(args)} -> method')

    def fn_getInitialResourcePriorityOfNewLoad(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getInitialResourcePriorityOfNewLoad{tuple(args)} -> method')

    def fn_getInternalResponseURLList(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getInternalResponseURLList{tuple(args)} -> method')

    def fn_getNamedCookie(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getNamedCookie{tuple(args)} -> method')

    def fn_getParsedImportMap(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getParsedImportMap{tuple(args)} -> method')

    def fn_getProgrammaticScrollAnimationState(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getProgrammaticScrollAnimationState{tuple(args)} -> method')

    def fn_getReferencedFilePaths(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getReferencedFilePaths{tuple(args)} -> method')

    def fn_getResourceHeader(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getResourceHeader{tuple(args)} -> method')

    def fn_getScrollAnimationState(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getScrollAnimationState{tuple(args)} -> method')

    def fn_getSelectionInFlatTree(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getSelectionInFlatTree{tuple(args)} -> method')

    def fn_getVirtualSensorInformation(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.getVirtualSensorInformation{tuple(args)} -> method')

    def fn_hasAutofocusRequest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.hasAutofocusRequest{tuple(args)} -> method')

    def fn_hasGrammarMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.hasGrammarMarker{tuple(args)} -> method')

    def fn_hasLastEditCommand(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.hasLastEditCommand{tuple(args)} -> method')

    def fn_hasSpellingMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.hasSpellingMarker{tuple(args)} -> method')

    def fn_hitTestCacheHits(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.hitTestCacheHits{tuple(args)} -> method')

    def fn_hitTestCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.hitTestCount{tuple(args)} -> method')

    def fn_htmlNamespace(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.htmlNamespace{tuple(args)} -> method')

    def fn_htmlTags(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.htmlTags{tuple(args)} -> method')

    def fn_idleTimeSpellCheckerState(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.idleTimeSpellCheckerState{tuple(args)} -> method')

    def fn_initializeUKMRecorder(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.initializeUKMRecorder{tuple(args)} -> method')

    def fn_innerEditorElement(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.innerEditorElement{tuple(args)} -> method')

    def fn_isActivated(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isActivated{tuple(args)} -> method')

    def fn_isAnimatedCSSPropertyUseCounted(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isAnimatedCSSPropertyUseCounted{tuple(args)} -> method')

    def fn_isCSSPropertyUseCounted(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isCSSPropertyUseCounted{tuple(args)} -> method')

    def fn_isCompositedAnimation(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isCompositedAnimation{tuple(args)} -> method')

    def fn_isInCanvasFontCache(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isInCanvasFontCache{tuple(args)} -> method')

    def fn_isLoading(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isLoading{tuple(args)} -> method')

    def fn_isLoadingFromMemoryCache(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isLoadingFromMemoryCache{tuple(args)} -> method')

    def fn_isLowEndDevice(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isLowEndDevice{tuple(args)} -> method')

    def fn_isMediaElementSuspended(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isMediaElementSuspended{tuple(args)} -> method')

    def fn_isPreloaded(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isPreloaded{tuple(args)} -> method')

    def fn_isPreloadedBy(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isPreloadedBy{tuple(args)} -> method')

    def fn_isSelectPopupVisible(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isSelectPopupVisible{tuple(args)} -> method')

    def fn_isSiteIsolated(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isSiteIsolated{tuple(args)} -> method')

    def fn_isTrackingOcclusionForIFrame(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isTrackingOcclusionForIFrame{tuple(args)} -> method')

    def fn_isUseCounted(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isUseCounted{tuple(args)} -> method')

    def fn_isValidationMessageVisible(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isValidationMessageVisible{tuple(args)} -> method')

    def fn_isVibrating(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isVibrating{tuple(args)} -> method')

    def fn_isWebDXFeatureUseCounted(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.isWebDXFeatureUseCounted{tuple(args)} -> method')

    def fn_lastChildInFlatTree(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.lastChildInFlatTree{tuple(args)} -> method')

    def fn_lastSpellCheckProcessedSequence(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.lastSpellCheckProcessedSequence{tuple(args)} -> method')

    def fn_lastSpellCheckRequestSequence(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.lastSpellCheckRequestSequence{tuple(args)} -> method')

    def fn_layerTreeAsText(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.layerTreeAsText{tuple(args)} -> method')

    def fn_layoutCountForTesting(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.layoutCountForTesting{tuple(args)} -> method')

    def fn_lengthFromRange(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.lengthFromRange{tuple(args)} -> method')

    def fn_locationFromRange(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.locationFromRange{tuple(args)} -> method')

    def fn_mainThreadScrollingReasons(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.mainThreadScrollingReasons{tuple(args)} -> method')

    def fn_markerBackgroundColorForNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.markerBackgroundColorForNode{tuple(args)} -> method')

    def fn_markerCountForNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.markerCountForNode{tuple(args)} -> method')

    def fn_markerDescriptionForNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.markerDescriptionForNode{tuple(args)} -> method')

    def fn_markerRangeForNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.markerRangeForNode{tuple(args)} -> method')

    def fn_markerTextForListItem(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.markerTextForListItem{tuple(args)} -> method')

    def fn_markerUnderlineColorForNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.markerUnderlineColorForNode{tuple(args)} -> method')

    def fn_mediaKeySessionCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.mediaKeySessionCount{tuple(args)} -> method')

    def fn_mediaKeysCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.mediaKeysCount{tuple(args)} -> method')

    def fn_mediaPlayerPlayingRemotelyChanged(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.mediaPlayerPlayingRemotelyChanged{tuple(args)} -> method')

    def fn_mediaPlayerRemoteRouteAvailabilityChanged(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.mediaPlayerRemoteRouteAvailabilityChanged{tuple(args)} -> method')

    def fn_monotonicTimeToZeroBasedDocumentTime(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.monotonicTimeToZeroBasedDocumentTime{tuple(args)} -> method')

    def fn_needsLayoutCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.needsLayoutCount{tuple(args)} -> method')

    def fn_nextInFlatTree(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.nextInFlatTree{tuple(args)} -> method')

    def fn_nextSiblingInFlatTree(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.nextSiblingInFlatTree{tuple(args)} -> method')

    def fn_nodeNeedsStyleRecalc(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.nodeNeedsStyleRecalc{tuple(args)} -> method')

    def fn_nodesFromRect(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.nodesFromRect{tuple(args)} -> method')

    def fn_nonDraggableRegions(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.nonDraggableRegions{tuple(args)} -> method')

    def fn_nonFastScrollableRects(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.nonFastScrollableRects{tuple(args)} -> method')

    def fn_numberOfLiveAXObjects(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.numberOfLiveAXObjects{tuple(args)} -> method')

    def fn_numberOfLiveDocuments(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.numberOfLiveDocuments{tuple(args)} -> method')

    def fn_numberOfLiveNodes(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.numberOfLiveNodes{tuple(args)} -> method')

    def fn_numberOfPages(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.numberOfPages{tuple(args)} -> method')

    def fn_numberOfScrollableAreas(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.numberOfScrollableAreas{tuple(args)} -> method')

    def fn_observeGC(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.observeGC{tuple(args)} -> method')

    def fn_observeUseCounter(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.observeUseCounter{tuple(args)} -> method')

    def fn_originTrialsTest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.originTrialsTest{tuple(args)} -> method')

    def fn_pageNumber(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.pageNumber{tuple(args)} -> method')

    def fn_pageScaleFactor(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.pageScaleFactor{tuple(args)} -> method')

    def fn_pageZoomFactor(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.pageZoomFactor{tuple(args)} -> method')

    def fn_parentTreeScope(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.parentTreeScope{tuple(args)} -> method')

    def fn_pauseAnimations(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.pauseAnimations{tuple(args)} -> method')

    def fn_peerConnectionCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.peerConnectionCount{tuple(args)} -> method')

    def fn_pendingVibrationPattern(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.pendingVibrationPattern{tuple(args)} -> method')

    def fn_pointerEventHandlerCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.pointerEventHandlerCount{tuple(args)} -> method')

    def fn_previousInFlatTree(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.previousInFlatTree{tuple(args)} -> method')

    def fn_promiseCheck(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.promiseCheck{tuple(args)} -> method')

    def fn_promiseCheckOverload(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.promiseCheckOverload{tuple(args)} -> method')

    def fn_promiseCheckRange(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.promiseCheckRange{tuple(args)} -> method')

    def fn_promiseCheckWithoutExceptionState(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.promiseCheckWithoutExceptionState{tuple(args)} -> method')

    def fn_rangeAsText(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.rangeAsText{tuple(args)} -> method')

    def fn_rangeFromLocationAndLength(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.rangeFromLocationAndLength{tuple(args)} -> method')

    def fn_recordTest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.recordTest{tuple(args)} -> method')

    def fn_registerURLSchemeAsBypassingContentSecurityPolicy(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.registerURLSchemeAsBypassingContentSecurityPolicy{tuple(args)} -> method')

    def fn_removeMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.removeMarker{tuple(args)} -> method')

    def fn_removeURLSchemeRegisteredAsBypassingContentSecurityPolicy(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.removeURLSchemeRegisteredAsBypassingContentSecurityPolicy{tuple(args)} -> method')

    def fn_removeVirtualSensor(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.removeVirtualSensor{tuple(args)} -> method')

    def fn_replaceMisspelled(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.replaceMisspelled{tuple(args)} -> method')

    def fn_resetSelectListTypeAheadSession(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.resetSelectListTypeAheadSession{tuple(args)} -> method')

    def fn_resetTypeAheadSession(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.resetTypeAheadSession{tuple(args)} -> method')

    def fn_rtcCertificateEquals(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.rtcCertificateEquals{tuple(args)} -> method')

    def fn_runFuzzer(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.runFuzzer{tuple(args)} -> method')

    def fn_runIdleTimeSpellChecker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.runIdleTimeSpellChecker{tuple(args)} -> method')

    def fn_scrollEventHandlerCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.scrollEventHandlerCount{tuple(args)} -> method')

    def fn_scrollingStateTreeAsText(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.scrollingStateTreeAsText{tuple(args)} -> method')

    def fn_selectColorInColorChooser(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectColorInColorChooser{tuple(args)} -> method')

    def fn_selectFedCmAccount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectFedCmAccount{tuple(args)} -> method')

    def fn_selectMenuListText(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectMenuListText{tuple(args)} -> method')

    def fn_selectPopupItemStyleFontHeight(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectPopupItemStyleFontHeight{tuple(args)} -> method')

    def fn_selectPopupItemStyleIsRtl(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectPopupItemStyleIsRtl{tuple(args)} -> method')

    def fn_selectedHTMLForClipboard(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectedHTMLForClipboard{tuple(args)} -> method')

    def fn_selectedTextForClipboard(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectedTextForClipboard{tuple(args)} -> method')

    def fn_selectionBounds(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.selectionBounds{tuple(args)} -> method')

    def fn_sequenceTest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.sequenceTest{tuple(args)} -> method')

    def fn_serializeObject(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.serializeObject{tuple(args)} -> method')

    def fn_setAllowPerChunkTransferring(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setAllowPerChunkTransferring{tuple(args)} -> method')

    def fn_setAutofilled(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setAutofilled{tuple(args)} -> method')

    def fn_setAutofilledValue(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setAutofilledValue{tuple(args)} -> method')

    def fn_setBackForwardCacheRestorationBufferSize(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setBackForwardCacheRestorationBufferSize{tuple(args)} -> method')

    def fn_setBrowserControlsShownRatio(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setBrowserControlsShownRatio{tuple(args)} -> method')

    def fn_setBrowserControlsState(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setBrowserControlsState{tuple(args)} -> method')

    def fn_setCapsLockState(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setCapsLockState{tuple(args)} -> method')

    def fn_setDarkPreferredColorScheme(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setDarkPreferredColorScheme{tuple(args)} -> method')

    def fn_setDarkPreferredRootScrollbarColorScheme(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setDarkPreferredRootScrollbarColorScheme{tuple(args)} -> method')

    def fn_setDeviceEmulationScale(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setDeviceEmulationScale{tuple(args)} -> method')

    def fn_setDevicePostureOverride(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setDevicePostureOverride{tuple(args)} -> method')

    def fn_setEventTimingBufferSize(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setEventTimingBufferSize{tuple(args)} -> method')

    def fn_setFocused(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setFocused{tuple(args)} -> method')

    def fn_setForcedColorsAndDarkPreferredColorScheme(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setForcedColorsAndDarkPreferredColorScheme{tuple(args)} -> method')

    def fn_setFormControlStateOfHistoryItem(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setFormControlStateOfHistoryItem{tuple(args)} -> method')

    def fn_setInitialFocus(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setInitialFocus{tuple(args)} -> method')

    def fn_setIsAdFrame(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setIsAdFrame{tuple(args)} -> method')

    def fn_setIsCursorVisible(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setIsCursorVisible{tuple(args)} -> method')

    def fn_setIsLowEndDevice(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setIsLowEndDevice{tuple(args)} -> method')

    def fn_setMarkedTextMatchesAreHighlighted(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setMarkedTextMatchesAreHighlighted{tuple(args)} -> method')

    def fn_setMarker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setMarker{tuple(args)} -> method')

    def fn_setMaxNumberOfFramesToTen(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setMaxNumberOfFramesToTen{tuple(args)} -> method')

    def fn_setMediaControlsTestMode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setMediaControlsTestMode{tuple(args)} -> method')

    def fn_setMockHyphenation(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setMockHyphenation{tuple(args)} -> method')

    def fn_setNetworkConnectionInfoOverride(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setNetworkConnectionInfoOverride{tuple(args)} -> method')

    def fn_setPageScaleFactor(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setPageScaleFactor{tuple(args)} -> method')

    def fn_setPageScaleFactorLimits(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setPageScaleFactorLimits{tuple(args)} -> method')

    def fn_setPermission(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setPermission{tuple(args)} -> method')

    def fn_setPersistent(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setPersistent{tuple(args)} -> method')

    def fn_setPseudoClassState(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setPseudoClassState{tuple(args)} -> method')

    def fn_setSaveDataEnabled(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setSaveDataEnabled{tuple(args)} -> method')

    def fn_setScrollbarVisibilityInScrollableArea(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setScrollbarVisibilityInScrollableArea{tuple(args)} -> method')

    def fn_setSelectionRangeForNumberType(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setSelectionRangeForNumberType{tuple(args)} -> method')

    def fn_setShouldRevealPassword(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setShouldRevealPassword{tuple(args)} -> method')

    def fn_setStorageAccess(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setStorageAccess{tuple(args)} -> method')

    def fn_setSuggestedValue(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setSuggestedValue{tuple(args)} -> method')

    def fn_setSystemTimeZone(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setSystemTimeZone{tuple(args)} -> method')

    def fn_setTextMatchMarkersActive(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setTextMatchMarkersActive{tuple(args)} -> method')

    def fn_setUserPreferredLanguages(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setUserPreferredLanguages{tuple(args)} -> method')

    def fn_setValueForUser(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setValueForUser{tuple(args)} -> method')

    def fn_setVisualViewportOffset(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.setVisualViewportOffset{tuple(args)} -> method')

    def fn_shadowPseudoId(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.shadowPseudoId{tuple(args)} -> method')

    def fn_shadowRoot(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.shadowRoot{tuple(args)} -> method')

    def fn_shortcutIconURLs(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.shortcutIconURLs{tuple(args)} -> method')

    def fn_simulateRasterUnderInvalidations(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.simulateRasterUnderInvalidations{tuple(args)} -> method')

    def fn_spellCheckedTextLength(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.spellCheckedTextLength{tuple(args)} -> method')

    def fn_startTrackingRepaints(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.startTrackingRepaints{tuple(args)} -> method')

    def fn_stopResponsivenessMetricsUkmSampling(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.stopResponsivenessMetricsUkmSampling{tuple(args)} -> method')

    def fn_stopTrackingRepaints(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.stopTrackingRepaints{tuple(args)} -> method')

    def fn_styleForElementCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.styleForElementCount{tuple(args)} -> method')

    def fn_suggestedValue(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.suggestedValue{tuple(args)} -> method')

    def fn_supportedTextEncodingLabels(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.supportedTextEncodingLabels{tuple(args)} -> method')

    def fn_svgNamespace(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.svgNamespace{tuple(args)} -> method')

    def fn_svgTags(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.svgTags{tuple(args)} -> method')

    def fn_terminateServiceWorker(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.terminateServiceWorker{tuple(args)} -> method')

    def fn_touchEndOrCancelEventHandlerCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchEndOrCancelEventHandlerCount{tuple(args)} -> method')

    def fn_touchEventTargetLayerRects(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchEventTargetLayerRects{tuple(args)} -> method')

    def fn_touchNodeAdjustedToBestClickableNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchNodeAdjustedToBestClickableNode{tuple(args)} -> method')

    def fn_touchNodeAdjustedToBestContextMenuNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchNodeAdjustedToBestContextMenuNode{tuple(args)} -> method')

    def fn_touchNodeAdjustedToBestStylusWritableNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchNodeAdjustedToBestStylusWritableNode{tuple(args)} -> method')

    def fn_touchPositionAdjustedToBestClickableNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchPositionAdjustedToBestClickableNode{tuple(args)} -> method')

    def fn_touchPositionAdjustedToBestContextMenuNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchPositionAdjustedToBestContextMenuNode{tuple(args)} -> method')

    def fn_touchStartOrMoveEventHandlerCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.touchStartOrMoveEventHandlerCount{tuple(args)} -> method')

    def fn_treeScopeRootNode(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.treeScopeRootNode{tuple(args)} -> method')

    def fn_triggerTestInspectorIssue(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.triggerTestInspectorIssue{tuple(args)} -> method')

    def fn_typeConversions(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.typeConversions{tuple(args)} -> method')

    def fn_unionTypesTest(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.unionTypesTest{tuple(args)} -> method')

    def fn_unscopableMethod(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.unscopableMethod{tuple(args)} -> method')

    def fn_updateLayoutAndRunPostLayoutTasks(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.updateLayoutAndRunPostLayoutTasks{tuple(args)} -> method')

    def fn_updateStyleAndReturnAffectedElementCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.updateStyleAndReturnAffectedElementCount{tuple(args)} -> method')

    def fn_updateVirtualSensor(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.updateVirtualSensor{tuple(args)} -> method')

    def fn_useMockOverlayScrollbars(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.useMockOverlayScrollbars{tuple(args)} -> method')

    def fn_userPreferredLanguages(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.userPreferredLanguages{tuple(args)} -> method')

    def fn_viewportAsText(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.viewportAsText{tuple(args)} -> method')

    def fn_waitForPeerConnectionDispatchEventsTaskCreated(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.waitForPeerConnectionDispatchEventsTaskCreated{tuple(args)} -> method')

    def fn_wheelEventHandlerCount(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.wheelEventHandlerCount{tuple(args)} -> method')

    def fn_zeroBasedDocumentTimeToMonotonicTime(self, *args):
        logger.debug(f'patch -> v8_internals.py -> Internals.zeroBasedDocumentTimeToMonotonicTime{tuple(args)} -> method')
