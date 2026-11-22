# Question 27: Write a program to demonstrate the use of int(), float() and str() functions.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    val = "100"
    
    int_val = int(val)
    float_val = float(val)
    str_val = str(float_val)
    
    print(f"Using int('{val}'): {int_val} (Type: {type(int_val)})")
    print(f"Using float('{val}'): {float_val} (Type: {type(float_val)})")
    print(f"Using str({float_val}): '{str_val}' (Type: {type(str_val)})")

if __name__ == "__main__":
    main()