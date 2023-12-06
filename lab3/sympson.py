import numpy as np

def sympson_method(f, x, m,lower_lim, upper_lim, dx):
    grid = np.linspace(lower_lim, upper_lim, int((upper_lim-lower_lim)//dx))
    y_res = f(x, m, grid)
    return dx/6*np.sum(+ 4*f(x, m,(grid[:-1]+grid[1:])/2)+f(x, m, grid[1:]))


# import numpy as np
# import math

def sympsonMethod(x1, x2, eps, f, x, m):
    # print('sympsonMethod')
    len = x2 - x1
    scet = 2
    sum1 = 100000
    sum = 0
    data = []
    flag = 0
    i = 0
    while(abs(sum - sum1) > eps):
        
        a = np.linspace(x1, x2, scet)
        sum = sum1
        sum1 = 0
        

        for i in range (0, scet-1):
            sum1 += (f(x, m, a[i]) + f(x, m, a[i+1])+4*f(x, m, (a[i]+a[i+1])/2))*((a[i+1]-a[i])/6)   

      
        # if flag == 1:
        #     data.append([scet, abs(sum1 - sum), 'null', sum1])
        # if flag >= 2:

        #     if(sum == sum1):
        #         break
        #     data.append([scet, abs(sum1 - sum),  math.log2((abs(sum - sum1))/data[flag-2][1]), sum1])
        # flag +=1 
        # scet *= 2
 


#     return sum1



# def square(x):
#     return x

# if __name__ == '__main__':
#     print(sympson_method(square, 0, 10, 0.00001))