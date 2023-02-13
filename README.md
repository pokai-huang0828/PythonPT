# PythonPT

## Basic

### 1. Variables (變數)

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

```python
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

### 5. 

## LeetCode practice

 1. Array

## [Relit learning](https://replit.com/@PoKaiHuang)

1. [Type of Data，input，math，String](https://colab.research.google.com/drive/1L1rmni0BsjDtkZcRSpoXKJJxxv9MtVYF?usp=sharing)
2. [Raw String，F - String，Dict，if...else，Range，while](https://colab.research.google.com/drive/1BjIARwAvbfhjGEyDrEzsuHcAaGJ1s9zr?usp=sharing)
3. [函式宣告，變數範圍Scope，Lambda 運算式](https://colab.research.google.com/drive/1qqO56TXBki-bxEjsjD6j9ld2FpAjpqcs)
4. [import package](https://github.com/pokai-huang0828/PythonPT/tree/main/Example/import_package)
5. [import os module](https://github.com/pokai-huang0828/PythonPT/tree/main/Example/useful_os_module)
