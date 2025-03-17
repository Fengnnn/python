def find_students(N,M,recommendation_pairs):
    # N 1->100
    #N students, M recommendations happened 
    # find students that  recommended N-1 times
    if N == 1:
        return 0
    
    # transitive , A -> B B-> C, C Has AB, sorting back

    student_recommended_array = [[] for _ in range(N+1)]
    for value in recommendation_pairs:
        student_recommended_array[value[1]].append(value[0])
    

    student_count = 0

    for index, recommendes_array in enumerate(student_recommended_array):
        recommended_set = set()

        count_recommendation(recommended_set, index, student_recommended_array,recommendes_array)
        if len(recommended_set) == N-1:
             student_count += 1

    return student_count

def count_recommendation(recommended_set,target_index,student_recommended_array, recommendes_array):
    for student_index in recommendes_array:
            # skip the target student 
            if student_index == target_index:
                 continue
            # remove duplicate recommendation
            if student_index not in  recommended_set:
                 recommended_set.add(student_index)
            else:
                 continue
            count_recommendation(recommended_set,target_index,student_recommended_array,student_recommended_array[student_index])
            



## deepseek DFS node search
def find_students_2(N, M, recommendation_pairs):
    if N == 1:
        return 0
    
    # Initialize adjacency list
    adj = [[] for _ in range(N+1)]
    for a, b in recommendation_pairs:
        adj[b].append(a)
    
    # Function to perform DFS and find all reachable nodes
    def dfs(start, visited):
        stack = [start]
        while stack:
            node = stack.pop()
            for neighbor in adj[node]:
                if neighbor != start  and neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
    
    # Count students recommended by every other student
    student_count = 0
    for i in range(1, N+1):
        visited = set()
        dfs(i, visited)
        if len(visited) == N-1:
            student_count += 1
    
    return student_count

def test():
    assert find_students_2(3,3,[[1,2],[2,3],[1,3],[3,2]]) == 2