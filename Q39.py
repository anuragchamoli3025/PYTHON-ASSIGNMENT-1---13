# Question 39: Write a program to demonstrate the use of type() with string, list, tuple and dictionary variables.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    s = "Hello Python"
    lst = [1, 2, 3]
    tup = (1, 2, 3)
    dct = {"id": 13}
    
    print("s:", type(s))
    print("lst:", type(lst))
    print("tup:", type(tup))
    print("dct:", type(dct))

if __name__ == "__main__":
    main()