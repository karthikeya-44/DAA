graph = {}

n = int(input("Enter number of vertices: "))

for i in range(n):
    graph[i] = list(map(int, input(f"Enter neighbours of {i}: ").split()))

start = int(input("Enter starting vertex: "))

visited = set()
stack = [start]
visited.add(start)

print("DFS:", end=" ")

while stack:
    node = stack.pop()
    print(node, end=" ")

    for x in reversed(graph[node]):
        if x not in visited:
            visited.add(x)
            stack.append(x)