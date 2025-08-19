# 🎰 This Is the Last Time  

## 📝 Problem Description  

You are given **n casinos**, each casino `i` is described by three integers:  
- `li` → the minimum coins required to enter.  
- `ri` → the maximum coins allowed to enter.  
- `reali` → the number of coins you will have after playing (where `li ≤ reali ≤ ri`).  

You start with **k coins**.  

Rules:  
1. You can **play at casino i** only if the current number of coins `x` satisfies `li ≤ x ≤ ri`.  
2. After playing, your coins become exactly `reali`.  
3. Each casino can be visited **at most once**.  
4. You can visit casinos in **any order**.  

🎯 **Goal:** Maximize the final number of coins after choosing the best sequence of casinos.  

---

## 📥 Input Format  

- The first line contains a single integer `t` — the number of test cases.  
  `1 ≤ t ≤ 10^4`  
- For each test case:  
  - One line with two integers `n, k` — number of casinos and initial coins.  
    `1 ≤ n ≤ 10^5, 0 ≤ k ≤ 10^9`  
  - Then `n` lines follow, each containing three integers:  
    - `li, ri, reali`  
    `0 ≤ li ≤ reali ≤ ri ≤ 10^9`  

It is guaranteed that the total sum of all `n` across test cases does not exceed `10^5`.  

---

## 📤 Output Format  

For each test case, output a single integer — the **maximum final number of coins** you can obtain.  

---

## 💡 Solution Explanation  

1. **Sort casinos** by their lower bound `li`.  
2. Iterate through casinos:  
   - If the current number of coins `k` satisfies `li ≤ k ≤ ri` → we can play.  
   - If after playing, the result `reali` increases or keeps `k`, update `k = reali`.  
3. Continue checking casinos in sorted order.  
4. Print the maximum `k` reached.  

This greedy approach works because we always try to upgrade `k` to the best possible value within valid ranges.  

---

## 🧑‍💻 Code by Mohamed  


