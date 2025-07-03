from .flags import *
from .v8_animation_timeline import AnimationTimeline


@construct_110001
class DocumentTimeline(AnimationTimeline):
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        super(DocumentTimeline, self).__init__(*args, **kw)
