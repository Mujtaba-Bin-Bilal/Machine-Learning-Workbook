import random
def train_test_split(data,test_size=0.2,seed=None):
    n=len(data)
    if n==0:
        return [],[]
    if 0<test_size<1:
        n_test=int(n*test_size)
    else:
        n_test=int(test_size)
    n_test=max(0,min(n,n_test))
    data_shuffled=data[:]
    if seed is None:
        random.shuffle(data_shuffled)
    else:
        rng=random.Random(seed)
        rng.shuffle(data_shuffled)
    split_index=n-n_test
    train=data_shuffled[:split_index]
    test=data_shuffled[split_index:]
    return train,test
m=[122,23,34,55,3,12,3,4,23,234,24234,5,2]
print(m)
print(train_test_split(m),0.2,5)
