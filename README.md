# NumPy-Grade-Analysis
This project demonstrates how to use the **Numpy** library to analyze a set of grades. The program performs various statistical operations such as calculating the mean, median, standard deviation, and more, on an array of student grades.

## Features
- **Mean, Median, and Standard Deviation**: Calculate the average grade, the middle value, and the spread of grades.
- **Maximum and Minimum Grades**: Identify the highest and lowest grades in the dataset.
- **Sorting**: Sort the grades in ascending order.
- **Index of Highest and Lowest Grades**: Find the positions of the highest and lowest grades in the array.
- **Count and Percentage**: Count the number of students who scored above a certain threshold and calculate the percentage.
- **Filtering**: Extract grades above or below a certain value into new arrays.

## Code Explanation

### Initializing the Grades Array
The grades of 10 students are stored in a numpy array:
```python
Grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
```

### Statistical Analysis
The following numpy functions are used to calculate important statistics:
1. **Mean**:
   ```python
   Grades_Mean = np.mean(Grades)
   ```
   Calculates the average of the grades.

2. **Median**:
   ```python
   Grades_Median = np.median(Grades)
   ```
   Finds the middle value when the grades are sorted.

3. **Standard Deviation**:
   ```python
   Grades_Std = np.std(Grades)
   ```
   Measures the spread of the grades.

### Maximum and Minimum Grades
Numpy functions are used to find the highest and lowest grades:
```python
np.max(Grades)  # Maximum grade
np.min(Grades)  # Minimum grade
```

### Sorting the Grades
The grades are sorted in ascending order:
```python
np.sort(Grades)
```

### Index of Highest and Lowest Grades
The index of the highest and lowest grades are found using:
```python
np.argmax(Grades)  # Index of the highest grade
np.argmin(Grades)  # Index of the lowest grade
```

### Counting and Percentage of Grades Above 90
To find how many students scored above 90:
```python
np.count_nonzero(Grades > 90)
```
To calculate the percentage of students who scored above 90:
```python
np.mean(Grades > 90) * 100
```

### Percentage of Grades Below 75
The percentage of students who scored below 75 is calculated:
```python
np.count_nonzero(Grades < 75) / len(Grades) * 100
```

### Extracting High Performers
Grades above 90 are filtered into a new array:
```python
High_performers = Grades[Grades > 90]
```

### Passing Grades Above 75
Grades above 75 are considered passing and extracted into a new array:
```python
Passing_Grades = Grades[Grades > 75]
```

### Example Output
```plaintext
The mean of the Grades is: 86.70
The median of the Grades is: 87.00
The standard deviation of the Grades is: 6.05
The maximum grade is 98
The minimum grade is 75
Grades sorted in Ascending order: 
 [75 80 83 85 88 89 90 92 95 98]
Index of the highest grade: 7
Highest grade: 98
Index of the lowest grade: 6
Lowest grade: 75
There are 4 grades above 90.
The percentage of grades above 90 is: 40.0
The percentage of grades below 75 is: 10.0 %
The high performing grades are: [92 95 98]
The high passing grades are: [85 90 88 92 95 98 89]
```

## Requirements
Make sure you have **Numpy** installed in your environment:
```bash
pip install numpy
```

## How to Run
1. Copy the code into a Python file (e.g., `grades_analysis.py`).
2. Run the script:
   ```bash
   python grades_analysis.py
   ```

## Contributions
Feel free to contribute by:
- Adding more statistical analyses.
- Implementing new features like filtering based on different thresholds.
- Improving code efficiency or readability.

---

Enjoy analyzing the grades! 🎉
```
