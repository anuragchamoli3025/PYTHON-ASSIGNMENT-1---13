# Question 47: Write a program to demonstrate the use of list(), tuple() and dict() constructors.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    # list constructor
    l = list((1, 2, 3, 4))
    
    # tuple constructor
    t = tuple([5, 6, 7, 8])
    
    # dict constructor
    d = dict(roll=13, course="Python", university="UTU")
    
    print("Constructed list:", l, type(l))
    print("Constructed tuple:", t, type(t))
    print("Constructed dict:", d, type(d))

if __name__ == "__main__":
    main()