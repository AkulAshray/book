# List and Tuples
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

## Why should we use lists?

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

## Our first list

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

## What can we do with lists?

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

## Tuples

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

## Examples

Here's the same program we had in the beginning of this tutorial, but
using a list:

pets = ['cat', 'dog', 'goldfish', 'gerbil', 'hamster']

name = input("What animal is your pet: ")
if name in pets:
    print("I know you!")
else:
    print("Sorry, I don't know this animal :(")