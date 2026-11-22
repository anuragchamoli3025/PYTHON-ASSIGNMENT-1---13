# Question 17: Write a program to convert distance from kilometres to metres and centimetres.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    km = 4.5
    
    metres = km * 1000
    centimetres = metres * 100
    
    print(f"Distance in Kilometres: {km} km")
    print(f"Equivalent in Metres: {metres:.2f} m")
    print(f"Equivalent in Centimetres: {centimetres:.2f} cm")

if __name__ == "__main__":
    main()