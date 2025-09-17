def f(x):
    return x**2
def grad_f(x):
    return 2*x
def gradient_descent(lr=0.1,epoch=30):
    s=4
    history=[(x,f(x))]
    for i in range(epoch):
        dx=grad_f(x)
        x=x-lr*dx
        history.append((x,f(x)))
        return history
flag=True
while flag:
    if inp==1:
        lr=float(input("enter the learning rate:"))
        path=gradient_descent(lr,30)
        xs,ys=zip(*path)
        plt.plot(xs,ys,'o-',label='path of gd')
        plt.xlabel("X")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()
    elif inp==2:
        flag=False

