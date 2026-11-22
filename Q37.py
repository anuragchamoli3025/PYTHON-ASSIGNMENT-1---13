# Question 37: Write a program to create a dictionary containing five countries and their capitals.
# Student Name: Anurag Chamoli | Roll Number: 13
# Course: B.Tech (2nd Year, Section 1) | Branch: Computer Science & Engineering (CSE)
# University: Veer Madho Singh Bhandari Uttarakhand Technical University, Dehradun

def main():
    country_capitals = {
        "India": "New Delhi",
        "Japan": "Tokyo",
        "France": "Paris",
        "Australia": "Canberra",
        "Canada": "Ottawa"
    }
    
    print("Countries and Capitals:")
    for country, capital in country_capitals.items():
        print(f"{country} -> {capital}")

if __name__ == "__main__":
    main()