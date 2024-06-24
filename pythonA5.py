#1
def compute_division():
    try:
        result = 5 / 0
        print("Result of division:", result)  # This line won't be reached if an exception occurs
    except ZeroDivisionError:
        print("Error: Division by zero!")

# Example usage
compute_division()


#2
subjects = ["Americans", "Indians"]
verbs = ["play", "watch"]
objects = ["Baseball", "Cricket"]

# Generate all sentences
for subject in subjects:
    for verb in verbs:
        for obj in objects:
            sentence = f"{subject} {verb} {obj}."
            print(sentence)
