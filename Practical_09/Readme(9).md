# Prim's Algorithm

## Time Complexity

| Case             | Complexity     | Description                                                         |
| ---------------- | -------------- | ------------------------------------------------------------------- |
| **Best Case**    | **O(E log E)** | Priority queue operations process the graph's edges.                |
| **Average Case** | **O(E log E)** | Edges are processed using a priority queue.                         |
| **Worst Case**   | **O(E log E)** | All edges may be inserted into and removed from the priority queue. |

> **Where:**
>
> * `V` = Number of vertices
> * `E` = Number of edges

---

## Space Complexity

* **O(V + E)** → Stores the graph using an adjacency list.
* **O(E)** → Priority queue may store edges.
* **Overall Space Complexity: O(V + E)**

---

## Conclusion

**Prim's algorithm** finds the Minimum Spanning Tree (MST) of a connected, weighted, undirected graph. It uses a **priority queue** to select the minimum-weight edge and gradually connects all vertices with minimum total cost.

The time complexity is **O(E log E)**, and the overall space complexity is **O(V + E)**. It is commonly used in **network design, road connections, and cable installation**.
