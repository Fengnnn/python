#N is an odd integer within the range [1..1,000,000] always has a odd
#A non-empty array A consisting of N integers is given. can't be empty
#each element of array A is an integer within the range [1..1,000,000,000] all positive
#all but one of the values in A occur an even number of times. can only has one unpair number


# you will have to read the array till the end, so have to loop at lease once
#Detected time complexity:O(N**2)
def solution(A):
    
    first_part, unpaired_number_array = setup_parts(A)
    do_pair = True
    while do_pair:
        for number in first_part:
            # if number found inside unpaired_number_array, return the number from it
            # else add this number into unpaired_number_array
            paired_number_index = find_paired_number_index(number, unpaired_number_array)
            if(paired_number_index> -1):
                del unpaired_number_array[paired_number_index]
                continue
            else:
                # add into the array
                unpaired_number_array.append(number)
        if  len(unpaired_number_array) >1:
            # if still have value to pair, break the array and pair again
            first_part, unpaired_number_array = setup_parts(unpaired_number_array)
        else:
            do_pair = False # stop the loop


    # should have one value left in the array
    return unpaired_number_array[0]
            

# find the paired number and return index
def find_paired_number_index(number_to_find, array):
    for index, number in enumerate(array):
        if number == number_to_find:
            return index
        
    # no pair found   
    return -1

def setup_parts(array_to_pair):
    length  = len(array_to_pair)
    middle_index = length//2+1
    first_part = array_to_pair[0:middle_index]
    unpaired_number_array = array_to_pair[middle_index:]
    return (first_part, unpaired_number_array)


def test_add():
    assert solution( [9, 3, 9, 3, 9, 7, 9]) == 7
