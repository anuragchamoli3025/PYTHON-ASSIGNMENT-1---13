# Question 22: Write a program to display the data type of different variables using type().
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    roll = 13
    grade = 'A'
    percentage = 91.4
    passed = True
    subjects = ["Maths", "Python", "Physics"]
    
    print("Checking variable types using type():")
    print("roll:", type(roll))
    print("grade:", type(grade))
    print("percentage:", type(percentage))
    print("passed:", type(passed))
    print("subjects:", type(subjects))

if __name__ == "__main__":
    main()