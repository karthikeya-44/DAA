## Time Complexity of Travelling Salesperson Problem (TSP) Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(n!)** | The algorithm explores possible city combinations to find the minimum travelling cost. |
| **Average Case** | **O(n!)** | The algorithm explores different possible paths by visiting each unvisited city recursively. |
| **Worst Case** | **O(n!)** | The algorithm explores all possible permutations of the remaining cities to find the minimum-cost tour. |

> **Where:**  
> `n` = Number of cities

---

## Space Complexity

- **O(n)** → The program creates a `visited` list to keep track of visited cities.
- The recursive `solve()` function uses **O(n)** stack space because the maximum recursion depth is `n`.
- The `graph` adjacency matrix requires **O(n × n)** space.
- Therefore, the **overall space complexity is O(n²)**, including the graph matrix.

---

## Conclusion

The **Travelling Salesperson Problem (TSP)** is solved using the **Brute Force (Backtracking) Approach** in this program to find the minimum travelling cost.

The program starts from city `0` and recursively explores all possible paths by visiting every city exactly once. After visiting all cities, it checks whether a path exists back to the starting city.

The `visited` list keeps track of visited cities and prevents visiting the same city more than once. The program uses `999` to represent the absence of a direct path between two cities.

The algorithm has **O(n!)** time complexity in the best, average, and worst cases because it explores all possible permutations of the cities.

Its overall space complexity is **O(n²)** because of the adjacency matrix, visited list, and recursive function calls.

This approach guarantees the minimum travelling cost by checking all possible valid tours, but it becomes inefficient for a large number of cities because of its factorial time complexity.