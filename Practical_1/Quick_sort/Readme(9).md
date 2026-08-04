## Time Complexity of Quick Sort

| Case | Complexity | Description |
|------|------------|-------------|
| **Best Case** | **O(n log n)** | The pivot divides the array into two nearly equal halves at each step. |
| **Average Case** | **O(n log n)** | On average, the pivot creates balanced partitions, leading to efficient sorting. |
| **Worst Case** | **O(n²)** | If the pivot is always the smallest or largest element (e.g., already sorted array with poor pivot selection), the partitions become highly unbalanced. |

---

## Space Complexity

- **O(log n)** → Due to the recursive function calls in the average case.
- **Worst Case:** **O(n)** → When recursion becomes unbalanced because of poor pivot selection.

---

## Conclusion

Quick Sort is a **divide-and-conquer** sorting algorithm that selects a pivot element and partitions the array into smaller and larger elements before recursively sorting the partitions. It is one of the fastest sorting algorithms in practice due to its average **O(n log n)** time complexity and low memory usage. However, its worst-case time complexity is **O(n²)**, which can be reduced by choosing a good pivot (such as a random or median pivot).