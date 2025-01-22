import sys
import argparse
from sympy import (
    symbols, diff, simplify, sympify, SympifyError,
    sin, cos, tan, cot, sec, csc,
    exp, log, gamma, sqrt, erf, pretty
)

ALLOWED_FUNCTIONS = {
    'sin': sin, 'cos': cos, 'tan': tan,
    'cot': cot, 'sec': sec, 'csc': csc,
    'exp': exp, 'log': log, 'gamma': gamma,
    'sqrt': sqrt, 'erf': erf
}

def calculate_derivative(expr_str, variable='x', order=1, track_steps=False):
    """计算指定变量的n阶导数并化简结果"""
    try:
        var = symbols(variable)
        expr = sympify(expr_str, locals=ALLOWED_FUNCTIONS)
        
        if not isinstance(order, int) or order < 1:
            raise ValueError("导数阶数必须是正整数")
            
        derivative = expr
        steps = [expr] if track_steps else None
        
        for i in range(order):
            derivative = diff(derivative, var)
            derivative = simplify(derivative)  # 立即简化每一步的结果
            if track_steps:
                steps.append(derivative)  # 记录简化后的形式
                
        final = derivative  # 最终结果已包含简化
        return (final, steps) if track_steps else final
    except SympifyError as e:
        raise ValueError(f"无效的表达式格式或包含不支持的函数: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"计算错误: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='符号微分计算器',
        formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('expression', help='要求导的数学表达式（使用Python语法，如"exp(x)*cos(x)"）')
    parser.add_argument('-o', '--order', type=int, default=1,
                      help='导数阶数 (默认: 1)')
    parser.add_argument('-v', '--variable', default='x',
                      help='求导变量 (默认: x)')
    parser.add_argument('-s', '--steps', action='store_true',
                      help='显示详细计算步骤')
    
    args = parser.parse_args()
    
    try:
        from rendering import render_expression, show_derivation_steps, console
        
        result, steps = calculate_derivative(
            args.expression,
            variable=args.variable,
            order=args.order,
            track_steps=args.steps
        )
        
        if args.steps:
            show_derivation_steps(steps, args.variable)
            print("\n最终结果：")
        console.print(render_expression(result))
        
    except (ValueError, RuntimeError) as e:
        print(f"错误：{str(e)}")
        print(f"支持函数列表：{', '.join(sorted(ALLOWED_FUNCTIONS))}")
        sys.exit(1)
    except Exception as e:
        print(f"未知错误：{str(e)}")
        sys.exit(1)
