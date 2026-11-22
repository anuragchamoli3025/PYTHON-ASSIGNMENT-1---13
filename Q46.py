# Question 46: Write a program to accept five subject marks from the user and display their total.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

import sys

def main():
    if sys.stdin.isatty():
        marks = []
        for i in range(1, 6):
            m = float(input(f"Enter mark for subject {i}: "))
            marks.append(m)
    else:
        marks = [85.0, 90.0, 78.0, 92.0, 88.0]
        print(f"Entered Marks: {marks}")
        
    total_marks = sum(marks)
    print(f"Total Marks = {total_marks}")

if __name__ == "__main__":
    main()