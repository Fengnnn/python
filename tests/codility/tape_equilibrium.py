def solution(A):
    total_A = sum(A)
    left_sum = 0
    min_different = 3000
    length = len(A)

    for index, i in enumerate(A):
        if(index == length-1): # can not slipt the last value
            break

        left_sum += i
        right_sum = total_A - left_sum
        different = abs(left_sum - right_sum )
        if different < min_different:
            min_different = different

   
    return min_different