from typing import Tuple, List, Optional, Union
from sympy import Expr, symbols, diff, simplify, sympify, SympifyError
from config import ALLOWED_FUNCTIONS, DEFAULT_VARIABLE, MAX_ORDER

class DerivativeError(Exception):
    """导数计算错误的基类"""
    pass

class InputValidationError(DerivativeError):
    """输入验证错误"""
    pass

class CalculationError(DerivativeError):
    """计算过程错误"""
    pass

class FunctionNotSupportedError(DerivativeError):
    """不支持的函数错误"""
    pass

def validate_input(expr_str: str, variable: str, order: int) -> None:
    """验证输入参数的有效性"""
    if not isinstance(expr_str, str) or not expr_str.strip():
        raise InputValidationError("表达式必须是非空字符串")
    
    if not isinstance(variable, str) or not variable.isidentifier():
        raise InputValidationError("变量名必须是有效的标识符")
    
    if not isinstance(order, int) or order < 1 or order > MAX_ORDER:
        raise InputValidationError(f"阶数必须是1到{MAX_ORDER}之间的整数")

def calculate_derivative(
    expr_str: str,
    variable: str = DEFAULT_VARIABLE,
    order: int = 1,
    track_steps: bool = False
) -> Union[Expr, Tuple[Expr, List[Expr]]]:
    """
    计算指定变量的n阶导数
    
    参数:
        expr_str: 数学表达式字符串
        variable: 求导变量 (默认: 'x')
        order: 导数阶数 (默认: 1)
        track_steps: 是否记录计算步骤 (默认: False)
    
    返回:
        如果track_steps为False，返回最终导数表达式
        如果track_steps为True，返回(最终导数表达式, 步骤列表)
    """
    try:
        validate_input(expr_str, variable, order)
        
        var = symbols(variable)
        expr = sympify(expr_str, locals=ALLOWED_FUNCTIONS)
        
        derivative = expr
        steps = [expr] if track_steps else None
        
        for _ in range(order):
            derivative = diff(derivative, var)
            derivative = simplify(derivative)
            if track_steps:
                steps.append(derivative)
                
        return (derivative, steps) if track_steps else derivative
        
    except SympifyError as e:
        raise FunctionNotSupportedError(f"表达式包含不支持的函数或格式错误: {str(e)}")
    except Exception as e:
        raise CalculationError(f"计算过程中发生错误: {str(e)}")