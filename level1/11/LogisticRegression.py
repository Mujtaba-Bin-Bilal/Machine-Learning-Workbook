import math
import random
def generate_blobs(n_samples=100,centers=2,cluster_std=2.0):
    random.seed(42)
    X=[]    #holds the features
    Y=[]    /#holds the class labels, in this case 0 and 1
    center_coords=[[random.gauss(0,10) for _ in range(2)] for _ in range(centers)]
    for i in range(centers):
        for _ in range(n_samples//centers):
            point=[random.gauss(0,cluster_std) +c for c in center_coords[i]]
            X.append(point)
            Y.append([i])
            return X,Y
def dot_product(v1,v2):
    return sum(x*y for x,y in zip(v1,v2))
def sigmoid(z):
    return 1/(1+math.exp(-z))
def logistic_regression_gd(X,Y,lr=0.01,n_iterations=1000):
    m=len(X)
    n=len(X[0])+1
    weights=[0.0]*n
    for _ in range(n_iterations):
        dw=[0.0]*n
        for j in range(m):
            linear_model=dot_product(X_b[j],weights)
            y_predicted
