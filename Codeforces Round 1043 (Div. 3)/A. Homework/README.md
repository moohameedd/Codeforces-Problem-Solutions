# 🏫 Problem A — Homework

## 📝 Problem Description

Vlad and Dima are assigned a task in English class:

- They have two strings, **`a`** and **`b`**.  
- All characters of `b` must be appended to `a` in the order they appear.  
- Vlad can **only add characters to the beginning** of the string.  
- Dima can **only add characters to the end** of the string.  
- The distribution of work is given in a string **`c`** (`'V'` for Vlad, `'D'` for Dima).  

Your task is to **determine the final string** after both Vlad and Dima finish appending the characters.

---

## 📥 Input Format

- First line: integer `t` — number of test cases (`1 ≤ t ≤ 1000`).  
- For each test case:
  - Integer `n` — length of string `a` (`1 ≤ n ≤ 10`).
  - String `a` — consisting of lowercase English letters.
  - Integer `m` — length of string `b` (`1 ≤ m ≤ 10`).
  - String `b` — characters to append.
  - String `c` — distribution of work (`'V'` or `'D'`).

---

## 📤 Output Format

For each test case, output the **final string** after Vlad and Dima finish their work.

---

## 💡 Solution Explanation

The solution follows the instructions **literally**:

1. Iterate over the characters of `b` from left to right.  
2. For each character `b[i]`:
   - If `c[i] == 'D'`, append it to the **end** of `a`.  
   - If `c[i] == 'V'`, append it to the **beginning** of `a`.  
3. Print the resulting string after processing all characters.

> Since `n, m ≤ 10`, the complexity is **O(m)** per test case.

---

## ⏱️ Complexity

- **Time:** `O(t * m)`  
- **Space:** `O(n + m)` for storing strings.

---

## 🧑‍💻 Code by Mohamed
