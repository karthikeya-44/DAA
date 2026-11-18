# Breadth First Search (BFS)

## Time Complexity of Breadth First Search Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(V + E)** | The BFS traversal visits the vertices and checks the edges of the graph. |
| **Average Case** | **O(V + E)** | Each vertex is visited once, and each edge is checked during the traversal. |
| **Worst Case** | **O(V + E)** | BFS may need to visit all `V` vertices and examine all `E` edges in the graph. |

> **Where:**

> - `V` = Number of vertices
> - `E` = Number of edges

---

## Space Complexity

- **O(V)** → The `visited` set stores the vertices that have already been visited.

- **O(V)** → The `queue` can contain up to `V` vertices in the worst case.

- **O(V + E)** → The `graph` dictionary stores all vertices and their adjacency lists.

- Therefore, the **overall space complexity is O(V + E)**.

- The **auxiliary space complexity** used by BFS for `visited` and `queue` is **O(V)**.

---

## Conclusion

The **Breadth First Search (BFS)** algorithm is used to traverse a graph **level by level**. In this program, the graph is represented using an **adjacency list**, and Python's `deque` is used as a queue.

The program starts from the given starting vertex, marks it as visited, and adds it to the queue. It then removes vertices from the front of the queue and visits their unvisited neighbouring vertices.

The algorithm has **O(V + E)** time complexity in the **best, average, and worst cases**, because each vertex is visited once and each edge is examined during the traversal.

The overall space complexity is **O(V + E)** because the graph itself requires space for vertices and edges, while the auxiliary space required by the `visited` set and queue is **O(V)**.

BFS is commonly used for **graph traversal, finding the shortest path in an unweighted graph, level-order traversal, and checking connectivity**.