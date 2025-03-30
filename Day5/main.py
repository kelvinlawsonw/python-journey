# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# student_scores = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
# sum = 0
# for score in student_scores:
#     sum += score

# print(sum)


# student_scores = [150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]
# max = 0 # Initialize max to 0
# # Iterate through the list of scores
# for score in student_scores:    
#     if score > max: # If the current score is greater than max
#         max = score # Update max to the current score
# print(max)

# print(range(1, 10)) # This will print a range object

# for i in range(1, 10):
#     print(i) # This will print numbers from 1 to 9

# total = 0
# for number in range(1, 101):
#     total += number
# print(total) # This will print the sum of numbers from 1 to 100  

# fizzbuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
# This code prints numbers from 1 to 100, replacing multiples of 3 with "Fizz", multiples of 5 with "Buzz", and multiples of both with "FizzBuzz".