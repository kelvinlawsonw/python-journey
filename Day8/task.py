# def greet():
#     print("Hello, welcome to Day 8!")
#     print("Let's start coding!")
#     print("Good luck!")

# greet()

# Functions that allow inputs
# def greet_with_name(name):
#     print(f"Hello, {name}! Welcome to Day 8!")
#     print("Let's start coding!")
#     print("Good luck!")

# greet_with_name("Alice")


# def life_in_weeks(age):
#     years_remaining = 90 - age
#     weeks_remaining = years_remaining * 52
#     print(f"You have {weeks_remaining} weeks left.")

# life_in_weeks(25)

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

greet_with(location="Wonderland", name="Alice")
