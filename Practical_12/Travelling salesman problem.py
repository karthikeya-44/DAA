def tsp(graph, n):
    visited = [False] * n
    visited[0] = True

    def solve(city, count, cost):
        if count == n:
            if graph[city][0] != 999:
                return cost + graph[city][0]
            return float('inf')

        ans = float('inf')

        for i in range(n):
            if not visited[i] and graph[city][i] != 999:
                visited[i] = True
                ans = min(ans, solve(i, count + 1,
                                     cost + graph[city][i]))
                visited[i] = False

        return ans

    return solve(0, 1, 0)


n = int(input("Enter number of cities: "))

graph = []

print("Enter cost matrix (use 999 for no path):")

for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

result = tsp(graph, n)

if result == float('inf'):
    print("No possible tour")
else:
    print("Minimum travelling cost:", result)