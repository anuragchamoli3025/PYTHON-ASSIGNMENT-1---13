# Question 48: Write a program to demonstrate the use of print() with multiple variables and formatted output.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    name = "Anurag Chamoli"
    roll = 13
    marks = 94.75
    
    print("Student Details:", name, roll, sep=" | ")
    print("Formatted with .format(): Name = {}, Roll = {}, Marks = {:.2f}".format(name, roll, marks))
    print(f"Formatted with f-string : Name = {name}, Roll = {roll}, Marks = {marks:.2f}")

if __name__ == "__main__":
    main()