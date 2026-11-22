# Question 5: Write a program to demonstrate the use of valid and invalid Python identifiers.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    # Valid Identifiers
    student_name = "Anurag Chamoli"
    _roll_number = 13
    totalMarks2026 = 95
    BRANCH_NAME = "CSE"
    
    print("Valid Identifiers used in this program:")
    print("student_name :", student_name)
    print("_roll_number :", _roll_number)
    print("totalMarks2026 :", totalMarks2026)
    print("BRANCH_NAME :", BRANCH_NAME)
    
    print("\nRules for Invalid Identifiers (commented to prevent syntax errors):")
    print("1. 2nd_name = 'Anurag'    (Cannot begin with a digit)")
    print("2. student-name = 'Anurag' (Hyphens are not permitted)")
    print("3. for = 13                (Reserved keywords cannot be used)")
    print("4. roll no = 13            (Whitespace is not permitted)")

if __name__ == "__main__":
    main()