# Sequence, Loops and Methods
<hr style="height:0.6px;border:none;color:#666;background-color:#666;" />

In this section we will look at another type of data called *Sequence Type*, which is a collection of data values. `str`, `list` and `tuple` are examples of sequence types. They are specific kind of [iterable](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Iterables.html)- an object that can be "iterated over" using loops, allowing us to ask the type to give each of its items in turn. 


## In this section we will:
- Learn about basic string operations and methods
- explain the difference between mutable objects like a list and immutable objects like tuple
- write for and while loops

## String Methods

Python strings are just pieces of text. So far we looked at how to concatenate (add) them together.



greeting = 'Hello World!'
'My computer says ' + greeting

We can even repeat the strings several times by using `*` operator

greeting * 3

Python strings are [immutable](https://docs.python.org/3/glossary.html#term-immutable).
That's just a fancy way to say that
they cannot be changed in-place, and we need to create a new string to
change them. Even `some_string += another_string` creates a new string.
Python will treat that as `some_string = some_string + another_string`,
so it creates a new string but it puts it back to the same variable.

`+` and `*` are nice, but what else can we do with strings?

### Slicing

Slicing is really simple. It just means getting a part of the string.
For example, to get all characters between the second place between the
characters and the fifth place between the characters, we can do this:

greeting[0:4]

So the syntax is like `some_string[start:end]`.

This picture explains how the slicing works:

```{figure} slicing1.png
---
width: 60%
name: Slicing
alt: Slicing with non-negative values.
---
Slicing strings
```

But what happens if we slice with negative values?

greeting[-6:-3]

It turns out we can slice strings using negative values by simply starts counting
from the end of the string.

```{figure} slicing2.png
---
width: 60%
name: Slicing Strings
alt: Slicing with negative values.
---
Slicing strings using negative values
```

If we don't specify the beginning it defaults to 0, and if we don't
specify the end it defaults to the length of the string. For example, we
can get everything except the first or last character like this:

greeting[1:]

greeting[:-1]

As mentioned cannot be changed in-place, so if we write something like...

greeting[:5] = 'Hiyaa'

we get an error message

greeting[0:5]

### Indexing

So now we know how slicing works. But what happens if we forget the `:`?

greeting[1]

That's interesting. We get a string that is only one character long. But
the first character of `Hello World!` should be `H`, not `e`, so why did
we get an e?

Programming starts at zero. Indexing strings also starts at zero. The
first character is `greeting[0]`, the second character is
`greeting[1]`, and so on.

```Python
>>> greeting[0]
'H'
>>> greeting[1]
'e'
>>> greeting[2]
'l'
>>> greeting[3]
'l'
>>> greeting[4]
'o'
```

So string indexes work like this:

```{figure} indexing1.png
---
width: 60%
name: Indexing Strings
alt: Indexing Strings.
---
String Index
```

How about negative values?

greeting[-1]

We got the last character.

But why didn't that start at zero? `our_string[-1]` is the last
character, but `our_string[1]` is not the first character!

That's because 0 and -0 are equal, so indexing with -0 would do the same
thing as indexing with 0.

```Python
>>> greeting[0]
'H'
>>> greeting[-0]
'H'
```

### String Methods

Python's strings have many useful methods.
[The official documentation](https://docs.python.org/3/library/stdtypes.html#string-methods)
covers them all, but I'm going to just show some of the most commonly
used ones briefly. Python also comes with built-in documentation about
the string methods and we can run `help(str)` to read it. We can also
get help about one string method at a time, like `help(str.upper)`.

Again, nothing can modify strings in-place. Most string methods
return a new string, but things like `our_string = our_string.upper()`
still work because the new string is assigned to the old variable.

```{admonition} Also note that
All of these methods are used like `our_string.stuff()`,
not like `stuff(our_string)`. The idea with that is that our string
knows how to do all these things, like `our_string.stuff()`, we don't
need a separate function that does these things like `stuff(our_string)`. We will learn more about methods and functions later.
```

Here's an example with some of the most commonly used string methods:

all_caps = "HOW ARE YOU TODAY?"
all_caps

all_lower = all_caps.lower()
all_lower

Note that the method lower doesn't change the original string but rather returns a new one. If we check **all_caps** it will still contain the same value

all_caps

There are *many* string methods. Check out the [documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

all_caps.split()

all_caps.count("O")

We can even replace the string with a different character, by using the replace method.

# replaces all 'o' with '@'
greeting.replace('o', '@') 

# replaces just the first 'o'
greeting.replace('o', '@', 1)

We can use replace to change more than one character like
``` Python
>>> greeting.replace('World', 'Earth')
'Hello Earth!'
```

### String formatting

To add a string in the middle of another string, we can do something
like this:

name = 'Tony'
'My name is ' + name + '.'

But that gets complicated if we have too many strings to add.

Python has ways of creating strings by "filling in the blanks" and formatting them nicely. This is helpful for when you want to print statements that include variables or statements. There are a few ways of doing this but the recomended one is [f-strings](https://docs.python.org/3.6/whatsnew/3.6.html#whatsnew36-pep498). All you need to do is put the letter "f" out the front of your string and then you can include variables with curly-bracket notation `{}`.

name = "Bill Gates"
age = 65
day = 28
month = 10
year = 1955
template_new = f"Hello, my name is {name}. I am {age} years old. I was born {day}/{month:02}/{year}."
template_new

### Extra

We can use `in` and `not in` to check if a string contains another
string.


```Python
>>> greeting = "Hello World!"
>>> "Hello" in greeting
True
>>> "Python" in greeting
False
>>> "Python" not in greeting
True
```

We can get the length of a string with the `len` function. The name
`len` is short for "length".

len(greeting)

## List and Tuples

### Why should we use lists?

Sometimes we may end up doing something like this.

pet1 = 'cat'
pet2 = 'dog'
pet3 = 'goldfish'
pet4 = 'gerbil'
pet5 = 'hamster'

name = input("What animal is your pet: ")
if name == pet1 or name == pet2 or name == pet3 or name == pet4 or name == pet5:
    print("I know you!")
else:
    print("Sorry, I don't know this animal :(")

```{admonition} note
In the above code we see the function [input()](https://www.w3schools.com/python/ref_func_input.asp), which allows us to get input from the user. By default everything we enter is going to be considered as a string. 

```

This code works just fine, but there's a problem. The name check
is repetitive, and adding a new name requires adding even more
repetitive, boring checks.

### Our first list

Instead of adding a new variable for each name it might be
better to store all names in one variable. This means that our
one variable needs to point to multiple values. An easy way to
do this is using a list, we create them by putting all our pets inside `square brackets`.


pets = ['cat', 'dog', 'goldfish', 'gerbil', 'hamster']

Here the `pets` variable points to a list, which then points to
strings, like this:

```{figure} lists.png
---
width: 70%
name: Lists
alt: List of pets.
---
List of pets
```

### What can we do with lists?

In the previous section we saw that there are many things we can do with strings,
and some of these things also work with lists.

len(pets)

# This creates a new list with 'fox' inside it
pets + ['fox']

# When we check the original pets list there is no value called 'fox'
pets

With strings indexing and slicing both returned a string, but
with lists we get a new list when we're slicing and an element
from the list if we're indexing.

pets[:2]  # first two pets

pets[0] # the first pet

If we want to check if the program knows a name all we need to
do is to use the `in` keyword.

'lion' in pets

'gerbil' in pets

```{note}
We can't use this for checking if a list of names is a part of
our name list.
```Python
>>> ['cat', 'dog'] in pets
False
>>> ['goldfish'] in pets
False
```

Lists have a few [useful
methods](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists).
Some of the most commonly used ones are append, extend and remove.
`append` adds an item to the end of a list, `extend` adds
multiple items from another list and `remove` removes an item.

pets.remove('gerbil') # sorry gerbil
pets

pets.append('horse')
pets

pets.extend(['dog', 'fox'])
pets

````{important}
remove() only removes the first match it finds
``` Python
>>> pets.remove('dog')
>>> pets
['cat', 'goldfish', 'hamster', 'horse', 'dog', 'fox']

```
If we need to remove all matching items then we will need to use loops, we will learn about loops in the next section.
````

Similar to strings we can use slicing and indexing to change the content of the list.

pets[1]

pets[1] = 'puppy'
pets

As we can see, **list can be changed in-place**. In other
words, they are [**mutable**](https://medium.com/@meghamohan/mutable-and-immutable-side-of-python-c2145cf72747). Integers, floats, strings and many
other built-in types can't, so they are **immutable**.

With string we did something to them
and then set the result back to the same variable, like
`name = name.replace('i', 'u')`. This just doesn't work right with
most mutable types because they're designed to be changed in-place.

# strings are immutable and their value cant be changed
name = 'Bill'
name[1] = 'u'
name

### Tuples

Tuples are a lot like lists, but they're immutable so they
can't be changed in-place. We create them like lists, but
with `()` instead of `[]`.

``` Python
>>> thing = (1, 2, 3)
>>> thing
(1, 2, 3)
>>> thing = ()
>>> thing
()
```

If we need to create a tuple that contains only one item we
need to use `(item,)` instead of `(item)` because `(item)` is
used in places like `(1 + 2) * 3`.

num = (3) # python reads this as a number
print(num)
type(num)

num = (3,) # this gives us a tuple
print(num)
type(num)

(1 + 2) * 3

'''
In the following case it adds 1+2 to give us a tuple (3,) which is then multiplied by 3 
'''
(1 + 2,) * 3

It's also possible to create tuples by just separating things with
commas and adding no parentheses. Personally I don't like this feature,
but some people like to do it this way.

1, 2, 3

'hello', 'world'

Tuples don't have methods like append, extend and remove
because they can't change themselves in-place.

### Examples

Here's the same program we had in the beginning of this tutorial, but
using a list:

pets = ['cat', 'dog', 'goldfish', 'gerbil', 'hamster']

name = input("What animal is your pet: ")
if name in pets:
    print("I know you!")
else:
    print("Sorry, I don't know this animal :(")

## Loops


In programming, a **loop** means repeating something multiple times.
There are different kinds of loops:

- [For loops](#for-loops) repeat something for each element of something.
- [While loops](#while-loops) repeat something while a condition is true.
- [Until loops](#until-loops) repeat something while a condition is false.

We'll talk about all of these in this tutorial.



### For loops

Let's say we have a list of things we want to print. To print each item in it, we could just do a bunch of prints:

stuff = ['Hello', 'Hi', 'How are you doing', 'Im fine', 'How about you']

print(stuff[0])
print(stuff[1])
print(stuff[2])
print(stuff[3])
print(stuff[4])

But the problem with this approach is that it is only going to print five items, so if we add something new to
the list, it's not going to be printed. Likewise, if we remove something from our list, we'll get an error saying "list index out of range".

This is when for loops come in:

print("I'm starting the loop!!!")
for things in stuff:
# this is repeated for each element of stuff, that is, first for stuff[0], then for stuff[1], etc.
   print(things)
print("I'm done with loop!!!")

Without the comments, that's only two simple lines, and one variable. Much better than anything else we tried before.

The main points to notice:

* Keyword `for` begins the loop. Colon `:` ends the first line of the loop.
* Block of code indented is executed for each value in the list (hence the name "for" loops)
* We can use any variable name (in this case `things`) to refer to items in the list
* The loop ends after the variable `things` has taken all the values in the list
* We can iterate over any kind of "iterable": `list`, `tuple`, `range`, `set`, `string`.
* An iterable is really just any object with a sequence of values that can be looped over. In this case, we are iterating over the values in a list.

``` {note}
Note that `for thing in stuff:` is not same as `for (things in stuff):`.
Here the `in` keyword is just a part of the for loop and it has a
different meaning than it would have if we had `things in stuff` without
a `for`. Trying to do `for (things in stuff):` creates an error.
```

word = 'racecar'
for letter in word:
    print(f'Gimme a {letter}!')

print(f"What's that spell?!! {word}!")

A very common pattern is to use `for` with the [range()](https://www.w3schools.com/python/ref_func_range.asp). range() gives us a sequence of integers up to some value (non-inclusive of the end-value) and is typically used for looping.

range(10)

list(range(10))

for i in range(10):
    print(i)

We can also specify a start value and a skip-by value with `range`:

for i in range(1, 101, 10):
    print(i)

We can write a loop inside another loop to iterate over multiple dimensions of data:

for subjects in ['science', 'math', 'history']:
    for grade in ['a', 'b', 'c']:
        print((subjects, grade))

subjects = ['science', 'math', 'history']
grades = ['a', 'b', 'c']
for number in range(3):
    print(subjects[number], grades[number])

There are many clever ways of doing these kinds of things in Python. When looping over objects, I tend to use `zip()` and `enumerate()` quite a lot in my work. `zip()` returns a zip object which is an iterable of tuples.

for number in zip(subjects, grades):
    print(number)

We notice that the variable `number` when used with zip() function, points to a tuple. We can even "unpack" these tuples directly in the `for` loop:

for subject, grade in zip(subjects, grades):
    print(subject, grade)

`enumerate()` adds a counter to an iterable which we can use within the loop.

for i in enumerate(grades):
    print(i)

for index, value in enumerate(grades):
    print(f"index {index}, value {value}")

```` {note}
There's only one big limitation with for looping over lists. We
shouldn't modify the list in the for loop. If we do, the results can
be surprising:

``` Python
>>> stuff = ['hello', 'hi', 'how are you doing', 'im fine', 'how about you']
>>> for thing in stuff:
...     stuff.remove(thing)
...
>>> stuff
['hi', 'im fine']
```
````


### While loops

We can also use a [`while` loop](https://docs.python.org/3/reference/compound_stmts.html#while) to execute a block of code several times. They are very similar to how a if statement works. But beware! If the conditional expression is always `True`, then you've got an infintite loop! 

its_raining = True
if its_raining:
    print("Oh! it's raining!")

While loop would look something like this

``` Python
its_raining = True
while its_raining:
    print("Oh! it's raining!")
    # we'll jump back to the line with the word "while" from here
print("It's not raining anymore.")
```

If you're not familiar with while loops, the program's output may be a
bit surprising:

    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    Oh! it's raining!
    (much more raining)

Again, this program does not break your computer. It just prints the
same thing multiple times. We can interrupt it by pressing Ctrl+C.

In this example, `its_raining` was the **condition**. If something in
the while loop would have set `its_raining` to False, the loop would
have ended and the program would have printed `It's not raining anymore`.

Let's actually create a program that does just that:

its_raining = True
counter = 1
while its_raining and counter < 11:
    print(f"{counter} Oh! it's raining!")
    counter = counter + 1
    
print("It's not raining anymore.")

Let's read the `while` statement above as if it were in English. It means, “While `its_raining` is True and the value of counter is less than 10, display the print statement and then increase counter by 1. When the counter reaches 10, it ends the loop”.

Hence, in some cases, we may want to force a `while` loop to stop based on some criteria, using the `break` keyword.

number = 123
counter = 0
while number != 1:
    print(int(number))
    if number % 2 == 0: # number is even
        number = number / 2
    else: # number is odd
        number = number * 3 + 1
    counter = counter + 1
    if counter == 10:
        print(f"Ugh, too many iterations!")
        break

The `continue` keyword is similar to `break` but won't stop the loop. Instead, it just restarts the loop from the top.

number = 10
while number > 0:
    if number % 2 != 0: # n is odd
        number = number - 1
        continue
        break  # this line is never executed because continue restarts the loop from the top
    print(number)
    number = number - 1

print("Blast off!")

### Until loops

Python doesn't have until loops. If we need an until loop, we can use
`while not`:

raining = False
while not raining:
    print("It's not raining.")
    if input("Is it raining? (y/n) ") == 'y':
        raining = True
print("It's raining!")