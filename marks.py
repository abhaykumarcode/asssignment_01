import numpy as np

marks = np.array([75, 82, 68, 90, 85, 72, 88, 95, 60, 78])


mean = np.mean(marks)
median = np.median(marks)
std_dev = np.std(marks)
maximum = np.max(marks)
minimum = np.min(marks)

print("Marks:", marks)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print("Maximum:", maximum)
print("Minimum:", minimum)