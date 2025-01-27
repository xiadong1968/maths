import argparse
import sys
from typing import Optional

from core import (
    calculate_derivative,
    DerivativeError,
    InputValidationError,
    CalculationError,
    FunctionNotSupportedError
)
from display import render_expression, show_derivation_steps, console
from config import DEFAULT_VARIABLE, MAX_ORDER

def parse_args() -> argparse.Namespace:
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description='符号微分计算器',
        formatter_class=argparse.RawTextHelpFormatter
    )
    
    parser.add_argument(
        'expression',
        help='要求导的数学表达式（使用Python语法，如"exp(x)*cos(x)"）'
    )
    
    parser.add_argument(
        '-o', '--order',
        type=int,
        default=1,
        help=f'导数阶数 (默认: 1, 最大: {MAX_ORDER})'
    )
    
    parser.add_argument(
        '-v', '--variable',
        default=DEFAULT_VARIABLE,
        help=f'求导变量 (默认: {DEFAULT_VARIABLE})'
    )
    
    parser.add_argument(
        '-s', '--steps',
        action='store_true',
        help='显示详细计算步骤'
    )
    
    parser.add_argument(
        '-l', '--latex',
        action='store_true',
        help='以LaTeX格式输出结果'
    )
    
    return parser.parse_args()

def main() -> None:
    """命令行入口函数"""
    args = parse_args()
    
    try:
        if args.steps or args.latex:
            result, steps = calculate_derivative(
                args.expression,
                variable=args.variable,
                order=args.order,
                track_steps=True
            )
            
            if args.steps:
                show_derivation_steps(steps, args.variable)
                console.print("\n最终结果：")
        else:
            result = calculate_derivative(
                args.expression,
                variable=args.variable,
                order=args.order,
                track_steps=False
            )
            
        if args.latex:
            from display import render_latex
            console.print(render_latex(result))
        else:
            console.print(render_expression(result))
            
    except InputValidationError as e:
        console.print(f"[red]输入错误: {str(e)}[/red]")
        sys.exit(1)
    except FunctionNotSupportedError as e:
        console.print(f"[red]函数不支持: {str(e)}[/red]")
        sys.exit(1)
    except CalculationError as e:
        console.print(f"[red]计算错误: {str(e)}[/red]")
        sys.exit(1)
    except Exception as e:
        console.print(f"[red]未知错误: {str(e)}[/red]")
        sys.exit(1)

if __name__ == "__main__":
    main()
