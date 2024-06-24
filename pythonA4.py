#1
class Triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def input_sides(self):
        self.a = float(input("Enter length of side a: "))
        self.b = float(input("Enter length of side b: "))
        self.c = float(input("Enter length of side c: "))

class Area(Triangle):
    def __init__(self):
        super().__init__()

    def calculate_area(self):
        # Semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # Area calculation using Heron's formula
        area = (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        return area

# Creating an instance of Area class
triangle = Area()
# Input the sides
triangle.input_sides()
# Calculate and print the area
print(f"The area of the triangle is: {triangle.calculate_area()}")


#2
def filter_long_words(words, n):
    return [word for word in words if len(word) > n]

# Example usage
words_list = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
n = 5
filtered_words = filter_long_words(words_list, n)
print(filtered_words)
# Output should be ['banana', 'cherry', 'elderberry']


#3
def map_words_to_lengths(words):
    return [len(word) for word in words]

# Example usage
words_list = ["ab", "cde", "erty"]
lengths = map_words_to_lengths(words_list)
print(lengths)
# Output should be [2, 3, 4]


#4
def is_vowel(char):
    vowels = 'aeiouAEIOU'
    return char in vowels

# Example usage
print(is_vowel('a'))  # Output: True
print(is_vowel('b'))  # Output: False

