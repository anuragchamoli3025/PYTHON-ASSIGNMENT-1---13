# Question 15: Write a program to calculate the total and average of five subject marks.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    # Marks obtained in five subjects
    marks = [85, 92, 78, 88, 90]
    
    total = sum(marks)
    average = total / len(marks)
    
    print("Subject Marks:", marks)
    print(f"Total Marks = {total}")
    print(f"Average Marks = {average:.2f}")

if __name__ == "__main__":
    main()