# 📘 DSA in Python

---

## 📖 Overview

This repository is a **structured, self-paced learning path** for mastering Data Structures and Algorithms using Python. Every topic is organized into its own module with clean, well-commented, and runnable code.

Whether you are:
- 🎓 A **student** learning DSA for the first time
- 💼 Preparing for **coding interviews** at top tech companies
- 🏆 Practicing **competitive programming**
- 👨‍🏫 A **mentor** looking for teaching material

…this repo is designed to serve you.

---

## ✨ Features

- ✅ **180+ runnable Python files** across 23+ modules
- ✅ **Clean, readable, and well-commented code**
- ✅ **Beginner → Advanced progression**
- ✅ **Covers theory, implementation, and classic problems**
- ✅ **Modular folder structure** — easy to navigate
- ✅ **No external dependencies** (except `matplotlib` for one visualization file)
- ✅ **Ideal for interview preparation and CP**

---

## 🗂️ Repository Structure

```
DSA-in-Python/
│
├── 01_Complexity_Analysis/        # Big-O notation, time & space analysis
├── 02_Recursion/                  # Basics, backtracking, divide & conquer
├── 03_Arrays/                     # Traversal, prefix sums, classic problems
├── 04_Strings/                    # Reversal, palindrome, anagram, matching
├── 05_Searching/                  # Linear, binary, rotated array, answer search
├── 06_Sorting/                    # Comparison & non-comparison sorts
├── 07_Hashing/                    # Hash maps, sets, frequency counters
├── 08_Linked_Lists/               # Singly, doubly, circular + problems
├── 09_Stacks/                     # Stack implementations & applications
├── 10_Queues/                     # Queue, deque, circular, priority queue
├── 11_Two_Pointers_Sliding_Window/
├── 12_Bit_Manipulation/
├── 13_Matrices/
├── 14_Trees/                      # Binary trees, BST, balanced trees
├── 15_Heaps/
├── 16_Graphs/                     # BFS, DFS, shortest paths, MST
├── 17_Greedy/
├── 18_Dynamic_Programming/        # Memoization, tabulation, classic DP
├── 19_Advanced_Data_Structures/   # Trie, DSU, Fenwick, Segment Tree
├── 20_String_Algorithms/          # KMP, Rabin-Karp, Z-algorithm
├── 21_Number_Theory/              # GCD, primes, modular arithmetic
├── 22_Advanced_Algorithms/        # Meet-in-middle, network flow, etc.
└── 23_Competitive_Programming/    # Templates & contest solutions
```


---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/DSA-in-Python.git
cd DSA-in-Python
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Install Optional Dependencies

Only needed for `01_Complexity_Analysis/05_complexity_comparison.py`:

```bash
pip install matplotlib
```

### 4. Run Any File

```bash
python 01_Complexity_Analysis/01_time_complexity.py
python 18_Dynamic_Programming/basics/03_climbing_stairs.py
```

---

## 📚 Topics Covered

| # | Module | Key Concepts |
|---|--------|--------------|
| 01 | Complexity Analysis | Big-O, time & space complexity |
| 02 | Recursion | Base case, backtracking, divide & conquer |
| 03 | Arrays | Traversal, prefix sum, Kadane, rotation |
| 04 | Strings | Palindrome, anagram, prefix matching |
| 05 | Searching | Linear, binary, rotated arrays |
| 06 | Sorting | Bubble → Merge, Quick, Heap, Radix |
| 07 | Hashing | HashMap, HashSet, Two-Sum, Anagrams |
| 08 | Linked Lists | Singly, Doubly, Circular + classic problems |
| 09 | Stacks | Implementations, NGE, Min Stack |
| 10 | Queues | Circular, Deque, Priority Queue |
| 11 | Two Pointers & Sliding Window | Pair sum, longest substring |
| 12 | Bit Manipulation | Bitwise ops, XOR tricks, bitmasking |
| 13 | Matrices | Traversal, rotation, spiral, search |
| 14 | Trees | Traversals, BST, LCA, Diameter, AVL |
| 15 | Heaps | Min/Max heap, Top-K, Merge K lists |
| 16 | Graphs | BFS, DFS, Dijkstra, Kruskal, Prim |
| 17 | Greedy | Activity selection, Knapsack, Intervals |
| 18 | Dynamic Programming | 1D, 2D, Bitmask, Tree DP |
| 19 | Advanced Data Structures | Trie, DSU, Fenwick, Segment Tree |
| 20 | String Algorithms | KMP, Rabin-Karp, Z-Algorithm |
| 21 | Number Theory | GCD, Sieve, Modular arithmetic |
| 22 | Advanced Algorithms | Meet-in-middle, Network flow |
| 23 | Competitive Programming | Fast I/O, Templates |

