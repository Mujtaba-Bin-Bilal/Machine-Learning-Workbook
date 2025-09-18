import random
import math
import matplotlib.pyplot as plt

# Generate Gaussian blobs
def generate_blobs(n=100, mean1=(2,2), mean2=(6,6), std=1.0):
    X, y = [], []
    for _ in range(n):
        x1 = random.gauss(mean1[0], std)
        x2 = random.gauss(mean1[1], std)
        X.append([x1, x2])
        y.append(0)  # Class 0
    for _ in range(n):
        x1 = random.gauss(mean2[0], std)
        x2 = random.gauss(mean2[1], std)  
        X.append([x1, x2])
        y.append(1)  # Class 1
    return X, y

# Sigmoid function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Prediction
def predict(x, w, b):
    z = w[0]*x[0] + w[1]*x[1] + b  
    return sigmoid(z)

# Loss function
def compute_loss(X, y, w, b):
    m = len(y)
    loss = 0
    for i in range(m):
        y_cap = predict(X[i], w, b)
        loss += -(y[i]*math.log(y_cap+1e-9) + (1-y[i])*math.log(1-y_cap+1e-9))
    return loss/m

# Gradient descent weight update
def update_weights(X, y, w, b, lr=0.1):
    m = len(y)
    dw = [0, 0]
    db = 0
    for i in range(m):
        y_cap = predict(X[i], w, b)
        error = y_cap - y[i]
        dw[0] += error * X[i][0]
        dw[1] += error * X[i][1]
        db += error
    w[0] -= lr * dw[0]/m   # ✅ fixed
    w[1] -= lr * dw[1]/m
    b -= lr * db/m
    return w, b
# Training
X, y = generate_blobs(100, mean1=(2,2), mean2=(6,6), std=1.0)

# Initialize weights
w = [random.random(), random.random()]
b = random.random()

epochs = 1000
lr = 0.1
losses = []

for epoch in range(epochs):
    w, b = update_weights(X, y, w, b, lr)
    if epoch % 50 == 0:
        loss = compute_loss(X, y, w, b)
        losses.append(loss)
        print(f"Epoch {epoch}, Loss={loss:.4f}")  
# Plot Decision Boundary
for i in range(len(y)):
    if y[i] == 0:
        plt.scatter(X[i][0], X[i][1], color="blue", s=20)
    else:
        plt.scatter(X[i][0], X[i][1], color="red", s=20)

# Decision boundary: w1*x + w2*y + b = 0 -> y = -(w1/w2)*x - b/w2
x_vals = [min(p[0] for p in X), max(p[0] for p in X)]
y_vals = [-(w[0]/w[1])*x - b/w[1] for x in x_vals]
plt.plot(x_vals, y_vals, color="green", linewidth=2)

plt.title("Logistic Regression Decision Boundary (from scratch)")
plt.xlabel("x1")
plt.ylabel("x2")
plt.show()

# Plot Loss Curve
plt.plot(range(0, epochs, 50), losses, marker='o')
plt.title("Training Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.show()
