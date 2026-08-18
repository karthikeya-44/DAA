## Time Complexity of Factorial Program

| Case             | Complexity | Description                                                                                                    |
| ---------------- | ---------- | -------------------------------------------------------------------------------------------------------------- |
| **Best Case**    | **O(n)**   | The `for` loop executes **n times**, performing one multiplication during each iteration.                      |
| **Average Case** | **O(n)**   | For any positive value of `n`, the loop runs exactly **n times**, so the time complexity is linear.            |
| **Worst Case**   | **O(n)**   | The loop executes **n iterations**, and each iteration performs a constant-time multiplication and assignment. |

---

## Space Complexity

* **O(1)** → The program uses only a constant amount of extra memory for variables such as `n`, `factorial`, and `i`. Therefore, the auxiliary space complexity is **O(1)**.

> **Note:** The factorial value itself can become very large as `n` increases, so actual integer storage can grow. In the usual algorithm-analysis model, this program is considered **O(1)** auxiliary space.

---

## Conclusion

The Factorial Program calculates the factorial of a given number `n` by initializing `factorial` to **1** and repeatedly multiplying it by every integer from **1 to n** using a `for` loop. The program has a **linear time complexity of O(n)** because the loop executes `n` times. It requires **O(1) auxiliary space** because only a fixed number of variables are used. Therefore, this is a simple and efficient iterative approach for calculating the factorial of a number.
