#1
# Create an empty list to store the results
results = []

# Iterate through the range of numbers from 2000 to 3200 (inclusive)
for number in range(2000, 3201):
    if (number % 7 == 0) and (number % 5 != 0):
        results.append(str(number))

# Print the results as a comma-separated sequence
print(", ".join(results))



############################################################################################################
#2
# Function to reverse the order of first and last name
def reverse_name_order():
    # Accept user's first and last name
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    
    # Print the names in reverse order
    print(f"{last_name} {first_name}")

# Call the function
reverse_name_order()

############################################################################################################
#3
import math

# Diameter of the sphere
diameter = 12

# Calculate the radius
radius = diameter / 2

# Calculate the volume of the sphere
volume = (4/3) * math.pi * (radius ** 3)

# Print the result
print(f"The volume of the sphere with diameter {diameter} cm is {volume:.2f} cubic centimeters.")


