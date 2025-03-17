# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
#O(N)
def solution(A):
    # Implement your solution here
    #non-empty array 
    #(P, Q), where 0 ≤ P < Q < N,
    # p can only be 0, pair with all the 1 after it
    # if 0 loop all the pair will be 
    if  len(A)==0:
        return 0
    pass_east_list = list()
    pass_west_list = list()

    for index, value in enumerate(A):
        pass_east_list.append(index) if value == 0 else pass_west_list.append(index)

    
    if len(pass_east_list)==0 or len(pass_west_list)==0:# no pair
        return 0
    
    pair_count = 0
    next_pass_west_start_index = 0 # next possible index to pair with east, which will the next index value that after east

    for  i in pass_east_list:

       next_pass_west_start_index = find_next_west_index( i, pass_west_list, next_pass_west_start_index )
       if next_pass_west_start_index < 0 :
            break
       else:
            pair_count += len(pass_west_list) - next_pass_west_start_index


    return pair_count if pair_count <= 1000000000 else -1

def find_next_west_index(east,pass_west_list,next_pass_west_start_index):
    for west_index in range(next_pass_west_start_index, len(pass_west_list)):
        if east <  pass_west_list[west_index]: # east is before west
            return west_index
    
    return -1 # all west index are before this east


#Use a single pass to count the number of cars traveling east (0) and update the total passing cars
def count_passing_cars(A):
    east_count = 0  # Number of cars traveling east so far
    passing_cars = 0  # Total number of passing cars

    for car in A:
        if car == 0:
            east_count += 1  # Increment east_count for cars traveling east
        else:
            passing_cars += east_count  # Add east_count for each car traveling west

        # If passing_cars exceeds 1,000,000,000, return -1
        if passing_cars > 1_000_000_000:
            return -1

    return passing_cars

def test():
    assert count_passing_cars( [1, 0, 1, 0, 1, 1]) == 5
    assert count_passing_cars( [1, 1, 1, 0, 0, 0]) == 0