# Functions and Exceptions
<hr style="height:0.6px;border:none;color:#666;background-color:#666;" />

We have used functions that are already available in Python, but never defineda function on our own. A [function](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) is a reusable piece of code that can accept input parameters, also known as "arguments".The purpose of defining a function is to give a name to a computational process that may be applied multiple times. There are many situations in computing that require repeated computation. For example, it is often the case that we want to perform the same manipulation on every value in a column of a table.

## Defining a Function

The definition of the `double` function below simply doubles a number.

# Our first function definition

def double(x):
    """ Double x """
    return 2 * x

Functions begin with the `def` keyword, then the function name, arguments in parentheses, and then a colon (`:`). The code executed by the function is defined by indentation. The output or "return" value of the function is specified using the `return` keyword.  Here is a breakdown of the parts (the *syntax*) of this small function:

![function syntax](function_definition.jpg)

When we run the cell above, no particular number is doubled, and the code inside the body of `double` is not yet evaluated.  In this respect, our function is analogous to a *recipe*.  Each time we follow the instructions in a recipe, we need to start with ingredients.  Each time we want to use our function to double a number, we need to specify a number.

We can call `double` in exactly the same way we have called other functions. Each time we do that, the code in the body is executed, with the value of the argument given the name `x`.

double(16)

double(64/8)

The two expressions above are both `call expressions`. In the second one, the value of the expression `64/8` is computed and then passed as the argument named `x` to the `double` function. Each call expresson results in the body of `double` being executed, but with a different value of `x`.

The body of `double` has only a single line:

`return 2*x`

Executing this *`return` statement* completes execution of the `double` function's body and computes the value of the call expression.

The argument to `double` can be any expression, as long as its value is a number.  For example, it can be a name.  The `double` function does not know or care how its argument is computed or stored; its only job is to execute its own body using the values of the arguments passed to it.

any_name = 64
double(any_name)

### Local Variables

Variables that are defined inside a function, including arguments like `double's x`, have only a fleeting existence. It is local, which means that it only exists inside the function. They are defined only while the function is being called, and they are only accessible inside the body of the function. We can't refer to `x` outside the body of `double`. The technical terminology is that `x` has `*local scope*`.

Let's look at another example

def concat(str1, str2):
    string = str1 + str2
    return string

concat('I love ', 'Python')

string

### Docstrings

Though `double` and `concat` are relatively easy to understand, many functions perform complicated tasks and are difficult to use without proper explanation. Therefore, a well-composed function has a name that evokes its behavior, as well as documentation.  In Python, this is called a *docstring* — a description of its behavior and expectations about its arguments. The docstring can also show example calls to the function, where the call is preceded by `>>>`.

A docstring can be any string, as long as it is the first thing in a function's body. Docstrings are typically defined using triple quotation marks at the start and end, which allows a string to span multiple lines. The first line is conventionally a complete but short description of the function, while following lines provide further guidance to future users of the function.

Here is a definition of a function called `percent` that takes two arguments. The definition includes a docstring.


def percent(x, total):
    """Convert x to a percentage of total.
    
    More precisely, this function divides x by total,
    multiplies the result by 100, and rounds the result
    to two decimal places.
    
    >>> percent(4, 16)
    25.0
    >>> percent(1, 6)
    16.67
    """
    return round((x/total)*100, 2)

percent(45,200)

### Null Return Type

If you do not specify a return value, the function returns `None` when it terminates:

def test_function(x):
    x + 1 # no return!
    if x == 999:
        return
print(test_function(0))

### Optional & Required Arguments

Sometimes it is convenient to have _default values_ for some arguments in a function. Because they have default values, these arguments are optional, and are hence called "optional arguments". For example:

def repeat_string(string, n=2):
    return string * n

repeat_string('Hello! ')

repeat_string('Hello! ', 6)

Ideally, the default value for optional arguments should be carefully chosen. In the function above, the idea of "repeating" something makes me think of having 2 copies, so `n=2` feels like a reasonable default.

```` {admonition} Required and Optional arguments
---
class: dropdown
---

You can have any number of required arguments and any number of optional arguments. All the optional arguments must come after the required arguments. The required arguments are mapped by the order they appear. The optional arguments can be specified out of order when using the function.

