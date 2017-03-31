# ctci 4.1
from collections import deque, defaultdict

def bfs(adjlist, a, b):
    queue = deque(a)
    visited = defaultdict(int)
    while len(queue):
        current = queue.popleft()
        visited[current] += 1
        for item in adjlist[current]:
            if item not in visited:
                queue.append(item)
            if current == b:
                return True
    return True
