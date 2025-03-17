def solution(number):
    if not is_number_valid(number):
        return -1
    next_number = number
    while True:
        next_number += 1
        if is_number_valid(next_number):
            break


    return next_number
 

def is_number_valid(number):
    if '7' in str(number):
        return False
    
    for i in range(7,number-6):
        if '7' in str(i) and number % i == 0:
            return False
        
    return True

def test():
    assert(solution(69)== 80)
    assert(solution(36)== 38)
    assert(solution(14)== -1)
    assert(solution(51)== -1)