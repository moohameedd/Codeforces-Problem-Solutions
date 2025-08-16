# 🧠 Binary String Intelligence Test

## 📝 Problem Description

In order to test his patients' intelligence, Dr. TC devised the following challenge:

He begins by creating a binary string `s` of length `n`. Then, he generates `n` new binary strings, `a1, a2, ..., an`, each created by flipping exactly one bit in `s` — specifically, the i-th bit is flipped to get the i-th string.

Each of these new strings becomes a row in a grid.

🧪 The challenge is: **Count the total number of `1`s in the entire grid.**


Total number of `1`s: **4**

## 📥 Input Format

- The first line contains a single integer `t` — the number of test cases.  
`1 ≤ t ≤ 1000`
- For each test case:
- A line with an integer `n` — the length of the binary string `s`.  
  `1 ≤ n ≤ 10`
- A line with the binary string `s` of length `n`.

## 📤 Output Format

For each test case, output a single integer — the total number of `1`s in the final grid.

---

## 💡 Solution Explanation

To solve the problem efficiently, we avoid creating the entire grid. Instead, we compute the number of `1`s by:

1. **Iterating through each position `i`** of the string:
 - If `s[i] == '0'`, flipping it will add a new `1` in string `ai`, so we increment the total count.
2. **For all other positions** (those not flipped), we count how many of them are `'1'` and add that to the total (since they remain unchanged in every flipped string).

⏱️ This is efficient because `n` is small (`≤ 10`), so even this nested approach works well.

---

## 🧑‍💻 Code by Mohamed

