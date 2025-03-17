#O(N) or O(N * log(N))
def solution(A):
    # length is  [1..100,000]
    # smallest positive integer 1
    if len(A) == 1:
       return 2 if A[0] == 1 else 1
    positive_set = set()

    for i in A:
        if i >0:
            positive_set.add(i)

    if len(positive_set) == 0:
        return 1
    sorted_positive_set = sorted(positive_set)
    if sorted_positive_set[0] != 1: # missing 1
        return 1
    
    for i in range(1, len(sorted_positive_set)):
        if sorted_positive_set[i] - sorted_positive_set[i-1] >1:
            result = sorted_positive_set[i-1] +1
            return result

    return sorted_positive_set.pop()+1


            
        

def test():
    assert solution([1]) == 2
    assert solution([-1,2, 4,2,1]) == 3
    assert solution([4,2,1]) == 3
    assert solution([0,2,3]) == 1
    assert solution([1,1,1]) == 2