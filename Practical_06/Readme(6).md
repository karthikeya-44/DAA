# Chain Matrix Multiplication using Dynamic Programming

## Time Complexity of Chain Matrix Multiplication Dynamic Programming Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(n³)** | The program considers all possible ways to split the chain of `n` matrices and calculates the minimum multiplication cost. |
| **Average Case** | **O(n³)** | For each chain length and starting position, the program checks all possible split points to find the minimum cost. |
| **Worst Case** | **O(n³)** | The nested loops over chain length, starting position, and split position result in approximately `n³` operations. |

> **Where:** 
> `n` = Number of matrices in the chain

---

## Space Complexity

- **O(n²)** → The program creates a 2D DP table `dp` with **`n × n` entries** to store the minimum multiplication cost for different matrix chains.
- The `dimensions` list requires **O(n)** additional space.
- Therefore, the **overall space complexity is O(n²)** because the DP table requires the most memory.

---

## Conclusion

The **Chain Matrix Multiplication Problem** is solved using **Dynamic Programming** in this program. A 2D DP table is created where `dp[i][j]` represents the **minimum number of scalar multiplications required to multiply matrices from `i` to `j`**.

For every possible matrix chain, the program considers different **split positions** and selects the one that gives the minimum multiplication cost.

The algorithm has **O(n³)** time complexity in the **best, average, and worst cases**, because it checks all possible combinations of matrix chains and split positions. Its space complexity is **O(n²)** because of the 2D DP table.

This Dynamic Programming approach is more efficient than the simple recursive approach because it **stores previously calculated results** and avoids solving the same subproblems repeatedly. It helps find the **optimal order of matrix multiplication** with the minimum number of scalar multiplications.