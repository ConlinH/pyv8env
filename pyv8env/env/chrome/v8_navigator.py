from .flags import *


@construct_100001
class Navigator:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("vendorSub", "get_vendorSub", None, 0, 1, 0, 0, 0, 0, 1),
        ("productSub", "get_productSub", None, 0, 1, 0, 0, 0, 0, 1),
        ("vendor", "get_vendor", None, 0, 1, 0, 0, 0, 0, 1),
        ("maxTouchPoints", "get_maxTouchPoints", None, 0, 1, 0, 0, 0, 0, 1),
        ("scheduling", "get_scheduling", None, 0, 1, 0, 0, 0, 0, 1),
        ("userActivation", "get_userActivation", None, 0, 1, 0, 0, 0, 0, 1),
        ("doNotTrack", "get_doNotTrack", None, 0, 1, 0, 0, 0, 0, 1),
        ("geolocation", "get_geolocation", None, 0, 1, 0, 0, 0, 0, 1),
        ("connection", "get_connection", None, 0, 1, 0, 0, 0, 0, 1),
        ("plugins", "get_plugins", None, 0, 1, 0, 0, 0, 0, 1),
        ("mimeTypes", "get_mimeTypes", None, 0, 1, 0, 0, 0, 0, 1),
        ("pdfViewerEnabled", "get_pdfViewerEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitTemporaryStorage", "get_webkitTemporaryStorage", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitPersistentStorage", "get_webkitPersistentStorage", None, 0, 1, 0, 0, 0, 0, 1),
        ("windowControlsOverlay", "get_windowControlsOverlay", None, 0, 1, 0, 0, 0, 0, 1),
        ("hardwareConcurrency", "get_hardwareConcurrency", None, 0, 1, 0, 0, 0, 0, 1),
        ("cookieEnabled", "get_cookieEnabled", None, 0, 1, 0, 0, 0, 0, 1),
        ("appCodeName", "get_appCodeName", None, 0, 1, 0, 0, 0, 0, 1),
        ("appName", "get_appName", None, 0, 1, 0, 0, 0, 0, 1),
        ("appVersion", "get_appVersion", None, 0, 1, 0, 0, 0, 0, 1),
        ("platform", "get_platform", None, 0, 1, 0, 0, 0, 0, 1),
        ("product", "get_product", None, 0, 1, 0, 0, 0, 0, 1),
        ("userAgent", "get_userAgent", None, 0, 1, 0, 0, 0, 0, 1),
        ("language", "get_language", None, 0, 1, 0, 0, 0, 0, 1),
        ("languages", "get_languages", None, 0, 1, 0, 0, 0, 0, 1),
        ("onLine", "get_onLine", None, 0, 1, 0, 0, 0, 0, 1),
        ("webdriver", "get_webdriver", None, 0, 1, 0, 0, 0, 0, 1),
        ("preferences", "get_preferences", None, 0, 1, 0, 0, 0, 0, 1),
        ("deprecatedRunAdAuctionEnforcesKAnonymity", "get_deprecatedRunAdAuctionEnforcesKAnonymity", None, 0, 1, 0, 0, 0, 0, 1),
        ("protectedAudience", "get_protectedAudience", None, 0, 1, 0, 0, 0, 0, 1),
        ("bluetooth", "get_bluetooth", None, 0, 1, 0, 0, 0, 0, 1),
        ("storageBuckets", "get_storageBuckets", None, 0, 1, 0, 0, 0, 0, 1),
        ("clipboard", "get_clipboard", None, 0, 1, 0, 0, 0, 0, 1),
        ("credentials", "get_credentials", None, 0, 1, 0, 0, 0, 0, 1),
        ("keyboard", "get_keyboard", None, 0, 1, 0, 0, 0, 0, 1),
        ("managed", "get_managed", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaDevices", "get_mediaDevices", None, 0, 1, 0, 0, 0, 0, 1),
        ("storage", "get_storage", None, 0, 1, 0, 0, 0, 0, 1),
        ("serviceWorker", "get_serviceWorker", None, 0, 1, 0, 0, 0, 0, 1),
        ("virtualKeyboard", "get_virtualKeyboard", None, 0, 1, 0, 0, 0, 0, 1),
        ("wakeLock", "get_wakeLock", None, 0, 1, 0, 0, 0, 0, 1),
        ("deviceMemory", "get_deviceMemory", None, 0, 1, 0, 0, 0, 0, 1),
        ("userAgentData", "get_userAgentData", None, 0, 1, 0, 0, 0, 0, 1),
        ("contacts", "get_contacts", None, 0, 1, 0, 0, 0, 0, 1),
        ("cookieDeprecationLabel", "get_cookieDeprecationLabel", None, 0, 1, 0, 0, 0, 0, 1),
        ("identity", "get_identity", None, 0, 1, 0, 0, 0, 0, 1),
        ("login", "get_login", None, 0, 1, 0, 0, 0, 0, 1),
        ("ink", "get_ink", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaCapabilities", "get_mediaCapabilities", None, 0, 1, 0, 0, 0, 0, 1),
        ("devicePosture", "get_devicePosture", None, 0, 1, 0, 0, 0, 0, 1),
        ("hid", "get_hid", None, 0, 1, 0, 0, 0, 0, 1),
        ("lockedMode", "get_lockedMode", None, 0, 1, 0, 0, 0, 0, 1),
        ("locks", "get_locks", None, 0, 1, 0, 0, 0, 0, 1),
        ("gpu", "get_gpu", None, 0, 1, 0, 0, 0, 0, 1),
        ("mediaSession", "get_mediaSession", None, 0, 1, 0, 0, 0, 0, 1),
        ("ml", "get_ml", None, 0, 1, 0, 0, 0, 0, 1),
        ("permissions", "get_permissions", None, 0, 1, 0, 0, 0, 0, 1),
        ("presentation", "get_presentation", None, 0, 1, 0, 0, 0, 0, 1),
        ("subApps", "get_subApps", None, 0, 1, 0, 0, 0, 0, 1),
        ("usb", "get_usb", None, 0, 1, 0, 0, 0, 0, 1),
        ("xr", "get_xr", None, 0, 1, 0, 0, 0, 0, 1),
        ("printing", "get_printing", None, 0, 1, 0, 0, 0, 0, 1),
        ("serial", "get_serial", None, 0, 1, 0, 0, 0, 0, 1),
        ("smartCard", "get_smartCard", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getGamepads", "fn_getGamepads", 0, 0, 1, 0, 0, 0, 0),
        ("javaEnabled", "fn_javaEnabled", 0, 0, 1, 0, 0, 0, 0),
        ("sendBeacon", "fn_sendBeacon", 1, 0, 1, 0, 0, 0, 0),
        ("vibrate", "fn_vibrate", 1, 0, 1, 0, 0, 0, 0),
        ("adAuctionComponents", "fn_adAuctionComponents", 1, 0, 1, 0, 0, 0, 0),
        ("runAdAuction", "fn_runAdAuction", 1, 0, 1, 0, 1, 0, 0),
        ("canLoadAdAuctionFencedFrame", "fn_canLoadAdAuctionFencedFrame", 0, 0, 1, 0, 0, 0, 0),
        ("canShare", "fn_canShare", 0, 0, 1, 0, 0, 0, 0),
        ("share", "fn_share", 0, 0, 1, 0, 1, 0, 0),
        ("clearAppBadge", "fn_clearAppBadge", 0, 0, 1, 0, 1, 0, 0),
        ("getBattery", "fn_getBattery", 0, 0, 1, 0, 1, 0, 0),
        ("getUserMedia", "fn_getUserMedia", 3, 0, 1, 0, 0, 0, 0),
        ("requestMIDIAccess", "fn_requestMIDIAccess", 0, 0, 1, 0, 1, 0, 0),
        ("requestMediaKeySystemAccess", "fn_requestMediaKeySystemAccess", 2, 0, 1, 0, 1, 0, 0),
        ("setAppBadge", "fn_setAppBadge", 0, 0, 1, 0, 1, 0, 0),
        ("webkitGetUserMedia", "fn_webkitGetUserMedia", 3, 0, 1, 0, 0, 0, 0),
        ("clearOriginJoinedAdInterestGroups", "fn_clearOriginJoinedAdInterestGroups", 1, 0, 1, 0, 1, 0, 0),
        ("createAdRequest", "fn_createAdRequest", 1, 0, 1, 0, 1, 0, 0),
        ("finalizeAd", "fn_finalizeAd", 2, 0, 1, 0, 1, 0, 0),
        ("createAuctionNonce", "fn_createAuctionNonce", 0, 0, 1, 0, 1, 0, 0),
        ("createHandwritingRecognizer", "fn_createHandwritingRecognizer", 1, 0, 1, 0, 1, 0, 0),
        ("queryHandwritingRecognizer", "fn_queryHandwritingRecognizer", 1, 0, 1, 0, 1, 0, 0),
        ("deprecatedReplaceInURN", "fn_deprecatedReplaceInURN", 2, 0, 1, 0, 1, 0, 0),
        ("deprecatedURNToURL", "fn_deprecatedURNToURL", 1, 0, 1, 0, 1, 0, 0),
        ("getInstalledRelatedApps", "fn_getInstalledRelatedApps", 0, 0, 1, 0, 1, 0, 0),
        ("getInterestGroupAdAuctionData", "fn_getInterestGroupAdAuctionData", 1, 0, 1, 0, 1, 0, 0),
        ("joinAdInterestGroup", "fn_joinAdInterestGroup", 1, 0, 1, 0, 1, 0, 0),
        ("leaveAdInterestGroup", "fn_leaveAdInterestGroup", 0, 0, 1, 0, 1, 0, 0),
        ("updateAdInterestGroups", "fn_updateAdInterestGroups", 0, 0, 1, 0, 0, 0, 0),
        ("registerProtocolHandler", "fn_registerProtocolHandler", 2, 0, 1, 0, 0, 0, 0),
        ("unregisterProtocolHandler", "fn_unregisterProtocolHandler", 2, 0, 1, 0, 0, 0, 0),

    )

    def get_vendorSub(self):
        val = self._attr.get('vendorSub')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.vendorSub -> get attr')

    def get_productSub(self):
        val = self._attr.get('productSub')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.productSub -> get attr')

    def get_vendor(self):
        val = self._attr.get('vendor')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.vendor -> get attr')

    def get_maxTouchPoints(self):
        val = self._attr.get('maxTouchPoints')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.maxTouchPoints -> get attr')

    def get_scheduling(self):
        val = self._attr.get('scheduling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.scheduling -> get attr')

    def get_userActivation(self):
        val = self._attr.get('userActivation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.userActivation -> get attr')

    def get_doNotTrack(self):
        val = self._attr.get('doNotTrack')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.doNotTrack -> get attr')

    def get_geolocation(self):
        val = self._attr.get('geolocation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.geolocation -> get attr')

    def get_connection(self):
        val = self._attr.get('connection')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.connection -> get attr')

    def get_plugins(self):
        val = self._attr.get('plugins')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.plugins -> get attr')

    def get_mimeTypes(self):
        val = self._attr.get('mimeTypes')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.mimeTypes -> get attr')

    def get_pdfViewerEnabled(self):
        val = self._attr.get('pdfViewerEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.pdfViewerEnabled -> get attr')

    def get_webkitTemporaryStorage(self):
        val = self._attr.get('webkitTemporaryStorage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.webkitTemporaryStorage -> get attr')

    def get_webkitPersistentStorage(self):
        val = self._attr.get('webkitPersistentStorage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.webkitPersistentStorage -> get attr')

    def get_windowControlsOverlay(self):
        val = self._attr.get('windowControlsOverlay')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.windowControlsOverlay -> get attr')

    def get_hardwareConcurrency(self):
        val = self._attr.get('hardwareConcurrency')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.hardwareConcurrency -> get attr')

    def get_cookieEnabled(self):
        val = self._attr.get('cookieEnabled')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.cookieEnabled -> get attr')

    def get_appCodeName(self):
        val = self._attr.get('appCodeName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.appCodeName -> get attr')

    def get_appName(self):
        val = self._attr.get('appName')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.appName -> get attr')

    def get_appVersion(self):
        val = self._attr.get('appVersion')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.appVersion -> get attr')

    def get_platform(self):
        val = self._attr.get('platform')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.platform -> get attr')

    def get_product(self):
        val = self._attr.get('product')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.product -> get attr')

    def get_userAgent(self):
        val = self._attr.get('userAgent')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.userAgent -> get attr')

    def get_language(self):
        val = self._attr.get('language')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.language -> get attr')

    def get_languages(self):
        val = self._attr.get('languages')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.languages -> get attr')

    def get_onLine(self):
        val = self._attr.get('onLine')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.onLine -> get attr')

    def get_webdriver(self):
        val = self._attr.get('webdriver')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.webdriver -> get attr')

    def get_preferences(self):
        val = self._attr.get('preferences')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.preferences -> get attr')

    def get_deprecatedRunAdAuctionEnforcesKAnonymity(self):
        val = self._attr.get('deprecatedRunAdAuctionEnforcesKAnonymity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.deprecatedRunAdAuctionEnforcesKAnonymity -> get attr')

    def get_protectedAudience(self):
        val = self._attr.get('protectedAudience')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.protectedAudience -> get attr')

    def get_bluetooth(self):
        val = self._attr.get('bluetooth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.bluetooth -> get attr')

    def get_storageBuckets(self):
        val = self._attr.get('storageBuckets')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.storageBuckets -> get attr')

    def get_clipboard(self):
        val = self._attr.get('clipboard')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.clipboard -> get attr')

    def get_credentials(self):
        val = self._attr.get('credentials')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.credentials -> get attr')

    def get_keyboard(self):
        val = self._attr.get('keyboard')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.keyboard -> get attr')

    def get_managed(self):
        val = self._attr.get('managed')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.managed -> get attr')

    def get_mediaDevices(self):
        val = self._attr.get('mediaDevices')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.mediaDevices -> get attr')

    def get_storage(self):
        val = self._attr.get('storage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.storage -> get attr')

    def get_serviceWorker(self):
        val = self._attr.get('serviceWorker')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.serviceWorker -> get attr')

    def get_virtualKeyboard(self):
        val = self._attr.get('virtualKeyboard')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.virtualKeyboard -> get attr')

    def get_wakeLock(self):
        val = self._attr.get('wakeLock')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.wakeLock -> get attr')

    def get_deviceMemory(self):
        val = self._attr.get('deviceMemory')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.deviceMemory -> get attr')

    def get_userAgentData(self):
        val = self._attr.get('userAgentData')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.userAgentData -> get attr')

    def get_contacts(self):
        val = self._attr.get('contacts')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.contacts -> get attr')

    def get_cookieDeprecationLabel(self):
        val = self._attr.get('cookieDeprecationLabel')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.cookieDeprecationLabel -> get attr')

    def get_identity(self):
        val = self._attr.get('identity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.identity -> get attr')

    def get_login(self):
        val = self._attr.get('login')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.login -> get attr')

    def get_ink(self):
        val = self._attr.get('ink')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.ink -> get attr')

    def get_mediaCapabilities(self):
        val = self._attr.get('mediaCapabilities')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.mediaCapabilities -> get attr')

    def get_devicePosture(self):
        val = self._attr.get('devicePosture')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.devicePosture -> get attr')

    def get_hid(self):
        val = self._attr.get('hid')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.hid -> get attr')

    def get_lockedMode(self):
        val = self._attr.get('lockedMode')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.lockedMode -> get attr')

    def get_locks(self):
        val = self._attr.get('locks')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.locks -> get attr')

    def get_gpu(self):
        val = self._attr.get('gpu')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.gpu -> get attr')

    def get_mediaSession(self):
        val = self._attr.get('mediaSession')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.mediaSession -> get attr')

    def get_ml(self):
        val = self._attr.get('ml')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.ml -> get attr')

    def get_permissions(self):
        val = self._attr.get('permissions')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.permissions -> get attr')

    def get_presentation(self):
        val = self._attr.get('presentation')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.presentation -> get attr')

    def get_subApps(self):
        val = self._attr.get('subApps')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.subApps -> get attr')

    def get_usb(self):
        val = self._attr.get('usb')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.usb -> get attr')

    def get_xr(self):
        val = self._attr.get('xr')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.xr -> get attr')

    def get_printing(self):
        val = self._attr.get('printing')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.printing -> get attr')

    def get_serial(self):
        val = self._attr.get('serial')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.serial -> get attr')

    def get_smartCard(self):
        val = self._attr.get('smartCard')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_navigator.py -> Navigator.smartCard -> get attr')

    def fn_getGamepads(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.getGamepads{tuple(args)} -> method')

    def fn_javaEnabled(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.javaEnabled{tuple(args)} -> method')

    def fn_sendBeacon(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.sendBeacon{tuple(args)} -> method')

    def fn_vibrate(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.vibrate{tuple(args)} -> method')

    def fn_adAuctionComponents(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.adAuctionComponents{tuple(args)} -> method')

    def fn_runAdAuction(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.runAdAuction{tuple(args)} -> method')

    def fn_canLoadAdAuctionFencedFrame(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.canLoadAdAuctionFencedFrame{tuple(args)} -> method')

    def fn_canShare(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.canShare{tuple(args)} -> method')

    def fn_share(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.share{tuple(args)} -> method')

    def fn_clearAppBadge(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.clearAppBadge{tuple(args)} -> method')

    def fn_getBattery(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.getBattery{tuple(args)} -> method')

    def fn_getUserMedia(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.getUserMedia{tuple(args)} -> method')

    def fn_requestMIDIAccess(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.requestMIDIAccess{tuple(args)} -> method')

    def fn_requestMediaKeySystemAccess(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.requestMediaKeySystemAccess{tuple(args)} -> method')

    def fn_setAppBadge(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.setAppBadge{tuple(args)} -> method')

    def fn_webkitGetUserMedia(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.webkitGetUserMedia{tuple(args)} -> method')

    def fn_clearOriginJoinedAdInterestGroups(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.clearOriginJoinedAdInterestGroups{tuple(args)} -> method')

    def fn_createAdRequest(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.createAdRequest{tuple(args)} -> method')

    def fn_finalizeAd(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.finalizeAd{tuple(args)} -> method')

    def fn_createAuctionNonce(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.createAuctionNonce{tuple(args)} -> method')

    def fn_createHandwritingRecognizer(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.createHandwritingRecognizer{tuple(args)} -> method')

    def fn_queryHandwritingRecognizer(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.queryHandwritingRecognizer{tuple(args)} -> method')

    def fn_deprecatedReplaceInURN(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.deprecatedReplaceInURN{tuple(args)} -> method')

    def fn_deprecatedURNToURL(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.deprecatedURNToURL{tuple(args)} -> method')

    def fn_getInstalledRelatedApps(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.getInstalledRelatedApps{tuple(args)} -> method')

    def fn_getInterestGroupAdAuctionData(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.getInterestGroupAdAuctionData{tuple(args)} -> method')

    def fn_joinAdInterestGroup(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.joinAdInterestGroup{tuple(args)} -> method')

    def fn_leaveAdInterestGroup(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.leaveAdInterestGroup{tuple(args)} -> method')

    def fn_updateAdInterestGroups(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.updateAdInterestGroups{tuple(args)} -> method')

    def fn_registerProtocolHandler(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.registerProtocolHandler{tuple(args)} -> method')

    def fn_unregisterProtocolHandler(self, *args):
        logger.debug(f'patch -> v8_navigator.py -> Navigator.unregisterProtocolHandler{tuple(args)} -> method')
