
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# find the gap and return gap and next gap index
def find_gap(digits, next_gap_index):
    gap = 0
    for digit in digits:
        next_gap_index+=1
        if digit == '0':
            gap+=1
        else:
            return (gap, next_gap_index)
    # if can't find the ending 1, gap will be 0
    return (0, next_gap_index)

def solution(N)->int:
    # Implement your solution here
    # convert N into binary
    binary_representation = bin(N)[2:]
    # Split the binary string into individual digits
    binary_digits = [bit for bit in binary_representation]
    max_gap = 0
    next_gap = 0

    for digit in binary_digits:
        if digit == '0':
            next_gap += 1
        else:
            if next_gap > max_gap:
                max_gap = next_gap

            next_gap = 0
            
    return max_gap


    

def test_add():
    assert solution(20) == 1
    assert solution(15) == 0







