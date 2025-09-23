def std_deviation(l):
    s=0
    for i in l:
        s=s+(i**2-mean(l))
    s=(s/len(l))**0.5
    return s
def mean(l):
    s=0
    for i in l:
        s+=i
    s/=len(l)
    return s
def zNormalization(l):
    m=[]
    for i in l:
        a=(i-mean(l))/std_deviation(l)
        m.append(a)
    return m
l=[23,12,44,21,12,44,89]
print(l)
print(zNormalization(l))