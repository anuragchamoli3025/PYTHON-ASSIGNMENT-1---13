# Question 50: Write a program to store personal details in separate variables and display them in a formatted manner.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    full_name = "Anurag Chamoli"
    roll_no = 13
    course = "B.Tech (2nd Year, Section 1)"
    branch = "Computer Science & Engineering (CSE)"
    university = "Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun"
    
    print("=" * 65)
    print("                   STUDENT PROFILE")
    print("=" * 65)
    print(f"Name         : {full_name}")
    print(f"Roll Number  : {roll_no}")
    print(f"Course       : {course}")
    print(f"Domain/Branch: {branch}")
    print(f"University   : {university}")
    print("=" * 65)

if __name__ == "__main__":
    main()