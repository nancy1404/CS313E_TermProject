# **Sports Stats Tracker**

### **Team Members (Group 50)**

| Name          | GitHub Handle       | Contribution                                                                 |
|----------------|--------------------|------------------------------------------------------------------------------|
| **Nancy Kwak** | [@nancy1404](https://github.com/nancy1404) | Lead developer, algorithm implementation, testing, documentation |
| **Jooyeong Lee** | _(pending)_ | bla bla  |

---

## **Project Overview**

The **Sports Stats Tracker** is a Python-based software project developed for **CS 313E — Elements of Software Design** at The University of Texas at Austin.  

It demonstrates **object-oriented programming (OOP)**, **data structures**, and **algorithms** covered in class by processing baseball player statistics.  
The program loads a CSV dataset, computes batting averages, and allows users to:

- Sort players by **batting average** or **home runs**
- Search for a player by **player ID**
- Display **top-K performers**
- Compute **team average batting averages**

This project was completed using only **standard Python libraries** (`csv`, `heapq`) and manual algorithm implementations — no external packages.

---

## **Key Features**

| Feature | Concept Demonstrated |
|----------|----------------------|
| Data loading & parsing | File I/O using `csv.DictReader` |
| Player object model | Custom class with attributes + methods |
| Sorting | **Merge Sort** (manual recursive implementation) |
| Searching | **Binary Search** |
| Ranking | **Heap** (`heapq.nlargest`) |
| Aggregation | **Dictionary** for team averages |
| Output testing | Formatted console output and test cases |

---

## **Dataset Information**

- **Dataset Name:** `Batting.csv`  
- **Source:** [Lahman Baseball Database on Kaggle](https://www.kaggle.com/datasets/open-source-sports/baseball-databank)  
- **Columns Used:**  
  `playerID, teamID, AB, H, HR, RBI, BB, SO` (Remaining columns like yearID, 2B, 3B, etc. are part of the original Lahman dataset but not used in this project.)
- **Subset:** Only the first 20 rows are read for simplicity and speed.  
- **Computation:** Batting Average = `H / AB` (rounded to 3 decimals)

---

## **Implementation Details**

### Classes

- **`Player`**  
  Represents a single player’s batting statistics.  
  Automatically calculates the batting average when instantiated.

- **`StatsManager`**  
  Handles data loading, sorting, searching, top-K queries, and team-average calculations.

### Data Structures Used
- **List** → Stores `Player` objects  
- **Dictionary** → Maps teamID → list of averages  
- **Heap** → Finds top K performers efficiently

### Algorithms Implemented
| Algorithm | Used For | Complexity |
|------------|-----------|-------------|
| **Merge Sort** | Sorting by AVG / HR | O(n log n) |
| **Binary Search** | Finding a player ID | O(log n) |
| **Heap (Top-K)** | Retrieving top K players | O(n log k) |

All algorithms are implemented manually (no built-in `sorted()` or `bisect`).

---

## **Test Cases (Automatic)**

These are executed automatically in `main()` when you run the file.

| # | Function Tested | Input | Expected Behavior |
|---|-----------------|--------|-------------------|
| 1 | Sorting by AVG | – | Players printed in descending AVG order |
| 2 | Binary Search | `barnero01` and `nancyk05` | Find existing player, report if not found |
| 3 | Top-K Hitters | `k = 3`, by `HR` and `AVG` | Print top 3 players |
| 4 | Team Averages | – | Print dictionary of team → mean AVG |

Output examples are displayed directly in the console.

---

## **Setup and Execution**

### **Clone the Repository**
```bash
git clone https://github.com/nancy1404/CS313E_TermProject.git
cd CS313E_TermProject
```

### **Run the Program**
```bash
python3 main.py
```

### **Optional Interactive Menu**
Uncomment the line in `main()`:
```python
# stats.run_menu()
```
Then re-run the program to explore features interactively:
```
1. Display all players
2. Sort by AVG
3. Sort by HR
4. Search player
5. Show Top-K
6. Team averages
7. Exit
```

---

## **Results & Expected Output**

Example snippet (from Batting.csv subset):

```
Top 3 players by 'AVG':

1. barnero01    (BS1)  AVG: 0.401  HR:  0  RBI:  34
2. beaveed01    (TRO)  AVG: 0.400  HR:  0  RBI:   5
3. bechtge01    (PH1)  AVG: 0.351  HR:  1  RBI:  21
--------------------------

Team Average Batting Averages:

TRO: 0.217  
RC1: 0.282  
CL1: 0.198  
WS3: 0.253  
FW1: 0.141  
BS1: 0.276  
PH1: 0.200  
--------------------------
```

---

## **Next Steps / Future Improvements**

- Add user interface or GUI (front end)  
- Allow dynamic CSV selection or full dataset use  
- Handle missing data and zero AB cases more gracefully  
- Export results to CSV or JSON

---

## **References**

- Lahman Baseball Database (Kaggle): [https://www.kaggle.com/datasets/open-source-sports/baseball-databank](https://www.kaggle.com/datasets/open-source-sports/baseball-databank)  
- CS 313E Lecture Notes: Object-Oriented Programming, Sorting, Searching, Recursion, Data Structures
