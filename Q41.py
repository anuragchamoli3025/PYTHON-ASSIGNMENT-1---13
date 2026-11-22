# Question 41: Write a program to create variables using different naming conventions and display their values.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    # snake_case (standard Python convention)
    student_roll_number = 13
    
    # camelCase
    studentRollNumber = 13
    
    # PascalCase
    StudentRollNumber = 13
    
    # SCREAMING_SNAKE_CASE (for constants)
    MAX_SEATS = 60
    
    print("snake_case:", student_roll_number)
    print("camelCase:", studentRollNumber)
    print("PascalCase:", StudentRollNumber)
    print("SCREAMING_SNAKE_CASE:", MAX_SEATS)

if __name__ == "__main__":
    main()