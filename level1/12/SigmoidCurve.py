import matplotlib.pyplot as plt
import random
import math
def sigmoid(x):
    return 1/(1+math.exp(-x))
def d_sigmoid(x):
    return sigmoid(x)*(1-sigmoid(x))

X=[i+1e-10 for i in range(-10,10)]
y=[sigmoid(i) for i in X]
d_y=[d_sigmoid(i) for i in X]
plt.plot(X,y,label="sigmoid",color="blue")
plt.plot(X,d_y,label="Derivative",color="red")
plt.title("sigmoid function andits derivative")
plt.xlabel("x")
plt.ylabel("value")
plt.legend()
plt.grid(True)
plt.show()
