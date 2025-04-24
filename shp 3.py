from collections import deque

def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited = {start: None}
    backward_visited = {goal: None}

    while forward_queue and backward_queue:
        if forward_queue:
            meeting_node = expand_search(graph, forward_queue, forward_visited, backward_visited)
            if meeting_node:
                return reconstruct_path(forward_visited, backward_visited, meeting_node)

        if backward_queue:
            meeting_node = expand_search(graph, backward_queue, backward_visited, forward_visited)
            if meeting_node:
                return reconstruct_path(forward_visited, backward_visited, meeting_node)

    return None

def expand_search(graph, queue, visited, opposite_visited):
    current = queue.popleft()
    for neighbor in graph[current]:
        if neighbor not in visited:
            visited[neighbor] = current
            queue.append(neighbor)
            if neighbor in opposite_visited:
                return neighbor
    return None

def reconstruct_path(forward_visited, backward_visited, meeting_node):
    path = []
    node = meeting_node

    # Reconstruct forward path
    while node is not None:
        path.append(node)
        node = forward_visited[node]
    path.reverse()

    # Reconstruct backward path (skip meeting_node to avoid duplicate)
    node = backward_visited[meeting_node]
    while node is not None:
        path.append(node)
        node = backward_visited[node]

    return path

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

start = 'A'
goal = 'H'
path = bidirectional_search(graph, start, goal)
print("Shortest Path:", path)
