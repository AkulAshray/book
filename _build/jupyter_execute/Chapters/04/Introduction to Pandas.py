# Introduction to Pandas
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

Pandas is most popular Python library for tabular data structures. You can think of Pandas as an extremely powerful version of Excel (but free and with a lot more features!) 

Pandas can be installed using `conda`:

```
conda install pandas
```

We usually import pandas with the alias `pd`. You'll see these two imports at the top of most data science workflows:



import pandas as pd

## Pandas Series
<hr>

### What are Series?

A Series is like an list/array but with labels. They are strictly 1-dimensional and can contain any data type (integers, strings, floats, objects, etc), including a mix of them. Series can be created from a scalar, a list, ndarray or dictionary using `pd.Series()` (**note the captial "S"**). Here are some example series:

![](series.png)

### Creating Series

By default, series are labelled with indices starting from 0. For example:

pd.Series(data = [-5, 1.3, 21, 6, 3])

But you can add a custom index:

pd.Series(data = [-5, 1.3, 21, 6, 3],
          index = ['a', 'b', 'c', 'd', 'e'])

You can create a Series from a dictionary:

pd.Series(data = {'a': 10, 'b': 20, 'c': 30})

### Series Characteristics

Series can be given a `name` attribute. I almost never use this but it might come up sometimes:

s = pd.Series(data = [34, 56, 45, 75, 90], name='random_series')
s

s.name

s.rename("another_name")

You can access the index labels of your series using the `.index` attribute:

s.index

## Pandas DataFrames
<hr>

### What are DataFrames?

Pandas DataFrames are you're new best friend. They are like the Excel spreadsheets you may be used to. DataFrames are really just Series stuck together! Think of a DataFrame as a dictionary of series, with the "keys" being the column labels and the "values" being the series data:

![](dataframe.png)

### Creating DataFrames

Dataframes can be created using `pd.DataFrame()` (note the capital "D" and "F"). Like series, index and column labels of dataframes are labelled starting from 0 by default:

