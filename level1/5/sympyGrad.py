import sympy as sp
def gradient_derivation(expr_str):
    x,y=sp.symbols('x y')
    exp=sp.sympify(expr_str)
    df_dx=sp.diff(exp,x)
    df_dy=sp.diff(exp,y)
    gradient=(df_dx,df_dy)
    return gradient
a=input("enter the equation as a python symbolic expression")
print("the gradient is {}".format(gradient_derivation(a)))
