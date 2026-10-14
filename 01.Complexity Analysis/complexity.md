# 📊 Complexity Analysis — DSA Notes

A comprehensive revision guide to **Time Complexity, Space Complexity, Nested Loops, Recursive Complexity, and Complexity Comparison** with Python implementations.

These notes are designed for quick revision, understanding code behavior, analyzing algorithm efficiency, and preparing for coding interviews.

---

## 📁 Folder Structure

```text
01.Complexity Analysis/
├── README.md
├── 01_time_complexity.py
├── 02_space_complexity.py
├── 03_nested_loops.py
├── 04_recursive_complexity.py
└── 05_complexity_comparison.py
```

## 📚 Table of Contents

1. [Introduction to Complexity Analysis](#1-introduction-to-complexity-analysis)
2. [Big-O Notation](#2-big-o-notation)
3. [Time Complexity](#3-time-complexity)
4. [Space Complexity](#4-space-complexity)
5. [Nested Loops](#5-nested-loops)
6. [Recursive Complexity](#6-recursive-complexity)
7. [Complexity Comparison](#7-complexity-comparison)
8. [Important Python Code Patterns](#8-important-python-code-patterns)
9. [Common Mistakes](#9-common-mistakes)
10. [Quick Revision Sheet](#10-quick-revision-sheet)
11. [Practice Questions](#11-practice-questions)

---

# 1. Introduction to Complexity Analysis

Complexity analysis helps us understand how an algorithm's resource requirements grow as the input size increases.

The two primary types are:

- **Time Complexity:** How the number of operations grows with input size.
- **Space Complexity:** How much memory an algorithm requires as input size grows.

Here, `n` usually represents the size of the input.

### Why is it important?

Suppose two algorithms solve the same problem:

- Algorithm A performs approximately `n` operations.
- Algorithm B performs approximately `n²` operations.

For small inputs, both might work well. For large inputs, Algorithm A generally scales much better.

Complexity analysis helps us choose efficient algorithms without depending on a particular computer's speed.

**Remember:** Big-O describes growth, not the exact number of seconds an algorithm takes.

---

# 2. Big-O Notation

Big-O notation describes an upper bound on an algorithm's asymptotic growth. In introductory DSA, it is commonly used to express how time or space requirements scale with input size.

## 2.1 Common Complexity Classes

| Complexity | Name | Example |
|---|---|---|
| `O(1)` | Constant | Accessing an array element |
| `O(log n)` | Logarithmic | Binary search |
| `O(n)` | Linear | Traversing an array |
| `O(n log n)` | Linearithmic | Merge sort |
| `O(n²)` | Quadratic | Comparing every pair |
| `O(n³)` | Cubic | Three full nested loops |
| `O(2ⁿ)` | Exponential | Naive recursive Fibonacci |
| `O(n!)` | Factorial | Generating all permutations |

A useful growth comparison is:

```text
O(1)
  <
O(log n)
  <
O(n)
  <
O(n log n)
  <
O(n²)
  <
O(n³)
  <
O(2ⁿ)
  <
O(n!)
```

This ordering is for sufficiently large `n`; actual runtime also depends on implementation, constants, and hardware.

## 2.2 Rules for Simplifying Big-O

### Rule 1: Ignore constant factors

```python
for i in range(n):
    print(i)
```

Complexity: `O(n)`

Even if the loop performs a constant amount of extra work per iteration, its complexity remains `O(n)`.

### Rule 2: Keep the dominant term

```python
for i in range(n):
    print(i)

for j in range(n * n):
    print(j)
```

Total work:

```text
O(n) + O(n²) = O(n²)
```

The quadratic term dominates.

### Rule 3: Sequential loops add

```python
for i in range(n):
    pass

for j in range(n):
    pass
```

Total: `O(n + n) = O(n)`.

### Rule 4: Independent nested loops multiply

```python
for i in range(n):
    for j in range(n):
        pass
```

Total: `O(n × n) = O(n²)`.

### Rule 5: Repeated division or multiplication often gives logarithmic growth

```python
while n > 1:
    n //= 2
```

The value is halved each iteration, so the number of iterations is `O(log n)`.

---

# 3. Time Complexity

**File:** `01_time_complexity.py`

This file demonstrates common time complexity classes through Python functions.

## 3.1 Constant Time — O(1)

```python
def constant_time(arr):
    return arr[0] if arr else None
```

**How it works:**

- Checks whether the list is empty.
- If not empty, returns the first element.
- Does not traverse the list.

**Why `O(1)`?**

The number of operations does not grow with the list length.

The empty-list check also prevents an `IndexError` when the input is empty.

**Example:**

```python
constant_time([10, 20, 30])
# Output: 10

constant_time([])
# Output: None
```

- Time: `O(1)`
- Auxiliary space: `O(1)`

## 3.2 Logarithmic Time — O(log n)

```python
def logarithmic_time(n):
    count = 0

    while n > 1:
        n //= 2
        count += 1

    return count
```

**How it works:**

Each iteration divides `n` by two using integer division.

For `n = 16`:

```text
16 → 8 → 4 → 2 → 1
```

There are four iterations.

**Why `O(log n)`?**

After `k` iterations, the value is approximately:

```text
n / 2ᵏ
```

The loop stops when the value becomes at most one. Therefore, the iteration count grows logarithmically.

- Time: `O(log n)`
- Auxiliary space: `O(1)`
- Assumption: `n` is a positive integer for the usual interpretation.

## 3.3 Linear Time — O(n)

```python
def linear_time(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

**How it works:**

The function visits every element once and adds it to `total`.

For `[2, 4, 6, 8]`:

```text
total = 0
total = 0 + 2
total = 2 + 4
total = 6 + 6
total = 12 + 8
```

Result: `20`.

If the list contains `n` elements, the loop performs `n` iterations.

- Time: `O(n)`
- Auxiliary space: `O(1)`

The returned sum is a single value; no additional list is created.

## 3.4 Linearithmic Time — O(n log n)

### Merge Sort

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
```

Merge sort uses the divide-and-conquer approach.

**Step 1 — Divide:** Split the list into two halves.

**Step 2 — Conquer:** Recursively sort each half.

**Step 3 — Combine:** Merge the sorted halves.

The `merge()` function performs the combining step:

```python
def merge(left, right):
    result, i, j = [], 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
```

The two pointers `i` and `j` track the current positions in the left and right lists.

When one list is exhausted, `extend()` appends the remaining elements from the other list.

**Example:**

```text
[3, 1, 4, 2]
       ↓
   [3, 1] [4, 2]
       ↓
 [1, 3] [2, 4]
       ↓
    [1, 2, 3, 4]
```

**Why `O(n log n)`?**

- The list is divided into approximately `log n` levels.
- Each level performs `O(n)` total merging work.

Therefore:

```text
O(n) × O(log n) = O(n log n)
```

- Time: `O(n log n)`
- Auxiliary space: `O(n)` for the merging lists, with additional recursion-stack space of `O(log n)`.

Python slicing also creates copies of the sublists, contributing to the extra space usage.

## 3.5 Quadratic Time — O(n²)

```python
def quadratic_time(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count
```

The outer loop runs `n` times.

For each outer iteration, the inner loop also runs `n` times.

Total iterations:

```text
n × n = n²
```

For `n = 5`, the function returns `25`.

- Time: `O(n²)`
- Auxiliary space: `O(1)`

Typical use cases include comparing every pair of elements and simple brute-force pair-search algorithms.

## 3.6 Exponential Time — O(2ⁿ)

```python
def exponential_time(n):
    if n <= 1:
        return n

    return exponential_time(n - 1) + exponential_time(n - 2)
```

This function calculates Fibonacci numbers recursively without memoization.

For example:

```text
F(4)
├── F(3)
│   ├── F(2)
│   └── F(1)
└── F(2)
    ├── F(1)
    └── F(0)
```

The same subproblems are solved repeatedly.

The recurrence is:

```text
T(n) = T(n - 1) + T(n - 2) + O(1)
```

Its tight asymptotic time complexity is `Θ(φⁿ)`, where `φ ≈ 1.618`. It is commonly described using the looser upper bound `O(2ⁿ)`.

- Time: `O(2ⁿ)` as a convenient upper bound.
- Auxiliary space: `O(n)` due to the maximum recursion depth.

**Important:** This is an inefficient implementation for large inputs.

## 3.7 Factorial Time — O(n!)

The function in this file is:

```python
def permutations_count(n):
    if n <= 1:
        return 1

    return n * permutations_count(n - 1)
```

Despite the function name, it calculates the factorial `n!`, rather than explicitly generating permutations.

For `n = 5`:

```text
5 × 4 × 3 × 2 × 1 = 120
```

- Time: `O(n)`
- Auxiliary space: `O(n)`

**Important distinction:** Computing `n!` takes linear time in this recursive implementation. Generating all permutations of `n` distinct elements generally requires factorial-scale work because there are `n!` permutations.

---

# 4. Space Complexity

**File:** `02_space_complexity.py`

Space complexity measures how memory requirements grow with input size.

In these notes, auxiliary space means additional working memory, excluding the input itself and the returned output unless explicitly stated otherwise.

## 4.1 Constant Auxiliary Space — O(1)

```python
def sum_array(arr):
    total = 0

    for x in arr:
        total += x

    return total
```

The function maintains only a running total and the current element reference.

It does not create another list or a data structure that grows with `n`.

- Time: `O(n)`
- Auxiliary space: `O(1)`

## 4.2 Linear Space — O(n)

```python
def double_array(arr):
    return [x * 2 for x in arr]
```

For every input element, a corresponding element is added to a new list.

For an input containing `n` elements, the result contains `n` elements.

- Time: `O(n)`
- Auxiliary space: `O(n)`

Example:

```python
double_array([1, 2, 3])
# Output: [2, 4, 6]
```

## 4.3 Recursive Stack Space — O(n)

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

The function calls itself with decreasing arguments.

For `factorial(4)`, the calls are:

```text
factorial(4)
    factorial(3)
        factorial(2)
            factorial(1)
```

The maximum recursion depth grows proportionally to `n`.

- Time: `O(n)`
- Auxiliary space: `O(n)`

Although each call performs constant additional work, all active calls occupy stack space until the recursion unwinds.

## 4.4 Quadratic Space — O(n²)

```python
def create_matrix(n):
    return [[0] * n for _ in range(n)]
```

The function creates a matrix containing `n` rows and `n` elements per row.

Total elements:

```text
n × n = n²
```

- Time: `O(n²)`
- Space: `O(n²)`

Example:

```python
create_matrix(3)
```

Output:

```text
[
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

Each row is created independently, so modifying one row does not modify the others.

## 4.5 Logarithmic Stack Space — O(log n)

The file implements recursive binary search:

```python
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)

    else:
        return binary_search(arr, target, low, mid - 1)
```

**How it works:**

1. Calculate the middle index.
2. Compare the middle element with the target.
3. Discard the half that cannot contain the target.
4. Repeat recursively on the remaining half.

For an array of eight elements, the search range can shrink as follows:

```text
8 → 4 → 2 → 1
```

- Time: `O(log n)`
- Auxiliary space: `O(log n)` for recursive calls.

**Prerequisite:** Binary search requires the array to be sorted in ascending order for this implementation.

---

# 5. Nested Loops

**File:** `03_nested_loops.py`

Nested loops are a fundamental pattern in complexity analysis. Their complexity depends on how many times each loop executes.

## 5.1 Two Full Nested Loops — O(n²)

```python
def nested_loops_n_squared(n):
    count = 0

    for i in range(n):
        for j in range(n):
            count += 1

    return count
```

Both loops run `n` times.

Total iterations:

```text
n × n = n²
```

For `n = 5`, the result is `25`.

## 5.2 Triangular Nested Loops — O(n²)

```python
def nested_loops_triangular(n):
    count = 0

    for i in range(n):
        for j in range(i, n):
            count += 1

    return count
```

Unlike the previous example, the inner loop starts at `i`.

The iteration counts are:

```text
i = 0 → n iterations
i = 1 → n - 1 iterations
i = 2 → n - 2 iterations
...
i = n - 1 → 1 iteration
```

Total:

```text
n + (n - 1) + ... + 1
= n(n + 1) / 2
```

Expanding:

```text
(n² + n) / 2
```

Ignoring constants and lower-order terms gives `O(n²)`.

For `n = 5`, the result is `15`.

**Remember:** Doing approximately half as many iterations does not change the Big-O class.

## 5.3 Three Full Nested Loops — O(n³)

```python
def nested_loops_n_cubed(n):
    count = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                count += 1

    return count
```

Each of the three loops runs `n` times.

Total iterations:

```text
n × n × n = n³
```

For `n = 3`, the result is `27`.

- Time: `O(n³)`
- Auxiliary space: `O(1)`

## 5.4 Nested Loop with Doubling — O(n log n)

```python
def log_nested(n):
    count = 0

    for i in range(n):
        j = 1

        while j < n:
            count += 1
            j *= 2

    return count
```

The outer loop runs `n` times.

The inner loop doubles `j` on each iteration:

```text
1 → 2 → 4 → 8 → 16 → ...
```

The inner loop executes `O(log n)` times.

Therefore:

```text
O(n) × O(log n) = O(n log n)
```

For `n = 8`, the outer loop runs eight times and the inner loop runs three times per outer iteration, giving `24`.

- Time: `O(n log n)`
- Auxiliary space: `O(1)`

### Nested Loop Revision Table

| Pattern | Complexity |
|---|---|
| One loop over `n` | `O(n)` |
| Two independent full loops, one nested in the other | `O(n²)` |
| Three independent full nested loops | `O(n³)` |
| Inner loop starts at the outer index | `O(n²)` |
| Inner loop doubles its counter | Depends on the outer loop; often `O(n log n)` |

---

# 6. Recursive Complexity

**File:** `04_recursive_complexity.py`

Recursive algorithms solve problems by calling themselves on smaller subproblems.

To analyze a recursive function, determine:

1. The base case.
2. The number of recursive calls.
3. The size of each subproblem.
4. The additional work performed in each call.
5. The maximum recursion depth.

## 6.1 Recursive Factorial — O(n)

```python
def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

Each call reduces `n` by one.

Recurrence:

```text
T(n) = T(n - 1) + O(1)
```

There are approximately `n` calls, each doing constant additional work.

- Time: `O(n)`
- Auxiliary space: `O(n)`

## 6.2 Naive Fibonacci — Exponential Time

```python
def fibonacci_naive(n):
    if n <= 1:
        return n

    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
```

The function branches into two recursive calls.

Recurrence:

```text
T(n) = T(n - 1) + T(n - 2) + O(1)
```

Many values are calculated repeatedly.

- Time: `O(2ⁿ)` as an upper bound.
- Auxiliary space: `O(n)`.

## 6.3 Fibonacci with Memoization — O(n)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n <= 1:
        return n

    return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
```

`lru_cache` stores the result of each function call so that the same argument does not need to be calculated again.

For example, after calculating `fibonacci_memo(3)`, its result is cached. Later calls with argument `3` reuse that result.

There are only `n + 1` distinct arguments from `0` to `n`.

- Time: `O(n)`.
- Space: `O(n)` for cached results and recursion stack.

**Key lesson:** Memoization can turn an exponential-time recursive algorithm into a linear-time algorithm when many subproblems overlap.

## 6.4 Merge Sort — Divide and Conquer

The recurrence is:

```text
T(n) = 2T(n / 2) + O(n)
```

Explanation:

- `2T(n / 2)`: Sort two halves recursively.
- `O(n)`: Merge the sorted halves.

By the Master Theorem:

```text
T(n) = O(n log n)
```

The implementation in this file uses slicing, two recursive calls, and a merge operation.

- Time: `O(n log n)`.
- Auxiliary space: `O(n)` for temporary lists, plus `O(log n)` recursion depth.

### Recursion Complexity Summary

| Algorithm | Time | Auxiliary Space |
|---|---|---|
| Factorial | `O(n)` | `O(n)` |
| Naive Fibonacci | `O(2ⁿ)` upper bound | `O(n)` |
| Memoized Fibonacci | `O(n)` | `O(n)` |
| Merge sort | `O(n log n)` | `O(n)` |

---

# 7. Complexity Comparison

**File:** `05_complexity_comparison.py`

This file compares algorithm execution times experimentally.

## 7.1 Measuring Runtime

```python
import time

def measure(func, *args):
    start = time.time()
    func(*args)
    return time.time() - start
```

**How it works:**

1. Record the start time.
2. Execute the function with the supplied arguments.
3. Record the end time.
4. Return the elapsed time.

The `*args` syntax allows the function to receive a variable number of positional arguments.

Example:

```python
measure(sum, [1, 2, 3])
```

**Important:** A single measurement is not reliable evidence of an algorithm's complexity. Runtime varies with hardware, system load, input data, interpreter overhead, and other factors.

For more reliable benchmarking, use repeated measurements, multiple input sizes, and tools such as Python's `timeit` module.

## 7.2 Constant Time — O(1)

```python
def o_1(n):
    return 1
```

The function returns the same value regardless of `n`.

Its operation count does not grow with input size.

## 7.3 Logarithmic Time — O(log n)

```python
def o_log_n(n):
    c = 0

    while n > 1:
        n //= 2
        c += 1

    return c
```

Repeatedly halves the input.

The number of iterations grows logarithmically.

## 7.4 Linear Time — O(n)

```python
def o_n(n):
    return sum(range(n))
```

Creates an iterable representing the integers from `0` through `n - 1` and sums them.

The summation takes linear time in `n`.

## 7.5 Linearithmic Time — O(n log n)

```python
def o_n_log_n(n):
    c = 0

    for i in range(n):
        j = 1

        while j < n:
            j *= 2
            c += 1

    return c
```

The outer loop executes `n` times, and the inner loop executes `O(log n)` times.

Total: `O(n log n)`.

## 7.6 Quadratic Time — O(n²)

```python
def o_n_squared(n):
    return sum(
        i * j
        for i in range(n)
        for j in range(n)
    )
```

Every possible pair `(i, j)` is processed.

The total number of pairs is `n²`.

Time: `O(n²)`.

## 7.7 Running the Comparison

```python
sizes = [10, 50, 100, 500]

funcs = {
    "O(1)": o_1,
    "O(log n)": o_log_n,
    "O(n)": o_n,
    "O(n log n)": o_n_log_n,
    "O(n^2)": o_n_squared,
}

for name, f in funcs.items():
    times = [measure(f, n) for n in sizes]
    print(f"{name}: {[f'{t:.6f}' for t in times]}")
```

The program runs each function on different input sizes and prints elapsed times in seconds.

For example, a result might look like this:

```text
O(1):       [measured times]
O(log n):   [measured times]
O(n):       [measured times]
O(n log n): [measured times]
O(n^2):     [measured times]
```

The actual measurements will depend on your computer.

**Note:** Although `matplotlib.pyplot` is imported in the original file, the current code does not produce a graph. It only prints timings. A graph would require additional plotting code.

---

# 8. Important Python Code Patterns

These patterns appear repeatedly throughout the folder.

## 8.1 Integer Division

```python
n //= 2
```

Equivalent to:

```python
n = n // 2
```

For positive integers, this halves `n` and discards the fractional part.

## 8.2 List Slicing

```python
left = arr[:mid]
right = arr[mid:]
```

- `arr[:mid]` returns a new list containing elements before `mid`.
- `arr[mid:]` returns a new list starting at `mid`.

List slicing takes time and additional space proportional to the number of copied elements.

## 8.3 List Comprehension

```python
[x * 2 for x in arr]
```

Creates a new list by applying `x * 2` to every element.

Time: `O(n)`.

Space: `O(n)` for the resulting list.

## 8.4 List Extension

```python
result.extend(left[i:])
```

Appends all elements from the specified slice to `result`.

This is useful in merge sort when one side has remaining elements.

## 8.5 Recursive Function Calls

```python
return n * factorial(n - 1)
```

A recursive call creates another active function call until the base case is reached.

Always identify the base case before analyzing recursive behavior.

## 8.6 Memoization

```python
@lru_cache(maxsize=None)
```

Caches function results by their arguments. It is useful when a recursive algorithm repeatedly solves the same subproblems.

---

# 9. Common Mistakes

### Mistake 1: Assuming every nested loop is O(n²)

Not necessarily. Analyze the actual iteration counts.

```python
for i in range(n):
    j = 1
    while j < n:
        j *= 2
```

This is `O(n log n)`, not `O(n²)`.

### Mistake 2: Assuming a recursive algorithm is always exponential

Factorial recursion is linear-time. Memoized Fibonacci is linear-time. The number and size of recursive subproblems determine the complexity.

### Mistake 3: Ignoring extra memory created by slicing

```python
left = arr[:mid]
```

Creates a copy of part of the list. Such allocations matter when analyzing auxiliary space.

### Mistake 4: Confusing factorial calculation with permutation generation

```python
return n * factorial(n - 1)
```

Computes `n!` in `O(n)` time. It does not enumerate `n!` different permutations.

### Mistake 5: Treating measured runtime as Big-O proof

One benchmark measures execution time for a particular run. Big-O analysis describes asymptotic growth and should primarily be derived from the algorithm's structure.

### Mistake 6: Forgetting input requirements

Binary search requires sorted input. Complexity analysis alone does not guarantee an algorithm produces correct results.

### Mistake 7: Confusing auxiliary space with total space

A function returning a new list may use `O(n)` auxiliary memory, while the returned list itself also occupies `O(n)` memory. Always state which convention you are using.

---

# 10. Quick Revision Sheet

## Time Complexity

| Code Pattern | Complexity |
|---|---|
| `return arr[0]` | `O(1)` |
| `while n > 1: n //= 2` | `O(log n)` |
| `for x in arr` | `O(n)` |
| Merge sort | `O(n log n)` |
| Two full nested loops | `O(n²)` |
| Three full nested loops | `O(n³)` |
| Naive recursive Fibonacci | `O(2ⁿ)` upper bound |
| Generating all permutations | Typically factorial-scale |

## Space Complexity

| Code Pattern | Auxiliary Space |
|---|---|
| Running total | `O(1)` |
| New list of `n` elements | `O(n)` |
| Recursive factorial | `O(n)` |
| `n × n` matrix | `O(n²)` |
| Recursive binary search | `O(log n)` |
| Memoized Fibonacci | `O(n)` |

## Five Rules to Remember

1. **Sequential operations:** Add their complexities, then keep the dominant term.
2. **Independent nested loops:** Multiply iteration counts.
3. **Repeated halving or doubling:** Usually logarithmic iterations.
4. **Recursive algorithms:** Analyze the recurrence, recursion depth, and repeated subproblems.
5. **Extra data structures:** Include their memory requirements in space analysis.

---

# 11. Practice Questions

Try solving these without looking at the answers first.

### Beginner

1. What is the time complexity of accessing `arr[5]`?
2. What is the time complexity of traversing an array once?
3. What is the space complexity of creating a new list with one element per input element?
4. How many iterations does `while n > 1: n //= 2` perform asymptotically?

### Intermediate

5. What is the complexity of two consecutive loops, each running `n` times?
6. What is the time complexity of three nested loops, each running `n` times?
7. Why does the triangular nested-loop example remain `O(n²)`?
8. Why is recursive binary search `O(log n)` in time and auxiliary space?

### Advanced

9. Explain why naive Fibonacci performs repeated calculations.
10. How does memoization improve Fibonacci's time complexity?
11. Derive the recurrence for merge sort and explain why it is `O(n log n)`.
12. Why is calculating `n!` different from generating every permutation?
13. Why is a single runtime measurement insufficient to establish Big-O complexity?

### Answers

<details>
<summary>Click to revise the answers</summary>

1. `O(1)`
2. `O(n)`
3. `O(n)`
4. `O(log n)`
5. `O(n)`, because `O(n) + O(n) = O(n)`
6. `O(n³)`
7. Its iteration count is `n(n + 1) / 2`, which simplifies to `O(n²)`.
8. Each call halves the search range, producing logarithmically many calls, each with constant additional work.
9. The same Fibonacci subproblems are evaluated repeatedly.
10. Caching results avoids repeated work, reducing time to `O(n)` and using `O(n)` space.
11. `T(n) = 2T(n/2) + O(n)`, giving `O(n log n)` by the Master Theorem.
12. Factorial calculation uses `O(n)` arithmetic operations under the usual unit-cost model; permutation generation must produce `n!` outputs and therefore takes at least factorial-scale output work.
13. Hardware, system load, interpreter overhead, and input sizes affect measured runtime. Asymptotic analysis studies how resource usage grows.

</details>

---

## ✅ Completion Checklist

Use this checklist to track your revision.

- [ ] Understand the common Big-O classes.
- [ ] Analyze sequential and nested loops.
- [ ] Identify logarithmic loops.
- [ ] Explain time versus auxiliary space complexity.
- [ ] Understand recursion depth and recurrence relations.
- [ ] Compare naive recursion with memoization.
- [ ] Explain merge sort using divide and conquer.
- [ ] Run the Python files and understand their output.
- [ ] Solve the practice questions without referring to the notes.

## 🎯 Final Takeaway

Complexity analysis is not about memorizing labels. It is about understanding **how an algorithm's work and memory requirements grow as the input gets larger**.

When revising any DSA problem, ask yourself:

1. How many times does each operation execute?
2. How does the number of operations change as `n` grows?
3. Does the algorithm create additional data structures?
4. Does recursion create a deep call stack?
5. Can repeated work be eliminated using a better approach?

Master these questions, and analyzing the complexity of new algorithms becomes much easier.

---

**Next topic:** Recursion and recurrence relations are particularly useful to study alongside complexity analysis. Once these notes feel comfortable, try analyzing binary search, merge sort, and memoized Fibonacci independently.
