from .flags import *


@construct_100001
class WebGLRenderingContext:
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
        ("bindAttribLocation", "fn_bindAttribLocation", 3, 0, 1, 0, 0, 0, 0),
        ("bindRenderbuffer", "fn_bindRenderbuffer", 2, 0, 1, 0, 0, 0, 0),
        ("blendColor", "fn_blendColor", 4, 0, 1, 0, 0, 0, 0),
        ("blendEquation", "fn_blendEquation", 1, 0, 1, 0, 0, 0, 0),
        ("blendEquationSeparate", "fn_blendEquationSeparate", 2, 0, 1, 0, 0, 0, 0),
        ("blendFunc", "fn_blendFunc", 2, 0, 1, 0, 0, 0, 0),
        ("blendFuncSeparate", "fn_blendFuncSeparate", 4, 0, 1, 0, 0, 0, 0),
        ("bufferData", "fn_bufferData", 3, 0, 1, 0, 0, 0, 0),
        ("bufferSubData", "fn_bufferSubData", 3, 0, 1, 0, 0, 0, 0),
        ("checkFramebufferStatus", "fn_checkFramebufferStatus", 1, 0, 1, 0, 0, 0, 0),
        ("compileShader", "fn_compileShader", 1, 0, 1, 0, 0, 0, 0),
        ("compressedTexImage2D", "fn_compressedTexImage2D", 7, 0, 1, 0, 0, 0, 0),
        ("compressedTexSubImage2D", "fn_compressedTexSubImage2D", 8, 0, 1, 0, 0, 0, 0),
        ("copyTexImage2D", "fn_copyTexImage2D", 8, 0, 1, 0, 0, 0, 0),
        ("copyTexSubImage2D", "fn_copyTexSubImage2D", 8, 0, 1, 0, 0, 0, 0),
        ("createBuffer", "fn_createBuffer", 0, 0, 1, 0, 0, 0, 0),
        ("createFramebuffer", "fn_createFramebuffer", 0, 0, 1, 0, 0, 0, 0),
        ("createProgram", "fn_createProgram", 0, 0, 1, 0, 0, 0, 0),
        ("createRenderbuffer", "fn_createRenderbuffer", 0, 0, 1, 0, 0, 0, 0),
        ("createShader", "fn_createShader", 1, 0, 1, 0, 0, 0, 0),
        ("createTexture", "fn_createTexture", 0, 0, 1, 0, 0, 0, 0),
        ("cullFace", "fn_cullFace", 1, 0, 1, 0, 0, 0, 0),
        ("deleteBuffer", "fn_deleteBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("deleteFramebuffer", "fn_deleteFramebuffer", 1, 0, 1, 0, 0, 0, 0),
        ("deleteProgram", "fn_deleteProgram", 1, 0, 1, 0, 0, 0, 0),
        ("deleteRenderbuffer", "fn_deleteRenderbuffer", 1, 0, 1, 0, 0, 0, 0),
        ("deleteShader", "fn_deleteShader", 1, 0, 1, 0, 0, 0, 0),
        ("deleteTexture", "fn_deleteTexture", 1, 0, 1, 0, 0, 0, 0),
        ("depthFunc", "fn_depthFunc", 1, 0, 1, 0, 0, 0, 0),
        ("depthMask", "fn_depthMask", 1, 0, 1, 0, 0, 0, 0),
        ("depthRange", "fn_depthRange", 2, 0, 1, 0, 0, 0, 0),
        ("detachShader", "fn_detachShader", 2, 0, 1, 0, 0, 0, 0),
        ("disable", "fn_disable", 1, 0, 1, 0, 0, 0, 0),
        ("enable", "fn_enable", 1, 0, 1, 0, 0, 0, 0),
        ("finish", "fn_finish", 0, 0, 1, 0, 0, 0, 0),
        ("flush", "fn_flush", 0, 0, 1, 0, 0, 0, 0),
        ("framebufferRenderbuffer", "fn_framebufferRenderbuffer", 4, 0, 1, 0, 0, 0, 0),
        ("framebufferTexture2D", "fn_framebufferTexture2D", 5, 0, 1, 0, 0, 0, 0),
        ("frontFace", "fn_frontFace", 1, 0, 1, 0, 0, 0, 0),
        ("generateMipmap", "fn_generateMipmap", 1, 0, 1, 0, 0, 0, 0),
        ("getActiveAttrib", "fn_getActiveAttrib", 2, 0, 1, 0, 0, 0, 0),
        ("getActiveUniform", "fn_getActiveUniform", 2, 0, 1, 0, 0, 0, 0),
        ("getAttachedShaders", "fn_getAttachedShaders", 1, 0, 1, 0, 0, 0, 0),
        ("getAttribLocation", "fn_getAttribLocation", 2, 0, 1, 0, 0, 0, 0),
        ("getBufferParameter", "fn_getBufferParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getContextAttributes", "fn_getContextAttributes", 0, 0, 1, 0, 0, 0, 0),
        ("getError", "fn_getError", 0, 0, 1, 0, 0, 0, 0),
        ("getExtension", "fn_getExtension", 1, 0, 1, 0, 0, 0, 0),
        ("getFramebufferAttachmentParameter", "fn_getFramebufferAttachmentParameter", 3, 0, 1, 0, 0, 0, 0),
        ("getParameter", "fn_getParameter", 1, 0, 1, 0, 0, 0, 0),
        ("getProgramInfoLog", "fn_getProgramInfoLog", 1, 0, 1, 0, 0, 0, 0),
        ("getProgramParameter", "fn_getProgramParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getRenderbufferParameter", "fn_getRenderbufferParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getShaderInfoLog", "fn_getShaderInfoLog", 1, 0, 1, 0, 0, 0, 0),
        ("getShaderParameter", "fn_getShaderParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getShaderPrecisionFormat", "fn_getShaderPrecisionFormat", 2, 0, 1, 0, 0, 0, 0),
        ("getShaderSource", "fn_getShaderSource", 1, 0, 1, 0, 0, 0, 0),
        ("getSupportedExtensions", "fn_getSupportedExtensions", 0, 0, 1, 0, 0, 0, 0),
        ("getTexParameter", "fn_getTexParameter", 2, 0, 1, 0, 0, 0, 0),
        ("getUniform", "fn_getUniform", 2, 0, 1, 0, 0, 0, 0),
        ("getUniformLocation", "fn_getUniformLocation", 2, 0, 1, 0, 0, 0, 0),
        ("getVertexAttrib", "fn_getVertexAttrib", 2, 0, 1, 0, 0, 0, 0),
        ("getVertexAttribOffset", "fn_getVertexAttribOffset", 2, 0, 1, 0, 0, 0, 0),
        ("hint", "fn_hint", 2, 0, 1, 0, 0, 0, 0),
        ("isBuffer", "fn_isBuffer", 1, 0, 1, 0, 0, 0, 0),
        ("isContextLost", "fn_isContextLost", 0, 0, 1, 0, 0, 0, 0),
        ("isEnabled", "fn_isEnabled", 1, 0, 1, 0, 0, 0, 0),
        ("isFramebuffer", "fn_isFramebuffer", 1, 0, 1, 0, 0, 0, 0),
        ("isProgram", "fn_isProgram", 1, 0, 1, 0, 0, 0, 0),
        ("isRenderbuffer", "fn_isRenderbuffer", 1, 0, 1, 0, 0, 0, 0),
        ("isShader", "fn_isShader", 1, 0, 1, 0, 0, 0, 0),
        ("isTexture", "fn_isTexture", 1, 0, 1, 0, 0, 0, 0),
        ("lineWidth", "fn_lineWidth", 1, 0, 1, 0, 0, 0, 0),
        ("linkProgram", "fn_linkProgram", 1, 0, 1, 0, 0, 0, 0),
        ("pixelStorei", "fn_pixelStorei", 2, 0, 1, 0, 0, 0, 0),
        ("polygonOffset", "fn_polygonOffset", 2, 0, 1, 0, 0, 0, 0),
        ("readPixels", "fn_readPixels", 7, 0, 1, 0, 0, 0, 0),
        ("renderbufferStorage", "fn_renderbufferStorage", 4, 0, 1, 0, 0, 0, 0),
        ("sampleCoverage", "fn_sampleCoverage", 2, 0, 1, 0, 0, 0, 0),
        ("shaderSource", "fn_shaderSource", 2, 0, 1, 0, 0, 0, 0),
        ("stencilFunc", "fn_stencilFunc", 3, 0, 1, 0, 0, 0, 0),
        ("stencilFuncSeparate", "fn_stencilFuncSeparate", 4, 0, 1, 0, 0, 0, 0),
        ("stencilMask", "fn_stencilMask", 1, 0, 1, 0, 0, 0, 0),
        ("stencilMaskSeparate", "fn_stencilMaskSeparate", 2, 0, 1, 0, 0, 0, 0),
        ("stencilOp", "fn_stencilOp", 3, 0, 1, 0, 0, 0, 0),
        ("stencilOpSeparate", "fn_stencilOpSeparate", 4, 0, 1, 0, 0, 0, 0),
        ("texImage2D", "fn_texImage2D", 6, 0, 1, 0, 0, 0, 0),
        ("texParameterf", "fn_texParameterf", 3, 0, 1, 0, 0, 0, 0),
        ("texParameteri", "fn_texParameteri", 3, 0, 1, 0, 0, 0, 0),
        ("texSubImage2D", "fn_texSubImage2D", 7, 0, 1, 0, 0, 0, 0),
        ("useProgram", "fn_useProgram", 1, 0, 1, 0, 0, 0, 0),
        ("validateProgram", "fn_validateProgram", 1, 0, 1, 0, 0, 0, 0),
        ("commit", "fn_commit", 0, 0, 1, 0, 0, 0, 0),
        ("drawingBufferStorage", "fn_drawingBufferStorage", 3, 0, 1, 0, 0, 0, 0),
        ("makeXRCompatible", "fn_makeXRCompatible", 0, 0, 1, 0, 1, 0, 0),
        ("bindBuffer", "fn_bindBuffer", 2, 0, 1, 0, 0, 0, 0),
        ("bindFramebuffer", "fn_bindFramebuffer", 2, 0, 1, 0, 0, 0, 0),
        ("bindTexture", "fn_bindTexture", 2, 0, 1, 0, 0, 0, 0),
        ("clear", "fn_clear", 1, 0, 1, 0, 0, 0, 0),
        ("clearColor", "fn_clearColor", 4, 0, 1, 0, 0, 0, 0),
        ("clearDepth", "fn_clearDepth", 1, 0, 1, 0, 0, 0, 0),
        ("clearStencil", "fn_clearStencil", 1, 0, 1, 0, 0, 0, 0),
        ("colorMask", "fn_colorMask", 4, 0, 1, 0, 0, 0, 0),
        ("disableVertexAttribArray", "fn_disableVertexAttribArray", 1, 0, 1, 0, 0, 0, 0),
        ("drawArrays", "fn_drawArrays", 3, 0, 1, 0, 0, 0, 0),
        ("drawElements", "fn_drawElements", 4, 0, 1, 0, 0, 0, 0),
        ("enableVertexAttribArray", "fn_enableVertexAttribArray", 1, 0, 1, 0, 0, 0, 0),
        ("scissor", "fn_scissor", 4, 0, 1, 0, 0, 0, 0),
        ("uniform1f", "fn_uniform1f", 2, 0, 1, 0, 0, 0, 0),
        ("uniform1fv", "fn_uniform1fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform1i", "fn_uniform1i", 2, 0, 1, 0, 0, 0, 0),
        ("uniform1iv", "fn_uniform1iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform2f", "fn_uniform2f", 3, 0, 1, 0, 0, 0, 0),
        ("uniform2fv", "fn_uniform2fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform2i", "fn_uniform2i", 3, 0, 1, 0, 0, 0, 0),
        ("uniform2iv", "fn_uniform2iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform3f", "fn_uniform3f", 4, 0, 1, 0, 0, 0, 0),
        ("uniform3fv", "fn_uniform3fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform3i", "fn_uniform3i", 4, 0, 1, 0, 0, 0, 0),
        ("uniform3iv", "fn_uniform3iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform4f", "fn_uniform4f", 5, 0, 1, 0, 0, 0, 0),
        ("uniform4fv", "fn_uniform4fv", 2, 0, 1, 0, 0, 0, 0),
        ("uniform4i", "fn_uniform4i", 5, 0, 1, 0, 0, 0, 0),
        ("uniform4iv", "fn_uniform4iv", 2, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix2fv", "fn_uniformMatrix2fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix3fv", "fn_uniformMatrix3fv", 3, 0, 1, 0, 0, 0, 0),
        ("uniformMatrix4fv", "fn_uniformMatrix4fv", 3, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib1f", "fn_vertexAttrib1f", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib1fv", "fn_vertexAttrib1fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib2f", "fn_vertexAttrib2f", 3, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib2fv", "fn_vertexAttrib2fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib3f", "fn_vertexAttrib3f", 4, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib3fv", "fn_vertexAttrib3fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib4f", "fn_vertexAttrib4f", 5, 0, 1, 0, 0, 0, 0),
        ("vertexAttrib4fv", "fn_vertexAttrib4fv", 2, 0, 1, 0, 0, 0, 0),
        ("vertexAttribPointer", "fn_vertexAttribPointer", 6, 0, 1, 0, 0, 0, 0),
        ("viewport", "fn_viewport", 4, 0, 1, 0, 0, 0, 0),

    )

    def get_canvas(self):
        val = self._attr.get('canvas')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.canvas -> get attr')

    def get_drawingBufferWidth(self):
        val = self._attr.get('drawingBufferWidth')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.drawingBufferWidth -> get attr')

    def get_drawingBufferHeight(self):
        val = self._attr.get('drawingBufferHeight')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.drawingBufferHeight -> get attr')

    def get_drawingBufferColorSpace(self):
        val = self._attr.get('drawingBufferColorSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.drawingBufferColorSpace -> get attr')

    def set_drawingBufferColorSpace(self, val):
        self._attr['drawingBufferColorSpace'] = val

    def get_unpackColorSpace(self):
        val = self._attr.get('unpackColorSpace')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.unpackColorSpace -> get attr')

    def set_unpackColorSpace(self, val):
        self._attr['unpackColorSpace'] = val

    def get_drawingBufferFormat(self):
        val = self._attr.get('drawingBufferFormat')
        if val is not None:
            return val
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.drawingBufferFormat -> get attr')

    def fn_activeTexture(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.activeTexture{tuple(args)} -> method')

    def fn_attachShader(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.attachShader{tuple(args)} -> method')

    def fn_bindAttribLocation(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.bindAttribLocation{tuple(args)} -> method')

    def fn_bindRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.bindRenderbuffer{tuple(args)} -> method')

    def fn_blendColor(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.blendColor{tuple(args)} -> method')

    def fn_blendEquation(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.blendEquation{tuple(args)} -> method')

    def fn_blendEquationSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.blendEquationSeparate{tuple(args)} -> method')

    def fn_blendFunc(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.blendFunc{tuple(args)} -> method')

    def fn_blendFuncSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.blendFuncSeparate{tuple(args)} -> method')

    def fn_bufferData(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.bufferData{tuple(args)} -> method')

    def fn_bufferSubData(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.bufferSubData{tuple(args)} -> method')

    def fn_checkFramebufferStatus(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.checkFramebufferStatus{tuple(args)} -> method')

    def fn_compileShader(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.compileShader{tuple(args)} -> method')

    def fn_compressedTexImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.compressedTexImage2D{tuple(args)} -> method')

    def fn_compressedTexSubImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.compressedTexSubImage2D{tuple(args)} -> method')

    def fn_copyTexImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.copyTexImage2D{tuple(args)} -> method')

    def fn_copyTexSubImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.copyTexSubImage2D{tuple(args)} -> method')

    def fn_createBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.createBuffer{tuple(args)} -> method')

    def fn_createFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.createFramebuffer{tuple(args)} -> method')

    def fn_createProgram(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.createProgram{tuple(args)} -> method')

    def fn_createRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.createRenderbuffer{tuple(args)} -> method')

    def fn_createShader(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.createShader{tuple(args)} -> method')

    def fn_createTexture(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.createTexture{tuple(args)} -> method')

    def fn_cullFace(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.cullFace{tuple(args)} -> method')

    def fn_deleteBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.deleteBuffer{tuple(args)} -> method')

    def fn_deleteFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.deleteFramebuffer{tuple(args)} -> method')

    def fn_deleteProgram(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.deleteProgram{tuple(args)} -> method')

    def fn_deleteRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.deleteRenderbuffer{tuple(args)} -> method')

    def fn_deleteShader(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.deleteShader{tuple(args)} -> method')

    def fn_deleteTexture(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.deleteTexture{tuple(args)} -> method')

    def fn_depthFunc(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.depthFunc{tuple(args)} -> method')

    def fn_depthMask(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.depthMask{tuple(args)} -> method')

    def fn_depthRange(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.depthRange{tuple(args)} -> method')

    def fn_detachShader(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.detachShader{tuple(args)} -> method')

    def fn_disable(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.disable{tuple(args)} -> method')

    def fn_enable(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.enable{tuple(args)} -> method')

    def fn_finish(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.finish{tuple(args)} -> method')

    def fn_flush(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.flush{tuple(args)} -> method')

    def fn_framebufferRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.framebufferRenderbuffer{tuple(args)} -> method')

    def fn_framebufferTexture2D(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.framebufferTexture2D{tuple(args)} -> method')

    def fn_frontFace(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.frontFace{tuple(args)} -> method')

    def fn_generateMipmap(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.generateMipmap{tuple(args)} -> method')

    def fn_getActiveAttrib(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getActiveAttrib{tuple(args)} -> method')

    def fn_getActiveUniform(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getActiveUniform{tuple(args)} -> method')

    def fn_getAttachedShaders(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getAttachedShaders{tuple(args)} -> method')

    def fn_getAttribLocation(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getAttribLocation{tuple(args)} -> method')

    def fn_getBufferParameter(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getBufferParameter{tuple(args)} -> method')

    def fn_getContextAttributes(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getContextAttributes{tuple(args)} -> method')

    def fn_getError(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getError{tuple(args)} -> method')

    def fn_getExtension(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getExtension{tuple(args)} -> method')

    def fn_getFramebufferAttachmentParameter(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getFramebufferAttachmentParameter{tuple(args)} -> method')

    def fn_getParameter(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getParameter{tuple(args)} -> method')

    def fn_getProgramInfoLog(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getProgramInfoLog{tuple(args)} -> method')

    def fn_getProgramParameter(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getProgramParameter{tuple(args)} -> method')

    def fn_getRenderbufferParameter(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getRenderbufferParameter{tuple(args)} -> method')

    def fn_getShaderInfoLog(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getShaderInfoLog{tuple(args)} -> method')

    def fn_getShaderParameter(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getShaderParameter{tuple(args)} -> method')

    def fn_getShaderPrecisionFormat(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getShaderPrecisionFormat{tuple(args)} -> method')

    def fn_getShaderSource(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getShaderSource{tuple(args)} -> method')

    def fn_getSupportedExtensions(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getSupportedExtensions{tuple(args)} -> method')

    def fn_getTexParameter(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getTexParameter{tuple(args)} -> method')

    def fn_getUniform(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getUniform{tuple(args)} -> method')

    def fn_getUniformLocation(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getUniformLocation{tuple(args)} -> method')

    def fn_getVertexAttrib(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getVertexAttrib{tuple(args)} -> method')

    def fn_getVertexAttribOffset(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.getVertexAttribOffset{tuple(args)} -> method')

    def fn_hint(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.hint{tuple(args)} -> method')

    def fn_isBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isBuffer{tuple(args)} -> method')

    def fn_isContextLost(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isContextLost{tuple(args)} -> method')

    def fn_isEnabled(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isEnabled{tuple(args)} -> method')

    def fn_isFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isFramebuffer{tuple(args)} -> method')

    def fn_isProgram(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isProgram{tuple(args)} -> method')

    def fn_isRenderbuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isRenderbuffer{tuple(args)} -> method')

    def fn_isShader(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isShader{tuple(args)} -> method')

    def fn_isTexture(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.isTexture{tuple(args)} -> method')

    def fn_lineWidth(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.lineWidth{tuple(args)} -> method')

    def fn_linkProgram(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.linkProgram{tuple(args)} -> method')

    def fn_pixelStorei(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.pixelStorei{tuple(args)} -> method')

    def fn_polygonOffset(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.polygonOffset{tuple(args)} -> method')

    def fn_readPixels(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.readPixels{tuple(args)} -> method')

    def fn_renderbufferStorage(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.renderbufferStorage{tuple(args)} -> method')

    def fn_sampleCoverage(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.sampleCoverage{tuple(args)} -> method')

    def fn_shaderSource(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.shaderSource{tuple(args)} -> method')

    def fn_stencilFunc(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.stencilFunc{tuple(args)} -> method')

    def fn_stencilFuncSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.stencilFuncSeparate{tuple(args)} -> method')

    def fn_stencilMask(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.stencilMask{tuple(args)} -> method')

    def fn_stencilMaskSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.stencilMaskSeparate{tuple(args)} -> method')

    def fn_stencilOp(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.stencilOp{tuple(args)} -> method')

    def fn_stencilOpSeparate(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.stencilOpSeparate{tuple(args)} -> method')

    def fn_texImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.texImage2D{tuple(args)} -> method')

    def fn_texParameterf(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.texParameterf{tuple(args)} -> method')

    def fn_texParameteri(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.texParameteri{tuple(args)} -> method')

    def fn_texSubImage2D(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.texSubImage2D{tuple(args)} -> method')

    def fn_useProgram(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.useProgram{tuple(args)} -> method')

    def fn_validateProgram(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.validateProgram{tuple(args)} -> method')

    def fn_commit(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.commit{tuple(args)} -> method')

    def fn_drawingBufferStorage(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.drawingBufferStorage{tuple(args)} -> method')

    def fn_makeXRCompatible(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.makeXRCompatible{tuple(args)} -> method')

    def fn_bindBuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.bindBuffer{tuple(args)} -> method')

    def fn_bindFramebuffer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.bindFramebuffer{tuple(args)} -> method')

    def fn_bindTexture(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.bindTexture{tuple(args)} -> method')

    def fn_clear(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.clear{tuple(args)} -> method')

    def fn_clearColor(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.clearColor{tuple(args)} -> method')

    def fn_clearDepth(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.clearDepth{tuple(args)} -> method')

    def fn_clearStencil(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.clearStencil{tuple(args)} -> method')

    def fn_colorMask(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.colorMask{tuple(args)} -> method')

    def fn_disableVertexAttribArray(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.disableVertexAttribArray{tuple(args)} -> method')

    def fn_drawArrays(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.drawArrays{tuple(args)} -> method')

    def fn_drawElements(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.drawElements{tuple(args)} -> method')

    def fn_enableVertexAttribArray(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.enableVertexAttribArray{tuple(args)} -> method')

    def fn_scissor(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.scissor{tuple(args)} -> method')

    def fn_uniform1f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform1f{tuple(args)} -> method')

    def fn_uniform1fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform1fv{tuple(args)} -> method')

    def fn_uniform1i(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform1i{tuple(args)} -> method')

    def fn_uniform1iv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform1iv{tuple(args)} -> method')

    def fn_uniform2f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform2f{tuple(args)} -> method')

    def fn_uniform2fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform2fv{tuple(args)} -> method')

    def fn_uniform2i(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform2i{tuple(args)} -> method')

    def fn_uniform2iv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform2iv{tuple(args)} -> method')

    def fn_uniform3f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform3f{tuple(args)} -> method')

    def fn_uniform3fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform3fv{tuple(args)} -> method')

    def fn_uniform3i(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform3i{tuple(args)} -> method')

    def fn_uniform3iv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform3iv{tuple(args)} -> method')

    def fn_uniform4f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform4f{tuple(args)} -> method')

    def fn_uniform4fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform4fv{tuple(args)} -> method')

    def fn_uniform4i(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform4i{tuple(args)} -> method')

    def fn_uniform4iv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniform4iv{tuple(args)} -> method')

    def fn_uniformMatrix2fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniformMatrix2fv{tuple(args)} -> method')

    def fn_uniformMatrix3fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniformMatrix3fv{tuple(args)} -> method')

    def fn_uniformMatrix4fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.uniformMatrix4fv{tuple(args)} -> method')

    def fn_vertexAttrib1f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib1f{tuple(args)} -> method')

    def fn_vertexAttrib1fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib1fv{tuple(args)} -> method')

    def fn_vertexAttrib2f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib2f{tuple(args)} -> method')

    def fn_vertexAttrib2fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib2fv{tuple(args)} -> method')

    def fn_vertexAttrib3f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib3f{tuple(args)} -> method')

    def fn_vertexAttrib3fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib3fv{tuple(args)} -> method')

    def fn_vertexAttrib4f(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib4f{tuple(args)} -> method')

    def fn_vertexAttrib4fv(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttrib4fv{tuple(args)} -> method')

    def fn_vertexAttribPointer(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.vertexAttribPointer{tuple(args)} -> method')

    def fn_viewport(self, *args):
        logger.debug(f'patch -> v8_webgl_rendering_context.py -> WebGLRenderingContext.viewport{tuple(args)} -> method')
