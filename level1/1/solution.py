def vector_dot(vector1,vector2):
    product=0
    for i,j in zip(vector1, vector2):
        product=product+i*j
    return product
vec1=[1,2,3]
vec2=[3,4,5]
print("the  of vectors 1 and 2 is:{}".format(vector_dot(vec1,vec2)))
