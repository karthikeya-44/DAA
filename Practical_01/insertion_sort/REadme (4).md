##  Time Complexity of Insertion Sort

| Case          | Complexity | Description                                                                 |
|---------------|------------|-----------------------------------------------------------------------------|
| **Best Case** | **O(n)**   | If the array is already sorted, only one comparison per element is needed.  |
| **Average Case** | **O(n²)** | For a randomly ordered array, elements are shifted multiple times.          |
| **Worst Case** | **O(n²)** | If the array is sorted in reverse order, every new element must be compared and shifted through the entire sorted portion. |

---

##  Space Complexity
- **O(1)** → Insertion Sort is an **in-place sorting algorithm**, requiring only a constant amount of extra memory.

---

##  Conclusion
Insertion Sort is a simple and intuitive sorting algorithm that works by building a sorted portion of the list one element at a time. It is efficient for small datasets and nearly sorted arrays, with a best-case time complexity of O(n). However, for larger or completely unsorted datasets, its performance degrades to O(n²). Writing and running this program helped me understand how shifting elements can gradually place each value in its correct position, making it a useful algorithm for learning the fundamentals of sorting in Python.
