# Add or XOR Problem

## Problem Description
You are given **two non-negative integers** `a` and `b`. You can perform **two types of operations** on `a` any number of times and in any order:  

1. `a ← a + 1` — **cost:** `x`  
2. `a ← a ⊕ 1` (bitwise XOR with 1) — **cost:** `y`  

Your task is to make `a = b` at the **minimum total cost**, or report `-1` if it is impossible.

---

## Problem Explanation
- Input:
  - First line: integer `t` — number of test cases.  
  - Each test case: integers `a b x y` — starting value, target value, and operation costs.  
- Constraints:
  - `1 ≤ a, b ≤ 100`  
  - `1 ≤ x, y ≤ 10^7`  
  - `1 ≤ t ≤ 10^4`  
- Operations:
  - You can **increase `a` by 1** (cost `x`).  
  - You can **XOR `a` with 1** (cost `y`).  
- Goal: Find **minimum total cost** to make `a = b`, or `-1` if impossible.

---

## Solution Explanation
1. **Check if `a > b`**:  
   - Only XOR may help.  
   - If `a ^ 1 == b` → cost is `y`.  
   - Otherwise → impossible (`-1`).  

2. **If `a ≤ b`**:  
   - Let `diff = b - a` (number of +1 operations needed if we use only addition).  
   - Let `xor_count = (b + 1)//2 - (a + 1)//2` (number of times XOR can reduce cost).  
   - Compute **two possible total costs**:  
     - `cost_only_add = diff * x` — using only +1.  
     - `cost_mix = xor_count * y + (diff - xor_count) * x` — combination of XOR and +1.  
   - **Answer:** minimum of the two costs.  
