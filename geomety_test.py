import numpy as np
from matplotlib import pyplot as plt

N = 10
N_part = 10
    
def parts(x):
    count = 0
    stop_flag = False
    pre_stop_flag = False
    start_flag = True
    x = -x
    n = x.shape[0]
    m = x.shape[1]
    while not stop_flag:
        find_flag = False
        for i in range(n):
            for j in range(m):
                if x[i, j] < 0:
                    if start_flag:
                        count += 1
                        x[i, j] = count
                        find_flag = True
                        start_flag = False
                    if j<m-1 and x[i, j+1] == count:
                        x[i, j] = count
                        find_flag = True
                    if j>0 and x[i, j-1] == count:
                        x[i, j] = count
                        find_flag = True
                    if i<n-1 and x[i+1, j] == count:
                        x[i, j] = count
                        find_flag = True
                    if i>0 and x[i-1, j] == count:
                        x[i, j] = count
                        find_flag = True

                    if x[i, j] == count:
                        if j<m-1 and x[i, j+1] == -1:
                            x[i, j+1] = count
                            find_flag = True
                        if j>0 and x[i, j-1] == -1:
                            x[i, j-1] = count
                            find_flag = True
                        if i<n-1 and x[i+1, j] == -1:
                            x[i+1, j] = count
                            find_flag = True
                        if i>0 and x[i-1, j] == -1:
                            x[i-1, j] = count
                            find_flag = True
        if not find_flag:
            start_flag = True
            if pre_stop_flag:
                stop_flag = True
            else:
               pre_stop_flag = True
        else:
            pre_stop_flag = False
    
    return x, count

def smooth(x):
    n = x.shape[0]
    m = x.shape[1]
    stop_flag = False
    pre_stop_flag = False
    while not stop_flag:
        find_flag = False
        for i in range(n):
            for j in range(m):
                if x[i, j] != 0:
                    score = 0
                    if j<m-1 and x[i, j+1] == 0:
                        score += 1
                    if j>0 and x[i, j-1] == 0:
                        score += 1
                    if i<n-1 and x[i+1, j] == 0:
                        score += 1
                    if i>0 and x[i-1, j] == 0:
                        score += 1
                    if score >= 3:
                        x[i, j] = 0
                        find_flag = True

                if x[i, j] == 0:
                    score = 0
                    if j<m-1 and x[i, j+1] == 1:
                        score += 1
                    if j>0 and x[i, j-1] == 1:
                        score += 1
                    if i<n-1 and x[i+1, j] == 1:
                        score += 1
                    if i>0 and x[i-1, j] == 1:
                        score += 1
                    if score >= 3:
                        x[i, j] = 1
                        find_flag = True
        if not find_flag:
            if pre_stop_flag:
                stop_flag = True
            else:
               pre_stop_flag = True
        else:
            pre_stop_flag = False
    
    return x
    

'''
count = 0
while count != N_part:
    x = np.random.randint(0, 2, (N,N))
    y, count = parts(x)
'''
x = np.random.randint(0, 2, (N,N))

plt.imshow(x)
plt.colorbar()
plt.show()
x1 = smooth(x)
y, count = parts(x1)
plt.imshow(x1)
plt.colorbar()
plt.show()
plt.imshow(y)
plt.colorbar()
plt.show()