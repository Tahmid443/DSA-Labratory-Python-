# 🔁 Recursion, Backtracking & Divide and Conquer — DSA Notes

A comprehensive revision guide to recursion, backtracking, and divide-and-conquer algorithms using Python.

These notes explain the purpose of each implementation, how the code works, the underlying problem-solving approach, time and space complexity, and important interview concepts.

## 📁 Folder Structure

```text
02.Recursion/
├── README.md
├── 01.Basics/
│   ├── 01_countdown.py
│   ├── 02_factorial.py
│   ├── 03_fibonacci.py
│   ├── 04_sum_of_array.py
│   ├── 05_reverse_string.py
│   └── 06_binary_search.py
├── 02.Backtracking/
│   ├── 01_subsets.py
│   ├── 02_permutations.py
│   ├── 03_combinations.py
│   ├── 04_combination_sum.py
│   ├── 05_n_queens.py
│   └── 06_sudoku_solver.py
└── 03.Divide And Conquer/
    ├── 01_merge_sort.py
    ├── 02_quick_sort.py
    └── 03_maximum_subarray.py
```

## 📚 Table of Contents

1. [Introduction to Recursion](#1-introduction-to-recursion)
2. [Recursion Basics](#2-recursion-basics)
3. [Backtracking](#3-backtracking)
4. [Divide and Conquer](#4-divide-and-conquer)
5. [Time and Space Complexity Summary](#5-time-and-space-complexity-summary)
6. [Important Patterns](#6-important-patterns-to-remember)
7. [Common Mistakes](#7-common-mistakes)
8. [Quick Revision Sheet](#8-quick-revision-sheet)
9. [Practice Questions](#9-practice-questions)

---

# 1. Introduction to Recursion

Recursion is a programming technique in which a function calls itself to solve a smaller version of the same problem.

A recursive function usually contains two important components.

### 1.1 Base Case

The condition that stops further recursive calls.

```python
if n <= 0:
    return
```

Without an appropriate base case, recursion may continue until Python raises a `RecursionError`.

### 1.2 Recursive Case

The part that calls the function again with a smaller or simpler input.

```python
return factorial(n - 1)
```

The recursive call should make progress toward the base case.

### Example

```python
def countdown(n):
    if n <= 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)
```

For `countdown(3)`:

```text
countdown(3) → print 3
    countdown(2) → print 2
        countdown(1) → print 1
            countdown(0) → print Done!
```

Output:

```text
3
2
1
Done!
```

### How recursion uses memory

Each active function call occupies a frame on the call stack. Once the base case is reached, calls return in reverse order.

```text
Calling phase:
f(3) → f(2) → f(1) → f(0)

Returning phase:
f(0) → f(1) → f(2) → f(3)
```

For a recursion chain of depth `n`, the call stack can require `O(n)` auxiliary space.

---

# 2. Recursion Basics

## 2.1 Countdown

**File:** `01.Basics/01_countdown.py`

```python
def countdown(n):
    if n <= 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)
```

**Approach:** Linear recursion.

The function prints the current value and calls itself with `n - 1`. It stops when `n <= 0`.

For `countdown(5)`:

```text
5
4
3
2
1
Done!
```

- Time: `O(n)` for positive `n`.
- Auxiliary space: `O(n)` due to recursive calls.

**Remember:** Printing happens before the recursive call, so values appear in descending order.

---

## 2.2 Factorial

**File:** `01.Basics/02_factorial.py`

The factorial of a non-negative integer is:

\[
n! = n \times (n-1) \times \cdots \times 1
\]

By convention, \(0! = 1\).

### Recursive implementation

```python
def factorial(n):
    if n < 0:
        raise ValueError("Negative not allowed")

    if n <= 1:
        return 1

    return n * factorial(n - 1)
```

For `factorial(4)`:

```text
factorial(4)
= 4 × factorial(3)
= 4 × 3 × factorial(2)
= 4 × 3 × 2 × factorial(1)
= 4 × 3 × 2 × 1
= 24
```

The multiplication waits for the recursive call to return.

### Iterative implementation

```python
def factorial_iter(n):
    result = 1

    for i in range(2, n + 1):
        result *= i

    return result
```

This version multiplies numbers using a loop rather than recursive calls.

| Implementation | Time | Auxiliary Space |
|---|---|---|
| Recursive factorial | `O(n)` | `O(n)` |
| Iterative factorial | `O(n)` | `O(1)` |

The iterative implementation in the supplied file does not explicitly reject negative input; it returns `1` for a negative integer. To match the recursive function's behavior, it should also validate `n`.

**Key lesson:** Recursion and iteration can solve the same problem, but their memory usage may differ.

---

## 2.3 Fibonacci

**File:** `01.Basics/03_fibonacci.py`

The Fibonacci sequence is defined as:

\[
F(0)=0,\quad F(1)=1
\]

\[
F(n)=F(n-1)+F(n-2)
\]

The first ten values are:

```text
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
```

### A. Naive recursion

```python
def fib_naive(n):
    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)
```

Each call creates two smaller recursive calls.

For example, `fib_naive(5)` repeatedly calculates values such as `fib_naive(3)` and `fib_naive(2)`.

- Time: `O(2ⁿ)` as a convenient upper bound.
- Auxiliary space: `O(n)`.

This implementation is inefficient for large inputs because it repeats work.

### B. Memoization

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n

    return fib_memo(n - 1) + fib_memo(n - 2)
```

`@lru_cache(maxsize=None)` stores previously calculated results.

Each value from `F(0)` through `F(n)` needs to be calculated only once.

- Time: `O(n)`.
- Space: `O(n)` for the cache and recursive stack.

### C. Iterative Fibonacci

```python
def fib_iter(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
```

Here:

- `a` stores the previous Fibonacci value.
- `b` stores the current Fibonacci value.
- `a + b` calculates the next value.

Python evaluates the right-hand side before assigning the variables, so both values update correctly.

- Time: `O(n)`.
- Auxiliary space: `O(1)`.

### Comparison

| Method | Time | Auxiliary Space |
|---|---|---|
| Naive recursion | `O(2ⁿ)` upper bound | `O(n)` |
| Memoization | `O(n)` | `O(n)` |
| Iteration | `O(n)` | `O(1)` |

**Interview takeaway:** Memoization avoids repeated work. Iteration avoids the recursive stack as well.

---

## 2.4 Sum of an Array

**File:** `01.Basics/04_sum_of_array.py`

### A. Using slicing

```python
def sum_array(arr):
    if not arr:
        return 0

    return arr[0] + sum_array(arr[1:])
```

The function adds the first element to the sum of the remaining elements.

For `[1, 2, 3]`:

```text
sum([1, 2, 3])
= 1 + sum([2, 3])
= 1 + 2 + sum([3])
= 1 + 2 + 3 + sum([])
= 6
```

The empty list is the base case and returns `0`.

Because `arr[1:]` creates a new list at each call, this implementation takes:

- Time: `O(n²)` in typical Python list-slicing cost.
- Auxiliary space: `O(n²)` cumulatively for the copied slices, with `O(n)` recursion depth.

### B. Using an index

```python
def sum_array_index(arr, i=0):
    if i == len(arr):
        return 0

    return arr[i] + sum_array_index(arr, i + 1)
```

Instead of creating a smaller list, the function advances an index.

- Time: `O(n)`.
- Auxiliary space: `O(n)` for the recursive stack.

**Key lesson:** Both implementations use recursion, but avoiding repeated slicing improves efficiency.

---

## 2.5 Reverse a String

**File:** `01.Basics/05_reverse_string.py`

```python
def reverse_string(s):
    if len(s) <= 1:
        return s

    return reverse_string(s[1:]) + s[0]
```

The function recursively reverses everything except the first character, then appends that first character at the end.

For `"cat"`:

```text
reverse("cat")
= reverse("at") + "c"
= (reverse("t") + "a") + "c"
= "tac"
```

- Time: `O(n²)` due to repeated slicing and string concatenation.
- Auxiliary space: `O(n²)` cumulatively for intermediate strings, with `O(n)` recursion depth.

### Important note about `reverse_inplace`

The supplied `reverse_inplace(s, i=0)` function is **incomplete**. It converts the string into a list but does not perform any swaps or return the reversed string.

Python strings are immutable, so a true in-place character swap cannot be performed directly on a string. A list of characters can be modified instead.

---

## 2.6 Recursive Binary Search

**File:** `01.Basics/06_binary_search.py`

Binary search finds a target in a sorted array by repeatedly eliminating half of the search range.

```python
def binary_search(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    if arr[mid] < target:
        return binary_search(arr, target, mid + 1, high)

    return binary_search(arr, target, low, mid - 1)
```

### How it works

For the sorted array:

```text
[1, 3, 5, 7, 9, 11, 13]
```

Searching for `7`:

1. Calculate the middle index.
2. Compare the middle element with `7`.
3. If equal, return its index.
4. Otherwise, continue in the half that could contain the target.

If the target is not present, the function returns `-1`.

- Time: `O(log n)`.
- Auxiliary space: `O(log n)` due to recursion.

**Prerequisite:** The array must be sorted in ascending order for this implementation.

---

# 3. Backtracking

Backtracking is a problem-solving technique that builds a candidate solution step by step. If a choice leads to a dead end or an invalid solution, the algorithm undoes that choice and tries another.

The general pattern is:

```python
def backtrack(state):
    if solution_is_complete(state):
        save_solution(state)
        return

    for choice in available_choices:
        if is_valid(choice):
            make_choice(choice)
            backtrack(updated_state)
            undo_choice(choice)
```

The three essential actions are:

1. **Choose:** Make a temporary decision.
2. **Explore:** Recursively investigate the result.
3. **Undo:** Restore the state so another decision can be explored.

This is often called the **choose → explore → unchoose** pattern.

## 3.1 Subsets

**File:** `02.Backtracking/01_subsets.py`

A subset contains any selection of the input elements, including the empty subset and the entire set.

```python
def subsets(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
```

For `[1, 2, 3]`, there are \(2^3=8\) subsets.

```text
[]
[1]
[1, 2]
[1, 2, 3]
[1, 3]
[2]
[2, 3]
[3]
```

### Important code details

- `path` stores the current subset.
- `start` prevents revisiting earlier positions.
- `path[:]` saves a copy of the current subset.
- `path.pop()` removes the last choice before trying another branch.

Why use `path[:]`? Without copying, saved results could refer to the same mutable list, which changes during backtracking.

- Time: `O(n × 2ⁿ)` including the cost of copying and storing subsets.
- Space: `O(n × 2ⁿ)` for the output; auxiliary working space is `O(n)` excluding the output.

---

## 3.2 Permutations

**File:** `02.Backtracking/02_permutations.py`

A permutation is an arrangement of elements in a particular order.

For `[1, 2, 3]`, there are:

\[
3! = 6
\]

permutations.

### A. Using a remaining list

```python
def permutations(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path[:])
            return

        for i in range(len(remaining)):
            path.append(remaining[i])

            backtrack(
                path,
                remaining[:i] + remaining[i + 1:]
            )

            path.pop()

    backtrack([], nums)
    return result
```

The function chooses one element, removes it from the remaining choices, and continues until no elements remain.

### B. Using swapping

```python
def permutations_swap(nums):
    result = []
    nums = nums[:]

    def backtrack(start):
        if start == len(nums):
            result.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]

            backtrack(start + 1)

            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result
```

This implementation fixes one position at a time by swapping elements. After exploring a branch, it swaps back to restore the original state.

- Time: `O(n × n!)` for generating and copying all permutations.
- Output space: `O(n × n!)`.
- Recursive auxiliary space: `O(n)`, excluding the output and temporary allocations.

**Remember:** Subsets select elements; permutations arrange elements in different orders.

---

## 3.3 Combinations

**File:** `02.Backtracking/03_combinations.py`

A combination selects `k` elements from the integers `1` through `n`, without considering order.

```python
def combinations(n, k):
    result = []

    def backtrack(start, path):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(start, n + 1):
            path.append(i)
            backtrack(i + 1, path)
            path.pop()

    backtrack(1, [])
    return result
```

For `combinations(4, 2)`:

```text
[1, 2]
[1, 3]
[1, 4]
[2, 3]
[2, 4]
[3, 4]
```

The number of combinations is:

\[
\binom{n}{k}=\frac{n!}{k!(n-k)!}
\]

The `start` argument ensures that elements are selected in increasing index order, preventing duplicate combinations in different orders.

- Time: `O(k × C(n,k))` for producing and copying the results, where `C(n,k)` is the binomial coefficient.
- Output space: `O(k × C(n,k))`.
- Auxiliary recursion space: `O(k)`.

**Difference from permutations:** `[1, 2]` and `[2, 1]` represent the same combination, but different permutations.

---

## 3.4 Combination Sum

**File:** `02.Backtracking/04_combination_sum.py`

The goal is to find combinations of candidate numbers that sum to a target. In this implementation, a candidate may be used repeatedly.

```python
def combination_sum(candidates, target):
    result = []
    candidates.sort()

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if candidates[i] > remaining:
                break

            path.append(candidates[i])
            backtrack(i, path, remaining - candidates[i])
            path.pop()

    backtrack(0, [], target)
    return result
```

For:

```python
combination_sum([2, 3, 6, 7], 7)
```

The result is:

```text
[[2, 2, 3], [7]]
```

### Why does the recursive call use `i` rather than `i + 1`?

```python
backtrack(i, path, remaining - candidates[i])
```

Using `i` allows the same candidate to be selected again.

If the recursive call used `i + 1`, each candidate could be selected at most once.

### Why sort the candidates?

```python
candidates.sort()
```

Because the candidates are sorted, once `candidates[i] > remaining`, all later candidates are also too large. The loop can stop with `break`.

**Important assumptions:** The typical problem expects positive candidate values. Zero or negative candidates can invalidate the termination assumptions.

Complexity depends on the candidate values and target; the number of valid combinations can grow exponentially. There is no single polynomial time bound for unrestricted instances of this problem.

---

## 3.5 N-Queens

**File:** `02.Backtracking/05_n_queens.py`

The N-Queens problem asks us to place `n` queens on an `n × n` chessboard so that no two queens attack one another.

Queens cannot share:

- A column.
- A main diagonal.
- An anti-diagonal.

```python
def solve_n_queens(n):
    result = []
    cols, diag1, diag2 = set(), set(), set()
    board = [["."] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if (
                col in cols
                or (row - col) in diag1
                or (row + col) in diag2
            ):
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            board[row][col] = "Q"

            backtrack(row + 1)

            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return result
```

### How the code works

**Step 1:** Place one queen in the current row.

**Step 2:** Check whether its column or diagonals are already occupied.

**Step 3:** Record the placement in the sets and board.

**Step 4:** Recursively process the next row.

**Step 5:** Undo the placement if the recursive exploration returns.

The diagonal identifiers are:

```text
Main diagonal:      row - col
Anti-diagonal:     row + col
```

Cells on the same diagonal share the corresponding identifier.

The sets make conflict checks efficient, typically `O(1)` average time per membership check.

The search has exponential worst-case behavior, often described by an `O(n!)`-scale search bound with this row-by-row approach; actual work depends on pruning and valid placements. Output storage must also be counted when analyzing space.

For `n = 4`, the algorithm finds two solutions.

---

## 3.6 Sudoku Solver

**File:** `02.Backtracking/06_sudoku_solver.py`

The Sudoku solver fills empty cells while maintaining the rules of a standard 9 × 9 Sudoku puzzle.

Each digit from `1` to `9` must appear exactly once in every row, every column, and every 3 × 3 box.

### Validity checking

```python
def is_valid(r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    br, bc = 3 * (r // 3), 3 * (c // 3)

    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == num:
                return False

    return True
```

The function checks:

1. The row.
2. The column.
3. The corresponding 3 × 3 box.

### Backtracking

```python
def backtrack():
    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                for num in "123456789":
                    if is_valid(r, c, num):
                        board[r][c] = num

                        if backtrack():
                            return True

                        board[r][c] = "."

                return False

    return True
```

The function finds an empty cell, tries valid digits, and recursively solves the rest of the puzzle.

If a choice leads to a dead end, the cell is restored to `"."`.

- Time: Exponential in the worst case, with a crude upper bound of `O(9^m)` for `m` initially empty cells before accounting for pruning.
- Auxiliary recursion space: At most `O(m)` for this implementation, where `m` is the number of initially empty cells.

**Important limitation:** The supplied `solve_sudoku()` calls `backtrack()` but ignores its Boolean return value. It returns the board whether the puzzle was solved or not. For reliable use, check the result and report unsolvable puzzles explicitly.

---

# 4. Divide and Conquer

Divide and conquer breaks a problem into smaller subproblems, solves them recursively, and combines their results.

The three common stages are:

1. **Divide:** Split the original problem.
2. **Conquer:** Solve the smaller problems.
3. **Combine:** Merge or compare the results.

## 4.1 Merge Sort

**File:** `03.Divide And Conquer/01_merge_sort.py`

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)
```

The `merge()` helper combines two sorted lists by repeatedly taking the smaller front element.

Example:

```text
[38, 27, 43, 3]
       ↓
  [38, 27] [43, 3]
       ↓
  [27, 38] [3, 43]
       ↓
  [3, 27, 38, 43]
```

Recurrence:

\[
T(n)=2T(n/2)+O(n)
\]

Therefore:

- Time: `O(n log n)`.
- Auxiliary space: `O(n)` for temporary lists, plus `O(log n)` recursion depth.

**Strength:** Predictable `O(n log n)` time.

**Trade-off:** The supplied implementation allocates new lists rather than sorting entirely in place.

---

## 4.2 Quick Sort

**File:** `03.Divide And Conquer/02_quick_sort.py`

Quick sort partitions elements around a pivot and recursively sorts the resulting sections.

### A. List-based quick sort

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + mid + quick_sort(right)
```

This implementation:

1. Selects the middle element as the pivot value.
2. Collects smaller values in `left`.
3. Collects equal values in `mid`.
4. Collects larger values in `right`.
5. Recursively sorts `left` and `right`.

Separating equal values helps handle duplicate values without repeatedly partitioning them into smaller recursive calls.

- Average time: `O(n log n)` for balanced partitions.
- Worst-case time: `O(n²)`.
- Auxiliary space: Additional lists are allocated, so space usage is greater than an in-place implementation.

### B. In-place quick sort

```python
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        p = partition(arr, low, high)

        quick_sort_inplace(arr, low, p - 1)
        quick_sort_inplace(arr, p + 1, high)

    return arr
```

This version modifies the original list.

The `partition()` function uses the last element as the pivot:

```python
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1
```

After partitioning, the pivot is in its final sorted position. Values on its left are less than or equal to it, and values on its right are greater.

- Average time: `O(n log n)`.
- Worst-case time: `O(n²)`.
- Auxiliary stack space: `O(log n)` on balanced partitions and `O(n)` in the worst case.

**Important difference:** Although called in-place, this implementation still uses recursive stack space.

---

## 4.3 Maximum Subarray — Divide and Conquer

**File:** `03.Divide And Conquer/03_maximum_subarray.py`

The maximum-subarray problem asks for the largest possible sum of a non-empty contiguous subarray.

Example:

```python
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

The best subarray is:

```text
[4, -1, 2, 1]
```

Its sum is `6`.

### A. Divide-and-conquer implementation

```python
def max_subarray_divide(arr):
    def helper(l, r):
        if l == r:
            return arr[l]

        mid = (l + r) // 2

        left = helper(l, mid)
        right = helper(mid + 1, r)

        left_sum = float("-inf")
        s = 0

        for i in range(mid, l - 1, -1):
            s += arr[i]
            left_sum = max(left_sum, s)

        right_sum = float("-inf")
        s = 0

        for i in range(mid + 1, r + 1):
            s += arr[i]
            right_sum = max(right_sum, s)

        return max(left, right, left_sum + right_sum)

    return helper(0, len(arr) - 1)
```

The maximum subarray can be in one of three locations:

1. Entirely in the left half.
2. Entirely in the right half.
3. Crossing the midpoint.

The algorithm calculates the best crossing sum by finding the best suffix of the left half and the best prefix of the right half.

Then it returns the maximum of the three candidates.

Recurrence:

\[
T(n)=2T(n/2)+O(n)
\]

- Time: `O(n log n)`.
- Auxiliary space: `O(log n)` for the recursion stack.

**Input requirement:** The supplied implementation assumes a non-empty array. An empty array causes an error.

### B. Kadane's Algorithm

```python
def kadane(arr):
    max_so_far = curr = arr[0]

    for x in arr[1:]:
        curr = max(x, curr + x)
        max_so_far = max(max_so_far, curr)

    return max_so_far
```

Kadane's algorithm solves the same problem in linear time.

At every element:

- `x` means start a new subarray at the current element.
- `curr + x` means extend the previous subarray.

The algorithm chooses whichever produces the larger sum.

- Time: `O(n)`.
- Auxiliary space: `O(1)`.

It also correctly handles an array containing only negative values, provided the array is non-empty.

**Interview takeaway:** Kadane's algorithm is more efficient for finding the maximum subarray sum, while divide and conquer is useful for understanding recursive decomposition.

---

# 5. Time and Space Complexity Summary

## Recursion Basics

| Algorithm | Time | Auxiliary Space |
|---|---|---|
| Countdown | `O(n)` | `O(n)` |
| Recursive factorial | `O(n)` | `O(n)` |
| Iterative factorial | `O(n)` | `O(1)` |
| Naive Fibonacci | `O(2ⁿ)` upper bound | `O(n)` |
| Memoized Fibonacci | `O(n)` | `O(n)` |
| Iterative Fibonacci | `O(n)` | `O(1)` |
| Sum with slicing | `O(n²)` | `O(n²)` cumulative temporary allocations |
| Sum with index | `O(n)` | `O(n)` |
| Reverse string with slicing | `O(n²)` | `O(n²)` cumulative temporary allocations |
| Recursive binary search | `O(log n)` | `O(log n)` |

## Backtracking

| Algorithm | Time | Space Considerations |
|---|---|---|
| Subsets | `O(n × 2ⁿ)` | Output `O(n × 2ⁿ)` |
| Permutations | `O(n × n!)` | Output `O(n × n!)` |
| Combinations | `O(k × C(n,k))` | Output `O(k × C(n,k))` |
| Combination sum | Input-dependent; potentially exponential | Search depth and output |
| N-Queens | Exponential search; commonly `O(n!)`-scale bound | Board, search state, and output |
| Sudoku solver | Exponential worst case | Board and recursive search |

## Divide and Conquer

| Algorithm | Average/Typical Time | Worst-Case Time | Auxiliary Space |
|---|---|---|---|
| Merge sort | `O(n log n)` | `O(n log n)` | `O(n)` |
| List-based quick sort | `O(n log n)` | `O(n²)` | Additional lists and recursion |
| In-place quick sort | `O(n log n)` | `O(n²)` | `O(log n)` average stack; `O(n)` worst |
| Maximum subarray, divide and conquer | `O(n log n)` | `O(n log n)` | `O(log n)` |
| Kadane's algorithm | `O(n)` | `O(n)` | `O(1)` |

*Complexity conventions:* Output space is identified separately when it is substantial. Exact costs can depend on implementation details, input characteristics, and whether temporary allocations are counted.

---

# 6. Important Patterns to Remember

## Pattern 1: Basic recursion

```python
def solve(n):
    if base_case:
        return result

    return solve(smaller_problem)
```

Use for countdown, factorial, and other problems that reduce naturally to smaller inputs.

## Pattern 2: Recursion with an accumulator or index

```python
def solve(arr, i):
    if i == len(arr):
        return 0

    return arr[i] + solve(arr, i + 1)
```

Useful when the problem can be processed one element at a time without copying the remaining input.

## Pattern 3: Memoization

```python
@lru_cache(maxsize=None)
def solve(n):
    if base_case:
        return result

    return solve(n - 1) + solve(n - 2)
```

Use when multiple recursive branches solve the same subproblems.

## Pattern 4: Backtracking

```python
path.append(choice)
backtrack(next_state)
path.pop()
```

Use for subsets, permutations, combinations, constraint puzzles, and search problems that require exploring alternative choices.

## Pattern 5: Divide and conquer

```python
left = solve(left_half)
right = solve(right_half)

return combine(left, right)
```

Use when the problem can be split into smaller independent subproblems whose results can be combined.

## Pattern 6: Partition around a pivot

```python
p = partition(arr, low, high)
quick_sort_inplace(arr, low, p - 1)
quick_sort_inplace(arr, p + 1, high)
```

Use in quick sort and related partition-based algorithms.

---

# 7. Common Mistakes

1. **Missing the base case:** Recursive calls may never stop.
2. **Not reducing the problem:** Every recursive step should make progress toward termination.
3. **Forgetting to undo choices:** Backtracking state can leak between branches.
4. **Saving mutable state without copying:** Store `path[:]` rather than repeatedly storing the same list reference.
5. **Using the wrong starting index:** Combinations and subsets can produce duplicates if earlier choices are reconsidered.
6. **Confusing subsets and permutations:** Subsets ignore order; permutations depend on order.
7. **Ignoring slicing costs:** Operations such as `arr[1:]` and `remaining[:i]` allocate new lists.
8. **Assuming quick sort always takes `O(n log n)`:** The worst case is `O(n²)`.
9. **Forgetting input prerequisites:** Binary search needs sorted input, and the maximum-subarray implementations here expect a non-empty array.
10. **Confusing recursion depth with total work:** A recursion tree can have exponential total work even when its maximum depth is only linear.

---

# 8. Quick Revision Sheet

| Concept | Main Idea |
|---|---|
| Recursion | A function solves smaller instances of itself |
| Base case | Stops recursion |
| Call stack | Stores active recursive calls |
| Memoization | Caches results of repeated subproblems |
| Backtracking | Choose, explore, undo |
| Subsets | Every element is included or excluded |
| Permutations | Arrange elements in different orders |
| Combinations | Select elements without considering order |
| Constraint search | Reject invalid choices early |
| Divide and conquer | Divide, solve, combine |
| Merge sort | Split and merge sorted halves |
| Quick sort | Partition around a pivot |
| Maximum subarray | Find the largest sum of a contiguous segment |
| Kadane's algorithm | Extend or restart the current subarray |

## Three questions to ask when analyzing recursion

1. What is the base case?
2. How many recursive calls are made, and how much smaller is each subproblem?
3. How much work and memory are required at each level?

## Three questions to ask when analyzing backtracking

1. What choices can I make?
2. What constraints make a choice invalid?
3. How do I undo a choice and restore the previous state?

---

# 9. Practice Questions

Try answering these without looking at the code.

### Beginner

1. What are the two essential parts of a recursive function?
2. Why does `factorial(0)` return `1`?
3. What is the difference between recursive and iterative factorial?
4. Why does binary search require sorted input?
5. What is the purpose of `path.pop()` in backtracking?

### Intermediate

6. Why is naive Fibonacci inefficient?
7. How does memoization improve Fibonacci?
8. Why can the slicing-based array sum take `O(n²)` time?
9. What is the difference between subsets, permutations, and combinations?
10. Why does merge sort take `O(n log n)` time?
11. Why can quick sort take `O(n²)` time in the worst case?
12. Why does the N-Queens solution track columns and diagonals?

### Advanced

13. Explain the difference between memoization and backtracking.
14. Derive the recurrence for merge sort.
15. Explain how the maximum-subarray divide-and-conquer algorithm handles a subarray crossing the midpoint.
16. Why is Kadane's algorithm `O(n)` time and `O(1)` auxiliary space?
17. Why must a backtracking algorithm restore state after exploring a branch?
18. What changes would make the Sudoku solver report an unsolvable puzzle?
19. Why does generating all permutations require factorial-scale output work?
20. What is the difference between the recursion stack and total auxiliary space?

<details>
<summary>Show answers</summary>

1. A base case and a recursive case.
2. By the factorial definition, `0! = 1`.
3. Recursive factorial uses a call stack; iterative factorial uses a loop.
4. Sorted order lets the algorithm safely discard half of the search range.
5. It removes the last choice and restores the previous state.
6. It repeatedly calculates the same Fibonacci values.
7. It caches results, reducing time to `O(n)`.
8. Each recursive call copies a remaining slice whose length decreases by one; the total copied elements can be quadratic.
9. Subsets select any elements; permutations order them; combinations select a fixed number without considering order.
10. It has `O(log n)` levels with `O(n)` merging work per level.
11. Highly unbalanced partitions can lead to quadratic total work.
12. Those sets make it efficient to check whether a new queen conflicts with an existing queen.
13. Memoization reuses previously calculated results; backtracking explores choices and undoes them to search for valid solutions.
14. `T(n) = 2T(n/2) + O(n)`.
15. It combines the best suffix ending at the midpoint with the best prefix starting at the next position.
16. It visits each element once and maintains only a constant number of variables.
17. Otherwise, later branches can inherit choices made by earlier branches.
18. Check the Boolean return from `backtrack()` and report failure if it returns `False`.
19. There are `n!` permutations, each containing `n` elements.
20. The recursion stack is memory used by active calls; total auxiliary space also includes other temporary data structures.

</details>

---

## ✅ Completion Checklist

- [ ] Understand base cases and recursive cases.
- [ ] Trace recursive calls and returns manually.
- [ ] Compare recursive and iterative solutions.
- [ ] Understand memoization and overlapping subproblems.
- [ ] Implement subsets, permutations, and combinations.
- [ ] Apply the choose-explore-undo pattern.
- [ ] Explain merge sort and quick sort.
- [ ] Solve the maximum-subarray problem using both approaches.
- [ ] Identify time and space complexity.
- [ ] Fix the incomplete `reverse_inplace()` implementation.
- [ ] Test the Sudoku solver's success and failure cases.

## 🎯 Final Takeaway

Recursion teaches you to break a problem into smaller versions of itself. Backtracking teaches you to explore possibilities while undoing unsuccessful choices. Divide and conquer teaches you to split a problem into smaller subproblems and combine their results.

Together, these techniques form a foundation for many DSA problems, from binary search and sorting to combinatorial search and optimization.

**Recommended revision order:**

1. Recursion basics
2. Recursion with arrays and strings
3. Binary search
4. Subsets and combinations
5. Permutations and combination sum
6. N-Queens and Sudoku
7. Merge sort and quick sort
8. Maximum subarray and Kadane's algorithm
