# 🔢 Problem B — The Secret Number

## 📝 Problem Description

Vadim thought of a **secret number `x`**.  
To hide it, he did the following:

- Appended one or more **zeros** to the right of `x`, forming a new number `y`.  
- Then computed `n = x + y`.  

You are given `n`. Your task is to find **all possible values of `x`**.

---

## 📥 Input Format

- First line: integer `t` — number of test cases (`1 ≤ t ≤ 10^4`).  
- Each of the next `t` lines: integer `n` (`11 ≤ n ≤ 10^18`).

---

## 📤 Output Format

For each test case:

- If **no valid `x` exists**, print `0`.  
- Otherwise, print:  
  - the number of valid `x`,  
  - followed by all valid values of `x` in ascending order.

---

## 💡 Solution Explanation

Vadim’s construction works like this:


➡️ To find all possible `x`:

1. Loop over possible values of `k` (as long as `10^k < n`).  
2. Compute `div = 1 + 10^k`.  
3. If `n % div == 0`, then `x = n / div` is valid.  
4. Collect all valid `x` and output them sorted.

---

## ⏱️ Complexity

- At most `log10(n)` iterations per test case.  
- Each iteration is constant time.  
- Total: **O(t · log n)**, efficient for the given constraints.

---

## 🧑‍💻 Code by Mohamed


