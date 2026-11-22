# Question 38: Write a program to display the length of a string, list, tuple and dictionary using len().
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    sample_str = "Uttarakhand"
    sample_list = [10, 20, 30, 40]
    sample_tuple = (1, 2, 3, 4, 5)
    sample_dict = {"a": 1, "b": 2, "c": 3}
    
    print(f"Length of string '{sample_str}': {len(sample_str)}")
    print(f"Length of list {sample_list}: {len(sample_list)}")
    print(f"Length of tuple {sample_tuple}: {len(sample_tuple)}")
    print(f"Length of dict {sample_dict}: {len(sample_dict)}")

if __name__ == "__main__":
    main()