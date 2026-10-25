# Floyd–Warshall Algorithm

## Time Complexity of Floyd–Warshall Algorithm

| Case             | Complexity | Description                                                                                                                                    |
| ---------------- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Best Case**    | **O(V³)**  | The algorithm executes three nested loops to check all possible intermediate vertices and pairs of source and destination vertices.            |
| **Average Case** | **O(V³)**  | For every intermediate vertex, the algorithm checks all pairs of vertices and updates their shortest distances if a shorter path is found.     |
| **Worst Case**   | **O(V³)**  | The algorithm performs all iterations of the three nested loops, checking every combination of intermediate, source, and destination vertices. |

> **Where:**

> * `V` = Number of vertices in the graph

---

## Space Complexity

* **O(V²)** → The adjacency matrix `a` stores the distances between all pairs of vertices.
* **O(1)** → The algorithm uses only a constant amount of additional space for the loop variables `i`, `j`, and `k`.
* Therefore, the **overall space complexity is O(V²)** because the adjacency matrix requires quadratic space.
* The **auxiliary space complexity is O(1)** because the algorithm updates the existing adjacency matrix without creating another matrix.

---

## Conclusion

The **Floyd–Warshall algorithm** is used to find the **shortest distances between all pairs of vertices** in a weighted graph. In this program, the graph is represented using an **adjacency matrix**, where each element represents the distance between two vertices.

The program first accepts the number of vertices and the adjacency matrix as input. It then uses three nested loops to consider every vertex as an intermediate vertex between each pair of source and destination vertices.

For each pair of vertices, the algorithm compares the existing distance with the distance obtained by travelling through the intermediate vertex. If the new path is shorter, the distance matrix is updated with the minimum value.

The algorithm has **O(V³)** time complexity in the **best, average, and worst cases** because it executes three nested loops over the vertices.

The overall space complexity is **O(V²)** because the adjacency matrix stores distances between all pairs of vertices, while the auxiliary space complexity is **O(1)**.

The Floyd–Warshall algorithm is commonly used for **all-pairs shortest paths, network routing, finding shortest distances between cities, and detecting negative-weight cycles**. However, the input matrix must represent unreachable vertices appropriately, and negative-weight cycles can be detected by checking whether any diagonal entry becomes negative after the algorithm finishes.
