# Coin Change using Dynamic Programming

## Time Complexity of Coin Change Dynamic Programming Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(n × N)** | The program fills the complete DP table by checking every coin denomination for every amount from `1` to `N`. |
| **Average Case** | **O(n × N)** | For each coin denomination, the program processes every amount from `1` to `N` to calculate the number of possible ways. |
| **Worst Case** | **O(n × N)** | The nested loops run for all `n` coin denominations and all `N` possible amounts, resulting in approximately `n × N` operations. |

> **Where:**

> - `n` = Number of coin denominations
> - `N` = Target amount

---

## Space Complexity

- **O(n × N)** → The program creates a 2D DP table `dp` with `(n + 1) × (N + 1)` entries.

- The `coins` list requires **O(n)** additional space to store the coin denominations.

- Therefore, the **overall space complexity is O(n × N + n)**.

- Since `O(n × N)` dominates `O(n)`, the overall space complexity is commonly stated as **O(n × N)**.

---

## Conclusion

The **Coin Change Problem** is solved using **Dynamic Programming** in this program. A 2D DP table is created where `dp[i][j]` represents the **number of ways to make amount `j` using the first `i` coin denominations**.

For every coin denomination and every possible amount, the program considers two possibilities: **not using the current coin** and **using the current coin**. The results of these two possibilities are added to calculate the total number of ways.

The algorithm has **O(n × N)** time complexity in the **best, average, and worst cases**, because the complete DP table is processed. Its overall space complexity is **O(n × N)** because a 2D DP table is used.

This Dynamic Programming approach is efficient because it **stores previously calculated results** and avoids repeatedly solving the same subproblems. The program calculates the **total number of different combinations of coins that can be used to make the given target amount**.