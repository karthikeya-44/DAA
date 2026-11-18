## Time Complexity of 0/1 Knapsack Dynamic Programming Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(n × W)** | The program fills the entire DP table for all `n` items and every capacity from `1` to `W`, regardless of the item weights or values. |
| **Average Case** | **O(n × W)** | For each of the `n` items, the program checks all `W` possible capacities and performs constant-time operations such as comparison and `max()`. |
| **Worst Case** | **O(n × W)** | The nested loops execute `n × W` times, where `n` is the number of items and `W` is the knapsack capacity. |

> **Where:**  
> `n` = Number of items  
> `W` = Capacity of the knapsack

---

## Space Complexity

- **O(n × W)** → The program creates a 2D DP table `dp` with **`n + 1` rows** and **`W + 1` columns**.
- The `weights` and `values` lists require **O(n)** additional space.
- Therefore, the **overall space complexity is O(n × W)** because the DP table requires the most memory.

---

## Conclusion

The **0/1 Knapsack Problem** is solved using **Dynamic Programming** in this program. A 2D DP table is created where `dp[i][w]` represents the **maximum value that can be obtained using the first `i` items with a knapsack capacity of `w`**.

For every item and capacity, the program decides whether to **include or exclude the item** and stores the maximum possible value.

The algorithm has **O(n × W)** time complexity in the **best, average, and worst cases**, because it fills every cell of the DP table. Its space complexity is **O(n × W)** because of the 2D DP table.

This Dynamic Programming approach is more efficient than the simple recursive approach because it avoids solving the same subproblems repeatedly by **storing previously calculated results**.