# Question 44: Write a program to accept two numbers from the user and display their sum.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

import sys

def main():
    if sys.stdin.isatty():
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    else:
        num1, num2 = 13.0, 27.0
        print(f"Input numbers: {num1}, {num2}")
        
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is: {total}")

if __name__ == "__main__":
    main()