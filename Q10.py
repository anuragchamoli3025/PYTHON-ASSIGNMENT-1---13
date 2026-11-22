# Question 10: Write a program to swap two variables without using a temporary variable.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    a = 45
    b = 90
    print(f"Before swap: a = {a}, b = {b}")
    
    # Tuple unpacking / Pythonic swap
    a, b = b, a
    
    print(f"After swap without temp: a = {a}, b = {b}")

if __name__ == "__main__":
    main()