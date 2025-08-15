# Valorant Weapon Problem

## Problem Description
There is an Agent in Valorant who has **n weapons**. The i-th weapon deals damage **ai**.  
The Agent will face an enemy with health **H**.  

- The Agent can use weapons to decrease the enemy's health.  
- The same weapon **cannot be used twice in a row**.  
- Goal: Find the **minimum number of moves** required to kill the enemy.

---

## Problem Explanation
- You have `n` weapons, each dealing damage `ai`.  
- Enemy has health `H`.  
- In each move, you can choose **one weapon**.  
- Enemy dies when health ≤ 0.  
- You **cannot use the same weapon consecutively**.  
- Find the **minimum number of moves** to defeat the enemy.

---

## Solution Explanation
1. **Sort the weapons** in descending order of damage.  
2. Take the **two strongest weapons**: `a[0]` and `a[1]`.  
3. A **cycle** consists of using the strongest weapon then the second strongest weapon (**2 moves**).  
4. **Count full cycles**:  
5. **Compute remainder**:  

- If `remainder == 0` → no extra moves needed.  
- If `remainder <= a[0]` → add **1 move**.  
- If `remainder > a[0]` → add **2 moves**.


