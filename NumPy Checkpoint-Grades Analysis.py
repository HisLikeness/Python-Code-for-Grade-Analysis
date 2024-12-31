# Create a numpy array called "grades" that contains the following grades: [85, 90, 88, 92, 95, 80, 75, 98, 89, 83]
import numpy as np
Grades = np.array([85, 90, 88, 92, 95, 80, 75, 98, 89, 83])
print(Grades)

# Use numpy functions to calculate the mean, median, and standard deviation of the grades.
Grades_Mean = np.mean(Grades)
Grades_Median = np.median(Grades)
Grades_Std = np.std(Grades)

print("The mean of the Grades is:", format(Grades_Mean, ".2f"))
print("The median of the Grades is:", format(Grades_Median, ".2f"))
print("The standard deviation of the Grades is:", format(Grades_Std, ".2f"))

# Use numpy function to find the maximum and minimum of the grades.
print("The maximum grade is", np.max(Grades))
print("The minimum grade is", np.min(Grades))

# Use numpy function to sort the grades in ascending order.
print("Grades sorted in Ascending order: \n",np.sort(Grades))

# Use numpy function to find the index of the highest grade in the array.
highest_grade_index = np.argmax(Grades)
print("Index of the highest grade:", highest_grade_index)
print("Highest grade:", Grades[highest_grade_index])

# Use numpy function to find the index of the lowest grade in the array.
Lowest_grade_index = np.argmin(Grades)
print("Index of the lowest grade:", Lowest_grade_index)
print("Lowest grade:", Grades[Lowest_grade_index])

# Use numpy function to count the number of students who scored above 90.
Grades_above_90 = np.count_nonzero(Grades > 90)
print("There are", Grades_above_90, "grades above 90.")

# Use numpy function to calculate the percentage of students who scored above 90.
Percentge_of_above_90 = np.mean(Grades > 90) * 100
print("The percentage of grades above 90 is:", Percentge_of_above_90)

# Use numpy function to calculate the percentage of students who scored below 75.
Grades_below_75 = np.count_nonzero(Grades < 75)
Percentge_of_below_75 = (Grades_below_75 / len(Grades)) * 100
print("The percentage of grades below 75 is:", Percentge_of_below_75, "%")

# Use numpy function to extract all the grades above 90 and put them in a new array called "high_performers".
High_performers = Grades[Grades > 90]
print("The high performing grades are:", High_performers)

# Create a new array called "passing_grades" that contains all the grades above 75.
Passing_Grades = Grades[Grades > 75]
print("The high passing grades are:", Passing_Grades)