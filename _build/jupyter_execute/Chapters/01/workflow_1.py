# Basic Python Data Types

One of the most basic feature of `Python` is that it is a **object-oriented programming language**, and everything inside `Python` is an **object**. When we write programs, we essentially specify a set of actions to perform that manipuates the **object** in some capacity. Sometimes we even call the object as `value`, and each value is a piece of data that a computer program works with such as a number or text. There are different **types** of values: `42` is an integer and `"Hello!"` is a string. 

A **variable** is a name that refers to a value, it gives us a way to associate names with objects. In mathematics and statistics, we usually use variable names like $x$ and $y$. In Python, we can use any word as a variable name as long as it starts with a letter or an underscore. However, it should not be a [reserved word](https://docs.python.org/3.3/reference/lexical_analysis.html#keywords) in Python such as `for`, `while`, `class`, `lambda`, etc. as these words encode special functionality in Python that we don't want to overwrite!

It can be helpful to think of a variable as a box that holds some information (a single number, a vector, a string, etc). We use the **assignment operator** `=` to assign a value to a variable.

![](box.png)

Image taken from: [medium.com](https://www.google.com/url?sa=i&url=https%3A%2F%2Fmedium.com%2F%40stevenpcurtis.sc%2Fwhat-is-a-variable-3447ac1331b9&psig=AOvVaw3YbYfgb7XFOJ_sHP5eliob&ust=1595365663851000&source=images&cd=vfe&ved=0CA0QjhxqFwoTCMi8nrfe3OoCFQAAAAAdAAAAABAZ)

```{tip}
See the [Python 3 documentation](https://docs.python.org/3/library/stdtypes.html) for a summary of the standard built-in Python datatypes. In later chapters we will see how to create our own objects.
```

## Common built-in Python data types

| English name          | Type name  | Type Category  | Description                                   | Example                                    |
| :-------------------- | :--------- | :------------- | :-------------------------------------------- | :----------------------------------------- |
| integer               | `int`      | Numeric Type   | positive/negative whole numbers               | `42`                                       |
| floating point number | `float`    | Numeric Type   | real number in decimal form                   | `3.14159`                                  |
| boolean               | `bool`     | Boolean Values | true or false                                 | `True`                                     |
| string                | `str`      | Sequence Type  | text                                          | `"I Can Has Cheezburger?"`                 |
| list                  | `list`     | Sequence Type  | a collection of objects - mutable & ordered   | `['Ali', 'Xinyi', 'Miriam']`               |
| tuple                 | `tuple`    | Sequence Type  | a collection of objects - immutable & ordered | `('Thursday', 6, 9, 2018)`                 |
| dictionary            | `dict`     | Mapping Type   | mapping of key-value pairs                    | `{'name':'DSCI', 'code':511, 'credits':2}` |
| none                  | `NoneType` | Null Object    | represents no value                           | `None`                                     |

### Numeric data types

There are three distinct numeric types: `integers`, `floating point numbers`, and `complex numbers` (not covered here). We can determine the type of an object by using Python's in-built function `type()`. We can print the value of the object using another in-built function `print()`. You can find Pythons inbuilt functions [here](https://docs.python.org/3/library/functions.html). A `function` is simply a set of code lines which can take some input, do processing on it and return some output. We will learn more about functions later on, but for now...

Let's create a variable named x that stores the integer 7, which is the variable's value:

x = 7
type(x)

The snippet **x=2** is a `statement`. Each statement specifies a task to perform. The preceding statement creates **x** and uses the `assignment symbol` **(=)** to give **x** a value. The entire statement is an assignment variable that we read as "x is assigned the value 7". The following statement creates a variable y and assigns to it the value 42. We will even use the print() function to see what its value is:

y = 42
print(x)

In Jupyter/IPython (an interactive version of Python, based on which this book was written), the last line of a cell will automatically return as an output and so we don't actually need to explicitly state `print()`.

y # Anything after the pound/hash symbol is a comment and will not be run

Python allows multiple assignment as well. The statement

```python
x, y = 1, 2
```
binds x to 1 and y to 2. All of the expressions on the right-hand side of the assignment are evaluated before any bindings are changed. This is convenient since it allows us to use multiple assignment to swap the bindings of two variables.

For examples, the code

```python
x, y = 1, 2
x, y = y, x
print('x =', x)
print('y =', y)
```
will print

```python
x = 2
y = 1
```

pi = 3.14 # assigning a decimal point number results in a float type
type(pi)



````{admonition} Consider the code

``` python
pi = 3
radius = 11
area = pi * (radius**2)
radius = 14
```

````

The code first `binds` the names **pi** and **radius** to different objects of type `int`. It then binds the name **area** to a third object of type `int`. This is depicted on the left side of figure below.

![](binding.png)


If the program then executes `radius = 14`, the name radius is rebound to a different object of type `int` as shown on the right side. 

```{note}
This assignment has no effect on the value to which area is bound, it will still keep denoting the object by the expression `3*(11**2)`
```

### Arithmetic Operators

The code above showed example of arithmetic operator, below is a table of the syntax for common arithmetic operations in Python:

| Operator |   Description    |
| :------: | :--------------: |
|   `+`    |     addition     |
|   `-`    |   subtraction    |
|   `*`    |  multiplication  |
|   `/`    |     division     |
|   `**`   |  exponentiation  |
|   `//`   | integer division / floor division |
|   `%`    |      modulo      |

Let's have a go at applying these operators to numeric types and observe the results.

1 + 2 + 3 + 4 + 5  # add

11 * 3.14159  # multiply

2 ** 10  # exponent

```{caution} 
Division may produce a differnt `dtype` than expected, it will change `int` to `float`
```

num = 5
type(num)

num / num  # divison

When we use the syntax `//`, it allows us to do "integer division" and retain the `int` data type. It gives us the quotient after division. 

50 / 3

50 // 3

type(50 // 3)

We call this the `integer division` because its like calling the `int` function on the result of the division.

int(50 // 3)

The `%` is called the `"modulo"` operator and this gives us the remainder after doing the division. In case you are wondering how its spelled, we call the below operation as `50 mod 3`

50 % 3

We can also perform the modulo operation on objects of `float` type.

50.5 % 3

### None

There are special object in Python that has no value, we call this type as `NoneType`. This type has only one possible value - `None`

x = None

print(x)

type(x)