``` Python
>>> def example(a, b, c="DEFAULT", d="DEFAULT"):
        print(a, b, c, d)
    
>>> example(1, 2, 3, 4)
1 2 3 4

```
Specifying only one of the optional arguments, by keyword:
``` Python
>>> example(1, 2, c=3)
1 2 3 DEFAULT
```
Specifying keyword arguments before non-keyword arguments will give an error
``` Python
>>> example(a=2, 1)
  File "<ipython-input-23-a37b920e8205>", line 1
    example(a=2, 1)
                ^
SyntaxError: positional argument follows keyword argument

```
````


### Multiple Return Values

In many programming languages, functions can only return one object. That is technically true in Python too, but there is a "workaround", which is to return a tuple.

def sum_and_product(x, y):
    return (x + y, x * y)

sum_and_product(5, 6)

The parentheses can be omitted (and often are), and a `tuple` is implicitly returned as defined by the use of the comma: 

def sum_and_product(x, y):
    return x + y, x * y

sum_and_product(5, 6)

It is common to immediately unpack a returned tuple into separate variables, so it really feels like the function is returning multiple values:

summed, product = sum_and_product(5, 6)

summed

product

### Functions with Arbitrary Number of Arguments

You can also call/define functions that accept an arbitrary number of positional or keyword arguments using `*args` and `**kwargs`.

def add(*args):
    print(args)
    return sum(args)

add(1, 2, 3, 4, 5, 6)

def add(**kwargs):
    print(kwargs)
    return sum(kwargs.values())

add(a=3, b=4, c=5)

### Functions as  a Data Type

In Python, functions are actually a data type:

def doubles(x):
    return x + x

type(doubles)

print(doubles)

This means you can pass functions as arguments into other functions.

def say_hi(default_greet = 'Hi'):
    return default_greet

def greet_person(function, name):
    return function() + f' {name}'

greet_person(say_hi, 'Bruce')

So what happened above?
- `function()` becomes `say_hi()`

### Anonymous Functions
There are two ways to define functions in Python. The way we've beenusing up until now:

def doubles(x):
    return x + x

Or by using the `lambda` keyword:

lambda_doubles = lambda x: x + x

type(lambda_doubles)

lambda_doubles(8)

The two approaches above are identical. The one with `lambda` is called an **anonymous function**. Anonymous functions can only take up one line of code, so they aren't appropriate in most cases, but can be useful for smaller things.

## Exceptions

So far we have made programs that ask the user to enter a string, and
we also know how to convert that to an integer.

text = input("Enter something: ")
number = int(text)
print("Your number doubled:", number*2)

This code seems to work fine when a number is given as an input but doesn't work when the given input is a non-numeric type like a string or list

text = input("Enter something: ")
number = int(text)
print("Your number doubled:", number*2)

In this section we will look at how to fix that?

### What are exceptions?

In the previous example we got a ValueError (first line of our error message). ValueError is an example of a **exception** which gets raised whenever a program execution hits an unexpected condition. The interactive prompt will display an error message and keep going.

There are different types of exceptions like..

# index error
mylist = [1, 2, 5, 7]
mylist[4]

# type error
int(mylist)

**Some common error types include:**
- `SyntaxError`: Python can’t parse program
- `NameError`: local or global name not found
- `AttributeError`: attribute reference fails "
- `TypeError`: operand doesn’t have correct type
- `ValueError`: operand type okay, but value is illegal
- `IOError`: IO system reports malfunction (e.g. file not found)

If an exception occurs, the program will stop and we get an error message.

### Catching exceptions

If we need to try to do something and see if we get an exception, we
can use `try` and `except`. This is also known as **catching** the
exception.

try:
    a = int(input("Give me a number:"))
    b = int(input("Give me another number:")) 
    print(a/b)
    print ("Okay")
except:
    print("Bug in user input.")
print("Outside")

The except part doesn't run if the try part succeeds.

try:
    a = int(input("Give me a number:"))
    b = int(input("Give me another number:")) 
    print(a/b)
    print ("Okay")
except:
    print("Bug in user input.")
print("Outside")

Python tries to execute the code in the `try` block. If an error is encountered, we "catch" this in the `except` block (also called `try`/`catch` in other languages). 