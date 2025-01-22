from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from sympy import pretty

console = Console()

def render_expression(expr):
    """使用SymPy的pretty打印和Rich语法高亮"""
    expr_str = pretty(expr, use_unicode=True)
    return Syntax(expr_str, "python", theme="monokai", line_numbers=False)

def show_derivation_steps(steps, variable='x'):
    """显示导数计算步骤表格"""
    table = Table(title=f"导数计算步骤追踪 (d/{variable})", show_header=False)
    table.add_column("Step", style="cyan")
    table.add_column("Expression", style="magenta")
    
    for i, step in enumerate(steps, 1):
        table.add_row(f"Step {i}", render_expression(step))
        
    console.print(table)
