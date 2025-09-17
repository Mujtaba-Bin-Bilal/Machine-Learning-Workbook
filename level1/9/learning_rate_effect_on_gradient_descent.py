import matplotlib.pyplot as plt

def f(x):
    return x**2 

def grad_f(x):
    return 2*x

def gradient_descent(lr=0.1, epochs=30):
    x = 4
    history = [(x, f(x))]
    for i in range(epochs):
        dx = grad_f(x)
        x = x - lr*dx
        history.append((x, f(x)))
    return history

# run gradient descent
flag = True
while flag:
    inp = int(input("enter the choice:\n 1. for finding the gradient \n 2. exit\n \t->>>>>"))
    if inp == 1:
        lr = float(input("enter the learning rate: "))
        path = gradient_descent(lr, 30)
        # extract values
        xs, ys = zip(*path)
        plt.plot(xs, ys, 'o-', label="path of GD")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid()
        plt.show()
    elif inp ==2:
        flag = False
