# Question 24: Write a program to convert a floating-point number into an integer.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    num_float = 99.85
    print(f"Original Float: {num_float}, Type: {type(num_float)}")
    
    num_int = int(num_float)
    print(f"Converted Integer: {num_int}, Type: {type(num_int)}")

if __name__ == "__main__":
    main()