# Question 18: Write a program to calculate the volume of a cube and a cuboid.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    # Cube
    cube_side = 6.0
    cube_volume = cube_side ** 3
    
    # Cuboid
    length, breadth, height = 8.0, 5.0, 4.0
    cuboid_volume = length * breadth * height
    
    print(f"Cube side: {cube_side} -> Volume of Cube = {cube_volume}")
    print(f"Cuboid dimensions: {length} x {breadth} x {height} -> Volume of Cuboid = {cuboid_volume}")

if __name__ == "__main__":
    main()