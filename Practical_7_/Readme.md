# Coin Change using Dynamic Programming

## Time Complexity of Coin Change Dynamic Programming Program

| Case | Complexity | Description |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case** | **O(n × A)** | The program checks every amount from `1` to `A` and compares it with all `n` coin denominations. |
| **Average Case** | **O(n × A)** | For each amount, the program checks all available coins to find the minimum number of coins required. |
| **Worst Case** | **O(n × A)** | The nested loops run for all `A` amounts and all `n` coins, resulting in approximately `n × A` operations. |

> **Where:**
> - `n` = Number of coin denominations
> - `A` = Target amount

---

## Space Complexity

- **O(A)** → The program creates a 1D DP array `dp` of size `amount + 1` to store the minimum number of coins required for each amount.

- The `coins` list requires **O(n)** additional space to store the coin denominations.

- Therefore, the **overall space complexity is O(A + n)**.

- If we consider the DP array as the main extra space, the space complexity is commonly stated as **O(A)**.

---

## Conclusion

The **Coin Change Problem** is solved using **Dynamic Programming** in this program. A 1D DP array is created where `dp[i]` represents the **minimum number of coins required to make amount `i`**.

For every amount from `1` to the target amount, the program checks all available **coin denominations** and selects the option that results in the minimum number of coins.

The algorithm has **O(n × A)** time complexity in the **best, average, and worst cases**, because it checks every coin for every possible amount. Its overall space complexity is **O(A + n)**, or **O(A)** when focusing on the DP array.

This Dynamic Programming approach is more efficient than a simple recursive approach because it **stores previously calculated results** and avoids solving the same subproblems repeatedly. It helps find the **minimum number of coins required to make the given amount**.