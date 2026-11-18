## Time Complexity of Merge Sort

| Case | Complexity | Description |
|------|------------|-------------|
| **Best Case** | **O(n log n)** | The array is divided into halves and merged efficiently, regardless of its initial order. |
| **Average Case** | **O(n log n)** | Every division and merging step processes all elements, resulting in logarithmic levels of recursion. |
| **Worst Case** | **O(n log n)** | Even for the most unsorted array, Merge Sort always divides and merges the array in the same way. |

---

## Space Complexity

- **O(n)** → Merge Sort requires an additional temporary array to merge the divided subarrays, so it is **not an in-place sorting algorithm**.

---

## Conclusion

Merge Sort is a **divide-and-conquer** sorting algorithm that recursively divides the array into smaller halves, sorts each half, and then merges them into a sorted array. It provides a consistent **O(n log n)** time complexity in all cases, making it efficient for large datasets. However, it requires extra memory for merging, which increases its space complexity.