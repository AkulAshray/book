# Working with Multiple DataFrames
<hr style="height:0.6px;border:none;color:#666;background-color:#666;" />

Often you'll work with multiple dataframes that you want to stick together or merge. `df.merge()` and `df.concat()` are all you need to know for combining dataframes. The Pandas [documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) is very helpful for these functions, but they are pretty easy to grasp.

```{note}
The example joins shown in this section are inspired by [Chapter 15](https://stat545.com/join-cheatsheet.html) of Jenny Bryan's STAT 545 materials.
```

## Sticking DataFrames Together with `pd.concat()`
<hr>
You can use `pd.concat()` to stick dataframes together:
- Vertically: if they have the same **columns**, OR
- Horizontally: if they have the same **rows**

import pandas as pd

df1 = pd.DataFrame({'A': [1, 3, 5],
                    'B': [2, 4, 6]})
df2 = pd.DataFrame({'A': [7, 9, 11],
                    'B': [8, 10, 12]})

df1

df2

pd.concat((df1, df2), axis=0)  # axis=0 specifies a vertical stick, i.e., on the columns

Notice that the indexes were simply joined together? This may or may not be what you want. To reset the index, you can specify the argument `ignore_index=True`:

pd.concat((df1, df2), axis=0, ignore_index=True)

Use `axis=1` to stick together horizontally:

pd.concat((df1, df2), axis=1, ignore_index=True)

You are not limited to just two dataframes, you can concatenate as many as you want:

pd.concat((df1, df2, df1, df2), axis=0, ignore_index=True)

## Joining DataFrames with `pd.merge()`
<hr>

`pd.merge()` gives you the ability to "join" dataframes using different rules (just like with SQL if you're familiar with it). You can use `df.merge()` to join dataframes based on shared `key` columns. Methods include:
- "inner join"
- "outer join"
- "left join"
- "right join"

See this great [cheat sheet](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#compare-with-sql-join) and [these great animations](https://github.com/gadenbuie/tidyexplain) for more insights.

df1 = pd.DataFrame({"name": ['Magneto', 'Storm', 'Mystique', 'Batman', 'Joker', 'Catwoman', 'Hellboy'],
                    'alignment': ['bad', 'good', 'bad', 'good', 'bad', 'bad', 'good'],
                    'gender': ['male', 'female', 'female', 'male', 'male', 'female', 'male'],
                    'publisher': ['Marvel', 'Marvel', 'Marvel', 'DC', 'DC', 'DC', 'Dark Horse Comics']})
df2 = pd.DataFrame({'publisher': ['DC', 'Marvel', 'Image'],
                    'year_founded': [1934, 1939, 1992]})

df1



An "inner" join will return all rows of `df1` where matching values for "publisher" are found in `df2`:

pd.merge(df1, df2, how="inner", on="publisher")

![](inner_join.png)

An "outer" join will return all rows of `df1` and `df2`, placing NaNs where information is unavailable:

pd.merge(df1, df2, how="outer", on="publisher")

Return all rows from `df1` and all columns of `df1` and `df2`, populated where matches occur:

pd.merge(df1, df2, how="left", on="publisher")

![](left_join.png)

pd.merge(df1, df2, how="right", on="publisher")

There are many ways to specify the `key` to join dataframes on, you can join on index values, different, column names, etc. Another helpful argument is the `indicator` argument which will add a column to the result telling you where matches were found in the dataframes:

pd.merge(df1, df2, how="outer", on="publisher", indicator=True)

By the way, you can use `pd.concat()` to do a simple "inner" or "outer" join on multiple datadrames at once. It's less flexible than merge, but can be useful sometimes.