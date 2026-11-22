# Question 33: Write a program to create a list containing different data types.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    mixed_list = [13, "Uttarakhand", 3.14, True, [1, 2]]
    
    print("Mixed data type list:", mixed_list)
    for index, element in enumerate(mixed_list):
        print(f"Element at index {index}: {element} (Type: {type(element).__name__})")

if __name__ == "__main__":
    main()