# 6. DataFrames in Python
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

Much of data anlysis involves working with data contained in rectangular form in tables or csv files. In python we call these data tables as `DataFrames`, they are one of the most common and useful forms of data for analysis. We introduce data manipulation using `pandas`, the standard Python library for working with dataframes. 

It is more important that you understand the types of useful operations on data than the exact details of `pandas` syntax. For example, knowing when to perform a group-by is generally more useful than knowing how to call the `pandas` function to group data. 

Because we will cover only the most commonly used `pandas` functions in this tutorial, you should bookmark the [`pandas` documentation](http://pandas.pydata.org/pandas-docs/stable/) for reference
when you conduct your own data analyses.

We begin by talking about the types of dataset structures that `pandas` can read. Then, we introduce indexes, grouping, apply, and strings.

## Chapter Learning Objectives
<hr>

- Create Pandas series with `pd.Series()` and Pandas dataframe with `pd.DataFrame()`
- Be able to access values from a Series/DataFrame by indexing, slicing and boolean indexing using notation such as `df[]`, `df.loc[]`, `df.iloc[]`, `df.query[]`
- Perform basic arithmetic operations between two series and anticipate the result.
- Describe how Pandas assigns dtypes to Series and what the `object` dtype is
- Read a standard .csv file from a local path or url using Pandas `pd.read_csv()`.
- Understand how to group dataset using `.groupby()` function



```{toctree}
:hidden:
:titlesonly:


Introduction to Pandas
Pandas grouping and pivoting
Pandas apply strings and plotting
Merge and Concat Dataset
```
