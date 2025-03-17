# you can write to stdout for debugging purposes, e.g.
# Max Counters problem.
#O(N*M)
def solution(N, A):
    counter_dict = [0 for _ in range(N)]
    max_value = 0

    for i in A:
        if i > N+1:
            continue
        elif i == N+1:
            counter_dict = [max_value] * N
        else:
            increased_value = increase_x(i-1, counter_dict)
            if increased_value > max_value:
                max_value = increased_value

    return counter_dict


def increase_x(x_postion, counter_dict):
    counter_dict[x_postion] += 1
    return  counter_dict[x_postion]

#O(N + M) avoid loop inside a loop

def solution_2(N, A):
    counter_dict = [0] * N  # Initialize counters to 0
    max_value = 0
    max_counter_value = 0

    for i in A:
        if i > N+1:
            continue
        elif i == N+1:
            max_counter_value = max_value
        else:
            before_increase = counter_dict[i-1]
            if max_counter_value > before_increase: # time to max counter
                counter_dict[i-1] = max_counter_value+1
            else:
                counter_dict[i-1] = before_increase+1

            if counter_dict[i-1] > max_value:
                max_value = counter_dict[i-1]

                
    
    for j in range(0,N):
        if counter_dict[j] < max_counter_value:
            counter_dict[j] = max_counter_value


    return counter_dict


def test_add():
    assert solution(5, [3, 4, 4, 6, 1, 4, 4]) == 1
