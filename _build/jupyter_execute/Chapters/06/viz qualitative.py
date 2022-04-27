# Visualizing Qualitative Data
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

For qualitative or categorical data, we most often use bar charts and dot charts. We will show how to create these plots using `seaborn` and the Titanic survivors dataset.

import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
sns.set()

# Load the dataset
titanic = sns.load_dataset('titanic').reset_index(drop=True)

# This table is too large to fit onto a page so we'll output sliders to
# pan through different sections.
titanic.head()

## Bar Charts
<hr>

In `seaborn`, there are two types of bar charts. The first type uses the `countplot` method to count up the number of times each category appears in a column.

# Counts how many passengers survived and didn't survive and
# draws bars with corresponding heights
sns.countplot(x='alive', data=titanic);

sns.countplot(x='class', data=titanic);

# As with box plots, we can break down each category further using color
sns.countplot(x='alive', hue='class', data=titanic);

The `barplot` method, on the other hand, groups the DataFrame by a categorical column and plots the height of the bars according to the average of a numerical column within each group.

# For each set of alive/not alive passengers, compute and plot the average age.
sns.barplot(x='alive', y='age', data=titanic);

The height of each bar can be computed by grouping the original DataFrame and averaging the `age` column:

titanic[['alive', 'age']].groupby('alive').mean()

By default, the `barplot` method will also compute a bootstrap 95% confidence interval for each averaged value, marked as the black lines in the bar chart above. The confidence intervals show that if the dataset contained a random sample of Titanic passengers, the difference between passenger age for those that survived and those that didn't is not statistically significant at the 5% significance level.

These confidence intervals take long to generate when we have larger datasets so it is sometimes useful to turn them off:

sns.barplot(x='alive', y='age', data=titanic, ci=False);

## Dot Charts
<hr>

Dot charts are similar to bar charts. Instead of plotting bars, dot charts mark a single point at the end of where a bar would go. We use the `pointplot` method to make dot charts in seaborn. Like the `barplot` method, the pointplot method also automatically groups the DataFrame and computes the average of a separate numerical variable, marking 95% confidence intervals as vertical lines centered on each point.

# For each set of alive/not alive passengers, compute and plot the average age.
sns.pointplot(x='alive', y='age', data=titanic);

Dot charts are most useful when comparing changes across categories:

# Shows the proportion of survivors for each passenger class
sns.pointplot(x='class', y='survived', data=titanic);

# Shows the proportion of survivors for each passenger class,
# split by whether the passenger was an adult male
sns.pointplot(x='class', y='survived', hue='adult_male', data=titanic);