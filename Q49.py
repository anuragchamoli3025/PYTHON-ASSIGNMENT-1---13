# Question 49: Write a program to demonstrate the difference between integer and floating-point values.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    int_val = 13
    float_val = 13.0
    
    print(f"int_val: {int_val} (Type: {type(int_val)})")
    print(f"float_val: {float_val} (Type: {type(float_val)})")
    
    print("Division (5 / 2):", 5 / 2, "-> Type:", type(5 / 2))
    print("Floor Division (5 // 2):", 5 // 2, "-> Type:", type(5 // 2))

if __name__ == "__main__":
    main()