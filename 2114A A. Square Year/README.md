# 🔲 Square Year Problem  

## 📝 Problem Description  
We notice a remarkable fact:  
- **2025 = (20 + 25)²**  

You are given a year as a **4-digit string `s`** (leading zeros allowed, e.g., `"0001"`, `"0185"`).  
You need to check if this year can be expressed as:  

\[
s = (a+b)^2
\]

Where:  
- `a ≥ 0`, `b ≥ 0` are integers.  
- If possible → output **two numbers `a` and `b`**.  
- If impossible → output `-1`.  

---

## 📥 Input Format  
- The first line contains integer `t` — number of test cases.  
  `1 ≤ t ≤ 10^4`  
- Each test case contains one string `s` (exactly 4 digits).  

---

## 📤 Output Format  
- If there exists `(a, b)` → print them.  
- If multiple pairs exist → print any.  
- Otherwise → print `-1`.  

---

## 💡 Solution Explanation  
1. Precompute all perfect squares up to `99² = 9801` (since max 4-digit number is `9999`).  
2. For each year `s`:  
   - Convert `s` → integer.  
   - Use **Binary Search** to check if `s` is in the precomputed list of squares.  
3. If found:  
   - Example representation: `(res-1, 1)` because `(res-1 + 1)² = res²`.  
   - Special case: if result is `0`, print `(0, 0)`.  
4. If not found → print `-1`.  

---

## ⚡ Complexity Analysis  
- Precomputing squares: **O(100)** → negligible.  
- Binary Search on sorted list of size `100`: **O(log 100) ≈ O(7)**.  
- For `t ≤ 10^4` test cases, total complexity: **O(t · log 100)** → extremely efficient.  

This shows why **Binary Search** is one of the most useful algorithms in **Competitive Programming**:  
- Much faster than linear search (**O(n)**).  
- Guarantees quick lookups in sorted data.  

---

