#1
def myreduce(function, iterable, initializer=None):
    # Get an iterator from the iterable
    it = iter(iterable)
    
    # If initializer is provided, use it as the initial value
    if initializer is None:
        try:
            # The first value from the iterator
            value = next(it)
        except StopIteration:
            raise TypeError("myreduce() of empty sequence with no initial value")
    else:
        value = initializer

    # Apply the function cumulatively to the items of the iterable
    for element in it:
        value = function(value, element)
    
    return value

# Example usage
def add(x, y):
    return x + y

result = myreduce(add, [1, 2, 3, 4])
print(result) 

#2
def myfilter(function, iterable):
    # If the function is None, use the identity function
    if function is None:
        function = bool
    
    # Create a generator to yield items for which the function returns True
    return (item for item in iterable if function(item))

# Example usage
def is_even(n):
    return n % 2 == 0

result = myfilter(is_even, [1, 2, 3, 4, 5, 6])
print(list(result)) 

#3
list1 = [letter for letter in 'ACADGILD']
print(list1)
# Output: ['A', 'C', 'A', 'D', 'G', 'I', 'L', 'D']

list2 = [char * i for char in 'xyz' for i in range(1, 5)]
print(list2)
# Output: ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']

list3 = [char * i for i in range(1, 5) for char in 'xyz']
print(list3)
# Output: ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']

list4 = [[i + j] for i in range(2, 5) for j in range(3)]
print(list4)
# Output: [[2], [3], [4], [3], [4], [5], [4], [5], [6]]

list5 = [[i + j for i in range(2, 6)] for j in range(4)]
print(list5)
# Output: [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]

list6 = [(i, j) for j in range(1, 4) for i in range(1, 4)]
print(list6)
# Output: [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]






