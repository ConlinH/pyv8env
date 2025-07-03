from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLIFrameElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLIFrameElement, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("src", "get_src", "set_src", 0, 1, 0, 0, 0, 0, 1),
        ("srcdoc", "get_srcdoc", "set_srcdoc", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("sandbox", "get_sandbox", "set_sandbox", 0, 1, 0, 0, 0, 0, 1),
        ("allowFullscreen", "get_allowFullscreen", "set_allowFullscreen", 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("contentDocument", "get_contentDocument", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentWindow", "get_contentWindow", None, 0, 1, 0, 0, 0, 0, 1),
        ("referrerPolicy", "get_referrerPolicy", "set_referrerPolicy", 0, 1, 0, 0, 0, 0, 1),
        ("csp", "get_csp", "set_csp", 0, 1, 0, 0, 0, 0, 1),
        ("allow", "get_allow", "set_allow", 0, 1, 0, 0, 0, 0, 1),
        ("featurePolicy", "get_featurePolicy", None, 0, 1, 0, 0, 0, 0, 1),
        ("loading", "get_loading", "set_loading", 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("scrolling", "get_scrolling", "set_scrolling", 0, 1, 0, 0, 0, 0, 1),
        ("frameBorder", "get_frameBorder", "set_frameBorder", 0, 1, 0, 0, 0, 0, 1),
        ("longDesc", "get_longDesc", "set_longDesc", 0, 1, 0, 0, 0, 0, 1),
        ("marginHeight", "get_marginHeight", "set_marginHeight", 0, 1, 0, 0, 0, 0, 1),
        ("marginWidth", "get_marginWidth", "set_marginWidth", 0, 1, 0, 0, 0, 0, 1),
        ("credentialless", "get_credentialless", "set_credentialless", 0, 1, 0, 0, 0, 0, 1),
        ("allowPaymentRequest", "get_allowPaymentRequest", "set_allowPaymentRequest", 0, 1, 0, 0, 0, 0, 1),
        ("policy", "get_policy", "set_policy", 0, 1, 0, 0, 0, 0, 1),
        ("privateToken", "get_privateToken", "set_privateToken", 0, 1, 0, 0, 0, 0, 1),
        ("browsingTopics", "get_browsingTopics", "set_browsingTopics", 0, 1, 0, 0, 0, 0, 1),
        ("adAuctionHeaders", "get_adAuctionHeaders", "set_adAuctionHeaders", 0, 1, 0, 0, 0, 0, 1),
        ("sharedStorageWritable", "get_sharedStorageWritable", "set_sharedStorageWritable", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("getSVGDocument", "fn_getSVGDocument", 0, 0, 1, 0, 0, 0, 0),

    )

    def get_src(self):
        val = self._attr.get('src')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.src -> get attr')

    def set_src(self, val):
        self._attr['src'] = val

    def get_srcdoc(self):
        val = self._attr.get('srcdoc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.srcdoc -> get attr')

    def set_srcdoc(self, val):
        self._attr['srcdoc'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_sandbox(self):
        val = self._attr.get('sandbox')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.sandbox -> get attr')

    def set_sandbox(self, val):
        self._attr['sandbox'] = val

    def get_allowFullscreen(self):
        val = self._attr.get('allowFullscreen')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.allowFullscreen -> get attr')

    def set_allowFullscreen(self, val):
        self._attr['allowFullscreen'] = val

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_contentDocument(self):
        val = self._attr.get('contentDocument')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.contentDocument -> get attr')

    def get_contentWindow(self):
        val = self._attr.get('contentWindow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.contentWindow -> get attr')

    def get_referrerPolicy(self):
        val = self._attr.get('referrerPolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.referrerPolicy -> get attr')

    def set_referrerPolicy(self, val):
        self._attr['referrerPolicy'] = val

    def get_csp(self):
        val = self._attr.get('csp')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.csp -> get attr')

    def set_csp(self, val):
        self._attr['csp'] = val

    def get_allow(self):
        val = self._attr.get('allow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.allow -> get attr')

    def set_allow(self, val):
        self._attr['allow'] = val

    def get_featurePolicy(self):
        val = self._attr.get('featurePolicy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.featurePolicy -> get attr')

    def get_loading(self):
        val = self._attr.get('loading')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.loading -> get attr')

    def set_loading(self, val):
        self._attr['loading'] = val

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_scrolling(self):
        val = self._attr.get('scrolling')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.scrolling -> get attr')

    def set_scrolling(self, val):
        self._attr['scrolling'] = val

    def get_frameBorder(self):
        val = self._attr.get('frameBorder')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.frameBorder -> get attr')

    def set_frameBorder(self, val):
        self._attr['frameBorder'] = val

    def get_longDesc(self):
        val = self._attr.get('longDesc')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.longDesc -> get attr')

    def set_longDesc(self, val):
        self._attr['longDesc'] = val

    def get_marginHeight(self):
        val = self._attr.get('marginHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.marginHeight -> get attr')

    def set_marginHeight(self, val):
        self._attr['marginHeight'] = val

    def get_marginWidth(self):
        val = self._attr.get('marginWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.marginWidth -> get attr')

    def set_marginWidth(self, val):
        self._attr['marginWidth'] = val

    def get_credentialless(self):
        val = self._attr.get('credentialless')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.credentialless -> get attr')

    def set_credentialless(self, val):
        self._attr['credentialless'] = val

    def get_allowPaymentRequest(self):
        val = self._attr.get('allowPaymentRequest')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.allowPaymentRequest -> get attr')

    def set_allowPaymentRequest(self, val):
        self._attr['allowPaymentRequest'] = val

    def get_policy(self):
        val = self._attr.get('policy')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.policy -> get attr')

    def set_policy(self, val):
        self._attr['policy'] = val

    def get_privateToken(self):
        val = self._attr.get('privateToken')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.privateToken -> get attr')

    def set_privateToken(self, val):
        self._attr['privateToken'] = val

    def get_browsingTopics(self):
        val = self._attr.get('browsingTopics')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.browsingTopics -> get attr')

    def set_browsingTopics(self, val):
        self._attr['browsingTopics'] = val

    def get_adAuctionHeaders(self):
        val = self._attr.get('adAuctionHeaders')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.adAuctionHeaders -> get attr')

    def set_adAuctionHeaders(self, val):
        self._attr['adAuctionHeaders'] = val

    def get_sharedStorageWritable(self):
        val = self._attr.get('sharedStorageWritable')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.sharedStorageWritable -> get attr')

    def set_sharedStorageWritable(self, val):
        self._attr['sharedStorageWritable'] = val

    def fn_getSVGDocument(self, *args):
        logger.debug(f'patch -> v8_html_iframe_element.py -> HTMLIFrameElement.getSVGDocument{tuple(args)} -> method')
