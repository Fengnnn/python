def solution(X, A):
    # Implement your solution here
    # read the array into dict
    position_dict = {}
    for index, value in enumerate(A):
        # all position has leave
        position_dict[value] = index

        if len(position_dict.keys()) == X:
            return index
            
    return -1



def solution_2(X, A):
    covered_positions = set()  # To track positions covered by leaves
    for time, position in enumerate(A):
        covered_positions.add(position)  # Add the current position
        if len(covered_positions) == X:  # Check if all positions are covered
            return time
    return -1  # If not all positions are covered