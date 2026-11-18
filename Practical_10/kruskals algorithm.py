def kruskal(n, edges):
    parent = [i for i in range(n)]
    cost = 0

    def find(i):
        if parent[i] != i:
            parent[i] = find(parent[i])
        return parent[i]

    edges.sort()

    for w, u, v in edges:
        root_u = find(u)
        root_v = find(v)

        if root_u != root_v:
            parent[root_u] = root_v
            cost += w
            print(u, "-", v, ":", w)

    return cost


n = int(input("Enter number of vertices: "))

e = int(input("Enter number of edges: "))

edges = []

for i in range(e):
    u, v, w = map(int, input("Enter edge (u v weight): ").split())
    edges.append((w, u, v))

print("Minimum Spanning Tree:")
print("Minimum cost:", kruskal(n, edges))