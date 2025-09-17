def f(x,y):
    return x**2+3*x*y+y**2
def numerical_gradient(f,x,y,h=1e-6):
    df_dx=(f(x+h,y)-f(x-h,y))/(2*h)
    df_dy=(f(x,y+h)-f(x,y-h))/(2*h)
    return df_dx,df_dy
grad=numerical_gradient(f,1,2)
print("the gradient at 1,2 is:",grad)
