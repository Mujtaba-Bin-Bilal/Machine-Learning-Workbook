def eigen_value_and_vector(m):
    a,b=m[0]
    c,d=m[1]
    #define the values of the eigenvalue atrix
    #(m1)x^2+(m2)x+m3
    m1,m2,m3=1,-1*(a+d),a*d-b*c
    lam=roots_calculator(m1,m2,m3)
    ev=[]
    for l in lam:
        y=a-l
        x=(-1*b)
        vec=[x,y]
        ev.append(vec)

    return lam,ev





def roots_calculator(a,b,c):
    r1=(-b+((b**2-4*a*c)**0.5))/(2*a)
    r2=(-b-((b**2-4*a*c)**0.5))/(2*a)
    return [r1,r2]
a=[[1,2],[2,1]]
print(eigen_value_and_vector(a))
