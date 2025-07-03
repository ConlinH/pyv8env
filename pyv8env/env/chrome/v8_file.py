from .flags import *
from .v8_blob import Blob


@construct_112001
class File(Blob):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(File, self).__init__(*args, **kw)

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("name", "get_name", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastModified", "get_lastModified", None, 0, 1, 0, 0, 0, 0, 1),
        ("lastModifiedDate", "get_lastModifiedDate", None, 0, 1, 0, 0, 0, 0, 1),
        ("webkitRelativePath", "get_webkitRelativePath", None, 0, 1, 0, 0, 0, 0, 1),

    )

    def get_name(self):
        val = self._attr.get('name')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file.py -> File.name -> get attr')

    def get_lastModified(self):
        val = self._attr.get('lastModified')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file.py -> File.lastModified -> get attr')

    def get_lastModifiedDate(self):
        val = self._attr.get('lastModifiedDate')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file.py -> File.lastModifiedDate -> get attr')

    def get_webkitRelativePath(self):
        val = self._attr.get('webkitRelativePath')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_file.py -> File.webkitRelativePath -> get attr')
