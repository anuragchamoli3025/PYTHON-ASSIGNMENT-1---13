# Question 23: Write a program to convert an integer into a float and display its data type.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    num_int = 13
    print(f"Original value: {num_int}, Type: {type(num_int)}")
    
    num_float = float(num_int)
    print(f"Converted value: {num_float}, Type: {type(num_float)}")

if __name__ == "__main__":
    main()