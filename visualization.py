# Data Visualization Project - Developed by Iram
# Using Matplotlib to Analyze Student Performance

import matplotlib.pyplot as plt

# Data
subjects = ['Python', 'Math', 'English', 'Science', 'Urdu']
marks = [85, 78, 92, 88, 75]
students = ['Ali', 'Iram', 'Sara', 'Ahmed', 'Ayesha']
python_marks = [85, 95, 70, 88, 92]

# 1. Bar Chart - Subject-wise Marks
plt.figure(figsize=(8, 5))
plt.bar(subjects, marks, color=['red', 'green', 'blue', 'orange', 'purple'])
plt.title('Subject-wise Marks - Developed by Iram', fontsize=14, fontweight='bold')
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.ylim(0, 100)
plt.savefig('bar_chart.png')
plt.show()

# 2. Line Chart - Student Performance in Python
plt.figure(figsize=(8, 5))
plt.plot(students, python_marks, marker='o', color='purple', linewidth=2, markersize=10)
plt.title('Python Marks - Student Comparison', fontsize=14, fontweight='bold')
plt.xlabel('Students')
plt.ylabel('Marks in Python')
plt.grid(True)
plt.savefig('line_chart.png')
plt.show()

# 3. Pie Chart - Marks Distribution
plt.figure(figsize=(7, 7))
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90, colors=['red', 'blue', 'green', 'orange', 'purple'])
plt.title('Marks Distribution by Subject', fontsize=14, fontweight='bold')
plt.savefig('pie_chart.png')
plt.show()

print("All charts created successfully! - By Iram")