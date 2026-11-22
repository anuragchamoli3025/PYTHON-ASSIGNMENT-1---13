# Question 11: Write a program to calculate the area and perimeter of a rectangle.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    length = 12.0
    breadth = 8.0
    
    area = length * breadth
    perimeter = 2 * (length + breadth)
    
    print(f"Length: {length}, Breadth: {breadth}")
    print(f"Area of Rectangle = {area}")
    print(f"Perimeter of Rectangle = {perimeter}")

if __name__ == "__main__":
    main()