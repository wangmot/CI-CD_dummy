# Program that calculates the year you turn 100 years old

def calculate_year_of_100th_birthday(name, age):
    current_year = 2024
    years_until_100 = 100 - age
    year_of_100th_birthday = current_year + years_until_100
    return year_of_100th_birthday

def main():
    print("Hello! Let's find out the year you'll turn 100 years old.")
    
    # Get user's name
    name = input("Please enter your name: ")
    
    # Get user's age and ensure it is a valid number
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                break
        except ValueError:
            print("That's not a valid age. Please enter a number.")
    
    # Calculate the year the user will turn 100
    year_of_100th_birthday = calculate_year_of_100th_birthday(name, age)
    
    # Print the result
    print(f"Hi {name}! You will turn 100 years old in the year {year_of_100th_birthday}.")

# Run the main function
if __name__ == "__main__":
    main()
