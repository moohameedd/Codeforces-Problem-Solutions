# 🎨 St. Chroma and His Favorite Color

## 📝 Problem Description

St. Chroma has a strip of `n` cells. He chooses a **permutation** `p` of length `n` (containing all numbers from `0` to `n-1`).  
For each prefix of the permutation, he paints the next cell with the value:


where **MEX** = the smallest non-negative integer not present in the prefix.  

You are given two integers `n` and `x`.  
Because St. Chroma loves color `x`, you must construct a permutation that **maximizes the number of cells painted with color `x`**.  

---

## 📥 Input Format

- The first line contains an integer `t` — the number of test cases.  
- Each test case contains two integers:  
  - `n` — length of the permutation.  
  - `x` — the favorite color.  

**Constraints:**  
- `1 ≤ t ≤ 4000`  
- `1 ≤ n ≤ 2⋅10^5`  
- `0 ≤ x ≤ n`  
- The total sum of `n` over all test cases ≤ `2⋅10^5`.  

---

## 📤 Output Format

For each test case, output a permutation `p` of length `n` such that the number of cells painted with color `x` is maximized.  
If impossible, output `0`.  

---

## 💡 Solution Explanation

We handle the problem based on the value of `x`:  

1. **❌ Impossible Case**  
   - If `x > n`, color `x` can never appear.  
   - If `n = 1` and `x = 0`, only one cell exists → impossible.  
   👉 Output `0`.  

2. **🎯 Case `x = n`**  
   - Simply use the natural permutation:  
     ```
     [0, 1, 2, ..., n-1]
     ```  
   - This ensures maximum cells colored with `n`.  

3. **✨ General Case (`x < n`)**  
   - Strategy:  
     - Take all numbers `0...n-1` but **skip `x`**.  
     - Place `x` at the **end** of the permutation.  
   - This keeps `x` as the **MEX of as many prefixes as possible**.  

---

## 🧩 Example

**Input:**

**Explanation:**  
- Case `n=4, x=2`: permutation `[0, 1, 3, 2]` maximizes MEX = 2.  
- Case `n=5, x=5`: permutation `[0, 1, 2, 3, 4]`.  
- Case `n=1, x=0`: impossible → output `0`.  

---

## 🧑‍💻 Code by Mohamed



