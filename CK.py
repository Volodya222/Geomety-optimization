import numpy as np
np.random.seed(2)

sample1 = np.random.binomial(10, 0.1, 10)
for i in range(6,10):
    print(sample1[i].round(2))
print(sum(sample1)/len(sample1))