# Python Speed Drill — 7 Day Plan
Goal: remove syntax hesitation so reasoning, not typing, is the bottleneck in live coding rounds.
~45-60 min/day. Each day = drill + applied problems + a speed check.

---

## Day 1 — Comprehensions (list/dict/set, nested, conditional)
**Drill (15 min):** Write 10 comprehensions from memory:
- Filter: `[x for x in arr if x % 2 == 0]`
- Transform: `[x**2 for x in arr]`
- Nested/flatten: `[x for row in matrix for x in row]`
- Dict from two lists: `{k: v for k, v in zip(a, b)}`
- Set comprehension for dedup: `{x for x in arr}`

**Apply (30 min):** 2 easy problems using comprehensions where possible (matrix flatten, word frequency via dict comp).

**Speed check:** Write a nested comprehension (flatten 2D list) in under 30 seconds.

---

## Day 2 — `collections` (defaultdict, Counter, deque, OrderedDict)
**Drill (15 min):** Rewrite the same grouping logic 3 ways — manual dict with `.get()`, `defaultdict(list)`, `Counter` — to internalize *why* each exists.

**Know cold:**
- `deque` for O(1) append/pop from both ends (sliding window, BFS queue)
- `Counter.most_common(k)`
- `OrderedDict` is largely legacy now (dicts are ordered since 3.7) — know the distinction

**Apply (30 min):** 1 problem with `defaultdict` (group anagrams), 1 with `deque` (sliding window max or BFS level order).

---

## Day 3 — Slicing + unpacking
**Drill (15 min):**
- `arr[::-1]`, `arr[::2]`, `arr[-3:]`, `arr[i:j:k]`
- Star-unpacking: `first, *mid, last = arr`
- Swap: `a, b = b, a`

**Apply (30 min):** 2 problems leaning on slicing (reverse in groups, rotate array via slices).

**Speed check:** One-liner to reverse every other word in a sentence, no helper function.

---

## Day 4 — `heapq`
**Drill (15 min):**
- Build a min-heap from scratch: `heapify`, `heappush`, `heappop`
- Max-heap trick cold: push/pop negated values, remember to negate again on read

**Know cold:** Heap of tuples for custom priority — `heapq.heappush(h, (priority, item))` — common pattern for "k closest" / "top k" problems.

**Apply (30 min):** "K closest points" and "top K frequent elements" (push style + pull style).

---

## Day 5 — `sorted()` with `key=lambda` + multi-key sorts
**Drill (15 min):**
- Single-key, multi-key, negated-key sorts
- `functools.cmp_to_key` for cases negation doesn't work (e.g., descending string sort)

**Apply (30 min):** Interval scheduling (sort by start, tiebreak by end descending) + custom sort (strings by frequency then alphabetically).

---

## Day 6 — `itertools`
**Drill (15 min):**
- `permutations(arr)`, `combinations(arr, k)`, `product(a, b)`
- `accumulate(arr)` (running sum), `accumulate(arr, func=operator.mul)` (running product)

**Know cold:** When brute-force "generate all permutations/combinations" is a legitimate interview answer vs. a signal you should be doing DP/backtracking instead.

**Apply (30 min):** 1 combinatorics problem using `combinations`, 1 using `accumulate` (prefix sum variant).

---

## Day 7 — Iterators/generators (`iter`, `next`, `yield`) + full review
**Drill (20 min):**
- `iter(obj)` / `next(it, default)` — manually step through without a for-loop (useful for merge-style two-pointer problems or peeking at a stream)
- Write a generator function with `yield` (e.g., infinite Fibonacci generator, lazy range)
- Know the difference: generator computes lazily/on-demand vs. list comprehension materializes everything — relevant if asked about memory tradeoffs

**Mixed review (25 min):** Solve 1 problem combining at least 3 tools from this week (e.g., heap + sorted key, or defaultdict + comprehension) — mirrors how real interview problems rarely test one tool in isolation.

**Self-test:** Without notes, write from memory — a max-heap push/pop, a multi-key sort, and a generator — back to back, timed.

---

## End of week goal
Reach for any of these tools without pausing to recall syntax. That hesitation is exactly what live coding rounds