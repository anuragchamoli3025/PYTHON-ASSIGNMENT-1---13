# Question 28: Write a program to demonstrate the use of abs(), round() and pow() functions.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    negative_num = -45.67
    float_num = 3.14159265
    base, exp = 4, 3
    
    print(f"abs({negative_num}) = {abs(negative_num)}")
    print(f"round({float_num}, 2) = {round(float_num, 2)}")
    print(f"pow({base}, {exp}) = {pow(base, exp)}")

if __name__ == "__main__":
    main()