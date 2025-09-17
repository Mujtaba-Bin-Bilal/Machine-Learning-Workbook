import matplotlib.pyplot as plt
def f(x,y):
    return x**2+2*x*y+y**2
def grad_f(x,y):
    df_dx=2*x+2*y
    df_dy=2*x+2*y
    return df_dx,df_dy
def  gradient_descent(lr=0.1,epochs=30):
    x,y=4,3
    history=[(x,y,f(x,y))]
    for i in range(epochs):
        dx,dy=grad_f(x,y)
        x=x-lr*dx
        y=y-lr*dy
        history.append((x,y,f(x,y)))
    return history
path=gradient_descent(0.1,30)
xs,ys,zs=zip(*path)
plt.plot(xs,ys,'o-',label="path of gd")
plt.xlabel="x"
plt.ylabel="y"
plt.legend()
plt.grid()
plt.show()
