# Question 20: Write a program to calculate the quotient and remainder of two numbers.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    dividend = 29
    divisor = 6
    
    quotient = dividend // divisor
    remainder = dividend % divisor
    
    print(f"Dividend: {dividend}, Divisor: {divisor}")
    print(f"Quotient (//): {quotient}")
    print(f"Remainder (%): {remainder}")

if __name__ == "__main__":
    main()