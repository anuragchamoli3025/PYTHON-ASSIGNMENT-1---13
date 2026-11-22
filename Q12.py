# Question 12: Write a program to calculate the area and circumference of a circle.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

import math

def main():
    radius = 7.0
    
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    
    print(f"Radius: {radius}")
    print(f"Area of Circle = {area:.2f}")
    print(f"Circumference of Circle = {circumference:.2f}")

if __name__ == "__main__":
    main()