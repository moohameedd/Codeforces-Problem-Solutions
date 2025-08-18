# 🏔️ No Casino in the Mountains

## 📝 Problem Description
Jean wants to climb as many mountain peaks as possible.  

- The weather is given as an array `a` of length `n`.  
  - `a[i] = 0` → good weather.  
  - `a[i] = 1` → rainy day.  
- To hike a peak, Jean needs exactly `k` consecutive days of **good weather**.  
- After finishing a hike, he must rest for **at least one day** before starting another hike.  

Your task: **Find the maximum number of hikes Jean can make.**

---

## 📥 Input Format
- First line: integer `t` — number of test cases.  
- For each test case:
  - Line 1: two integers `n, k`.  
  - Line 2: `n` integers `a1, a2, ..., an` where each `ai ∈ {0,1}`.  

**Constraints:**  
- `1 ≤ t ≤ 10^4`  
- `1 ≤ n ≤ 10^5`  
- `1 ≤ k ≤ n`  
- Total sum of `n` across all test cases ≤ `10^5`.  

---

## 📤 Output Format
For each test case, output a single integer: the maximum number of hikes Jean can make.  

---

## 💡 Solution Explanation
The problem boils down to finding **disjoint segments** of length `k` consisting only of zeros.  
- Each hike must fit entirely inside a `k`-length window of zeros.  
- After every chosen hike, we must skip the **rest day** (so we jump `k+1` days forward).  

### Python Attempt (❌ TLE)
I first solved it in **Python** by:
- Converting the array into a binary string.  
- Searching for substrings of `k` consecutive zeros (`"0"*k`).  
- Removing them and skipping one extra character each time.  

```python
# Code by Mohamed (Python attempt) ❌ TLE
t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = "".join(map(str, a))
    m = "0" * k

    nb = 0
    while m in s:
        nb += 1
        s = s[:s.find(m)] + s[k+1:]
    print(nb)
