import heapq

def prims(graph, n):
    visited = [False] * n
    pq = [(0, 0)]
    cost = 0

    while pq:
        weight, u = heapq.heappop(pq)

        if visited[u]:
            continue
        else:
            visited[u] = True
            cost += weight

            for v, w in graph[u]:
                if not visited[v]:
                    heapq.heappush(pq, (w, v))

    if all(visited):
        print("Minimum cost:", cost)
    else:
        print("Graph is not connected")


n = int(input("Enter number of vertices: "))
graph = [[] for i in range(n)]

e = int(input("Enter number of edges: "))

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

prims(graph, n)