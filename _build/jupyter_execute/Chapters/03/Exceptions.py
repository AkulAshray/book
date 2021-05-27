# Exceptions
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

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

## What are exceptions?

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

## Catching exceptions

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