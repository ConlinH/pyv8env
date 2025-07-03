from .flags import *
from .v8_performance_entry import PerformanceEntry


@construct_100001
class VisibilityStateEntry(PerformanceEntry):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(VisibilityStateEntry, self).__init__(*args, **kw)
