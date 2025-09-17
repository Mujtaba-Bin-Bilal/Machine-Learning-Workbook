import matplotlib.pyplot as plt
import math
def sigmoid(x):
    return 1/(1+math.exp(-x))
def derivative_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))
X=[i*0.1 for i in range(-100,100)]
Y=[sigmoid(x) for x in X]
dY=[derivative_sigmoid(x) for x in X]
plt.figure(figsize=(10,6))
plt.plot(X,Y,label="Sigmoid s(x)",linewidth=2)
plt.plot(X,dY,label="Derivative of Sigmoid d(s(x))/dx",linewidth=2,linestyle="--")
plt.title("sigmoid function and its derivaives")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show
