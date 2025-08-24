# 🍉 Problem C1 — The Cunning Seller (Easy Version)

## 📝 Problem Description

A cunning seller invented a new way of selling watermelons:  
- For any non-negative integer **`x`**, he can sell **`3^x`** watermelons.  
- The cost of this deal is:  

\[
\text{cost}(x) = 3^{x+1} + x \cdot 3^{x-1}
\]

The buyer wants to purchase **exactly `n` watermelons**, while making the **least possible number of deals**.  

Your task is to determine the **minimum total cost**.

---

## 📥 Input Format
- First line: integer `t` — number of test cases (`1 ≤ t ≤ 10^4`).  
- For each test case:  
  - A single integer `n` (`1 ≤ n ≤ 10^9`) — the number of watermelons the buyer wants.  

---

## 📤 Output Format
For each test case, print a single integer — the **minimum cost** to buy exactly `n` watermelons.  


---

## 💡 Solution Explanation

The idea is:  
1. At each step, pick the **largest possible power of 3** (deal size) that does not exceed `n`.  
2. Calculate how many times we can use this deal.  
3. Subtract the purchased watermelons from `n` and add the cost.  
4. Repeat until `n = 0`.  

This greedy approach works because deals grow exponentially, ensuring minimal number of deals.  

---

## ⏱️ Complexity
- **Time:** `O(log₃ n)` per test case (since we only check powers of 3).  
- **Space:** `O(1)` — constant extra memory.  

---

## 🧑‍💻 Code by Mohamed


