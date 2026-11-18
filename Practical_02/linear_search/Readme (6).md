##  Time Complexity of Linear Search

| Case          | Complexity | Description                                                                 |
|---------------|------------|-----------------------------------------------------------------------------|
| **Best Case** | **O(1)**   | The target element is found at the very first position.                      |
| **Average Case** | **O(n)** | The target element is somewhere in the middle, requiring about half the elements to be checked. |
| **Worst Case** | **O(n)** | The target element is at the last position or not present at all, requiring all elements to be checked. |

---

## Space Complexity
- **O(1)** → Linear Search uses only a constant amount of extra memory (for variables like index and target).  
- No additional data structures are required, and the search is performed directly on the given list.

---

##  Conclusion
Linear Search is the most straightforward searching technique, where each element is checked one by one until the target is found or the list ends. While it is easy to implement and works well for small or unsorted datasets, its performance is limited because the time complexity grows linearly with the size of the list. This makes it inefficient for large datasets compared to Binary Search, but it remains a useful starting point for understanding search algorithms in Python.
