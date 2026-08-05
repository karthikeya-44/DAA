## Time Complexity of Heap Sort (Max Heap)

| Case | Complexity | Description |
|------|------------|-------------|
| **Best Case** | **O(n log n)** | Building the max heap takes **O(n)** time, and each of the **n** elements is removed from the heap with heapify operations taking **O(log n)**. |
| **Average Case** | **O(n log n)** | For a randomly ordered array, Heap Sort maintains the heap property after every extraction, resulting in **O(log n)** work per element. |
| **Worst Case** | **O(n log n)** | Even in the worst case, Heap Sort performs heapify operations after every extraction, ensuring the time complexity remains **O(n log n)**. |

---

## Space Complexity
- **O(1)** → Heap Sort is an **in-place sorting algorithm**. It requires only a constant amount of extra memory for swapping elements and maintaining the heap.

---

## Conclusion
Heap Sort (Max Heap) works by first building a **max heap** from the input array and then repeatedly swapping the root (largest element) with the last element of the heap, followed by restoring the heap property using heapify. It guarantees **O(n log n)** time complexity in the best, average, and worst cases, making it more efficient than quadratic sorting algorithms like Bubble Sort and Selection Sort for large datasets. Since it is an **in-place** algorithm and does not require additional memory, Heap Sort is a reliable choice when consistent performance and low memory usage are important.