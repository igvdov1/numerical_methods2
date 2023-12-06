import numpy as np

sum = np.float16(1)
sum1 = np.float16(0)
while(sum != sum1):
    sum1 = sum
    sum *= 2
    sum = np.float64(sum)
print(sum1)
    