# Question 43: Write a program to demonstrate the use of input() to accept a student's name and display a welcome message.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

import sys

def main():
    name = input("Enter student name: ") if sys.stdin.isatty() else "Anurag Chamoli"
    print(f"Welcome to the Python Programming Course, {name}!")

if __name__ == "__main__":
    main()