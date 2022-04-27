# Introduction to Numpy
<hr style="height:0.6px;border:none;color:#666;background-color:#666;" />

![](numpy.png)

NumPy stands for "Numerical Python" and it is the standard Python library used for working with arrays (i.e., vectors & matrices), linear algerba, and other numerical computations. NumPy is written in C, making NumPy arrays faster and more memory efficient than Python lists or arrays, read more: ([link 1](https://www.datadiscuss.com/proof-that-numpy-is-much-faster-than-normal-python-array/), [link 2](https://www.jessicayung.com/numpy-arrays-memory-and-strides/), [link 3](https://www.labri.fr/perso/nrougier/from-python-to-numpy/)).

NumPy can be installed using `conda` (if not already):

```
conda install numpy
```

Knowing how to use Numpy is *essential* in domains such as machine learning, image analysis, and image processing.

Let's start by importing numpy, which is commonly done as follows:

import numpy as np

## NumPy Arrays
<hr>

### What are Arrays?
Arrays are "n-dimensional" data structures that can contain all the basic Python data types, e.g., floats, integers, strings etc, but work best with numeric data. `ndarrays` (which stands for *n*-*d*imensional array) are homogenous, which means that items in the array should be of the same type. ndarrays are also compatible with numpy's vast collection of in-built functions!

![](numpy_arrays.png)

Source: [Medium.com](https://medium.com/hackernoon/10-machine-learning-data-science-and-deep-learning-courses-for-programmers-7edc56078cde)



### Python lists vs. numpy arrays
Basically, numpy arrays are a lot like Python lists. The major difference, however, is that *numpy arrays may contain only a single data-type*, while Python lists may contain different data-types within the same list.

Let check this out:

# Python lists may contain mixed data-types: an integer, a float, a string, a list
python_list = [1, 2.5, "whatever", [3, 4, 5]] 

for value in python_list:
    
    print(f"{str(value)} is a: {type(value)}")

Unlike Python lists, numpy only allows entries of the same data-type. In fact, if you try to make a numpy array with different data-types, numpy will force the entries into the same data-type (in a smart way), as is shown in the example below:

# Importantly, you often specify your arrays as Python lists first, and then convert them to numpy
to_convert_to_numpy = [1, 2, 3.5]               # specify python list ...
numpy_array = np.array(to_convert_to_numpy)     # ... and convert ('cast') it to numpy

for entry in numpy_array:
    
    print(entry)
    print(f'this is a: {type(entry)} \n')

As you can see, Numpy converted our original list (to_convert_to_numpy), which contained both integers and floats, to an array with only floats! You might think that such a data structure that only allows one single data type is not ideal. However, the very fact that it only contains a single data-type makes operations on numpy arrays extremely fast. For example, loops over numpy arrays are often way faster than loops over python lists. This is because, internally, Python has to check the data-type of each loop entry before doing something with that entry. Because numpy arrays one allow a single data-type, it only has to check for the entries' data type **once**. If you imagine looping over an array or list of length 100,000, you probably understand that the numpy loop is way faster.

### Creating numpy arrays
As shown an earlier example, numpy arrays can be created as follows:

1. Define a Python list, e.g. `my_list = [0, 1, 2]` 
2. Convert the list to a numpy array, e.g. `numpy_array = np.array(my_list)`

Importantly, a simple Python list will be converted to a 1D numpy array, but a nested Python list will be converted to a 2D (or even higher-dimensional array). Nesting is simply combining different lists, separated by commans, as is shown here:

my_list = [1, 2, 3]
my_array = np.array(my_list)

print("A 1D (or 'flat') array:")
print(my_array, '\n')

my_nested_list = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

my_2D_array = np.array(my_nested_list)
print("A 2D array:")
print(my_2D_array)

<div class='alert alert-warning'>
    <b>ToDo</b>: Create the following 1D array:
math::
\begin{align}
\begin{bmatrix}
5 & 3 & 2 & 8 & 9
\end{bmatrix}
\end{align}

and store it in a variable named <tt>vec</tt>.
</div>

# YOUR CODE HERE

<div class='alert alert-warning'>
    <b>ToDo</b>:
    
Create the following matrix (2D array):
math::
\begin{align}
\begin{bmatrix}
5 & 2 & 8 \\
8 & 2 & 1 \\
4 & 4 & 4 \\
1 & 2 & 3
\end{bmatrix}
\end{align}

and store it in a variable named <tt>arr_2d</tt>. Hint: start by creating a nested python list (like we did with the <tt>my_nested_list</tt> variable) and then convert it to numpy.
</div>

# YOUR CODE HERE

As you can imagine, creating numpy arrays from nested lists becomes cumbersome if you want to create (large) arrays with more than 2 dimensions. There are, fortunately, a lot of other ways to create ('initialize') large, high-dimensional numpy arrays. One often-used method is to create an array with zeros using the numpy function `np.zeros`. This function takes one (mandatory) argument, which is a tuple with the dimensions of your desired array:

my_desired_dimensions = (2, 5) # suppose I want to create a matrix with zeros of size 2 by 5
my_array = np.zeros(my_desired_dimensions)

print(my_array)

Using arrays with zeros is often used in what is called 'pre-allocation', in which we create an 'empty' array with only zeros and for example, 'fill' that array in a loop. Below, we can see an example where we pre-allocate an array with 5 zeros, and fill that in a for-loop with the squares of 1 - 5.

my_array = np.zeros(5)

print('Original zeros-array')
print(my_array)

for i in range(5):  # notice the range function here! This loop now iterates over [0, 1, 2, 3, 4]
    number_to_calculate_the_square_of = i + 1
    my_array[i] = number_to_calculate_the_square_of ** 2

print('\nFilled array')
print(my_array)

In addition to `np.zeros`, you can create numpy arrays using other functions, like `np.ones` and `random` from the `np.random` module:

ones = np.ones((5, 10)) # create an array with ones
print(ones, '\n')

rndom = np.random.random((5, 10)) # Create an array filled with random values (0 - 1 uniform)
print(rndom)

## Numpy indexing
<hr>

Indexing (extracting a single value of an array) and slicing (extracting multiple values - a subset - from an array) of numpy arrays is largely the same as with regular Python lists. Let's check out a couple of examples of a 1D array:

my_array = np.arange(10, 21)  # numpy equivalent of list(range(10, 21))
print('Full array:')
print(my_array, '\n') 

print("Index the first element:")
print(my_array[0])

print("Index the second-to-last element:")
print(my_array[-2])

print("Slice from 5 until (not including!) 8")
print(my_array[5:8])

print("Slice from beginning until 4")
print(my_array[:4])

Setting values in numpy arrays works the same way as lists:

my_array = np.arange(10, 21)
my_array[0] = 10000
print(my_array)

my_array[5:7] = 0
print(my_array)

### Multidimensional indexing
Often, instead of working on and indexing 1D array, we'll work with multi-dimensional (>1D) arrays. Indexing multi-dimensional arrays is, again, quite similar to indexing and slicing list. 

Like indexing Python lists, indexing multidimensional numpy arrays is done with square brackets `[]`, in which you can put as many comma-delimited numbers as there are dimensions in your array. 

For example, suppose you have a 2D array of shape $3 \times 3$ and you want to index the value in the first row and first column. You would do this as follows:

my_array = np.zeros((3, 3)) # 3 by 3 array with zeros
indexed_value = my_array[0, 0]
print("Value of first row and first column: %.1f" % indexed_value)

We can also extract sub-arrays using slicing/indexing. An important construct here is that we use a single colon `:` to select all values from a particular dimension. For example, if we want to select all column-values (second dimension) from only the first row (first dimension), do this:

```
some_2d_arr[0, :]
```

Let's look at an examples below:

my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

print(my_array, '\n')

all_column_values_from_first_row = my_array[0, :]
print('First row')
print(all_column_values_from_first_row, '\n')

all_row_values_from_first_col = my_array[:, 0]
print('First column')
print(all_row_values_from_first_col)

## Methods vs. functions
<hr>
In the previous tutorials, we learned that, in addition to functions, 'methods' exist that are like functions of an object. We've seen examples of list methods, e.g. `my_list.append(1)`, and string methods, e.g. `my_string.replace('a', 'b')`.

Like lists and strings, numpy arrays have a lot of convenient methods that you can call (like the `astype` method). Again, this is just like a function, but then applied to itself. Often, numpy provides both a function and method for simple operations. 

Let's look at an example: 

my_array = np.arange(10)  # creates a numpy array from 0 until (excluding!) 10
print(my_array, '\n')

mean_array = np.mean(my_array)
print(f'The mean of the array is: {mean_array}')

mean_array2 = my_array.mean() 
print(f'The mean of the array (computed by its corresponding method) is: {mean_array2}')

print('Is the results from the numpy function the same as '
      f'the corresponding method? Answer: {str(mean_array == mean_array2)}')

If there is both a function and a method for the operation we want to apply to the array, it really doesn't matter what we choose! Let's look at some more (often used) methods of numpy ndarrays:

my_array = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

std_my_array = my_array.std()  # same as np.std(array)
print(f"Standard deviation of my_array: {std_my_array}", '\n')

transpose_my_array = my_array.T  # same as np.transpose(array)
print(f"Transpose of my_array:\n{transpose_my_array}", '\n')

min_my_array = my_array.min()  # same as np.min(array)
print(f"Minimum of my_array: {my_array.min()}", '\n')

max_my_array = my_array.max()  # same as np.max(array)
print(f"Maximum of my_array: {max_my_array}", '\n')

sum_my_array = my_array.sum()  # same as np.sum(array)
print(f"Sum of my_array: {sum_my_array}", '\n')

Importantly, a method may or may not take arguments (input).
If no arguments are given, it just looks like "object.method()", i.e. two enclosing brackets with nothing in between.
However, a method may take one or more arguments (like the my_list.append(1) method)! 
This argument may be named or unnamed - doesn't matter. An example:

my_array2 = np.random.random((3, 3))
print('Original array:')
print(my_array2, '\n')

print('Use the round() method with the argument 3:')
print(my_array2.round(3), '\n')

print('Use the round() method with the named argument 5:')
print(my_array2.round(decimals=5), '\n')

In addition to the methods listed above, you'll probably see the following methods a lot in the code of others.

Reshaping arrays:

my_array = np.arange(10)
print(my_array.reshape((5, 2))) # reshape to desired shape

Ravel ("flatten") an array:

temporary = my_array.reshape((5, 2))
print("Initial shape: %s" % (temporary.shape,))
print(temporary.ravel()) # unroll multi-dimensional array to single 1D array
print("Shape after ravel(): %s" % (temporary.ravel().shape,))