# 🏆 Tournament Problem

## 📝 Problem Description
You are given **n players**, each with a strength `ai`.  
A tournament is held where players fight until only **k players remain**.

Rules:
- In each fight, **two remaining players** are chosen at random.
- The player with **lower strength is eliminated** (if equal, one is chosen randomly).
- Given a player index `j`, determine if this player can be **one of the last k remaining** players.

---

## 📥 Input Format
- The first line contains an integer `t` — the number of test cases.  
  `1 ≤ t ≤ 10^4`
- For each test case:
  - One line with three integers `n, j, k` — number of players, target player index, and remaining players.  
    `2 ≤ n ≤ 2⋅10^5, 1 ≤ j, k ≤ n`
  - One line with `n` integers `a1, a2, ..., an` — strengths of the players.  
    `1 ≤ ai ≤ n`
- It is guaranteed that the total sum of `n` over all test cases does not exceed `2⋅10^5`.

---

## 📤 Output Format
For each test case, output `"YES"` if player `j` can be one of the last `k` remaining players, otherwise `"NO"`.

---

## 💡 Solution Explanation
1. Find the **maximum strength** among all players.
2. **Case k > 1**: Any player can survive because more than one player remains → `"YES"`.
3. **Case k == 1**: Only the strongest player can survive → `"YES"` if `a[j]` equals the maximum strength, otherwise `"NO"`.

This ensures an **O(n)** solution per test case without sorting or complicated logic.

---


