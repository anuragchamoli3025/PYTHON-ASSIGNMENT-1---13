# Question 26: Write a program to accept a number as a string and convert it into an integer.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    # Simulating input or reading from user
    str_input = "250"
    print(f"Input as string: '{str_input}', Type: {type(str_input)}")
    
    converted_int = int(str_input)
    print(f"Converted to integer: {converted_int}, Type: {type(converted_int)}")
    print(f"Result of arithmetic operation (+ 10): {converted_int + 10}")

if __name__ == "__main__":
    main()