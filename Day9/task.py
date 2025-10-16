# programming_dictionary = {
#     "Bug": "An error in a program that prevents the program from running as expected.",
#     "Function": "A piece of code that you can easily call over and over again.",
#     "Loop": "The action of doing something over and over again.",
# }
# # Retrieving items from dictionary
# print(programming_dictionary["Bug"])


# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {}
# for student, score in student_scores.items():
#     if score >= 90:
#         student_grades[student] = "Outstanding"
#     elif score >= 80:
#         student_grades[student] = "Exceeds Expectations"
#     elif score >= 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"

# print(student_grades)


# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

print(travel_log["France"]["cities_visited"][1])