---

## 🎯 Who Is This For?

| Audience | Benefit |
|----------|---------|
| **Beginners** | Learn DSA from scratch with clean examples |
| **Interview Prep** | Revise classic patterns and problems |
| **College Students** | Reference for coursework and labs |
| **Competitive Programmers** | Ready-to-use templates and tricks |
| **Instructors** | Ready-made teaching material |

---

## 🛠️ How to Contribute

Contributions are **welcome and appreciated**! To contribute:

1. **Fork** the repository
2. **Create** a new branch: `git checkout -b feature/your-feature-name`
3. **Commit** your changes: `git commit -m "Add: description of change"`
4. **Push** to the branch: `git push origin feature/your-feature-name`
5. **Open** a Pull Request

### Contribution Guidelines

- Follow **PEP 8** style guidelines
- Add **docstrings** and **comments** where necessary
- Keep each file **focused on a single concept**
- Include an `if __name__ == "__main__":` block for demo
- Update the relevant `README.md` when adding new topics

---

## 🧭 Learning Path (Suggested Order)

If you're new to DSA, follow this order:

```
1. Complexity Analysis       →  2. Recursion
        ↓
3. Arrays  →  4. Strings  →  5. Searching  →  6. Sorting
        ↓
7. Hashing  →  8. Linked Lists  →  9. Stacks  →  10. Queues
        ↓
11. Two Pointers  →  12. Bit Manipulation  →  13. Matrices
        ↓
14. Trees  →  15. Heaps  →  16. Graphs
        ↓
17. Greedy  →  18. Dynamic Programming
        ↓
19–22. Advanced Topics
        ↓
23. Competitive Programming
```

---

## 📌 Best Practices Followed

- 🧩 **Modular code** — each algorithm is self-contained
- 📝 **Descriptive naming** — function names reflect their purpose
- 🧪 **Testable** — each file runs independently
- 📖 **Documented** — every folder has a `README.md`
- 🚫 **Zero heavy dependencies** — focus on core Python

---

## 📈 Progress Tracker

You can use this checklist to track your learning:

- [ ] 01 — Complexity Analysis
- [ ] 02 — Recursion
- [ ] 03 — Arrays
- [ ] 04 — Strings
- [ ] 05 — Searching
- [ ] 06 — Sorting
- [ ] 07 — Hashing
- [ ] 08 — Linked Lists
- [ ] 09 — Stacks
- [ ] 10 — Queues
- [ ] 11 — Two Pointers & Sliding Window
- [ ] 12 — Bit Manipulation
- [ ] 13 — Matrices
- [ ] 14 — Trees
- [ ] 15 — Heaps
- [ ] 16 — Graphs
- [ ] 17 — Greedy
- [ ] 18 — Dynamic Programming
- [ ] 19 — Advanced Data Structures
- [ ] 20 — String Algorithms
- [ ] 21 — Number Theory
- [ ] 22 — Advanced Algorithms
- [ ] 23 — Competitive Programming

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

You are free to use, modify, and distribute this code for **personal and educational purposes**.

---

## 🙌 Acknowledgements

- Inspired by classic DSA curricula (CLRS, GeeksforGeeks, LeetCode patterns)
- Built with ❤️ by the open-source community
- Special thanks to every contributor who helps improve this repo

---

## ⭐ Show Your Support

If this repository helped you:

- ⭐ **Star** the repo
- 🍴 **Fork** it and share with friends
- 🐛 **Report issues** you find
- 💡 **Suggest improvements** via Pull Requests

---

<p align="center">
  <b>Happy Coding! 🚀</b><br>
  <i>“Talk is cheap. Show me the code.” — Linus Torvalds</i>
</p>
```

---
