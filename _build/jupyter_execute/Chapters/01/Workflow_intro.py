# Reference: https://jupyterbook.org/interactive/hiding.html
# Use {hide, remove}-{input, output, cell} tags to hiding content

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
%matplotlib inline
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

sns.set()
sns.set_context('talk')
np.set_printoptions(threshold=20, precision=2, suppress=True)
pd.set_option('display.max_rows', 7)
pd.set_option('display.max_columns', 8)
pd.set_option('precision', 2)
# This option stops scientific notation for pandas
# pd.set_option('display.float_format', '{:.2f}'.format)

def display_df(df, rows=pd.options.display.max_rows,
               cols=pd.options.display.max_columns):
    with pd.option_context('display.max_rows', rows,
                           'display.max_columns', cols):
        display(df)

# The Data Science Workflow

Here's a short video by DataBrew:

<iframe width="560" height="315" src="https://www.youtube.com/embed/5I2bYqeFQy4" title="Data Life Cycle" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

In data science, we use large and diverse data sets to make conclusions about
the world. In this book we discuss principles and techniques of
data science through the two lens, from the perspective of computational thinking and then from inferential thinking.
Practically speaking, this involves the following process:

1. Formulating a question or problem (Planning)
2. Acquiring and cleaning data (Preparation)
3. Conducting exploratory data analysis (Analysis)
4. Using prediction and inference to draw conclusions and model data (Modelling)
5. Evalutating different models and selecting the appropriate one (Compare and Refine)
6. Communicating your findings

It is quite common for more questions and problems to emerge after step 4 and 5 of 
this process, so we often think of a Data Scientists workflow as being iterative and non linear. 
This positive feedback loop is so central to our work that we call it the **data analytics/ science lifecycle**.

While simple to state, the data science lifecycle takes training and practice
to do well. In fact, each topic in this book revolves around a piece of this
lifecycle. We will get started with learning the essential concepts of computational thinking
so you can be skillful at making productive use of computational techniques. You will learn how to use
computational modes of thought to frame problems, to build computational models, and to guide the process
of extracting information from data. We cover most of Python's features, but the emphasis is on what one can do with a programming language and not on the language itself.




```{toctree}
:hidden:
:titlesonly:


workflow_1
workflow_2
workflow_3
```
