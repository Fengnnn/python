#O(N) or O(N*log(N))
# find unpaired number
def solution(A):
    unpaired = 0
    for num in A:
        unpaired ^= num  # XOR all elements
    return unpaired

# find missing number  array with n size but has value from 1 to n+1
#PermMissingElem

def solution(A):
    n = len(A)
    if n == 0:
        return 1

    xor_total = 0

    # XOR all numbers from 1 to N + 1
    for i in range(1, n + 2):
        xor_total ^= i

    # XOR all numbers in the array
    for num in A:
        xor_total ^= num

    # The remaining value is the missing number
    return xor_total
