#O(N) or O(N * log(N))
def solution(A):
    a_length = len(A)
    if a_length == 1 and A[0] != 1:
        return 0

    # permutation should always start from 1
    number_set = set()
    biggest_number = 0
    for i in A:
        number_set.add(i)
        if i > biggest_number:
            biggest_number = i
      
    if len(number_set) == a_length and a_length == biggest_number: 
        # has no duplicate number and has no missing number 
        return 1
    
    return 0 