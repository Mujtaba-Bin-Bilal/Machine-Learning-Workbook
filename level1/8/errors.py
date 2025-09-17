def mean_absulute_error(x,y):
    error=0
    for a,ap in zip(x,y):
       error +=abs(a-ap)
    error/=len(x)
    return error
def mean_square_error(x,y):
    error=0
    for a,ap in zip(x,y):
        error+=(a-ap)**2
    error/=len(x)
    return error
x=[2,4,6,7,8,0,2,3,4]
y=[2.23,5,7.75,8.23,0.34,2.12,3.98,4.75]
print(mean_absolute_error(x,y))
print(mean_square_error(x,y))
