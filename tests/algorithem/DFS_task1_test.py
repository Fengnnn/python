
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