# Question 14: Write a program to calculate simple interest using principal, rate and time.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    principal = 50000.0  # Principal amount in INR
    rate = 7.5           # Annual rate of interest in %
    time = 3.0           # Time period in years
    
    simple_interest = (principal * rate * time) / 100
    total_amount = principal + simple_interest
    
    print(f"Principal: ₹{principal}, Rate: {rate}%, Time: {time} years")
    print(f"Simple Interest = ₹{simple_interest:.2f}")
    print(f"Total Amount = ₹{total_amount:.2f}")

if __name__ == "__main__":
    main()