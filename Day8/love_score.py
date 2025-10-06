def calculate_love_score(name1, name2):
    # Combine names and convert to lowercase
    combined_names = (name1 + name2).lower()
    
    # Count occurrences of each letter in "TRUE LOVE"
    true_count = sum(combined_names.count(letter) for letter in "true")
    love_count = sum(combined_names.count(letter) for letter in "love")
    
    # Form the love score
    love_score = int(f"{true_count}{love_count}")
    
    return love_score

# Get names from user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")    

# Calculate and display love score
love_score = calculate_love_score(name1, name2)
print(f"Your love score is: {love_score}")
