# Depth First Search (DFS)

## Time Complexity of Depth First Search Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(V + E)** | The DFS traversal visits the vertices and checks the edges of the graph. |
| **Average Case** | **O(V + E)** | Each vertex is visited once, and each edge is checked during the traversal. |
| **Worst Case** | **O(V + E)** | DFS may need to visit all `V` vertices and examine all `E` edges in the graph. |

> **Where:**
>
> - `V` = Number of vertices
> - `E` = Number of edges

---

## Space Complexity

- **O(V)** → The `visited` set stores the vertices that have already been visited.

- **O(V)** → The `stack` can contain up to `V` vertices in the worst case.

- **O(V + E)** → The `graph` dictionary stores all vertices and their adjacency lists.

- Therefore, the **overall space complexity is O(V + E)**.

- The **auxiliary space complexity** used by DFS for the `visited` set and `stack` is **O(V)**.

---

## Conclusion

The **Depth First Search (DFS)** algorithm is used to traverse a graph by going **as deep as possible before backtracking**. In this program, the graph is represented using an **adjacency list**, and a Python list is used as a **stack**.

The program starts from the given starting vertex, marks it as visited, and adds it to the stack. It then removes a vertex from the top of the stack and visits its unvisited neighbouring vertices.

The algorithm has **O(V + E)** time complexity in the **best, average, and worst cases**, because each vertex is visited once and each edge is examined during the traversal.

The overall space complexity is **O(V + E)** because the graph itself requires space for vertices and edges, while the auxiliary space required by the `visited` set and stack is **O(V)**.

DFS is commonly used for **graph traversal, finding connected components, detecting cycles, solving mazes, path finding, and topological sorting**.