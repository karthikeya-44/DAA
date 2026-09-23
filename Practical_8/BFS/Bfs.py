from collections import deque

graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    graph[i] = list(map(int, input(f"Enter neighbours of {i}: ").split()))

start = int(input("Enter starting vertex: "))

visited = set()
queue = deque([start])
visited.add(start)

print("BFS:", end=" ")

while queue:
    node = queue.popleft()
    print(node, end=" ")

    for x in graph[node]:
        if x not in visited:
            visited.add(x)
            queue.append(x)