##  Time Complexity of Binary Search

| Case          | Complexity | Description                                                                 |
|---------------|------------|-----------------------------------------------------------------------------|
| **Best Case** | **O(1)**   | The target element is found immediately at the middle index in the first comparison. |
| **Average Case** | **O(log n)** | The search space is halved at each step, so the number of comparisons grows logarithmically with the size of the list. |
| **Worst Case** | **O(log n)** | Even if the element is at the extreme ends or not present, the algorithm still halves the search space until it is exhausted. |

---

##  Space Complexity
- **Iterative Implementation:** **O(1)** → Only a constant amount of extra memory is used (variables like `left`, `right`, and `mid`).  
- **Recursive Implementation:** **O(log n)** → Extra memory is used in the call stack due to recursive function calls.

---

##  Conclusion
Binary Search is a highly efficient searching algorithm that works only on sorted lists. By repeatedly dividing the search space in half, it quickly narrows down the possible location of the target element. Compared to Linear Search, Binary Search drastically reduces the number of comparisons, achieving logarithmic time complexity. This makes it ideal for large datasets where speed is important.
