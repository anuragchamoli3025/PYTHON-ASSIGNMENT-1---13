# Question 36: Write a program to create a dictionary containing student details such as roll number, name and marks.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    student = {
        "name": "Anurag Chamoli",
        "roll_number": 13,
        "course": "B.Tech (2nd Year, Section 1)",
        "branch": "Computer Science & Engineering (CSE)",
        "marks": 94.5
    }
    
    print("Student Details Dictionary:")
    for key, value in student.items():
        print(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()