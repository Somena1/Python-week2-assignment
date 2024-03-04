# Use specified integers for the list
numbers = [5, 55, 40, 70]

# Compute the sum o f all integers in the list
sum_of_numbers = sum(numbers)

print("Sum of the numbers:", sum_of_numbers)

 # Create a tuple containing five favorite books
favorite_books = ("Macmillian English", "Macmillian Mathematics", "Standard English", "Standard Literature", "Standard Mathematics")

# Print each book name on a separate line using a for loop
for book in favorite_books:
    print(book)

# Create an empty dictionary to store person's information
person = {}

# Assign Efemena's information directly
person["name"] = "Efemena"
person["age"] = "24"
person["favorite_color"] = "purple"

# Print the dictionary
print("Person's information:")
for key, value in person.items():
    print(key.capitalize() + ":", value)

 # Define the sets
set1 = {2, 4, 6, 8, 10, 20, 30}
set2 = {4, 8, 20, 40}

# Create a new set containing only the elements that are common to both sets
common_elements = set1.intersection(set2)

print("Common elements:", common_elements)

 # Store a list of words
word_list = ["bags", "shoes", "dresses", "hair", "perfume", "earings"]

# Create a new list containing only words with an odd number of characters using list comprehension
odd_length_words = [word for word in word_list if len(word) % 2 != 0]

print("Words with odd number of characters:", odd_length_words)