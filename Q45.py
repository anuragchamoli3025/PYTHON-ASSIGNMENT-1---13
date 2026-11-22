# Question 45: Write a program to accept the length and breadth of a rectangle and display its area.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

import sys

def main():
    if sys.stdin.isatty():
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
    else:
        length, breadth = 15.0, 8.0
        print(f"Length: {length}, Breadth: {breadth}")
        
    area = length * breadth
    print(f"Area of Rectangle: {area}")

if __name__ == "__main__":
    main()