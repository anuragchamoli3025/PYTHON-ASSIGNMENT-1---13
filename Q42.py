# Question 42: Write a program to demonstrate the use of the id() function for different variables.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    x = 100
    y = 100
    z = [1, 2, 3]
    
    print("Memory address of x (id):", id(x))
    print("Memory address of y (id):", id(y))
    print("Are x and y pointing to the same memory object?", id(x) == id(y))
    print("Memory address of list z (id):", id(z))

if __name__ == "__main__":
    main()