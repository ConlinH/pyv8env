from .flags import *


@construct_112001
class ImageData:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("width", "get_width", None, 0, 1, 0, 0, 0, 0, 1),
        ("height", "get_height", None, 0, 1, 0, 0, 0, 0, 1),
        ("colorSpace", "get_colorSpace", None, 0, 1, 0, 0, 0, 0, 1),
        ("data", "get_data", None, 0, 1, 0, 0, 0, 0, 1),
        ("storageFormat", "get_storageFormat", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_width(self):
        val = self._attr.get('width')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_data.py -> ImageData.width -> get attr')

    def get_height(self):
        val = self._attr.get('height')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_data.py -> ImageData.height -> get attr')

    def get_colorSpace(self):
        val = self._attr.get('colorSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_data.py -> ImageData.colorSpace -> get attr')

    def get_data(self):
        val = self._attr.get('data')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_data.py -> ImageData.data -> get attr')

    def get_storageFormat(self):
        val = self._attr.get('storageFormat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_image_data.py -> ImageData.storageFormat -> get attr')
