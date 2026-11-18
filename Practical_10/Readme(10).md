## Time Complexity of Kruskal's Algorithm Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(E log E)** | The program sorts all `E` edges in ascending order of weight. The `find()` operation with path compression takes nearly constant amortized time. |
| **Average Case** | **O(E log E)** | The program sorts all edges and checks each edge to determine whether it forms a cycle. Sorting takes the maximum time. |
| **Worst Case** | **O(E log E)** | All `E` edges are sorted, and the program performs `find()` operations for every edge. The overall complexity is dominated by sorting. |

> **Where:**  
> `V` = Number of vertices  
> `E` = Number of edges

---

## Space Complexity

- **O(V)** → The program creates a `parent` list to store the parent of each vertex.
- The `find()` function uses path compression to optimize searching.
- The `edges` list requires **O(E)** space to store all edges.
- Python's sorting operation may require additional temporary space.
- Therefore, the **overall space complexity is O(V + E)**, including the input edge list.

---

## Conclusion

The **Kruskal's Algorithm** is implemented using the **Greedy Approach** to find the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph.

The program first sorts all edges in ascending order of their weights. It then selects the smallest-weight edge and checks whether adding it creates a cycle using the **Disjoint Set (Union-Find)** technique with path compression.

If the edge does not form a cycle, it is added to the Minimum Spanning Tree, and its weight is added to the total cost.

The algorithm has **O(E log E)** time complexity in the best, average, and worst cases because sorting the edges dominates the execution time.

Its overall space complexity is **O(V + E)** because of the parent list and edge list.

Kruskal's Algorithm efficiently finds the Minimum Spanning Tree by selecting the minimum-weight edges without forming cycles.