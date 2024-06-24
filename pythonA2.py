#1
# Number of maximum stars in the middle row
max_stars = 5

# Generate the upper part of the pattern
for i in range(1, max_stars + 1):
    print('* ' * i)

# Generate the lower part of the pattern
for i in range(max_stars - 1, 0, -1):
    print('* ' * i)


####################################################################################################
#2
# Function to reverse the input word
def reverse_word():
    # Accept the input word from the user
    word = input("Input word: ")
    
    # Reverse the word using slicing
    reversed_word = word[::-1]
    
    # Print the reversed word
    print(f"Output: {reversed_word}")

# Call the function
reverse_word()
