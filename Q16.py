# Question 16: Write a program to convert temperature from Celsius to Fahrenheit.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    celsius = 37.0
    # Formula: F = (C * 9/5) + 32
    fahrenheit = (celsius * 9 / 5) + 32
    
    print(f"Temperature in Celsius: {celsius}°C")
    print(f"Temperature in Fahrenheit: {fahrenheit:.2f}°F")

if __name__ == "__main__":
    main()