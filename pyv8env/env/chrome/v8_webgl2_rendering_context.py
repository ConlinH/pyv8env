from .flags import *


@construct_100001
class WebGL2RenderingContext:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)
    DEPTH_BUFFER_BIT = 256
    STENCIL_BUFFER_BIT = 1024
    COLOR_BUFFER_BIT = 16384
    POINTS = 0
    LINES = 1
    LINE_LOOP = 2
    LINE_STRIP = 3
    TRIANGLES = 4
    TRIANGLE_STRIP = 5
    TRIANGLE_FAN = 6
    ZERO = 0
    ONE = 1
    SRC_COLOR = 768
    ONE_MINUS_SRC_COLOR = 769
    SRC_ALPHA = 770
    ONE_MINUS_SRC_ALPHA = 771
    DST_ALPHA = 772
    ONE_MINUS_DST_ALPHA = 773
    DST_COLOR = 774
    ONE_MINUS_DST_COLOR = 775
    SRC_ALPHA_SATURATE = 776
    FUNC_ADD = 32774
    BLEND_EQUATION = 32777
    BLEND_EQUATION_RGB = 32777
    BLEND_EQUATION_ALPHA = 34877
    FUNC_SUBTRACT = 32778
    FUNC_REVERSE_SUBTRACT = 32779
    BLEND_DST_RGB = 32968
    BLEND_SRC_RGB = 32969
    BLEND_DST_ALPHA = 32970
    BLEND_SRC_ALPHA = 32971
    CONSTANT_COLOR = 32769
    ONE_MINUS_CONSTANT_COLOR = 32770
    CONSTANT_ALPHA = 32771
    ONE_MINUS_CONSTANT_ALPHA = 32772
    BLEND_COLOR = 32773
    ARRAY_BUFFER = 34962
    ELEMENT_ARRAY_BUFFER = 34963
    ARRAY_BUFFER_BINDING = 34964
    ELEMENT_ARRAY_BUFFER_BINDING = 34965
    STREAM_DRAW = 35040
    STATIC_DRAW = 35044
    DYNAMIC_DRAW = 35048
    BUFFER_SIZE = 34660
    BUFFER_USAGE = 34661
    CURRENT_VERTEX_ATTRIB = 34342
    FRONT = 1028
    BACK = 1029
    FRONT_AND_BACK = 1032
    TEXTURE_2D = 3553
    CULL_FACE = 2884
    BLEND = 3042
    DITHER = 3024
    STENCIL_TEST = 2960
    DEPTH_TEST = 2929
    SCISSOR_TEST = 3089
    POLYGON_OFFSET_FILL = 32823
    SAMPLE_ALPHA_TO_COVERAGE = 32926
    SAMPLE_COVERAGE = 32928
    NO_ERROR = 0
    INVALID_ENUM = 1280
    INVALID_VALUE = 1281
    INVALID_OPERATION = 1282
    OUT_OF_MEMORY = 1285
    CW = 2304
    CCW = 2305
    LINE_WIDTH = 2849
    ALIASED_POINT_SIZE_RANGE = 33901
    ALIASED_LINE_WIDTH_RANGE = 33902
    CULL_FACE_MODE = 2885
    FRONT_FACE = 2886
    DEPTH_RANGE = 2928
    DEPTH_WRITEMASK = 2930
    DEPTH_CLEAR_VALUE = 2931
    DEPTH_FUNC = 2932
    STENCIL_CLEAR_VALUE = 2961
    STENCIL_FUNC = 2962
    STENCIL_FAIL = 2964
    STENCIL_PASS_DEPTH_FAIL = 2965
    STENCIL_PASS_DEPTH_PASS = 2966
    STENCIL_REF = 2967
    STENCIL_VALUE_MASK = 2963
    STENCIL_WRITEMASK = 2968
    STENCIL_BACK_FUNC = 34816
    STENCIL_BACK_FAIL = 34817
    STENCIL_BACK_PASS_DEPTH_FAIL = 34818
    STENCIL_BACK_PASS_DEPTH_PASS = 34819
    STENCIL_BACK_REF = 36003
    STENCIL_BACK_VALUE_MASK = 36004
    STENCIL_BACK_WRITEMASK = 36005
    VIEWPORT = 2978
    SCISSOR_BOX = 3088
    COLOR_CLEAR_VALUE = 3106
    COLOR_WRITEMASK = 3107
    UNPACK_ALIGNMENT = 3317
    PACK_ALIGNMENT = 3333
    MAX_TEXTURE_SIZE = 3379
    MAX_VIEWPORT_DIMS = 3386
    SUBPIXEL_BITS = 3408
    RED_BITS = 3410
    GREEN_BITS = 3411
    BLUE_BITS = 3412
    ALPHA_BITS = 3413
    DEPTH_BITS = 3414
    STENCIL_BITS = 3415
    POLYGON_OFFSET_UNITS = 10752
    POLYGON_OFFSET_FACTOR = 32824
    TEXTURE_BINDING_2D = 32873
    SAMPLE_BUFFERS = 32936
    SAMPLES = 32937
    SAMPLE_COVERAGE_VALUE = 32938
    SAMPLE_COVERAGE_INVERT = 32939
    COMPRESSED_TEXTURE_FORMATS = 34467
    DONT_CARE = 4352
    FASTEST = 4353
    NICEST = 4354
    GENERATE_MIPMAP_HINT = 33170
    BYTE = 5120
    UNSIGNED_BYTE = 5121
    SHORT = 5122
    UNSIGNED_SHORT = 5123
    INT = 5124
    UNSIGNED_INT = 5125
    FLOAT = 5126
    DEPTH_COMPONENT = 6402
    ALPHA = 6406
    RGB = 6407
    RGBA = 6408
    LUMINANCE = 6409
    LUMINANCE_ALPHA = 6410
    UNSIGNED_SHORT_4_4_4_4 = 32819
    UNSIGNED_SHORT_5_5_5_1 = 32820
    UNSIGNED_SHORT_5_6_5 = 33635
    FRAGMENT_SHADER = 35632
    VERTEX_SHADER = 35633
    MAX_VERTEX_ATTRIBS = 34921
    MAX_VERTEX_UNIFORM_VECTORS = 36347
    MAX_VARYING_VECTORS = 36348
    MAX_COMBINED_TEXTURE_IMAGE_UNITS = 35661
    MAX_VERTEX_TEXTURE_IMAGE_UNITS = 35660
    MAX_TEXTURE_IMAGE_UNITS = 34930
    MAX_FRAGMENT_UNIFORM_VECTORS = 36349
    SHADER_TYPE = 35663
    DELETE_STATUS = 35712
    LINK_STATUS = 35714
    VALIDATE_STATUS = 35715
    ATTACHED_SHADERS = 35717
    ACTIVE_UNIFORMS = 35718
    ACTIVE_ATTRIBUTES = 35721
    SHADING_LANGUAGE_VERSION = 35724
    CURRENT_PROGRAM = 35725
    NEVER = 512
    LESS = 513
    EQUAL = 514
    LEQUAL = 515
    GREATER = 516
    NOTEQUAL = 517
    GEQUAL = 518
    ALWAYS = 519
    KEEP = 7680
    REPLACE = 7681
    INCR = 7682
    DECR = 7683
    INVERT = 5386
    INCR_WRAP = 34055
    DECR_WRAP = 34056
    VENDOR = 7936
    RENDERER = 7937
    VERSION = 7938
    NEAREST = 9728
    LINEAR = 9729
    NEAREST_MIPMAP_NEAREST = 9984
    LINEAR_MIPMAP_NEAREST = 9985
    NEAREST_MIPMAP_LINEAR = 9986
    LINEAR_MIPMAP_LINEAR = 9987
    TEXTURE_MAG_FILTER = 10240
    TEXTURE_MIN_FILTER = 10241
    TEXTURE_WRAP_S = 10242
    TEXTURE_WRAP_T = 10243
    TEXTURE = 5890
    TEXTURE_CUBE_MAP = 34067
    TEXTURE_BINDING_CUBE_MAP = 34068
    TEXTURE_CUBE_MAP_POSITIVE_X = 34069
    TEXTURE_CUBE_MAP_NEGATIVE_X = 34070
    TEXTURE_CUBE_MAP_POSITIVE_Y = 34071
    TEXTURE_CUBE_MAP_NEGATIVE_Y = 34072
    TEXTURE_CUBE_MAP_POSITIVE_Z = 34073
    TEXTURE_CUBE_MAP_NEGATIVE_Z = 34074
    MAX_CUBE_MAP_TEXTURE_SIZE = 34076
    TEXTURE0 = 33984
    TEXTURE1 = 33985
    TEXTURE2 = 33986
    TEXTURE3 = 33987
    TEXTURE4 = 33988
    TEXTURE5 = 33989
    TEXTURE6 = 33990
    TEXTURE7 = 33991
    TEXTURE8 = 33992
    TEXTURE9 = 33993
    TEXTURE10 = 33994
    TEXTURE11 = 33995
    TEXTURE12 = 33996
    TEXTURE13 = 33997
    TEXTURE14 = 33998
    TEXTURE15 = 33999
    TEXTURE16 = 34000
    TEXTURE17 = 34001
    TEXTURE18 = 34002
    TEXTURE19 = 34003
    TEXTURE20 = 34004
    TEXTURE21 = 34005
    TEXTURE22 = 34006
    TEXTURE23 = 34007
    TEXTURE24 = 34008
    TEXTURE25 = 34009
    TEXTURE26 = 34010
    TEXTURE27 = 34011
    TEXTURE28 = 34012
    TEXTURE29 = 34013
    TEXTURE30 = 34014
    TEXTURE31 = 34015
    ACTIVE_TEXTURE = 34016
    REPEAT = 10497
    CLAMP_TO_EDGE = 33071
    MIRRORED_REPEAT = 33648
    FLOAT_VEC2 = 35664
    FLOAT_VEC3 = 35665
    FLOAT_VEC4 = 35666
    INT_VEC2 = 35667
    INT_VEC3 = 35668
    INT_VEC4 = 35669
    BOOL = 35670
    BOOL_VEC2 = 35671
    BOOL_VEC3 = 35672
    BOOL_VEC4 = 35673
    FLOAT_MAT2 = 35674
    FLOAT_MAT3 = 35675
    FLOAT_MAT4 = 35676
    SAMPLER_2D = 35678
    SAMPLER_CUBE = 35680
    VERTEX_ATTRIB_ARRAY_ENABLED = 34338
    VERTEX_ATTRIB_ARRAY_SIZE = 34339
    VERTEX_ATTRIB_ARRAY_STRIDE = 34340
    VERTEX_ATTRIB_ARRAY_TYPE = 34341
    VERTEX_ATTRIB_ARRAY_NORMALIZED = 34922
    VERTEX_ATTRIB_ARRAY_POINTER = 34373
    VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 34975
    IMPLEMENTATION_COLOR_READ_TYPE = 35738
    IMPLEMENTATION_COLOR_READ_FORMAT = 35739
    COMPILE_STATUS = 35713
    LOW_FLOAT = 36336
    MEDIUM_FLOAT = 36337
    HIGH_FLOAT = 36338
    LOW_INT = 36339
    MEDIUM_INT = 36340
    HIGH_INT = 36341
    FRAMEBUFFER = 36160
    RENDERBUFFER = 36161
    RGBA4 = 32854
    RGB5_A1 = 32855
    RGB565 = 36194
    DEPTH_COMPONENT16 = 33189
    STENCIL_INDEX8 = 36168
    DEPTH_STENCIL = 34041
    RENDERBUFFER_WIDTH = 36162
    RENDERBUFFER_HEIGHT = 36163
    RENDERBUFFER_INTERNAL_FORMAT = 36164
    RENDERBUFFER_RED_SIZE = 36176
    RENDERBUFFER_GREEN_SIZE = 36177
    RENDERBUFFER_BLUE_SIZE = 36178
    RENDERBUFFER_ALPHA_SIZE = 36179
    RENDERBUFFER_DEPTH_SIZE = 36180
    RENDERBUFFER_STENCIL_SIZE = 36181
    FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 36048
    FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 36049
    FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 36050
    FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 36051
    COLOR_ATTACHMENT0 = 36064
    DEPTH_ATTACHMENT = 36096
    STENCIL_ATTACHMENT = 36128
    DEPTH_STENCIL_ATTACHMENT = 33306
    NONE = 0
    FRAMEBUFFER_COMPLETE = 36053
    FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 36054
    FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 36055
    FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 36057
    FRAMEBUFFER_UNSUPPORTED = 36061
    FRAMEBUFFER_BINDING = 36006
    RENDERBUFFER_BINDING = 36007
    MAX_RENDERBUFFER_SIZE = 34024
    INVALID_FRAMEBUFFER_OPERATION = 1286
    UNPACK_FLIP_Y_WEBGL = 37440
    UNPACK_PREMULTIPLY_ALPHA_WEBGL = 37441
    CONTEXT_LOST_WEBGL = 37442
    UNPACK_COLORSPACE_CONVERSION_WEBGL = 37443
    BROWSER_DEFAULT_WEBGL = 37444
    READ_BUFFER = 3074
    UNPACK_ROW_LENGTH = 3314
    UNPACK_SKIP_ROWS = 3315
    UNPACK_SKIP_PIXELS = 3316
    PACK_ROW_LENGTH = 3330
    PACK_SKIP_ROWS = 3331
    PACK_SKIP_PIXELS = 3332
    COLOR = 6144
    DEPTH = 6145
    STENCIL = 6146
    RED = 6403
    RGB8 = 32849
    RGBA8 = 32856
    RGB10_A2 = 32857
    TEXTURE_BINDING_3D = 32874
    UNPACK_SKIP_IMAGES = 32877
    UNPACK_IMAGE_HEIGHT = 32878
    TEXTURE_3D = 32879
    TEXTURE_WRAP_R = 32882
    MAX_3D_TEXTURE_SIZE = 32883
    UNSIGNED_INT_2_10_10_10_REV = 33640
    MAX_ELEMENTS_VERTICES = 33000
    MAX_ELEMENTS_INDICES = 33001
    TEXTURE_MIN_LOD = 33082
    TEXTURE_MAX_LOD = 33083
    TEXTURE_BASE_LEVEL = 33084
    TEXTURE_MAX_LEVEL = 33085
    MIN = 32775
    MAX = 32776
    DEPTH_COMPONENT24 = 33190
    MAX_TEXTURE_LOD_BIAS = 34045
    TEXTURE_COMPARE_MODE = 34892
    TEXTURE_COMPARE_FUNC = 34893
    CURRENT_QUERY = 34917
    QUERY_RESULT = 34918
    QUERY_RESULT_AVAILABLE = 34919
    STREAM_READ = 35041
    STREAM_COPY = 35042
    STATIC_READ = 35045
    STATIC_COPY = 35046
    DYNAMIC_READ = 35049
    DYNAMIC_COPY = 35050
    MAX_DRAW_BUFFERS = 34852
    DRAW_BUFFER0 = 34853
    DRAW_BUFFER1 = 34854
    DRAW_BUFFER2 = 34855
    DRAW_BUFFER3 = 34856
    DRAW_BUFFER4 = 34857
    DRAW_BUFFER5 = 34858
    DRAW_BUFFER6 = 34859
    DRAW_BUFFER7 = 34860
    DRAW_BUFFER8 = 34861
    DRAW_BUFFER9 = 34862
    DRAW_BUFFER10 = 34863
    DRAW_BUFFER11 = 34864
    DRAW_BUFFER12 = 34865
    DRAW_BUFFER13 = 34866
    DRAW_BUFFER14 = 34867
    DRAW_BUFFER15 = 34868
    MAX_FRAGMENT_UNIFORM_COMPONENTS = 35657
    MAX_VERTEX_UNIFORM_COMPONENTS = 35658
    SAMPLER_3D = 35679
    SAMPLER_2D_SHADOW = 35682
    FRAGMENT_SHADER_DERIVATIVE_HINT = 35723
    PIXEL_PACK_BUFFER = 35051
    PIXEL_UNPACK_BUFFER = 35052
    PIXEL_PACK_BUFFER_BINDING = 35053
    PIXEL_UNPACK_BUFFER_BINDING = 35055
    FLOAT_MAT2x3 = 35685
    FLOAT_MAT2x4 = 35686
    FLOAT_MAT3x2 = 35687
    FLOAT_MAT3x4 = 35688
    FLOAT_MAT4x2 = 35689
    FLOAT_MAT4x3 = 35690
    SRGB = 35904
    SRGB8 = 35905
    SRGB8_ALPHA8 = 35907
    COMPARE_REF_TO_TEXTURE = 34894
    RGBA32F = 34836
    RGB32F = 34837
    RGBA16F = 34842
    RGB16F = 34843
    VERTEX_ATTRIB_ARRAY_INTEGER = 35069
    MAX_ARRAY_TEXTURE_LAYERS = 35071
    MIN_PROGRAM_TEXEL_OFFSET = 35076
    MAX_PROGRAM_TEXEL_OFFSET = 35077
    MAX_VARYING_COMPONENTS = 35659
    TEXTURE_2D_ARRAY = 35866
    TEXTURE_BINDING_2D_ARRAY = 35869
    R11F_G11F_B10F = 35898
    UNSIGNED_INT_10F_11F_11F_REV = 35899
    RGB9_E5 = 35901
    UNSIGNED_INT_5_9_9_9_REV = 35902
    TRANSFORM_FEEDBACK_BUFFER_MODE = 35967
    MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 35968
    TRANSFORM_FEEDBACK_VARYINGS = 35971
    TRANSFORM_FEEDBACK_BUFFER_START = 35972
    TRANSFORM_FEEDBACK_BUFFER_SIZE = 35973
    TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 35976
    RASTERIZER_DISCARD = 35977
    MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 35978
    MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 35979
    INTERLEAVED_ATTRIBS = 35980
    SEPARATE_ATTRIBS = 35981
    TRANSFORM_FEEDBACK_BUFFER = 35982
    TRANSFORM_FEEDBACK_BUFFER_BINDING = 35983
    RGBA32UI = 36208
    RGB32UI = 36209
    RGBA16UI = 36214
    RGB16UI = 36215
    RGBA8UI = 36220
    RGB8UI = 36221
    RGBA32I = 36226
    RGB32I = 36227
    RGBA16I = 36232
    RGB16I = 36233
    RGBA8I = 36238
    RGB8I = 36239
    RED_INTEGER = 36244
    RGB_INTEGER = 36248
    RGBA_INTEGER = 36249
    SAMPLER_2D_ARRAY = 36289
    SAMPLER_2D_ARRAY_SHADOW = 36292
    SAMPLER_CUBE_SHADOW = 36293
    UNSIGNED_INT_VEC2 = 36294
    UNSIGNED_INT_VEC3 = 36295
    UNSIGNED_INT_VEC4 = 36296
    INT_SAMPLER_2D = 36298
    INT_SAMPLER_3D = 36299
    INT_SAMPLER_CUBE = 36300
    INT_SAMPLER_2D_ARRAY = 36303
    UNSIGNED_INT_SAMPLER_2D = 36306
    UNSIGNED_INT_SAMPLER_3D = 36307
    UNSIGNED_INT_SAMPLER_CUBE = 36308
    UNSIGNED_INT_SAMPLER_2D_ARRAY = 36311
    DEPTH_COMPONENT32F = 36012
    DEPTH32F_STENCIL8 = 36013
    FLOAT_32_UNSIGNED_INT_24_8_REV = 36269
    FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 33296
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 33297
    FRAMEBUFFER_ATTACHMENT_RED_SIZE = 33298
    FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 33299
    FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 33300
    FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 33301
    FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 33302
    FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 33303
    FRAMEBUFFER_DEFAULT = 33304
    UNSIGNED_INT_24_8 = 34042
    DEPTH24_STENCIL8 = 35056
    UNSIGNED_NORMALIZED = 35863
    DRAW_FRAMEBUFFER_BINDING = 36006
    READ_FRAMEBUFFER = 36008
    DRAW_FRAMEBUFFER = 36009
    READ_FRAMEBUFFER_BINDING = 36010
    RENDERBUFFER_SAMPLES = 36011
    FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 36052
    MAX_COLOR_ATTACHMENTS = 36063
    COLOR_ATTACHMENT1 = 36065
    COLOR_ATTACHMENT2 = 36066
    COLOR_ATTACHMENT3 = 36067
    COLOR_ATTACHMENT4 = 36068
    COLOR_ATTACHMENT5 = 36069
    COLOR_ATTACHMENT6 = 36070
    COLOR_ATTACHMENT7 = 36071
    COLOR_ATTACHMENT8 = 36072
    COLOR_ATTACHMENT9 = 36073
    COLOR_ATTACHMENT10 = 36074
    COLOR_ATTACHMENT11 = 36075
    COLOR_ATTACHMENT12 = 36076
    COLOR_ATTACHMENT13 = 36077
    COLOR_ATTACHMENT14 = 36078
    COLOR_ATTACHMENT15 = 36079
    FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 36182
    MAX_SAMPLES = 36183
    HALF_FLOAT = 5131
    RG = 33319
    RG_INTEGER = 33320
    R8 = 33321
    RG8 = 33323
    R16F = 33325
    R32F = 33326
    RG16F = 33327
    RG32F = 33328
    R8I = 33329
    R8UI = 33330
    R16I = 33331
    R16UI = 33332
    R32I = 33333
    R32UI = 33334
    RG8I = 33335
    RG8UI = 33336
    RG16I = 33337
    RG16UI = 33338
    RG32I = 33339
    RG32UI = 33340
    VERTEX_ARRAY_BINDING = 34229
    R8_SNORM = 36756
    RG8_SNORM = 36757
    RGB8_SNORM = 36758
    RGBA8_SNORM = 36759
    SIGNED_NORMALIZED = 36764
    COPY_READ_BUFFER = 36662
    COPY_WRITE_BUFFER = 36663
    COPY_READ_BUFFER_BINDING = 36662
    COPY_WRITE_BUFFER_BINDING = 36663
    UNIFORM_BUFFER = 35345
    UNIFORM_BUFFER_BINDING = 35368
    UNIFORM_BUFFER_START = 35369
    UNIFORM_BUFFER_SIZE = 35370
    MAX_VERTEX_UNIFORM_BLOCKS = 35371
    MAX_FRAGMENT_UNIFORM_BLOCKS = 35373
    MAX_COMBINED_UNIFORM_BLOCKS = 35374
    MAX_UNIFORM_BUFFER_BINDINGS = 35375
    MAX_UNIFORM_BLOCK_SIZE = 35376
    MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 35377
    MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 35379
    UNIFORM_BUFFER_OFFSET_ALIGNMENT = 35380
    ACTIVE_UNIFORM_BLOCKS = 35382
    UNIFORM_TYPE = 35383
    UNIFORM_SIZE = 35384
    UNIFORM_BLOCK_INDEX = 35386
    UNIFORM_OFFSET = 35387
    UNIFORM_ARRAY_STRIDE = 35388
    UNIFORM_MATRIX_STRIDE = 35389
    UNIFORM_IS_ROW_MAJOR = 35390
    UNIFORM_BLOCK_BINDING = 35391
    UNIFORM_BLOCK_DATA_SIZE = 35392
    UNIFORM_BLOCK_ACTIVE_UNIFORMS = 35394
    UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 35395
    UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 35396
    UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 35398
    INVALID_INDEX = 4294967295
    MAX_VERTEX_OUTPUT_COMPONENTS = 37154
    MAX_FRAGMENT_INPUT_COMPONENTS = 37157
    MAX_SERVER_WAIT_TIMEOUT = 37137
    OBJECT_TYPE = 37138
    SYNC_CONDITION = 37139
    SYNC_STATUS = 37140
    SYNC_FLAGS = 37141
    SYNC_FENCE = 37142
    SYNC_GPU_COMMANDS_COMPLETE = 37143
    UNSIGNALED = 37144
    SIGNALED = 37145
    ALREADY_SIGNALED = 37146
    TIMEOUT_EXPIRED = 37147
    CONDITION_SATISFIED = 37148
    WAIT_FAILED = 37149
    SYNC_FLUSH_COMMANDS_BIT = 1
    VERTEX_ATTRIB_ARRAY_DIVISOR = 35070
    ANY_SAMPLES_PASSED = 35887
    ANY_SAMPLES_PASSED_CONSERVATIVE = 36202
    SAMPLER_BINDING = 35097
    RGB10_A2UI = 36975
    INT_2_10_10_10_REV = 36255
    TRANSFORM_FEEDBACK = 36386
    TRANSFORM_FEEDBACK_PAUSED = 36387
    TRANSFORM_FEEDBACK_ACTIVE = 36388
    TRANSFORM_FEEDBACK_BINDING = 36389
    TEXTURE_IMMUTABLE_FORMAT = 37167
    MAX_ELEMENT_INDEX = 36203
    TEXTURE_IMMUTABLE_LEVELS = 33503
    TIMEOUT_IGNORED = -1
    MAX_CLIENT_WAIT_TIMEOUT_WEBGL = 37447

    __v8_attribute__ = (
        # (attr_name, get_cb, set_cb, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # FlagCrossOriginCheck, FlagCrossOriginCheck, SideEffectType)
        ("canvas", "get_canvas", None, 0, 1, 0, 0, 0, 0, 1),
        ("drawingBufferWidth", "get_drawingBufferWidth", None, 0, 1, 0, 0, 0, 0, 1),
        ("drawingBufferHeight", "get_drawingBufferHeight", None, 0, 1, 0, 0, 0, 0, 1),
        ("drawingBufferColorSpace", "get_drawingBufferColorSpace", "set_drawingBufferColorSpace", 0, 1, 0, 0, 0, 0, 1),
        ("unpackColorSpace", "get_unpackColorSpace", "set_unpackColorSpace", 0, 1, 0, 0, 0, 0, 1),
        ("drawingBufferFormat", "get_drawingBufferFormat", None, 0, 1, 0, 0, 0, 0, 1),

    )

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("activeTexture", "fn_activeTexture", 1, 0, 1, 0, 0, 0, 0),
        ("attachShader", "fn_attachShader", 2, 0, 1, 0, 0, 0, 0),
        ("beginQuery", "fn_beginQuery", 2, 0, 1, 0, 0, 0, 0),
        ("beginTransformFeedback", "fn_beginTransformFeedback", 1, 0, 1, 0, 0, 0, 0),
        ("bindAttribLocation", "fn_bindAttribLocation", 3, 0, 1, 0, 0, 0, 0),
        ("bindBufferBase", "fn_bindBufferBase", 3, 0, 1, 0, 0, 0, 0),
        ("bindBufferRange", "fn_bindBufferRange", 5, 0, 1, 0, 0, 0, 0),
        ("bindRenderbuffer", "fn_bindRenderbuffer", 2, 0, 1, 0, 0, 0, 0),
        ("bindSampler", "fn_bindSampler", 2, 0, 1, 0, 0, 0, 0),
        ("bindTransformFeedback", "fn_bindTransformFeedback", 2, 0, 1, 0, 0, 0, 0),
        ("bindVertexArray", "fn_bindVertexArray", 1, 0, 1, 0, 0, 0, 0),
        ("blendColor", "fn_blendColor", 4, 0, 1, 0, 0, 0, 0),
        ("blendEquation", "fn_blendEquation", 1, 0, 1, 0, 0, 0, 0),
        ("blendEquationSeparate", "fn_blendEquationSeparate", 2, 0, 1, 0, 0, 0, 0),
        ("blendFunc", "fn_blendFunc", 2, 0, 1, 0, 0, 0, 0),
        ("blendFuncSeparate", "fn_blendFuncSeparate", 4, 0, 1, 0, 0, 0, 0),
        ("blitFramebuffer", "fn_blitFramebuffer", 10, 0, 1, 0, 0, 0, 0),
        ("bufferData", "fn_bufferData", 3, 0, 1, 0, 0, 0, 0),
        ("bufferSubData", "fn_bufferSubData", 3, 0, 1, 0, 0, 0, 0),
        ("checkFramebufferStatus", "fn_checkFramebufferStatus", 1, 0, 1, 0, 0, 0, 0),
        ("clientWaitSync", "fn_clientWaitSync", 3, 0, 1, 0, 0, 0, 0),
        ("compileShader", "fn_compileShader", 1, 0, 1, 0, 0, 0, 0),
        ("compressedTexImage2D", "fn_compressedTexImage2D", 7, 0, 1, 0, 0, 0, 0),
        ("compressedTexImage3D", "fn_compressedTexImage3D", 8, 0, 1, 0, 0, 0, 0),
        ("compressedTexSubImage2D", "fn_compressedTexSubImage2D", 8, 0, 1, 0, 0, 0, 0),
        ("compressedTexSubImage3D", "fn_compressedTexSubImage3D", 10, 0, 1, 0, 0, 0, 0),
        ("copyBufferSubData", "fn_copyBufferSubData", 5, 0, 1, 0, 0, 0, 0),
        ("copyTexImage2D", "fn_copyTexImage2D", 8, 0, 1, 0, 0, 0, 0),
        ("copyTexSubImage2D", "fn_copyTexSubImage2D", 8, 0, 1, 0, 0, 0, 0),
        ("copyTexSubImage3D", "fn_copyTexSubImage3D", 9, 0, 1, 0, 0, 0, 0),
        ("createBuffer", "fn_createBuffer", 0, 0, 1, 0, 0, 0, 0),
        ("createFramebuffer", "fn_createFramebuffer", 0, 0, 1, 0, 0, 0, 0),
        ("createProgram", "fn_createProgram", 0, 0, 1, 0, 0, 0, 0),
        ("createQuery", "fn_createQuery", 0, 0, 1, 0, 0, 0, 0),
        ("createRenderbuffer", "fn_createRenderbuffer", 0, 0, 1, 0, 0, 0, 0),
        ("createSampler", "fn_createSampler", 0, 0, 1, 0, 0, 0, 0),
        ("createShader", "fn_createShader", 1, 0, 1, 0, 0, 0, 0),
        ("createTexture", "fn_createTexture", 0, 0, 1, 0, 0, 0, 0),
        ("createTransformFeedback", "fn_createTransformFeedback", 0, 0, 1, 0, 0, 0, 0),
        ("createVertexArray", "fn_createVertexArray", 0, 0, 1, 0, 0, 0, 0),
        ("cullFace", "fn_cullFace", 1, 0, 1, 0, 0, 0, 0),
        ("deleteBuffer", "fn_deleteBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("deleteFramebuffer", "fn_deleteFramebuffer", 1, 0, 1, 0, 0, 0, 0),
        ("deleteProgram", "fn_deleteProgram", 1, 0, 1, 0, 0, 0, 0),
        ("deleteQuery", "fn_deleteQuery", 1, 0, 1, 0, 0, 0, 0),
        ("deleteRenderbuffer", "fn_deleteRenderbuffer", 1, 0, 1, 0, 0, 0, 0),
        ("deleteSampler", "fn_deleteSampler", 1, 0, 1, 0, 0, 0, 0),
        ("deleteShader", "fn_deleteShader", 1, 0, 1, 0, 0, 0, 0),
        ("deleteSync", "fn_deleteSync", 1, 0, 1, 0, 0, 0, 0),
        ("deleteTexture", "fn_deleteTexture", 1, 0, 1, 0, 0, 0, 0),
        ("deleteTransformFeedback", "fn_deleteTransformFeedback", 1, 0, 1, 0, 0, 0, 0),
        ("deleteVertexArray", "fn_deleteVertexArray", 1, 0, 1, 0, 0, 0, 0),
        ("depthFunc", "fn_depthFunc", 1, 0, 1, 0, 0, 0, 0),
        ("depthMask", "fn_depthMask", 1, 0, 1, 0, 0, 0, 0),
        ("depthRange", "fn_depthRange", 2, 0, 1, 0, 0, 0, 0),
        ("detachShader", "fn_detachShader", 2, 0, 1, 0, 0, 0, 0),
        ("disable", "fn_disable", 1, 0, 1, 0, 0, 0, 0),
        ("drawArraysInstanced", "fn_drawArraysInstanced", 4, 0, 1, 0, 0, 0, 0),
        ("drawElementsInstanced", "fn_drawElementsInstanced", 5, 0, 1, 0, 0, 0, 0),
        ("drawRangeElements", "fn_drawRangeElements", 6, 0, 1, 0, 0, 0, 0),
        ("enable", "fn_enable", 1, 0, 1, 0, 0, 0, 0),
        ("endQuery", "fn_endQuery", 1, 0, 1, 0, 0, 0, 0),
        ("endTransformFeedback", "fn_endTransformFeedback", 0, 0, 1, 0, 0, 0, 0),
        ("fenceSync", "fn_fenceSync", 2, 0, 1, 0, 0, 0, 0),
        ("finish", "fn_finish", 0, 0, 1, 0, 0, 0, 0),
        ("flush", "fn_flush", 0, 0, 1, 0, 0, 0, 0),
        ("framebufferRenderbuffer", "fn_framebufferRenderbuffer", 4, 0, 1, 0, 0, 0, 0),
        ("framebufferTexture2D", "fn_framebufferTexture2D", 5, 0, 1, 0, 0, 0, 0),
        ("framebufferTextureLayer", "fn_framebufferTextureLayer", 5, 0, 1, 0, 0, 0, 0),
        ("frontFace", "fn_frontFace", 1, 0, 1, 0, 0, 0, 0),
        ("generateMipmap", "fn_generateMipmap", 1, 0, 1, 0, 0, 0, 0),
        ("getActiveAttrib", "fn_getActiveAttrib", 2, 0, 1, 0, 0, 0, 0),
        ("getActiveUniform", "fn_getActiveUniform", 2, 0, 1, 0, 0, 0, 0),
        ("getActiveUniformBlockName", "fn_getActiveUniformBlockName", 2, 0, 1, 0, 0, 0, 0),
        ("getActiveUniformBlockParameter", "fn_getActiveUniformBlockParameter", 3, 0, 1, 0, 0, 0, 0),
        ("getActiveUniforms", "fn_getActiveUniforms", 3, 0, 1, 0, 0, 0, 0),
        ("getAttachedShaders", "fn_getAttachedShaders", 1, 0, 1, 0, 0, 0, 0),
        ("getAttribLocation", "fn_getAttribLocation", 2, 0, 1, 0, 0, 0, 0),
        ("getBufferParameter", "fn_getBufferParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getBufferSubData", "fn_getBufferSubData", 3, 0, 1, 0, 0, 0, 0),
        ("getContextAttributes", "fn_getContextAttributes", 0, 0, 1, 0, 0, 0, 0),
        ("getError", "fn_getError", 0, 0, 1, 0, 0, 0, 0),
        ("getExtension", "fn_getExtension", 1, 0, 1, 0, 0, 0, 0),
        ("getFragDataLocation", "fn_getFragDataLocation", 2, 0, 1, 0, 0, 0, 0),
        ("getFramebufferAttachmentParameter", "fn_getFramebufferAttachmentParameter", 3, 0, 1, 0, 0, 0, 0),
        ("getIndexedParameter", "fn_getIndexedParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getInternalformatParameter", "fn_getInternalformatParameter", 3, 0, 1, 0, 0, 0, 0),
        ("getParameter", "fn_getParameter", 1, 0, 1, 0, 0, 0, 0),
        ("getProgramInfoLog", "fn_getProgramInfoLog", 1, 0, 1, 0, 0, 0, 0),
        ("getProgramParameter", "fn_getProgramParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getQuery", "fn_getQuery", 2, 0, 1, 0, 0, 0, 0),
        ("getQueryParameter", "fn_getQueryParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getRenderbufferParameter", "fn_getRenderbufferParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getSamplerParameter", "fn_getSamplerParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getShaderInfoLog", "fn_getShaderInfoLog", 1, 0, 1, 0, 0, 0, 0),
        ("getShaderParameter", "fn_getShaderParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getShaderPrecisionFormat", "fn_getShaderPrecisionFormat", 2, 0, 1, 0, 0, 0, 0),
        ("getShaderSource", "fn_getShaderSource", 1, 0, 1, 0, 0, 0, 0),
        ("getSupportedExtensions", "fn_getSupportedExtensions", 0, 0, 1, 0, 0, 0, 0),
        ("getSyncParameter", "fn_getSyncParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getTexParameter", "fn_getTexParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getTransformFeedbackVarying", "fn_getTransformFeedbackVarying", 2, 0, 1, 0, 0, 0, 0),
        ("getUniform", "fn_getUniform", 2, 0, 1, 0, 0, 0, 0),
        ("getUniformBlockIndex", "fn_getUniformBlockIndex", 2, 0, 1, 0, 0, 0, 0),
        ("getUniformIndices", "fn_getUniformIndices", 2, 0, 1, 0, 0, 0, 0),
        ("getUniformLocation", "fn_getUniformLocation", 2, 0, 1, 0, 0, 0, 0),
        ("getVertexAttrib", "fn_getVertexAttrib", 2, 0, 1, 0, 0, 0, 0),
        ("getVertexAttribOffset", "fn_getVertexAttribOffset", 2, 0, 1, 0, 0, 0, 0),
        ("hint", "fn_hint", 2, 0, 1, 0, 0, 0, 0),
        ("invalidateFramebuffer", "fn_invalidateFramebuffer", 2, 0, 1, 0, 0, 0, 0),
        ("invalidateSubFramebuffer", "fn_invalidateSubFramebuffer", 6, 0, 1, 0, 0, 0, 0),
        ("isBuffer", "fn_isBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("isContextLost", "fn_isContextLost", 0, 0, 1, 0, 0, 0, 0),
        ("isEnabled", "fn_isEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("isFramebuffer", "fn_isFramebuffer", 1, 0, 1, 0, 0, 0, 0),
        ("isProgram", "fn_isProgram", 1, 0, 1, 0, 0, 0, 0),
        ("isQuery", "fn_isQuery", 1, 0, 1, 0, 0, 0, 0),
        ("isRenderbuffer", "fn_isRenderbuffer", 1, 0, 1, 0, 0, 0, 0),
        ("isSampler", "fn_isSampler", 1, 0, 1, 0, 0, 0, 0),
        ("isShader", "fn_isShader", 1, 0, 1, 0, 0, 0, 0),
        ("isSync", "fn_isSync", 1, 0, 1, 0, 0, 0, 0),
        ("isTexture", "fn_isTexture", 1, 0, 1, 0, 0, 0, 0),
        ("isTransformFeedback", "fn_isTransformFeedback", 1, 0, 1, 0, 0, 0, 0),
        ("isVertexArray", "fn_isVertexArray", 1, 0, 1, 0, 0, 0, 0),
        ("lineWidth", "fn_lineWidth", 1, 0, 1, 0, 0, 0, 0),
        ("linkProgram", "fn_linkProgram", 1, 0, 1, 0, 0, 0, 0),
        ("pauseTransformFeedback", "fn_pauseTransformFeedback", 0, 0, 1, 0, 0, 0, 0),
        ("pixelStorei", "fn_pixelStorei", 2, 0, 1, 0, 0, 0, 0),
        ("polygonOffset", "fn_polygonOffset", 2, 0, 1, 0, 0, 0, 0),
        ("readBuffer", "fn_readBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("readPixels", "fn_readPixels", 7, 0, 1, 0, 0, 0, 0),
        ("renderbufferStorage", "fn_renderbufferStorage", 4, 0, 1, 0, 0, 0, 0),
        ("renderbufferStorageMultisample", "fn_renderbufferStorageMultisample", 5, 0, 1, 0, 0, 0, 0),
        ("resumeTransformFeedback", "fn_resumeTransformFeedback", 0, 0, 1, 0, 0, 0, 0),
        ("sampleCoverage", "fn_sampleCoverage", 2, 0, 1, 0, 0, 0, 0),
        ("samplerParameterf", "fn_samplerParameterf", 3, 0, 1, 0, 0, 0, 0),
        ("samplerParameteri", "fn_samplerParameteri", 3, 0, 1, 0, 0, 0, 0),
        ("shaderSource", "fn_shaderSource", 2, 0, 1, 0, 0, 0, 0),
        ("stencilFunc", "fn_stencilFunc", 3, 0, 1, 0, 0, 0, 0),
        ("stencilFuncSeparate", "fn_stencilFuncSeparate", 4, 0, 1, 0, 0, 0, 0),
        ("stencilMask", "fn_stencilMask", 1, 0, 1, 0, 0, 0, 0),
        ("stencilMaskSeparate", "fn_stencilMaskSeparate", 2, 0, 1, 0, 0, 0, 0),
        ("stencilOp", "fn_stencilOp", 3, 0, 1, 0, 0, 0, 0),
        ("stencilOpSeparate", "fn_stencilOpSeparate", 4, 0, 1, 0, 0, 0, 0),
        ("texImage2D", "fn_texImage2D", 6, 0, 1, 0, 0, 0, 0),
        ("texImage3D", "fn_texImage3D", 10, 0, 1, 0, 0, 0, 0),
        ("texParameterf", "fn_texParameterf", 3, 0, 1, 0, 0, 0, 0),
        ("texParameteri", "fn_texParameteri", 3, 0, 1, 0, 0, 0, 0),
        ("texStorage2D", "fn_texStorage2D", 5, 0, 1, 0, 0, 0, 0),
        ("texStorage3D", "fn_texStorage3D", 6, 0, 1, 0, 0, 0, 0),
        ("texSubImage2D", "fn_texSubImage2D", 7, 0, 1, 0, 0, 0, 0),
        ("texSubImage3D", "fn_texSubImage3D", 11, 0, 1, 0, 0, 0, 0),
        ("transformFeedbackVaryings", "fn_transformFeedbackVaryings", 3, 0, 1, 0, 0, 0, 0),
        ("uniform1ui", "fn_uniform1ui", 2, 0, 1, 0, 0, 0, 0),
        ("uniform2ui", "fn_uniform2ui", 3, 0, 1, 0, 0, 0, 0),
        ("uniform3ui", "fn_uniform3ui", 4, 0, 1, 0, 0, 0, 0),
        ("uniform4ui", "fn_uniform4ui", 5, 0, 1, 0, 0, 0, 0),
        ("uniformBlockBinding", "fn_uniformBlockBinding", 3, 0, 1, 0, 0, 0, 0),
        ("useProgram", "fn_useProgram", 1, 0, 1, 0, 0, 0, 0),
        ("validateProgram", "fn_validateProgram", 1, 0, 1, 0, 0, 0, 0),
        ("vertexAttribDivisor", "fn_vertexAttribDivisor", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttribI4i", "fn_vertexAttribI4i", 5, 0, 1, 0, 0, 0, 0),
        ("vertexAttribI4ui", "fn_vertexAttribI4ui", 5, 0, 1, 0, 0, 0, 0),
        ("vertexAttribIPointer", "fn_vertexAttribIPointer", 5, 0, 1, 0, 0, 0, 0),
        ("waitSync", "fn_waitSync", 3, 0, 1, 0, 0, 0, 0),
        ("commit", "fn_commit", 0, 0, 1, 0, 0, 0, 0),
        ("drawingBufferStorage", "fn_drawingBufferStorage", 3, 0, 1, 0, 0, 0, 0),
        ("makeXRCompatible", "fn_makeXRCompatible", 0, 0, 1, 0, 1, 0, 0),
        ("bindBuffer", "fn_bindBuffer", 2, 0, 1, 0, 0, 0, 0),
        ("bindFramebuffer", "fn_bindFramebuffer", 2, 0, 1, 0, 0, 0, 0),
        ("bindTexture", "fn_bindTexture", 2, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 1, 0, 1, 0, 0, 0, 0),
        ("clearBufferfi", "fn_clearBufferfi", 4, 0, 1, 0, 0, 0, 0),
        ("clearBufferfv", "fn_clearBufferfv", 3, 0, 1, 0, 0, 0, 0),
        ("clearBufferiv", "fn_clearBufferiv", 3, 0, 1, 0, 0, 0, 0),
        ("clearBufferuiv", "fn_clearBufferuiv", 3, 0, 1, 0, 0, 0, 0),
        ("clearColor", "fn_clearColor", 4, 0, 1, 0, 0, 0, 0),
        ("clearDepth", "fn_clearDepth", 1, 0, 1, 0, 0, 0, 0),
        ("clearStencil", "fn_clearStencil", 1, 0, 1, 0, 0, 0, 0),
        ("colorMask", "fn_colorMask", 4, 0, 1, 0, 0, 0, 0),
        ("disableVertexAttribArray", "fn_disableVertexAttribArray", 1, 0, 1, 0, 0, 0, 0),
        ("drawArrays", "fn_drawArrays", 3, 0, 1, 0, 0, 0, 0),
        ("drawBuffers", "fn_drawBuffers", 1, 0, 1, 0, 0, 0, 0),
        ("drawElements", "fn_drawElements", 4, 0, 1, 0, 0, 0, 0),
        ("enableVertexAttribArray", "fn_enableVertexAttribArray", 1, 0, 1, 0, 0, 0, 0),
        ("scissor", "fn_scissor", 4, 0, 1, 0, 0, 0, 0),
        ("uniform1f", "fn_uniform1f", 2, 0, 1, 0, 0, 0, 0),
        ("uniform1fv", "fn_uniform1fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform1i", "fn_uniform1i", 2, 0, 1, 0, 0, 0, 0),
        ("uniform1iv", "fn_uniform1iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform1uiv", "fn_uniform1uiv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform2f", "fn_uniform2f", 3, 0, 1, 0, 0, 0, 0),
        ("uniform2fv", "fn_uniform2fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform2i", "fn_uniform2i", 3, 0, 1, 0, 0, 0, 0),
        ("uniform2iv", "fn_uniform2iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform2uiv", "fn_uniform2uiv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform3f", "fn_uniform3f", 4, 0, 1, 0, 0, 0, 0),
        ("uniform3fv", "fn_uniform3fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform3i", "fn_uniform3i", 4, 0, 1, 0, 0, 0, 0),
        ("uniform3iv", "fn_uniform3iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform3uiv", "fn_uniform3uiv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform4f", "fn_uniform4f", 5, 0, 1, 0, 0, 0, 0),
        ("uniform4fv", "fn_uniform4fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform4i", "fn_uniform4i", 5, 0, 1, 0, 0, 0, 0),
        ("uniform4iv", "fn_uniform4iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform4uiv", "fn_uniform4uiv", 2, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix2fv", "fn_uniformMatrix2fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix2x3fv", "fn_uniformMatrix2x3fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix2x4fv", "fn_uniformMatrix2x4fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix3fv", "fn_uniformMatrix3fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix3x2fv", "fn_uniformMatrix3x2fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix3x4fv", "fn_uniformMatrix3x4fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix4fv", "fn_uniformMatrix4fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix4x2fv", "fn_uniformMatrix4x2fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix4x3fv", "fn_uniformMatrix4x3fv", 3, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib1f", "fn_vertexAttrib1f", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib1fv", "fn_vertexAttrib1fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib2f", "fn_vertexAttrib2f", 3, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib2fv", "fn_vertexAttrib2fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib3f", "fn_vertexAttrib3f", 4, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib3fv", "fn_vertexAttrib3fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib4f", "fn_vertexAttrib4f", 5, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib4fv", "fn_vertexAttrib4fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttribI4iv", "fn_vertexAttribI4iv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttribI4uiv", "fn_vertexAttribI4uiv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttribPointer", "fn_vertexAttribPointer", 6, 0, 1, 0, 0, 0, 0),
        ("viewport", "fn_viewport", 4, 0, 1, 0, 0, 0, 0),

    )

    def get_canvas(self):
        val = self._attr.get('canvas')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.canvas -> get attr')

    def get_drawingBufferWidth(self):
        val = self._attr.get('drawingBufferWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawingBufferWidth -> get attr')

    def get_drawingBufferHeight(self):
        val = self._attr.get('drawingBufferHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawingBufferHeight -> get attr')

    def get_drawingBufferColorSpace(self):
        val = self._attr.get('drawingBufferColorSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawingBufferColorSpace -> get attr')

    def set_drawingBufferColorSpace(self, val):
        self._attr['drawingBufferColorSpace'] = val

    def get_unpackColorSpace(self):
        val = self._attr.get('unpackColorSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.unpackColorSpace -> get attr')

    def set_unpackColorSpace(self, val):
        self._attr['unpackColorSpace'] = val

    def get_drawingBufferFormat(self):
        val = self._attr.get('drawingBufferFormat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawingBufferFormat -> get attr')

    def fn_activeTexture(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.activeTexture{tuple(args)} -> method')

    def fn_attachShader(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.attachShader{tuple(args)} -> method')

    def fn_beginQuery(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.beginQuery{tuple(args)} -> method')

    def fn_beginTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.beginTransformFeedback{tuple(args)} -> method')

    def fn_bindAttribLocation(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindAttribLocation{tuple(args)} -> method')

    def fn_bindBufferBase(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindBufferBase{tuple(args)} -> method')

    def fn_bindBufferRange(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindBufferRange{tuple(args)} -> method')

    def fn_bindRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindRenderbuffer{tuple(args)} -> method')

    def fn_bindSampler(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindSampler{tuple(args)} -> method')

    def fn_bindTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindTransformFeedback{tuple(args)} -> method')

    def fn_bindVertexArray(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindVertexArray{tuple(args)} -> method')

    def fn_blendColor(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.blendColor{tuple(args)} -> method')

    def fn_blendEquation(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.blendEquation{tuple(args)} -> method')

    def fn_blendEquationSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.blendEquationSeparate{tuple(args)} -> method')

    def fn_blendFunc(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.blendFunc{tuple(args)} -> method')

    def fn_blendFuncSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.blendFuncSeparate{tuple(args)} -> method')

    def fn_blitFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.blitFramebuffer{tuple(args)} -> method')

    def fn_bufferData(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bufferData{tuple(args)} -> method')

    def fn_bufferSubData(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bufferSubData{tuple(args)} -> method')

    def fn_checkFramebufferStatus(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.checkFramebufferStatus{tuple(args)} -> method')

    def fn_clientWaitSync(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clientWaitSync{tuple(args)} -> method')

    def fn_compileShader(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.compileShader{tuple(args)} -> method')

    def fn_compressedTexImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.compressedTexImage2D{tuple(args)} -> method')

    def fn_compressedTexImage3D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.compressedTexImage3D{tuple(args)} -> method')

    def fn_compressedTexSubImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.compressedTexSubImage2D{tuple(args)} -> method')

    def fn_compressedTexSubImage3D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.compressedTexSubImage3D{tuple(args)} -> method')

    def fn_copyBufferSubData(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.copyBufferSubData{tuple(args)} -> method')

    def fn_copyTexImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.copyTexImage2D{tuple(args)} -> method')

    def fn_copyTexSubImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.copyTexSubImage2D{tuple(args)} -> method')

    def fn_copyTexSubImage3D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.copyTexSubImage3D{tuple(args)} -> method')

    def fn_createBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createBuffer{tuple(args)} -> method')

    def fn_createFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createFramebuffer{tuple(args)} -> method')

    def fn_createProgram(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createProgram{tuple(args)} -> method')

    def fn_createQuery(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createQuery{tuple(args)} -> method')

    def fn_createRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createRenderbuffer{tuple(args)} -> method')

    def fn_createSampler(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createSampler{tuple(args)} -> method')

    def fn_createShader(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createShader{tuple(args)} -> method')

    def fn_createTexture(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createTexture{tuple(args)} -> method')

    def fn_createTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createTransformFeedback{tuple(args)} -> method')

    def fn_createVertexArray(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.createVertexArray{tuple(args)} -> method')

    def fn_cullFace(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.cullFace{tuple(args)} -> method')

    def fn_deleteBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteBuffer{tuple(args)} -> method')

    def fn_deleteFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteFramebuffer{tuple(args)} -> method')

    def fn_deleteProgram(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteProgram{tuple(args)} -> method')

    def fn_deleteQuery(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteQuery{tuple(args)} -> method')

    def fn_deleteRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteRenderbuffer{tuple(args)} -> method')

    def fn_deleteSampler(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteSampler{tuple(args)} -> method')

    def fn_deleteShader(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteShader{tuple(args)} -> method')

    def fn_deleteSync(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteSync{tuple(args)} -> method')

    def fn_deleteTexture(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteTexture{tuple(args)} -> method')

    def fn_deleteTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteTransformFeedback{tuple(args)} -> method')

    def fn_deleteVertexArray(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.deleteVertexArray{tuple(args)} -> method')

    def fn_depthFunc(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.depthFunc{tuple(args)} -> method')

    def fn_depthMask(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.depthMask{tuple(args)} -> method')

    def fn_depthRange(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.depthRange{tuple(args)} -> method')

    def fn_detachShader(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.detachShader{tuple(args)} -> method')

    def fn_disable(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.disable{tuple(args)} -> method')

    def fn_drawArraysInstanced(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawArraysInstanced{tuple(args)} -> method')

    def fn_drawElementsInstanced(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawElementsInstanced{tuple(args)} -> method')

    def fn_drawRangeElements(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawRangeElements{tuple(args)} -> method')

    def fn_enable(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.enable{tuple(args)} -> method')

    def fn_endQuery(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.endQuery{tuple(args)} -> method')

    def fn_endTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.endTransformFeedback{tuple(args)} -> method')

    def fn_fenceSync(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.fenceSync{tuple(args)} -> method')

    def fn_finish(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.finish{tuple(args)} -> method')

    def fn_flush(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.flush{tuple(args)} -> method')

    def fn_framebufferRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.framebufferRenderbuffer{tuple(args)} -> method')

    def fn_framebufferTexture2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.framebufferTexture2D{tuple(args)} -> method')

    def fn_framebufferTextureLayer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.framebufferTextureLayer{tuple(args)} -> method')

    def fn_frontFace(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.frontFace{tuple(args)} -> method')

    def fn_generateMipmap(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.generateMipmap{tuple(args)} -> method')

    def fn_getActiveAttrib(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getActiveAttrib{tuple(args)} -> method')

    def fn_getActiveUniform(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getActiveUniform{tuple(args)} -> method')

    def fn_getActiveUniformBlockName(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getActiveUniformBlockName{tuple(args)} -> method')

    def fn_getActiveUniformBlockParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getActiveUniformBlockParameter{tuple(args)} -> method')

    def fn_getActiveUniforms(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getActiveUniforms{tuple(args)} -> method')

    def fn_getAttachedShaders(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getAttachedShaders{tuple(args)} -> method')

    def fn_getAttribLocation(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getAttribLocation{tuple(args)} -> method')

    def fn_getBufferParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getBufferParameter{tuple(args)} -> method')

    def fn_getBufferSubData(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getBufferSubData{tuple(args)} -> method')

    def fn_getContextAttributes(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getContextAttributes{tuple(args)} -> method')

    def fn_getError(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getError{tuple(args)} -> method')

    def fn_getExtension(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getExtension{tuple(args)} -> method')

    def fn_getFragDataLocation(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getFragDataLocation{tuple(args)} -> method')

    def fn_getFramebufferAttachmentParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getFramebufferAttachmentParameter{tuple(args)} -> method')

    def fn_getIndexedParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getIndexedParameter{tuple(args)} -> method')

    def fn_getInternalformatParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getInternalformatParameter{tuple(args)} -> method')

    def fn_getParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getParameter{tuple(args)} -> method')

    def fn_getProgramInfoLog(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getProgramInfoLog{tuple(args)} -> method')

    def fn_getProgramParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getProgramParameter{tuple(args)} -> method')

    def fn_getQuery(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getQuery{tuple(args)} -> method')

    def fn_getQueryParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getQueryParameter{tuple(args)} -> method')

    def fn_getRenderbufferParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getRenderbufferParameter{tuple(args)} -> method')

    def fn_getSamplerParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getSamplerParameter{tuple(args)} -> method')

    def fn_getShaderInfoLog(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getShaderInfoLog{tuple(args)} -> method')

    def fn_getShaderParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getShaderParameter{tuple(args)} -> method')

    def fn_getShaderPrecisionFormat(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getShaderPrecisionFormat{tuple(args)} -> method')

    def fn_getShaderSource(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getShaderSource{tuple(args)} -> method')

    def fn_getSupportedExtensions(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getSupportedExtensions{tuple(args)} -> method')

    def fn_getSyncParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getSyncParameter{tuple(args)} -> method')

    def fn_getTexParameter(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getTexParameter{tuple(args)} -> method')

    def fn_getTransformFeedbackVarying(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getTransformFeedbackVarying{tuple(args)} -> method')

    def fn_getUniform(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getUniform{tuple(args)} -> method')

    def fn_getUniformBlockIndex(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getUniformBlockIndex{tuple(args)} -> method')

    def fn_getUniformIndices(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getUniformIndices{tuple(args)} -> method')

    def fn_getUniformLocation(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getUniformLocation{tuple(args)} -> method')

    def fn_getVertexAttrib(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getVertexAttrib{tuple(args)} -> method')

    def fn_getVertexAttribOffset(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.getVertexAttribOffset{tuple(args)} -> method')

    def fn_hint(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.hint{tuple(args)} -> method')

    def fn_invalidateFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.invalidateFramebuffer{tuple(args)} -> method')

    def fn_invalidateSubFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.invalidateSubFramebuffer{tuple(args)} -> method')

    def fn_isBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isBuffer{tuple(args)} -> method')

    def fn_isContextLost(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isContextLost{tuple(args)} -> method')

    def fn_isEnabled(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isEnabled{tuple(args)} -> method')

    def fn_isFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isFramebuffer{tuple(args)} -> method')

    def fn_isProgram(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isProgram{tuple(args)} -> method')

    def fn_isQuery(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isQuery{tuple(args)} -> method')

    def fn_isRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isRenderbuffer{tuple(args)} -> method')

    def fn_isSampler(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isSampler{tuple(args)} -> method')

    def fn_isShader(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isShader{tuple(args)} -> method')

    def fn_isSync(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isSync{tuple(args)} -> method')

    def fn_isTexture(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isTexture{tuple(args)} -> method')

    def fn_isTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isTransformFeedback{tuple(args)} -> method')

    def fn_isVertexArray(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.isVertexArray{tuple(args)} -> method')

    def fn_lineWidth(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.lineWidth{tuple(args)} -> method')

    def fn_linkProgram(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.linkProgram{tuple(args)} -> method')

    def fn_pauseTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.pauseTransformFeedback{tuple(args)} -> method')

    def fn_pixelStorei(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.pixelStorei{tuple(args)} -> method')

    def fn_polygonOffset(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.polygonOffset{tuple(args)} -> method')

    def fn_readBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.readBuffer{tuple(args)} -> method')

    def fn_readPixels(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.readPixels{tuple(args)} -> method')

    def fn_renderbufferStorage(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.renderbufferStorage{tuple(args)} -> method')

    def fn_renderbufferStorageMultisample(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.renderbufferStorageMultisample{tuple(args)} -> method')

    def fn_resumeTransformFeedback(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.resumeTransformFeedback{tuple(args)} -> method')

    def fn_sampleCoverage(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.sampleCoverage{tuple(args)} -> method')

    def fn_samplerParameterf(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.samplerParameterf{tuple(args)} -> method')

    def fn_samplerParameteri(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.samplerParameteri{tuple(args)} -> method')

    def fn_shaderSource(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.shaderSource{tuple(args)} -> method')

    def fn_stencilFunc(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.stencilFunc{tuple(args)} -> method')

    def fn_stencilFuncSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.stencilFuncSeparate{tuple(args)} -> method')

    def fn_stencilMask(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.stencilMask{tuple(args)} -> method')

    def fn_stencilMaskSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.stencilMaskSeparate{tuple(args)} -> method')

    def fn_stencilOp(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.stencilOp{tuple(args)} -> method')

    def fn_stencilOpSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.stencilOpSeparate{tuple(args)} -> method')

    def fn_texImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texImage2D{tuple(args)} -> method')

    def fn_texImage3D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texImage3D{tuple(args)} -> method')

    def fn_texParameterf(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texParameterf{tuple(args)} -> method')

    def fn_texParameteri(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texParameteri{tuple(args)} -> method')

    def fn_texStorage2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texStorage2D{tuple(args)} -> method')

    def fn_texStorage3D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texStorage3D{tuple(args)} -> method')

    def fn_texSubImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texSubImage2D{tuple(args)} -> method')

    def fn_texSubImage3D(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.texSubImage3D{tuple(args)} -> method')

    def fn_transformFeedbackVaryings(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.transformFeedbackVaryings{tuple(args)} -> method')

    def fn_uniform1ui(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform1ui{tuple(args)} -> method')

    def fn_uniform2ui(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform2ui{tuple(args)} -> method')

    def fn_uniform3ui(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform3ui{tuple(args)} -> method')

    def fn_uniform4ui(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform4ui{tuple(args)} -> method')

    def fn_uniformBlockBinding(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformBlockBinding{tuple(args)} -> method')

    def fn_useProgram(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.useProgram{tuple(args)} -> method')

    def fn_validateProgram(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.validateProgram{tuple(args)} -> method')

    def fn_vertexAttribDivisor(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttribDivisor{tuple(args)} -> method')

    def fn_vertexAttribI4i(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttribI4i{tuple(args)} -> method')

    def fn_vertexAttribI4ui(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttribI4ui{tuple(args)} -> method')

    def fn_vertexAttribIPointer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttribIPointer{tuple(args)} -> method')

    def fn_waitSync(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.waitSync{tuple(args)} -> method')

    def fn_commit(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.commit{tuple(args)} -> method')

    def fn_drawingBufferStorage(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawingBufferStorage{tuple(args)} -> method')

    def fn_makeXRCompatible(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.makeXRCompatible{tuple(args)} -> method')

    def fn_bindBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindBuffer{tuple(args)} -> method')

    def fn_bindFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindFramebuffer{tuple(args)} -> method')

    def fn_bindTexture(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.bindTexture{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clear{tuple(args)} -> method')

    def fn_clearBufferfi(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clearBufferfi{tuple(args)} -> method')

    def fn_clearBufferfv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clearBufferfv{tuple(args)} -> method')

    def fn_clearBufferiv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clearBufferiv{tuple(args)} -> method')

    def fn_clearBufferuiv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clearBufferuiv{tuple(args)} -> method')

    def fn_clearColor(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clearColor{tuple(args)} -> method')

    def fn_clearDepth(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clearDepth{tuple(args)} -> method')

    def fn_clearStencil(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.clearStencil{tuple(args)} -> method')

    def fn_colorMask(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.colorMask{tuple(args)} -> method')

    def fn_disableVertexAttribArray(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.disableVertexAttribArray{tuple(args)} -> method')

    def fn_drawArrays(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawArrays{tuple(args)} -> method')

    def fn_drawBuffers(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawBuffers{tuple(args)} -> method')

    def fn_drawElements(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.drawElements{tuple(args)} -> method')

    def fn_enableVertexAttribArray(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.enableVertexAttribArray{tuple(args)} -> method')

    def fn_scissor(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.scissor{tuple(args)} -> method')

    def fn_uniform1f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform1f{tuple(args)} -> method')

    def fn_uniform1fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform1fv{tuple(args)} -> method')

    def fn_uniform1i(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform1i{tuple(args)} -> method')

    def fn_uniform1iv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform1iv{tuple(args)} -> method')

    def fn_uniform1uiv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform1uiv{tuple(args)} -> method')

    def fn_uniform2f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform2f{tuple(args)} -> method')

    def fn_uniform2fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform2fv{tuple(args)} -> method')

    def fn_uniform2i(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform2i{tuple(args)} -> method')

    def fn_uniform2iv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform2iv{tuple(args)} -> method')

    def fn_uniform2uiv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform2uiv{tuple(args)} -> method')

    def fn_uniform3f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform3f{tuple(args)} -> method')

    def fn_uniform3fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform3fv{tuple(args)} -> method')

    def fn_uniform3i(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform3i{tuple(args)} -> method')

    def fn_uniform3iv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform3iv{tuple(args)} -> method')

    def fn_uniform3uiv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform3uiv{tuple(args)} -> method')

    def fn_uniform4f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform4f{tuple(args)} -> method')

    def fn_uniform4fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform4fv{tuple(args)} -> method')

    def fn_uniform4i(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform4i{tuple(args)} -> method')

    def fn_uniform4iv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform4iv{tuple(args)} -> method')

    def fn_uniform4uiv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniform4uiv{tuple(args)} -> method')

    def fn_uniformMatrix2fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix2fv{tuple(args)} -> method')

    def fn_uniformMatrix2x3fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix2x3fv{tuple(args)} -> method')

    def fn_uniformMatrix2x4fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix2x4fv{tuple(args)} -> method')

    def fn_uniformMatrix3fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix3fv{tuple(args)} -> method')

    def fn_uniformMatrix3x2fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix3x2fv{tuple(args)} -> method')

    def fn_uniformMatrix3x4fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix3x4fv{tuple(args)} -> method')

    def fn_uniformMatrix4fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix4fv{tuple(args)} -> method')

    def fn_uniformMatrix4x2fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix4x2fv{tuple(args)} -> method')

    def fn_uniformMatrix4x3fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.uniformMatrix4x3fv{tuple(args)} -> method')

    def fn_vertexAttrib1f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib1f{tuple(args)} -> method')

    def fn_vertexAttrib1fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib1fv{tuple(args)} -> method')

    def fn_vertexAttrib2f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib2f{tuple(args)} -> method')

    def fn_vertexAttrib2fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib2fv{tuple(args)} -> method')

    def fn_vertexAttrib3f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib3f{tuple(args)} -> method')

    def fn_vertexAttrib3fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib3fv{tuple(args)} -> method')

    def fn_vertexAttrib4f(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib4f{tuple(args)} -> method')

    def fn_vertexAttrib4fv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttrib4fv{tuple(args)} -> method')

    def fn_vertexAttribI4iv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttribI4iv{tuple(args)} -> method')

    def fn_vertexAttribI4uiv(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttribI4uiv{tuple(args)} -> method')

    def fn_vertexAttribPointer(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.vertexAttribPointer{tuple(args)} -> method')

    def fn_viewport(self, *args):
        logger.debug(f'patch -> v8_webgl2_rendering_context.py -> WebGL2RenderingContext.viewport{tuple(args)} -> method')
