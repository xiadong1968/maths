from typing import Union, Tuple, List
from sympy import Expr, latex
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax

console = Console()

def render_expression(expr: Expr) -> Syntax:
    """使用SymPy的pretty打印和Rich语法高亮"""
    expr_str = str(expr)
    return Syntax(expr_str, "python", theme="monokai", line_numbers=False)

def render_latex(expr: Expr) -> str:
    """将表达式渲染为LaTeX格式"""
    return latex(expr, mode='plain')

from typing import List
from sympy import Expr

def show_derivation_steps(steps: List[Expr], variable: str = 'x') -> None:
    """显示导数计算步骤表格"""
    table = Table(title=f"导数计算步骤追踪 (d/{variable})", show_header=False)
    table.add_column("Step", style="cyan")
    table.add_column("Expression", style="magenta")
    
    for i, step in enumerate(steps, 1):
        table.add_row(f"Step {i}", render_expression(step))
        
    console.print(table)

def display_result(
    result: Union[Expr, Tuple[Expr, List[Expr]]],
    show_steps: bool = False,
    use_latex: bool = False,
    variable: str = 'x'
) -> None:
    """
    显示计算结果
    
    参数:
        result: 计算结果，可以是单个表达式或(表达式, 步骤列表)
        show_steps: 是否显示计算步骤
        use_latex: 是否使用LaTeX格式
        variable: 求导变量
    """
    if isinstance(result, tuple):
        expr, steps = result
        if show_steps:
            show_derivation_steps(steps, variable)
            console.print("\n最终结果：")
    else:
        expr = result
        
    if use_latex:
        console.print(render_latex(expr))
    else:
        console.print(render_expression(expr))