pd.DataFrame([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

We can use the `index` and `columns` arguments to give them labels:

pd.DataFrame([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]],
             index = ["R1", "R2", "R3"],
             columns = ["C1", "C2", "C3"])

There are so many ways to create dataframes. We can create them from dictionaries

pd.DataFrame({"C1": [1, 2, 3],
              "C2": ['A', 'B', 'C']},
             index=["R1", "R2", "R3"])

Here's a table of the main ways you can create dataframes (see the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/dsintro.html#dataframe) for more):

|Create DataFrame from|Code|
|---|---|
|Lists of lists|`pd.DataFrame([['Tom', 7], ['Mike', 15], ['Tiffany', 3]])`|
|ndarray|`pd.DataFrame(np.array([['Tom', 7], ['Mike', 15], ['Tiffany', 3]]))`|
|Dictionary|`pd.DataFrame({"Name": ['Tom', 'Mike', 'Tiffany'], "Number": [7, 15, 3]})`|
|List of tuples|`pd.DataFrame(zip(['Tom', 'Mike', 'Tiffany'], [7, 15, 3]))`|
|Series|`pd.DataFrame({"Name": pd.Series(['Tom', 'Mike', 'Tiffany']), "Number": pd.Series([7, 15, 3])})`|



### Indexing and Slicing DataFrames

There are several main ways to select data from a DataFrame:
1. `[]`
2. `.loc[]`
3. `.iloc[]`
4. Boolean indexing
5. `.query()`

df = pd.DataFrame({"Name": ["Harry", "George", "Lucas"],
                   "Language": ["Python", "Python", "R"],
                   "Confidence": [9, 4, 7]})
df

#### Indexing with `[]`
Select columns by single labels, lists of labels, or slices:

df['Name']  # returns a series

df[['Name']]  # returns a dataframe!

df[['Name', 'Language']]

You can only index rows by using slices, not single values (but not recommended, see preferred methods below).

df[0] # doesn't work

df[0:1] # does work

df[1:] # does work

#### Indexing with `.loc` and `.iloc`
Pandas created the methods `.loc[]` and `.iloc[]` as more flexible alternatives for accessing data from a dataframe. Use `df.iloc[]` for indexing with integers and `df.loc[]` for indexing with labels. These are typically the [recommended methods of indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#ix-indexer-is-deprecated) in Pandas.

df

First we'll try out `.iloc` which accepts *integers* as references to rows/columns:

df.iloc[0] 

df.iloc[0:2]  # slicing returns a dataframe

df.iloc[2, 1]  # returns the indexed object

df.iloc[[0, 1], [1, 2]]  # returns a dataframe

Now let's look at `.loc` which accepts *labels* as references to rows/columns:

df.loc[:, 'Name']

df.loc[:, 'Name':'Language']

df.loc[[0, 2], ['Language']]

Sometimes we want to use a mix of integers and labels to reference data in a dataframe. The easiest way to do this is to use `.loc[]` with a label then use an integer in combinations with `.index` or `.columns`:

df.index

df.columns

df.loc[df.index[0], 'Confidence']  # I want to reference the first row and the column named "Courses"

df.loc[2, df.columns[1]]  # I want to reference row "2" and the second column

#### Boolean indexing
Just like with series, we can select data based on boolean masks:

df[df['Confidence'] > 5]

df[df['Name'] == "Lucas"]

#### Indexing with `.query()`
Boolean masks work fine, but we can also use the `.query()` method for selecting data. `df.query()` is a powerful tool for filtering data. It has an odd syntax, it is more like SQL - `df.query()` accepts a string expression to evaluate and it "knows" the names of the columns in your dataframe.

df.query("Confidence > 4 & Language == 'Python'")

Note the use of single quotes AND double quotes above, lucky we have both in Python! Compare this to the equivalent boolean indexing operation and you can see that `.query()` is much more readable, especially as the query gets bigger!

df[(df['Confidence'] > 4) & (df['Language'] == 'Python')]

Query also allows you to reference variable in the current workspace using the `@` symbol:

confidence_threshold = 4
df.query("Confidence > @confidence_threshold")

## Reading/Writing Data From External Sources
<hr>

### .csv files

A lot of the time we will be loading .csv files for use in pandas. We can use the `pd.read_csv()` function for this. In the remaining sections of this chapter we will work with the Baby Names dataset. There are so many arguments that can be used to help read in your .csv file in an efficient and appropriate manner, feel free to check them out now (by using `shift + tab` in Jupyter, or typing `help(pd.read_csv)`).

path = 'babynames.csv'
baby = pd.read_csv(path)
baby

You can print a dataframe to .csv using `df.to_csv()`. Be sure to check out all of the possible arguments to write your dataframe exactly how you want it.

### Slicing using `.loc`

To select subsets of a DataFrame, we use the `.loc` slicing syntax. The first argument is the label of the row and the second is the label of the column:

baby.loc[1, 'Name'] # Row labeled 1, Column labeled 'Name'

To slice out multiple rows or columns, we can use `:`. Note that `.loc` slicing is inclusive, unlike Python's slicing.

# Get rows 1 through 5, columns Name through Count inclusive
baby.loc[1:5, 'Name':'Count']

We will often want a single column from a DataFrame:

baby.loc[:, 'Year']

To select out specific columns, we can pass a list into the `.loc` slice:

# This is a DataFrame again
baby.loc[:, ['Name', 'Year']]

### Common DataFrame Operations

DataFrames have built-in functions for performing most common operations, e.g., `.min()`, `idxmin()`, `sort_values()`, etc. They're all documented in the [Pandas documentation here](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) but I'll demonstrate a few below:

baby.min()

baby['Year'].min()

baby['Year'].idxmin()

baby['Year'].sum()

We can use the `.describe()` method to get the basic summary statistics for our numerical columns and `.info()` to get an overview of the different data types contained inside our dataframe.

baby.describe()

baby.info()

Some methods require arguments to be specified, like `.sort_values()`:

baby.sort_values(by='Year')

baby.sort_values(by='Year', ascending=False)

## Summary
<hr>

We now have learned to express the following operations in `pandas`:

| Operation | `pandas` |
| --------- | -------  |
| Read a CSV file | `pd.read_csv()` |
| Slicing using labels or indices | `.loc` and `.iloc` |
| Slicing rows using a predicate | Use a boolean-valued Series in `.loc` |
| Sorting rows | `.sort_values()` |