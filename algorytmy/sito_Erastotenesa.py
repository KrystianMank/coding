import sympy as sp

# Define the variable and the function
x = sp.symbols('x')
expr = ((x-1)*(1-x)) / ((1-6*x)*(x+1))

# Calculate the limit as x approaches infinity
limit_expr = sp.limit(expr, x, sp.oo)
print(limit_expr)
