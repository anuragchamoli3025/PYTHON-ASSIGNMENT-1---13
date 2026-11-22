# Question 35: Write a program to create a tuple containing different data types and display it.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    hetero_tuple = (101, "Roll 13", 88.5, False, (5, 6))
    
    print("Tuple with different data types:")
    print(hetero_tuple)
    for idx, item in enumerate(hetero_tuple):
        print(f"Item {idx}: {item} ({type(item).__name__})")

if __name__ == "__main__":
    main()