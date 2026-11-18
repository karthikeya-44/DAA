##  Time Complexity of Selection Sort

| Case          | Complexity | Description                                                                 |
|---------------|------------|-----------------------------------------------------------------------------|
| **Best Case** | **O(n²)**  | Even if the array is already sorted, Selection Sort still scans the entire list to find the minimum element in each pass. |
| **Average Case** | **O(n²)** | For a randomly ordered array, the algorithm performs nested loops to repeatedly find the minimum element. |
| **Worst Case** | **O(n²)** | If the array is sorted in reverse order, the algorithm still performs the maximum number of comparisons. |

---

##  Space Complexity
- **O(1)** → Selection Sort is an **in-place sorting algorithm**, requiring only a constant amount of extra memory.

---

##  Conclusion
Selection Sort works by repeatedly finding the minimum element from the unsorted portion of the list and placing it at the beginning. While it is simple to implement and requires fewer swaps compared to Bubble Sort, its quadratic time complexity makes it inefficient for large datasets. It is mainly useful for small lists or as a teaching example to understand basic sorting concepts.
