# String Methods
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

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

## Slicing

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

## String Methods

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

## String formatting

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

## Extra

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