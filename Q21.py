# Question 21: Write a program to demonstrate integer, float, complex, string and Boolean data types.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    a = 13               # int
    b = 3.14159          # float
    c = 2 + 5j           # complex
    d = "UTU Dehradun"   # str
    e = True             # bool
    
    print(f"Variable a = {a}, Type: {type(a)}")
    print(f"Variable b = {b}, Type: {type(b)}")
    print(f"Variable c = {c}, Type: {type(c)}")
    print(f"Variable d = '{d}', Type: {type(d)}")
    print(f"Variable e = {e}, Type: {type(e)}")

if __name__ == "__main__":
    main()