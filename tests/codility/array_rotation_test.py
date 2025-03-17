#given an array A consisting of N integers and an integer K, returns the array A rotated K times.
def solution(A, K):
    # if K is bigger than A length, take the remaining 
    length = len(A)
    # make sure check empty array
    if length == 0:
        return A

    time_to_rotate = K % length
    rotate_start_index = length - time_to_rotate
    first_part = A[0:rotate_start_index]

    second_part = A[rotate_start_index:]

    return second_part + first_part


def test_add():
    assert solution(20) == 1
    assert solution(15) == 0







