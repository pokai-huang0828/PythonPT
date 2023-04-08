# PythonPT

0. [Startup](/LeetCode_PT/Basic/Startup.py)
1. [Variables](#1-variables)
2. [If-Statements](#2-if-statements)
3. [Loops](#3-loops)
4. [Math](#4-math)
5. [Arrays](#5-arrays)
6. [Sorting](#6-sorting)
   1. [Advance sorting with modules](#advanced-sorting-with-modules)
7. [Strings](#7-strings)
8. [Queues](#8-queues)
   1. [Basic queue implementation](#basic-queue-implementation)
   2. [Advance queue implementation](#advanced-queue-implementation)
9. [HashSets](#9-hashsets)

## LeetCode practice

 1. Array
    1. [Max Consecutive Ones](/LeetCode_PT/Array/maxConsecutiveOnes_485.py)
    2. [Find Numbers with Even Number of Digits](/LeetCode_PT/Array/findNumberswithEvenNumberofDigits_.py)
    3. [Squares of a Sorted Array](/LeetCode_PT/Array/squaresofSortedArray_977.py) 
    4. [Duplicate Zero](/LeetCode_PT/Array/duplicateZeros_1089.py)


## Other Learning Notes
1. [Relit learning](https://replit.com/@PoKaiHuang)
1. [Type of Data，input，math，String](/Example/CoLab/py01.ipynb)
2. [Raw String，F - String，Dict，if...else，Range，while](/Example/CoLab/py02.ipynb)
3. [函式宣告，變數範圍Scope，Lambda 運算式](/Example/CoLab/py03.ipynb)
4. [import package](https://github.com/pokai-huang0828/PythonPT/tree/main/Example/import_package)


## Basic

### 1. Variables

In programming, a variable is a named location in memory where data can be stored and retrieved. Variables in Python are used to store values, such as numbers, strings, and lists, that can be used and manipulated in your code.

To create a variable in Python, you use the assignment operator (=) to assign a value to a variable name.
For example:

```python
x = 10
```

In this example, the variable x is assigned the value 10.
You can then use the variable x in your code by simply referring to its name:

```python
print(x) -> Output: 10
```

It's important to note that variable names in Python can only contain letters, numbers, and underscores, and they must start with a letter or an underscore. Additionally, Python has several reserved words that cannot be used as variable names, such as if, while, and for.

### 2. If-Statements

In Python, if-statements are used to execute code conditionally. An if-statement allows us to test a condition and execute a block of code based on the test result.
The basic syntax of an if-statement in Python is as follows:

```python
if condition:
    # code to be executed if the state is True
```

For example:

```python
x = 10
if x > 5:
    print("x is greater than 5")
```

In this example, the code inside the if block will be executed because the condition x > 5 is True. The code inside the if block is indented to indicate that it's part of the if statement.

We can also use elif (short for "else if") and else clauses in an if-statement to test multiple conditions and specify the code to be executed if none of the conditions are met:

```py
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is less than or equal to 5")
```

In this example, the code inside the elif block will be executed because condition ```x > 5``` is True, while condition ``` x > 15 ``` is False.
However, the code inside the else block will not be achieved.

### 3. Loops

In Python, loops allow us to repeat a code block multiple times. Python has two types of loops: **for loops** and **while loops**.
A for loop is used to iterate over a sequence (such as a list, tuple, or string) and execute a code block for each item.
The basic syntax of a for loop in Python is as follows:

```py
for item in sequence:
    # code to be executed for each item in the sequence
```

For example:

```py
fruits = ["apple",  "banana",  "cherry"]
for fruit in fruits:
    print(fruit)
```

In this example, the code inside the for loop will be executed once for each item in the list fruits. The output will be:

```py
apple
banana
cherry
```

On the other hand, a while loop is used to repeatedly execute a block of code as long as a specific condition is True.
The basic syntax of a while loop in Python is as follows:

```py
while condition:
    # code to be executed as long as the situation is True
```

For example:

```py
x = 1
while x <= 5:
    print(x)
    x = x + 1
```

In this example, the code inside the while loop will be executed repeatedly if the condition ```x <= 5``` is True. The output will be:

```py
1
2
3
4
5
```

It's essential to be careful when using while loops, as they can lead to infinite loops if the condition is never False.
To avoid this, we should always ensure that the situation will eventually become False.

### 4. Math

Using built-in operators, we can perform basic mathematical operations in Python, such as addition, subtraction, multiplication, and division.
Here's a list of the basic arithmetic operators in Python:

* **+** -->     Addition
* **-** -->     Subtraction
* **\*** -->    Multiplication
* **/** -->     Division (floating-point division)
* **//** -->    Floor division (integer division)
* **%** -->     Modulo (returns the remainder of a division operation)
* **\*\*** -->  Exponentiation (raising a number to a power)

For example:

```py
a = 5
b = 2

c = a + b
print("a + b =", c)

d = a - b
print("a - b =", d)

e = a * b
print("a * b =", e)

f = a / b
print("a / b =", f)

g = a // b
print("a // b =", g)

h = a % b
print("a % b =", h)

i = a ** b
print("a ** b =", i)
```

In this example, we assign values to the variables a and b.
Then we use the basic arithmetic operators to perform various mathematical operations, such as addition, subtraction, multiplication, and division.
The output will be:

```py
a + b = 7
a - b = 3
a * b = 10
a / b = 2.5
a // b = 2
a % b = 1
a ** b = 25
```

We can also perform various mathematical operations using the built-in math module for more options. This module provides various mathematical functions and constants, such as:

* ```math.pi```: the mathematical constant pi (π)
* ```math.e```: the mathematical constant e
* ```math.sqrt(x)```: the square root of x
* ```math.ceil(x)```: the smallest integer greater than or equal to x
* ```math.floor(x)```: the largest integer less than or equal to x
* ```math.pow(x, y)```: x raised to the power of y
* ```math.exp(x)```: the exponential function e^x
* ```math.log(x)```: the natural logarithm of x
* ```math.log10(x)```: the base-10 logarithm of x
* ```math.degrees(x)```: convert radian x to degrees
* ```math.radians(x)```: convert degree x to radians

For example:

```py
import math

x = math.pi
print("The value of pi is:", x)

y = math.sqrt(16)
print("The square root of 16 is:", y)

z = math.pow(2, 3)
print("2 raised to the power of 3 is:", z)
```

In this example, we import the math module and use it to perform various mathematical operations, such as finding the value of pi and the square root of 16 and raising 2 to the power of 3.
The output will be:

```py
The value of pi is: 3.141592653589793
The square root of 16 is: 4.0
2 raised to the power of 3 is: 8.0
```

### 5. Arrays

The built-in list type can be used in Python as an array. A list is an ordered collection of elements, and we can access the parts of a list using an index just like you would with an array in other programming languages.
Here's an example of how to create a list in Python:

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Output:
[1, 2, 3, 4, 5]
```

We can access the elements of the list using their index:

```py
print(my_list[0])  # Output: 1
print(my_list[2])  # Output: 3
```

We can also modify the elements of the list:

```py
my_list[1] = 7
print(my_list)  # Output: [1, 7, 3, 4, 5]
```

One crucial difference between a Python list and a traditional array in other programming languages is that a Python list can hold elements of different data types.
For example, we can create a list like this:

```py
mixed_list = [1, "hello", 3.14, True]
print(mixed_list)
# Output:
[1, 'hello', 3.14, True]
```

Python also provides several built-in functions to manipulate arrays, such as len() to get the length of the array, append() to add an element to the end of the array, and remove() to remove an element from the array.

Here are some examples of how to use these built-in functions:

```py
my_array = [1, 2, 3, 4, 5]

# Get the length of the array
print(len(my_array))  # Output: 5

# Add an element to the end of the array
my_array.append(6)
print(my_array)  # Output: [1, 2, 3, 4, 5, 6]

# Remove an element from the array
my_array.remove(3)
print(my_array)  # Output: [1, 2, 4, 5, 6]
```

We can also use slicing to access a subset of the array. For example:

```py
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Get the first three elements of the array
print(my_array[:3])  # Output: [1, 2, 3]

# Get the last three elements of the array
print(my_array[-3:])  # Output: [8, 9, 10]

# Get every other element of the array
print(my_array[::2])  # Output: [1, 3, 5, 7, 9]
```

Overall, while Python lists are not true arrays in the strict sense, they provide a flexible and convenient way to store and manipulate data collections.

### 6. Sorting

 In Python, sorting is arranging a sequence of elements in a specific order. Several built-in functions and modules can also be used for sorting.
Basic Sorting with Built-In Functions

##### sorted()

The sorted() function is a built-in function that can be used to sort any iterable, such as a list, tuple, or string. It returns a new sorted list:

```py
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list)
print(sorted_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

The sorted() function can also accept a reverse parameter to sort the iterable in descending order:

```py
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
```

##### sort()

The sort() method is a list method that sorts the list in place:

```py
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort()
print(my_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

The sort() method can also accept a reverse parameter to sort the list in descending order:

```py
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
my_list.sort(reverse=True)
print(my_list)  # Output: [9, 6, 5, 5, 5, 4, 3, 3, 2, 1, 1]
```

#### Advanced Sorting with Modules

##### heapq

The heapq module provides functions for working with heaps and specialized data structures for maintaining a collection of elements in a specific order. In addition, the heapq module provides two functions for sorting iterable:

```py
import heapq

my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
heapq.heapify(my_list)  # Convert the list to a heap
sorted_list = [heapq.heappop(my_list) for i in range(len(my_list))]
print(sorted_list)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

The heapify() function converts the iterable to a heap.
The heappop() function removes and returns the smallest element from the heap, so calling it len(my_list) times will return a sorted list.

##### bisect

The bisect module provides functions for working with sorted lists. For example, the bisect_left() and bisect_right() functions can be used to insert an element into a sorted list while maintaining the sort order:

```py
import bis

my_list = [1, 2, 4, 4, 4, 7] 
index = bisect.bisect_left(my_list, 4) 
my_list.insert(index, 4) 
print(my_list) # Output: [1, 2, 4, 4, 4, 4, 7]
```

The `bisect_left()` function returns the index where the new element should be inserted to maintain the sort order.
In this example, the element `4` is inserted after the first occurrence of `4`.

The `insort_left()` and `insort_right()` functions are similar to `bisect_left()` and `bisect_right()`, but they also insert the new element into the list:

```python
import bisect

my_list = [1, 2, 4, 4, 4, 7]
bisect.insort_left(my_list, 5)
print(my_list)  # Output: [1, 2, 4, 4, 4, 5, 7]
```

The insort_left() function inserts the new element into the list at the index returned by bisect_left(), maintaining the sort order.

Overall, Python provides various functions and modules for sorting data collections, from basic built-in functions to more advanced modules like heapq and bisect.

### 7. Strings

In Python, a string is a sequence of characters enclosed in quotes. Strings can be created using single quotes (') or double quotes ("). 
Here are some examples:

```py
my_string = 'Hello, World!'
my_other_string = "This is a string."
```

Strings are a fundamental data type in Python and are used to represent textual data. 
Here are some basic operations you can perform on strings:

```py
# Concatenation
my_string = 'Hello, ' + 'World!'
print(my_string)  # Output: 'Hello, World!'

# Repetition
my_string = 'Hello' * 3
print(my_string)  # Output: 'HelloHelloHello'

# Indexing
my_string = 'Hello, World!'
print(my_string[0])  # Output: 'H'
print(my_string[-1])  # Output: '!'

# Slicing
my_string = 'Hello, World!'
print(my_string[0:5])  # Output: 'Hello'
print(my_string[7:])  # Output: 'World!'
```

We can also use several built-in functions to manipulate strings, such as len() to get the length of a string, split() to split a string into a list of substrings, and join() to join a list of substrings into a string.
Here are some examples:

```py
# Length
my_string = 'Hello, World!'
print(len(my_string))  # Output: 13

# Split
my_string = 'Hello, World!'
my_list = my_string.split(',')
print(my_list)  # Output: ['Hello', ' World!']

# Join
my_list = ['Hello', 'World', '!']
my_string = '-'.join(my_list)
print(my_string)  # Output: 'Hello-World-!'
```

Python also provides several advanced features for working with strings, such as regular expressions, which are patterns used to match and manipulate strings. The re module provides functions for working with regular expressions:

```py
import re

# Find all occurrences of 'cat' or 'dog' in the string
my_string = 'The cat and the dog slept.'
matches = re.findall(r'cat|dog', my_string)
print(matches)  # Output: ['cat', 'dog']
```

In Python, strings are a fundamental data type, and they provide a powerful and flexible way to work with textual data.

### 8. Queues

A queue is a data structure that stores a collection of elements and allows us to add elements to the back of the queue and remove elements from the front. Several built-in and third-party modules can be used in Python to implement queues.

#### Basic Queue Implementation

##### Using List

One way to implement a queue in Python is to use a list. You can add elements to the back of the list using the append() method and remove elements from the front of the list using the pop() method:

```py
my_queue = []
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
print(my_queue)  # Output: [1, 2, 3]
my_queue.pop(0)
print(my_queue)  # Output: [2, 3]
```

However, this implementation could be more efficient because removing elements from the front of the list requires shifting all the remaining elements to the left.
Using Deque
A more efficient way to implement a queue in Python is to use the deque class from the collections module. Deque is short for "double-ended queue," and it provides methods for adding elements to both the front and back of the queue, as well as removing elements from both the front and back of the queue:

```py
from collections import deque

my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)
print(my_queue)  # Output: deque([1, 2, 3])
my_queue.popleft()
print(my_queue)  # Output: deque([2, 3])
```

#### Advanced Queue Implementation

##### Using Queue Module

Python also provides a built-in queue module that provides classes for implementing queues. The queue module provides several classes, including Queue, LifoQueue, and PriorityQueue. The queue is a class for implementing a basic first-in, first-out (FIFO) queue:

```py
import queue

my_queue = queue.Queue()
my_queue.put(1)
my_queue.put(2)
my_queue.put(3)
print(my_queue.queue)  # Output: [1, 2, 3]
my_queue.get()
print(my_queue.queue)  # Output: [2, 3]
```

The put() method adds an element to the back of the queue, and the get() method removes an element from the front.
Using Priority Queue
The PriorityQueue class is a class for implementing a priority queue, where elements are stored in the queue in order of priority. Elements with higher priority are dequeued first. To use a priority queue, you need to define a key function that takes an element as input and returns its priority. 
Here's an example:

```py
import queue

def get_priority(item):
    return item[1]

my_queue = queue.PriorityQueue()
my_queue.put(('A', 3))
my_queue.put(('B', 2))
my_queue.put(('C', 1))
print(my_queue.queue)  # Output: [('C', 1), ('B', 2), ('A', 3)]
my_queue.get()
print(my_queue.queue)  # Output: [('B', 2), ('A', 3)]
```

In this example, the priority queue is implemented as a queue of tuples. The first element of the tuple is the item to be stored in the queue, and the second element is its priority. The get_priority() function takes an element as input and returns its priority. The PriorityQueue class uses the key function to store the elements in the queue in order of priority.

### 9. HashSets

A hash set is a data structure that stores a collection of unique elements in no particular order and allows for constant-time insertion, deletion, and lookup of elements. The set data type in Python is implemented using a hash table, which allows for constant-time operations.
Basic Usage
Here's an example of using a set to implement a basic hash set:

```py
my_set = set()
my_set.add(1)
my_set.add(2)
my_set.add(3)
print(my_set)  # Output: {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}
```

In this example, we create a new set, add some elements to it using add(), and remove an element using remove().
Advanced Usage
Frozenset
A frozenset is an immutable set that can be used as a key in a dictionary or as an element of another set. It is helpful in situations where you need to store a set of sets or where you need to use a set as a key in a dictionary.

```py
my_set = frozenset([1, 2, 3])
my_dict = {my_set: 'value'}
print(my_dict)  # Output: {frozenset({1, 2, 3}): 'value'}
```

In this example, we create a new frozenset from a regular set and use it as a key in a dictionary.
Set Comprehension
Set comprehension creates a new set from an iterable, using a compact and readable syntax. It is similar to list comprehension but produces a set instead of a list.

```py
my_list = [1, 2, 3, 4, 5]
my_set = {x for x in my_list if x % 2 == 0}
print(my_set)  # Output: {2, 4}
```

In this example, we use set comprehension to create a new set that contains only the even numbers from a list.
Set Operations
Sets support several operations, including union, intersection, difference, and symmetric difference. Here's an example:

```py
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2))           # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2))    # Output: {4, 5}
print(set1.difference(set2))      # Output: {1, 2, 3}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 3, 6, 7, 8}
```

In this example, we create two sets and perform various set operations on them, including union, intersection, difference, and symmetric difference.
