from .flags import *


@construct_111001
class MLGraphBuilder:
    def __str__(self):
        return f'[object {self.__class__.__name__}]'

    def __init__(self, *args, **kw):
        self._attr = dict(kw)

    __v8_method__ = (
        # (name, cb, length, CallbackType, FlagLocation, V8Attribute, FlagReceiverCheck, 
        # cross_origin_check, SideEffectType)
        ("abs", "fn_abs", 1, 0, 1, 0, 0, 0, 0),
        ("add", "fn_add", 2, 0, 1, 0, 0, 0, 0),
        ("argMax", "fn_argMax", 1, 0, 1, 0, 0, 0, 0),
        ("argMin", "fn_argMin", 1, 0, 1, 0, 0, 0, 0),
        ("averagePool2d", "fn_averagePool2d", 1, 0, 1, 0, 0, 0, 0),
        ("batchNormalization", "fn_batchNormalization", 3, 0, 1, 0, 0, 0, 0),
        ("build", "fn_build", 1, 0, 1, 0, 1, 0, 0),
        ("cast", "fn_cast", 2, 0, 1, 0, 0, 0, 0),
        ("ceil", "fn_ceil", 1, 0, 1, 0, 0, 0, 0),
        ("clamp", "fn_clamp", 0, 0, 1, 0, 0, 0, 0),
        ("concat", "fn_concat", 2, 0, 1, 0, 0, 0, 0),
        ("constant", "fn_constant", 2, 0, 1, 0, 0, 0, 0),
        ("conv2d", "fn_conv2d", 2, 0, 1, 0, 0, 0, 0),
        ("convTranspose2d", "fn_convTranspose2d", 2, 0, 1, 0, 0, 0, 0),
        ("cos", "fn_cos", 1, 0, 1, 0, 0, 0, 0),
        ("div", "fn_div", 2, 0, 1, 0, 0, 0, 0),
        ("elu", "fn_elu", 0, 0, 1, 0, 0, 0, 0),
        ("equal", "fn_equal", 2, 0, 1, 0, 0, 0, 0),
        ("erf", "fn_erf", 1, 0, 1, 0, 0, 0, 0),
        ("exp", "fn_exp", 1, 0, 1, 0, 0, 0, 0),
        ("expand", "fn_expand", 2, 0, 1, 0, 0, 0, 0),
        ("floor", "fn_floor", 1, 0, 1, 0, 0, 0, 0),
        ("gather", "fn_gather", 2, 0, 1, 0, 0, 0, 0),
        ("gelu", "fn_gelu", 0, 0, 1, 0, 0, 0, 0),
        ("gemm", "fn_gemm", 2, 0, 1, 0, 0, 0, 0),
        ("greater", "fn_greater", 2, 0, 1, 0, 0, 0, 0),
        ("greaterOrEqual", "fn_greaterOrEqual", 2, 0, 1, 0, 0, 0, 0),
        ("gru", "fn_gru", 5, 0, 1, 0, 0, 0, 0),
        ("gruCell", "fn_gruCell", 5, 0, 1, 0, 0, 0, 0),
        ("hardSigmoid", "fn_hardSigmoid", 0, 0, 1, 0, 0, 0, 0),
        ("hardSwish", "fn_hardSwish", 0, 0, 1, 0, 0, 0, 0),
        ("identity", "fn_identity", 1, 0, 1, 0, 0, 0, 0),
        ("input", "fn_input", 2, 0, 1, 0, 0, 0, 0),
        ("instanceNormalization", "fn_instanceNormalization", 1, 0, 1, 0, 0, 0, 0),
        ("l2Pool2d", "fn_l2Pool2d", 1, 0, 1, 0, 0, 0, 0),
        ("layerNormalization", "fn_layerNormalization", 1, 0, 1, 0, 0, 0, 0),
        ("leakyRelu", "fn_leakyRelu", 0, 0, 1, 0, 0, 0, 0),
        ("lesser", "fn_lesser", 2, 0, 1, 0, 0, 0, 0),
        ("lesserOrEqual", "fn_lesserOrEqual", 2, 0, 1, 0, 0, 0, 0),
        ("linear", "fn_linear", 0, 0, 1, 0, 0, 0, 0),
        ("log", "fn_log", 1, 0, 1, 0, 0, 0, 0),
        ("logicalNot", "fn_logicalNot", 1, 0, 1, 0, 0, 0, 0),
        ("lstm", "fn_lstm", 5, 0, 1, 0, 0, 0, 0),
        ("lstmCell", "fn_lstmCell", 6, 0, 1, 0, 0, 0, 0),
        ("matmul", "fn_matmul", 2, 0, 1, 0, 0, 0, 0),
        ("max", "fn_max", 2, 0, 1, 0, 0, 0, 0),
        ("maxPool2d", "fn_maxPool2d", 1, 0, 1, 0, 0, 0, 0),
        ("min", "fn_min", 2, 0, 1, 0, 0, 0, 0),
        ("mul", "fn_mul", 2, 0, 1, 0, 0, 0, 0),
        ("neg", "fn_neg", 1, 0, 1, 0, 0, 0, 0),
        ("pad", "fn_pad", 3, 0, 1, 0, 0, 0, 0),
        ("pow", "fn_pow", 2, 0, 1, 0, 0, 0, 0),
        ("prelu", "fn_prelu", 2, 0, 1, 0, 0, 0, 0),
        ("reciprocal", "fn_reciprocal", 1, 0, 1, 0, 0, 0, 0),
        ("reduceL1", "fn_reduceL1", 1, 0, 1, 0, 0, 0, 0),
        ("reduceL2", "fn_reduceL2", 1, 0, 1, 0, 0, 0, 0),
        ("reduceLogSum", "fn_reduceLogSum", 1, 0, 1, 0, 0, 0, 0),
        ("reduceLogSumExp", "fn_reduceLogSumExp", 1, 0, 1, 0, 0, 0, 0),
        ("reduceMax", "fn_reduceMax", 1, 0, 1, 0, 0, 0, 0),
        ("reduceMean", "fn_reduceMean", 1, 0, 1, 0, 0, 0, 0),
        ("reduceMin", "fn_reduceMin", 1, 0, 1, 0, 0, 0, 0),
        ("reduceProduct", "fn_reduceProduct", 1, 0, 1, 0, 0, 0, 0),
        ("reduceSum", "fn_reduceSum", 1, 0, 1, 0, 0, 0, 0),
        ("reduceSumSquare", "fn_reduceSumSquare", 1, 0, 1, 0, 0, 0, 0),
        ("relu", "fn_relu", 0, 0, 1, 0, 0, 0, 0),
        ("resample2d", "fn_resample2d", 1, 0, 1, 0, 0, 0, 0),
        ("reshape", "fn_reshape", 2, 0, 1, 0, 0, 0, 0),
        ("sigmoid", "fn_sigmoid", 0, 0, 1, 0, 0, 0, 0),
        ("sin", "fn_sin", 1, 0, 1, 0, 0, 0, 0),
        ("slice", "fn_slice", 3, 0, 1, 0, 0, 0, 0),
        ("softmax", "fn_softmax", 0, 0, 1, 0, 0, 0, 0),
        ("softplus", "fn_softplus", 0, 0, 1, 0, 0, 0, 0),
        ("softsign", "fn_softsign", 0, 0, 1, 0, 0, 0, 0),
        ("split", "fn_split", 2, 0, 1, 0, 0, 0, 0),
        ("sqrt", "fn_sqrt", 1, 0, 1, 0, 0, 0, 0),
        ("sub", "fn_sub", 2, 0, 1, 0, 0, 0, 0),
        ("tan", "fn_tan", 1, 0, 1, 0, 0, 0, 0),
        ("tanh", "fn_tanh", 0, 0, 1, 0, 0, 0, 0),
        ("transpose", "fn_transpose", 1, 0, 1, 0, 0, 0, 0),
        ("triangular", "fn_triangular", 1, 0, 1, 0, 0, 0, 0),
        ("where", "fn_where", 3, 0, 1, 0, 0, 0, 0),

    )

    def fn_abs(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.abs{tuple(args)} -> method')

    def fn_add(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.add{tuple(args)} -> method')

    def fn_argMax(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.argMax{tuple(args)} -> method')

    def fn_argMin(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.argMin{tuple(args)} -> method')

    def fn_averagePool2d(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.averagePool2d{tuple(args)} -> method')

    def fn_batchNormalization(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.batchNormalization{tuple(args)} -> method')

    def fn_build(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.build{tuple(args)} -> method')

    def fn_cast(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.cast{tuple(args)} -> method')

    def fn_ceil(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.ceil{tuple(args)} -> method')

    def fn_clamp(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.clamp{tuple(args)} -> method')

    def fn_concat(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.concat{tuple(args)} -> method')

    def fn_constant(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.constant{tuple(args)} -> method')

    def fn_conv2d(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.conv2d{tuple(args)} -> method')

    def fn_convTranspose2d(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.convTranspose2d{tuple(args)} -> method')

    def fn_cos(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.cos{tuple(args)} -> method')

    def fn_div(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.div{tuple(args)} -> method')

    def fn_elu(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.elu{tuple(args)} -> method')

    def fn_equal(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.equal{tuple(args)} -> method')

    def fn_erf(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.erf{tuple(args)} -> method')

    def fn_exp(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.exp{tuple(args)} -> method')

    def fn_expand(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.expand{tuple(args)} -> method')

    def fn_floor(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.floor{tuple(args)} -> method')

    def fn_gather(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.gather{tuple(args)} -> method')

    def fn_gelu(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.gelu{tuple(args)} -> method')

    def fn_gemm(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.gemm{tuple(args)} -> method')

    def fn_greater(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.greater{tuple(args)} -> method')

    def fn_greaterOrEqual(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.greaterOrEqual{tuple(args)} -> method')

    def fn_gru(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.gru{tuple(args)} -> method')

    def fn_gruCell(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.gruCell{tuple(args)} -> method')

    def fn_hardSigmoid(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.hardSigmoid{tuple(args)} -> method')

    def fn_hardSwish(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.hardSwish{tuple(args)} -> method')

    def fn_identity(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.identity{tuple(args)} -> method')

    def fn_input(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.input{tuple(args)} -> method')

    def fn_instanceNormalization(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.instanceNormalization{tuple(args)} -> method')

    def fn_l2Pool2d(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.l2Pool2d{tuple(args)} -> method')

    def fn_layerNormalization(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.layerNormalization{tuple(args)} -> method')

    def fn_leakyRelu(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.leakyRelu{tuple(args)} -> method')

    def fn_lesser(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.lesser{tuple(args)} -> method')

    def fn_lesserOrEqual(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.lesserOrEqual{tuple(args)} -> method')

    def fn_linear(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.linear{tuple(args)} -> method')

    def fn_log(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.log{tuple(args)} -> method')

    def fn_logicalNot(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.logicalNot{tuple(args)} -> method')

    def fn_lstm(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.lstm{tuple(args)} -> method')

    def fn_lstmCell(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.lstmCell{tuple(args)} -> method')

    def fn_matmul(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.matmul{tuple(args)} -> method')

    def fn_max(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.max{tuple(args)} -> method')

    def fn_maxPool2d(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.maxPool2d{tuple(args)} -> method')

    def fn_min(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.min{tuple(args)} -> method')

    def fn_mul(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.mul{tuple(args)} -> method')

    def fn_neg(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.neg{tuple(args)} -> method')

    def fn_pad(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.pad{tuple(args)} -> method')

    def fn_pow(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.pow{tuple(args)} -> method')

    def fn_prelu(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.prelu{tuple(args)} -> method')

    def fn_reciprocal(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reciprocal{tuple(args)} -> method')

    def fn_reduceL1(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceL1{tuple(args)} -> method')

    def fn_reduceL2(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceL2{tuple(args)} -> method')

    def fn_reduceLogSum(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceLogSum{tuple(args)} -> method')

    def fn_reduceLogSumExp(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceLogSumExp{tuple(args)} -> method')

    def fn_reduceMax(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceMax{tuple(args)} -> method')

    def fn_reduceMean(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceMean{tuple(args)} -> method')

    def fn_reduceMin(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceMin{tuple(args)} -> method')

    def fn_reduceProduct(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceProduct{tuple(args)} -> method')

    def fn_reduceSum(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceSum{tuple(args)} -> method')

    def fn_reduceSumSquare(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reduceSumSquare{tuple(args)} -> method')

    def fn_relu(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.relu{tuple(args)} -> method')

    def fn_resample2d(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.resample2d{tuple(args)} -> method')

    def fn_reshape(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.reshape{tuple(args)} -> method')

    def fn_sigmoid(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.sigmoid{tuple(args)} -> method')

    def fn_sin(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.sin{tuple(args)} -> method')

    def fn_slice(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.slice{tuple(args)} -> method')

    def fn_softmax(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.softmax{tuple(args)} -> method')

    def fn_softplus(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.softplus{tuple(args)} -> method')

    def fn_softsign(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.softsign{tuple(args)} -> method')

    def fn_split(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.split{tuple(args)} -> method')

    def fn_sqrt(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.sqrt{tuple(args)} -> method')

    def fn_sub(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.sub{tuple(args)} -> method')

    def fn_tan(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.tan{tuple(args)} -> method')

    def fn_tanh(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.tanh{tuple(args)} -> method')

    def fn_transpose(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.transpose{tuple(args)} -> method')

    def fn_triangular(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.triangular{tuple(args)} -> method')

    def fn_where(self, *args):
        logger.debug(f'patch -> v8_ml_graph_builder.py -> MLGraphBuilder.where{tuple(args)} -> method')
