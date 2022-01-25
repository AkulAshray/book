# Loops
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

In programming, a **loop** means repeating something multiple times.
There are different kinds of loops:

- [For loops](#for-loops) repeat something for each element of something.
- [While loops](#while-loops) repeat something while a condition is true.
- [Until loops](#until-loops) repeat something while a condition is false.

We'll talk about all of these in this tutorial.



## For loops

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


## While loops

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

## Until loops

Python doesn't have until loops. If we need an until loop, we can use
`while not`:

raining = False
while not raining:
    print("It's not raining.")
    if input("Is it raining? (y/n) ") == 'y':
        raining = True
print("It's raining!")

```{raw} html
<script
   type="text/javascript"
   src="https://utteranc.es/client.js"
   async="async"
   repo="MultiverseDF/book"
   issue-term="pathname"
   theme="github-light"
   label="💬 comment"
   crossorigin="anonymous"
/>
```