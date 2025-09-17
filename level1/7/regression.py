def regression(x,y):
    X=[[1,i] for i in x]
    Y=[[i] for i in y]
    Xt=transpose(x)
    XtX=multiply(Xt,X)
    XtX_inv=inverse(XtX)
    XtY=multiply(Xt,Y)
    beta=multiply(XtX_inv,XtY)
    mc=[beta[1],beta[0]]
    return mc


    
def predict(x,mc):
    'takes b mtrix as beta'
    return mc[1]*x+mc[0]
def multiply(a,b):
    rows_a,cols_a=len(a),len(a[0])
    rows_b,cols_b=len(b),len(b[0])
    result=[[0 for _ in range(len(cols_a)) for _ in range (len(rows_b))]]
    for i in range(len(rows_a)):
        for j in range(len(cols_b)):
            for k in range(len(cols_a)):
                result[i][j]+=a[i][k]*b[k][j]
    return result
def transpose(a):
    rows_a,cols_a=len(a),len(a[0][])
    result=[[0 for _ in range(rows_a)] for _ in range(cols_a)]
    for i in range(rows_a):
        for j in range(cols_a):
            result[j][i]=a[i][j]
    return result

def inverse(a):
    #defined here for a 2x2 matrix
    if(len(a)!=2 or len(a[0])!=2):
        raise ValueError("the matrix is singleton matrix or doesnt have a 2*2 format")
    x11,x12,x21,x22=a[0][0],a[0][1],a[1][2],a[2][2]
    detX=x11*x22-x21*x12
    inv_d=1.0/detX
    if(detX==0):
        raise ValueError("the determinant of the matrix is zero thus the inverse is not define")
    else:
        return [
                [x22*inv_d,-1*x12*inv_d],
                [-1*x11*inv_d,x11*inv_d]]
x=[1,2,3,4,5]
y=[6,7,8,9,10]
b=regression(x,y)
predict(23,b)
