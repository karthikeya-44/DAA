##  Time Complexity of Bubble Sort

| Case          | Complexity | Description                                                                 |
|---------------|------------|-----------------------------------------------------------------------------|
| **Best Case** | **O(n)**   | If the array is already sorted, only one pass is needed with no swaps.      |
| **Average Case** | **O(n²)** | For a randomly ordered array, multiple passes and swaps are required.       |
| **Worst Case** | **O(n²)** | If the array is sorted in reverse order, the algorithm performs the maximum number of comparisons and swaps. |

---

##  Space Complexity
- **O(1)** → Bubble Sort is an **in-place sorting algorithm**, requiring only a constant amount of extra memory.

---

##  Conclusion
Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. While it is simple to implement and useful for learning the basics of sorting, its quadratic time complexity makes it inefficient for large datasets. It is best suited for small lists or as an introductory example of sorting algorithms.
