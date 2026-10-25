# DAA-0-1-Knapsack
0/1 Knapsack using Dynamic Programming with live ASCII visualization


# DAA Lab Assignment: 0/1 Knapsack Using Dynamic Programming

## 📌 Project Overview

This project implements the **0/1 Knapsack Problem using Dynamic Programming** as part of a Design and Analysis of Algorithms (DAA) lab assignment.

Given a set of items, each with a weight and a value, and a knapsack with a limited capacity, the program calculates the maximum total value that can be obtained without exceeding the capacity.

Each item can either be selected once or excluded. Items cannot be divided.

## ✨ Features

- Solves the 0/1 Knapsack problem using Dynamic Programming.
- Processes multiple test cases from a text file.
- Displays a live ASCII visualization of the DP table as it is calculated.
- Calculates the maximum achievable value for each test case.
- Saves the results of all test cases to `result.txt`.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Algorithm:** Dynamic Programming
- **Visualization:** ASCII-based terminal output

## 📂 Project Structure

```text
DAA-0-1-Knapsack/
├── knapsack_visualizer_live.py
├── Knapsack data (2).txt
├── result.txt
└── README.md
```

## ⚙️ Requirements

- Python 3 installed on your system.
- A terminal or command prompt to execute the program.

No additional Python libraries are required if the program uses only Python's standard library.

## ▶️ How to Run

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the following command:

   ```bash
   python knapsack_visualizer_live.py "Knapsack data (2).txt"
   ```

4. Observe the DP table being updated in the terminal.
5. After execution, check `result.txt` for the final results of all test cases.

On some systems, you may need to use `python3` instead of `python`.

## 📥 Input Format

The input file contains multiple test cases, separated by lines beginning with `#Test`.

Each test case contains:
- The number of items `n` and knapsack capacity `W`.
- `n` subsequent lines, each containing the weight and value of an item.

## 📤 Output

For each test case, the program displays the maximum achievable value and saves the result to `result.txt`.

The results follow this format:

```text
#Test case 1 input (4 10) test result 150
#Test case 2 input (5 15) test result 100
```

The actual output file contains the results for all 10 test cases in the supplied dataset.

## 🧠 Dynamic Programming Approach

Let `DP[i][w]` represent the maximum value obtainable using the first `i` items with a knapsack capacity of `w`.

The recurrence relation is:

\[
$$
DP[i][w] =
\begin{cases}
DP[i-1][w], & \text{if } w_i > w, \\[6pt]
\max\left(DP[i-1][w],\; v_i + DP[i-1][w-w_i]\right), & \text{otherwise}.
\end{cases}
$$
\]

The final answer is `DP[n][W]`.

## ⏱️ Complexity Analysis

- **Time Complexity:** `O(nW)`
- **Space Complexity:** `O(nW)`

Here, `n` is the number of items and `W` is the knapsack capacity.

## 📊 Test Results

The program was tested using the supplied dataset containing 10 test cases.

| Test Case | Number of Items | Capacity | Maximum Value |
|---:|---:|---:|---:|
| 1 | 4 | 10 | 150 |
| 2 | 5 | 15 | 100 |
| 3 | 6 | 12 | 150 |
| 4 | 5 | 8 | 90 |
| 5 | 7 | 20 | 122 |
| 6 | 4 | 6 | 90 |
| 7 | 5 | 25 | 47 |
| 8 | 6 | 18 | 95 |
| 9 | 8 | 30 | 290 |
| 10 | 10 | 50 | 100 |

## 🎯 Conclusion

The project demonstrates the implementation of the 0/1 Knapsack problem using Dynamic Programming. It processes multiple test cases, visualizes the DP table during execution, and saves the final results to a text file.
