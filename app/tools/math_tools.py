import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

def calculate_expression(expression: str) -> str:
    """Calculate mathematical expressions safely"""
    try:
        # Use sympy for safe evaluation
        result = sp.sympify(expression)
        evaluated = float(result.evalf())
        return f"Result: {evaluated}"
    except Exception as e:
        return f"Error calculating expression: {str(e)}"

def solve_equation(equation: str) -> str:
    """Solve mathematical equations"""
    try:
        # Parse equation (assume format like "2*x + 5 = 11")
        if "=" in equation:
            left, right = equation.split("=")
            eq = sp.Eq(sp.sympify(left.strip()), sp.sympify(right.strip()))
            x = sp.Symbol('x')
            solution = sp.solve(eq, x)
            return f"Solution: x = {solution}"
        else:
            return "Please provide equation in format: expression = value"
    except Exception as e:
        return f"Error solving equation: {str(e)}"

def create_graph(function: str, x_range: str = "-10,10") -> str:
    """Create graph of mathematical function"""
    try:
        x = sp.Symbol('x')
        expr = sp.sympify(function)
        
        # Parse range
        x_min, x_max = map(float, x_range.split(','))
        x_vals = np.linspace(x_min, x_max, 400)
        
        # Convert to numpy function
        f = sp.lambdify(x, expr, 'numpy')
        y_vals = f(x_vals)
        
        # Create plot
        plt.figure(figsize=(8, 6))
        plt.plot(x_vals, y_vals, 'b-', linewidth=2)
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Graph of f(x) = {function}')
        
        # Save plot and show
        plt.savefig(f'graph_{function.replace("/", "_div_").replace("*", "_mult_")}.png', 
                   dpi=150, bbox_inches='tight')
        plt.show()
        plt.close()
        
        return f"Graph created and displayed for f(x) = {function}. Range: [{x_min}, {x_max}]"
    except Exception as e:
        return f"Error creating graph: {str(e)}"
