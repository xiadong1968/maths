from sympy import (
    sin, cos, tan, cot, sec, csc,
    exp, log, gamma, sqrt, erf,
    sinh, cosh, tanh, asin, acos, atan
)

# 允许的数学函数及其对应的SymPy实现
ALLOWED_FUNCTIONS = {
    # 基本三角函数
    'sin': sin,
    'cos': cos,
    'tan': tan,
    'cot': cot,
    'sec': sec,
    'csc': csc,
    
    # 反三角函数
    'asin': asin,
    'acos': acos,
    'atan': atan,
    
    # 指数和对数函数
    'exp': exp,
    'log': log,
    
    # 特殊函数
    'gamma': gamma,
    'erf': erf,
    
    # 双曲函数
    'sinh': sinh,
    'cosh': cosh,
    'tanh': tanh,
    
    # 其他
    'sqrt': sqrt
}

# 默认配置
DEFAULT_VARIABLE = 'x'  # 默认求导变量
MAX_ORDER = 10          # 最大求导阶数