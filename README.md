# PythonPT

## Basic
### 1. Variables (變數)

In programming, a variable is a named location in memory where data can be stored and retrieved. Variables in Python are used to store values, such as numbers, strings, and lists, that can be used and manipulated in your code.

To create a variable in Python, you use the assignment operator (=) to assign a value to a variable name. For example:
```x = 10```

In this example, the variable x is assigned the value 10. 
You can then use the variable x in your code by simply referring to its name:

```print(x) -> Output: 10```

It's important to note that variable names in Python can only contain letters, numbers, and underscores, and they must start with a letter or an underscore. Additionally, Python has several reserved words that cannot be used as variable names, such as if, while, and for.

### 2. If-Statements 

In Python, if-statements are used to execute code conditionally. An if-statement allows us to test a condition and execute a block of code based on the test result.
The basic syntax of an if-statement in Python is as follows:

```
if condition:
    # code to be executed if the state is True
```
For example:

```
x = 10
if x > 5:
    print("x is greater than 5")
```

In this example, the code inside the if block will be executed because the condition x > 5 is True. The code inside the if block is indented to indicate that it's part of the if statement.

We can also use elif (short for "else if") and else clauses in an if-statement to test multiple conditions and specify the code to be executed if none of the conditions are met:
```
x = 10
if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is less than or equal to 5")
```
In this example, the code inside the elif block will be executed because condition x > 5 is True, while condition x > 15 is False. 
However, the code inside the else block will not be achieved.

### Loops


## LeetCode practice
   
 1. Array
## [Relit learning](https://replit.com/@PoKaiHuang)

1. [Type of Data，input，math，String](https://colab.research.google.com/drive/1L1rmni0BsjDtkZcRSpoXKJJxxv9MtVYF?usp=sharing)
2. [Raw String，F - String，Dict，if...else，Range，while](https://colab.research.google.com/drive/1BjIARwAvbfhjGEyDrEzsuHcAaGJ1s9zr?usp=sharing)
3. [函式宣告，變數範圍Scope，Lambda 運算式](https://colab.research.google.com/drive/1qqO56TXBki-bxEjsjD6j9ld2FpAjpqcs)
4. [import package](https://github.com/pokai-huang0828/PythonPT/tree/main/Example/import_package)
5. [import os module](https://github.com/pokai-huang0828/PythonPT/tree/main/Example/useful_os_module)
