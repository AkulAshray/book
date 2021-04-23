# Branching Programs

The kinds of computations we have been looking at so far are called `straight-line programs`. This means they execute code one statement at a time, one after another, in the order in which they appear and stop when they run out of statements to execute. We can't really describe anything interesting with straight-line programs, as they can be downright boring.

`Branching` programs are more interesting, the simplest branchihng programs is a `conditional`. It has three parts:
- A `test` is performed to check if a statement is evaluated as either True or False
- `if` the test evaluates as True then a block of code is executed
- `else`, an optional block of code gets executed if the test is False

After a conditional statement is executed, execution resumes at the code followiing the statement

```{figure} ifelse.png
---
height: 300px
name: Branching Programs
alt: Control Flow.
---
Branching Program Flowchart.
```


## Boolean

In Python, we perform test using an objedct called the `Boolean`, which has the type **bool** and has only two values: `True` or `False`


Truth = True
Truth

type(Truth)

lies = False
type(lies)

In Python, branching program can take the following form

```sh
if Boolean expression:
    block of code
else:
    block of code
```

or

```sh
if Boolean expression:
    block of code
```



## Comparison Operators

Boolean expressions are created in Python with the help of `comparison operators`. Python includes a variety of operators that compare values. For example, we can check if 3 is larger than 1 + 1 using the comparison operator `'>'` and it will return a boolean value. There are other comparison operators in Python


| Operator  | Description                          |
| :-------- | :----------------------------------- |
| `x == y ` | is `x` equal to `y`?                 |
| `x != y`  | is `x` not equal to `y`?             |
| `x > y`   | is `x` greater than `y`?             |
| `x >= y`  | is `x` greater than or equal to `y`? |
| `x < y`   | is `x` less than `y`?                |
| `x <= y`  | is `x` less than or equal to `y`?    |
| `x is y`  | is `x` the same object as `y`?       |

"Machine learning" == "Solve all the world's problems"

An expression can contain multiple comparison and they all must hold in order for the whole expression to be True. For example, we can express that 1+1 is between 1 and 3 using the following expression.

1 < 1 + 1 < 3

Strings can also be compared, and their order is `alphabetical`. A shorter string is less than a longer string that begins with the shorter string.

"Dog" > "Catastrophe" > "Cat"

Let's use comparison operators to create the following program that prints `"Even"` if the value of the variable $x$ is even and `"Odd"` otherwise:



```Python
if x%2 == 0:
    print('Even')
else:
    print('Odd')
print('Done with conditional')
```

The expression x%2 == 0 will evaluate to True when the remainder of $x$ divided by 2 is 0, and False otherwise. Remember than == is used for comparison, since = is reserved for assignment.

The main points to notice:
- Use keywords `if`, `elif` and `else`
- The colon `:` ends each conditional expression
- Indentation (by 4 empty space) defines code blocks
- In an `if` statement, the first block whose conditional statement returns `True` is executed and the program exits the `if` block
- `if` statements don't necessarily need `elif` or `else`
- `elif` lets us check several conditions
- `else` lets us evaluate a default block if all other conditions are `False`
- the end of the entire `if` statement is where the indentation returns to the same level as the first `if` keyword

`Indentation` is semantically meaningful in Python. For example, if the last statement in the above code were indented, it would be part of the block of code associated with the else, rather than the block of code following the conditional assignment.

Python is unusual in using indentation this way. Most other programmig languages use bracketing symbols to delineate blocks of code, see comparison below,

````{tab} Python
```python
if 20 > 18:
    print("20 is greater than 18")
```
````
````{tab} C++
```c++
if (20 > 18) {
  cout << "20 is greater than 18";
}
```
````

An advantage of Python approach is that it ensures that the visual structure of a program is an accurate representation of its semantic structure.


## Nested Conditionals

Sometimes our conditional statement may have another conditional, and they are called `nested` conditional. The code below contains nested conditionals in both branches of the top-level if statement.

x = 20

if x%2 == 0:
    if x%3 == 0:
        print('Divisible by 2 and 3')
    else:
        print('Divisible by 2 and not by 3')
elif x%3 == 0:
    print('Divisible by 3 and not by 2')

It is often convenient to use a `compound Boolean expression` in the test of a conditional. In order to create compound Boolean expression we use so called **"Boolean operators"** `and`, `or`, `not`. Their use case are shown below, and they evaluate to either True or False.

| Operator | Description |
| :---: | :--- |
|`x and y`| are `x` and `y` both True? |
|`x or y` | is at least one of `x` and `y` True? |
| `not x` | is `x` False? | 

True and True

True or False and True

Let's look at an example of how they can be used to compare three numbers...

x, y, z = 13, 34, 23
if x < y and x < z:
    print('x is least')
elif y < z:
    print('y is least')
else:
    print('z is least')


```{admonition} Try yourself
Write a program that examines three variables - $x$, $y$, and $z$ - and prints the largest even number among them. If none of them are even, it should print the smallest value of the three.
```

Python also supports `conditional expressions` as well as conditional statements. They take the form

> express1 if condition else express2

If the condition evaluates to True, the value of the entire expression is express1; otherwise it is express2. For example, the statement

```python
x = y if y > z else z
```
sets $x$ to the maximum of $y$ and $z$.
