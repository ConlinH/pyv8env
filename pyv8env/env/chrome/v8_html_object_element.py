from .flags import *
from .v8_html_element import HTMLElement


@construct_110001
class HTMLObjectElement(HTMLElement):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(HTMLObjectElement, self).__init__(*args, **kw)

    def __v8_name_get__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_name_get__')
            
    def __v8_name_set__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_name_set__')
            
    def __v8_name_del__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_name_del__')
            
    def __v8_name_definer__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_name_definer__')
            
    def __v8_name_desc__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_name_desc__')
            
    def __v8_index_get__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_index_get__')
            
    def __v8_index_set__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_index_set__')
            
    def __v8_index_del__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_index_del__')
            
    def __v8_index_definer__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_index_definer__')
            
    def __v8_index_desc__(self, *args):
        logger.debug('patch -> v8_html_object_element.py -> HTMLObjectElement.__v8_index_desc__')
            
    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("data", "get_data", "set_data", 0, 1, 0, 0, 0, 0, 1),
        ("type", "get_type", "set_type", 0, 1, 0, 0, 0, 0, 1),
        ("name", "get_name", "set_name", 0, 1, 0, 0, 0, 0, 1),
        ("useMap", "get_useMap", "set_useMap", 0, 1, 0, 0, 0, 0, 1),
        ("form", "get_form", None, 0, 1, 0, 0, 0, 0, 1),
        ("width", "get_width", "set_width", 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", "set_height", 0, 1, 0, 0, 0, 0, 1),
        ("contentDocument", "get_contentDocument", None, 0, 1, 0, 0, 0, 0, 1),
        ("contentWindow", "get_contentWindow", None, 0, 1, 0, 0, 0, 0, 1),
        ("willValidate", "get_willValidate", None, 0, 1, 0, 0, 0, 0, 1),
        ("validity", "get_validity", None, 0, 1, 0, 0, 0, 0, 1),
        ("validationMessage", "get_validationMessage", None, 0, 1, 0, 0, 0, 0, 1),
        ("align", "get_align", "set_align", 0, 1, 0, 0, 0, 0, 1),
        ("archive", "get_archive", "set_archive", 0, 1, 0, 0, 0, 0, 1),
        ("code", "get_code", "set_code", 0, 1, 0, 0, 0, 0, 1),
        ("declare", "get_declare", "set_declare", 0, 1, 0, 0, 0, 0, 1),
        ("hspace", "get_hspace", "set_hspace", 0, 1, 0, 0, 0, 0, 1),
        ("standby", "get_standby", "set_standby", 0, 1, 0, 0, 0, 0, 1),
        ("vspace", "get_vspace", "set_vspace", 0, 1, 0, 0, 0, 0, 1),
        ("codeBase", "get_codeBase", "set_codeBase", 0, 1, 0, 0, 0, 0, 1),
        ("codeType", "get_codeType", "set_codeType", 0, 1, 0, 0, 0, 0, 1),
        ("border", "get_border", "set_border", 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("checkValidity", "fn_checkValidity", 0, 0, 1, 0, 0, 0, 0),
        ("getSVGDocument", "fn_getSVGDocument", 0, 0, 1, 0, 0, 0, 0),
        ("reportValidity", "fn_reportValidity", 0, 0, 1, 0, 0, 0, 0),
        ("setCustomValidity", "fn_setCustomValidity", 1, 0, 1, 0, 0, 0, 0),

    )

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.data -> get attr')

    def set_data(self, val):
        self._attr['data'] = val

    def get_type(self):
        val = self._attr.get('type')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.type -> get attr')

    def set_type(self, val):
        self._attr['type'] = val

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.name -> get attr')

    def set_name(self, val):
        self._attr['name'] = val

    def get_useMap(self):
        val = self._attr.get('useMap')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.useMap -> get attr')

    def set_useMap(self, val):
        self._attr['useMap'] = val

    def get_form(self):
        val = self._attr.get('form')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.form -> get attr')

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.width -> get attr')

    def set_width(self, val):
        self._attr['width'] = val

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.height -> get attr')

    def set_height(self, val):
        self._attr['height'] = val

    def get_contentDocument(self):
        val = self._attr.get('contentDocument')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.contentDocument -> get attr')

    def get_contentWindow(self):
        val = self._attr.get('contentWindow')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.contentWindow -> get attr')

    def get_willValidate(self):
        val = self._attr.get('willValidate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.willValidate -> get attr')

    def get_validity(self):
        val = self._attr.get('validity')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.validity -> get attr')

    def get_validationMessage(self):
        val = self._attr.get('validationMessage')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.validationMessage -> get attr')

    def get_align(self):
        val = self._attr.get('align')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.align -> get attr')

    def set_align(self, val):
        self._attr['align'] = val

    def get_archive(self):
        val = self._attr.get('archive')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.archive -> get attr')

    def set_archive(self, val):
        self._attr['archive'] = val

    def get_code(self):
        val = self._attr.get('code')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.code -> get attr')

    def set_code(self, val):
        self._attr['code'] = val

    def get_declare(self):
        val = self._attr.get('declare')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.declare -> get attr')

    def set_declare(self, val):
        self._attr['declare'] = val

    def get_hspace(self):
        val = self._attr.get('hspace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.hspace -> get attr')

    def set_hspace(self, val):
        self._attr['hspace'] = val

    def get_standby(self):
        val = self._attr.get('standby')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.standby -> get attr')

    def set_standby(self, val):
        self._attr['standby'] = val

    def get_vspace(self):
        val = self._attr.get('vspace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.vspace -> get attr')

    def set_vspace(self, val):
        self._attr['vspace'] = val

    def get_codeBase(self):
        val = self._attr.get('codeBase')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.codeBase -> get attr')

    def set_codeBase(self, val):
        self._attr['codeBase'] = val

    def get_codeType(self):
        val = self._attr.get('codeType')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.codeType -> get attr')

    def set_codeType(self, val):
        self._attr['codeType'] = val

    def get_border(self):
        val = self._attr.get('border')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.border -> get attr')

    def set_border(self, val):
        self._attr['border'] = val

    def fn_checkValidity(self, *args):
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.checkValidity{tuple(args)} -> method')

    def fn_getSVGDocument(self, *args):
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.getSVGDocument{tuple(args)} -> method')

    def fn_reportValidity(self, *args):
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.reportValidity{tuple(args)} -> method')

    def fn_setCustomValidity(self, *args):
        logger.debug(f'patch -> v8_html_object_element.py -> HTMLObjectElement.setCustomValidity{tuple(args)} -> method')
