#A small frog wants to get to the other side of the road. 
# The frog is currently located at position X and wants to get to a position greater than or equal to Y. 
# The small frog always jumps a fixed distance, D.

#Count the minimal number of jumps that the small frog must perform to reach its target.

# edge case, x y is the same

#Floor division 10 // 3  = 3
#Ceiling division：向上取整除法（如果有余数，结果加 1）。
# (10 + 3 - 1) // 3     math.ceil(numerator / denominator)  math.ceil(10/3)
# abs the absoulte value abs(1-2)

import math


def solution(X, Y, D):
    distance = Y-X
    return (distance + D -1) // D



# 除法  
9//3
# 开方 
math.sqrt(9)
# 2次方
3 ** 2
#取整数  
int(3.44)