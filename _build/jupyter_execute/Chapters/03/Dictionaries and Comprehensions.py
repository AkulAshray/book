# Dictionaries and Comprehensions
<hr style="height:0.6px;border:none;color:#666;background-color:#666;" />

Now we know how [lists and tuples](https://ashrayshetty.netlify.app/chapters/02/list%20and%20tuples) work and how
to [for loop](https://ashrayshetty.netlify.app/chapters/02/loops) over them. If we make some kind of
program that needs to keep track of people's names and favorite pets,
we can use a list for that:

names_and_pets = [
    ('Jerry', 'cats'),
    ('Tom', 'cats and dogs'),
    ('Mario', 'cats'),
]

Then to check if cats are Mario's favorite pets we can do
`('Mario', 'cats') in names_and_pets`. Or we can add new people's
favorite pets easily by appending new `(name, pets)` tuples to the list.

But what if we need to check if we know anything about someone's
favorite pets? `'Tom' in names_and_pets` is always False because the
pet list consists of `(name, pets)` pairs instead of just names, so we
need to for loop over the whole pet list:

``` Python
found_tom = False
for pair in names_and_pets:
    if pair[0] == 'Tom':
        found_tom = True
        break
if found_tom:
    # do something
```
Or what if we need to find out what Tom's favorite pets are? That
also requires going through the whole list.

``` Python
pets = None
for pair in names_and_pets:
    if pair[0] == 'Tom':
        pets = pair[1]
        break
# make sure pets is not None and do something with it
```
As you can see, a list of `(name, pets)` pairs is not an ideal
way to store names and favorite pets.

## What are dictionaries?

A better way to store information about favorite pets might be a
dictionary. A dictionary is a mapping between key-values pairs and is defined with curly-brackets:


favorite_pets = {
    'Jerry': 'cats',
    'Tom': 'cats and dogs',
    'Mario': 'cats',
}

Here `'Jerry'` and `'Tom'` are **keys** in the dictionary, and
`'cats'` and `'cats and dogs'` are their **values**. Dictionaries are
often named by their values. This dictionary has favorite pets as its
values so the variable is named `favorite_pets`.

There are a few big differences between dictionaries and lists of pairs:

- Dictionaries are not ordered. There are **no guarantees** about which
    order the `name: pets` pairs appear in when we do something
    with the dictionary.
- Checking if a key is in the dictionary is simple and fast. We don't
    need a for loop through the whole dictionary.
- Getting the value of a key is also simple and fast.
- We can't have the same key in the dictionary multiple times, but
    multiple different keys can have the same value. This means that
    **multiple people can't have the same name, but they can have the
    same favorite pets**.

But wait... this is a lot like variables are! Our variables are not
ordered, getting a value of a variable is fast and easy and we can't
have multiple variables with the same name.

Variables are actually stored in a dictionary. We can get that
dictionary with the globals function. In this dictionary, keys are
variable names and values are what our variables point to.

## What can we do with dictionaries?

We can access a specific field of a dictionary with square brackets, this is a lot better than using `for` loop.

favorite_pets['Jerry']

We can also edit dictionaries (they are mutable):



favorite_pets['Mario'] = 'kitten'
favorite_pets

# we can also add a new key value pair like shown below
favorite_pets['Bruce'] = 'hamster'
favorite_pets


Dictionaries have some similarities with lists. For example, both
lists and dictionaries have a length.

``` Python
>>> len(names_and_pets)     # contains three elements
3
>>> len(favorite_pets)    # contains three key:value pairs
3
```

For looping over a dictionary gets its keys, and checking if something
is in the dictionary checks if the dictionary has a key like that. This
can be confusing at first but you'll get used to this.

'Bruce' in favorite_pets

'Tony' in favorite_pets

for name in favorite_pets:
    print(name)

Dictionaries have a values method that we can use if we want to do
something with the values:

favorite_pets.values()

The values method returned a `dict_values` object. Things like this
behave a lot like lists and usually we don't need to convert them to
lists.

for pets in favorite_pets.values():
    print(pets)

We can do things like `list(favorite_pets.values())` if we need a real
list for some reason, but doing that can slow down our program if the
dictionary is big. There's also a keys method, but usually we don't need
it because the dictionary itself behaves a lot like a list of keys.

If we need both keys and values we can use the items method with the
`for first, second in thing` trick.

favorite_pets.items()

for name, pets in favorite_pets.items():
    print(f"{pets} are {name}'s favorite pets")

This is also useful for checking if the dictionary has a `key: value`
pair.

('Jerry', 'cats') in favorite_pets.items()

('Dr. House', 'cats') in favorite_pets.items()

You’ll get an error if you try to access a non-existent key:

favorite_pets['Dr. House']

## Comprehensions

Comprehensions allow us to build lists/tuples/dictionaries in one convenient, compact line of code. Below is a standard `for` loop you might use to iterate over an iterable and create a list:

acronym = ['Specific', 'Measurable', 'Attainable', 'Realistic', 'Time-bound','!']
first_letters = []
for word in acronym:
    first_letters.append(word[0])
print(first_letters)

List comprehension allows us to do this in one compact line:

letters = [word[0] for word in acronym]  # list comprehension
letters

We can make things more complicated by doing multiple iteration or conditional iteration:

[(i, j) for i in range(3) for j in range(4)]

[i for i in range(11) if i % 2 == 0]  # condition the iterator, select only even numbers

[-i if i % 2 else i for i in range(11)]  # condition the value, -ve odd and +ve even numbers

There is also dictionary comprehension:

words = ['hello', 'hi', 'thanks', 'antidepressant']
word_lengths = {word:len(word) for word in words} # dictionary comprehension
word_lengths