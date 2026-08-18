## Time Complexity of Recursive Factorial Program

| Case             | Complexity | Description                                                                                                                                            |
| ---------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Best Case**    | **O(1)**   | When `n` is **0 or 1**, the base condition is satisfied immediately, so no recursive calls are made.                                                   |
| **Average Case** | **O(n)**   | For a typical positive value of `n`, the function makes recursive calls until it reaches the base case, resulting in approximately `n` function calls. |
| **Worst Case**   | **O(n)**   | For a positive value of `n`, the function recursively calls itself `n` times before reaching the base case.                                            |

---

## Space Complexity

* **O(n)** → The recursive function creates a new function call for each value from `n` down to `1`. These calls are stored in the **recursion call stack**, requiring **O(n)** auxiliary space.

---

## Conclusion

The Recursive Factorial Program calculates the factorial of a given number using **recursion**. The function repeatedly calls itself with `n - 1` until it reaches the base case, where `n` is either **0 or 1**. The algorithm has **O(n)** time complexity in the average and worst cases because it performs one recursive call for each value of `n`. Its space complexity is **O(n)** due to the recursion call stack. Although recursion makes the program simple and easy to understand, it requires more memory than the iterative factorial approach, which uses **O(1)** auxiliary space.
