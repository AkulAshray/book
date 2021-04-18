# Exploring Data Using Plotly Express and Graph Objects

While [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/) libraries are excellent for plotting beautiful static plots, they tend to be simple non-interactive images. In some cases, static plots may convey the message, but its always better to be able to allow users to interact with the plots. [Plotly](https://plotly.com/) on the other hand allows us to make beautiful, interactive, exportable figures in just a few lines of code.

I have used plotly before but never had the chance to fully explore the library, what better dataset to test it out than the Kaggle survey?

**So the main goal of this kernel is to:**
* Map the way using plotly to express and graph objects for EDA and interactive plots
* Demo and provide a tutorial on how to implement dropdown menu and sliders to change the attributes of our data presented in the chart

**I am still updating this Kernel!!! As I encounter and learn more about plotly express, I will keep updating the plots**

Before we begin plotting let's import our libraries and store our data in a dataframe


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import plotly.express as px
import warnings

warnings.filterwarnings("ignore") #can this be explained to it's importance?
pd.set_option('display.max_columns', 200)
pd.set_option('display.max_rows', 500)

df = pd.read_csv('kaggle_survey_2020_responses.csv')
descriptions = df.loc[0,:] #creating this will help see what the questions are about
df = df.loc[1:,:]
df['measure'] = 1  # creating a new column called measure will allow us to sum individual counts of rows during groupby

Now we can start plotting our data, since this is a plotly tutorial, we can begin with plotting the v*arious visualization platforms that are used by kagglers*. In the survey, **question 14** asked kagglers about the visulization platform that they use. This question has been split into multiple parts so before we plot the data, we need to create a new temporary dataframe that contains the information on different frameworks that are used along with their value counts.

I will do this by collecting the value counts for individual responses to the questions in a list and turning them into a dataframe.

Q14_cats = []
Q14_vals = []

# the following loop with go through each column containing 'Q14' and extend its value_counts to the list above
for col in df.columns:
    if 'Q14' in col:
        Q14_cats.extend(df[col].value_counts().reset_index()['index'].to_list())
        Q14_vals.extend(df[col].value_counts().reset_index()[col].to_list())

tmp_frameworks = pd.DataFrame({'Framework':Q14_cats,
                               'Values':Q14_vals})

tmp_frameworks.sort_values(by='Values', ascending=False, inplace=True)


''' Now that we have created the temporary dateframe, we can create the most simple plot using the plotly express bar function
'''
fig = px.bar(tmp_frameworks, x = tmp_frameworks.Framework, y = tmp_frameworks.Values,
      title='Visualization Platforms Popular Among Kagglers',
      labels={'Framework': 'Viz Platforms', 'Values':'Total Number of Users'})
fig.update_layout(title_x=0.5)
fig.show()

Plotly express seems to be the third most popular choice of Kagglers. Although this simple chart offers some functionality compared to Matplotlib, for example allowing us to zoom in and out and compare the columns of interest, it is still very basic. We can add more functionality by changing some of the other parameters in the px.bar() function.

Let us first explore the animation group parameter, which allows us to create sliders to explore different attributes of the data. You can learn more about it [here](https://plotly.com/python/animations/)




## Adding sliders to our visualization

Before we start to add sliders to our plot we need to make changes to the temporary dataframe we created. So far it only contains two columns, we need to add another one that has information on the profession of the kagglers taking the survey. I will change the values to reflect the reflective percentage of people in each profession using a specific viz platform.


table = pd.DataFrame(columns=[])
for item in df.Q5.unique():
    data = df[df.Q5 == item]
    Q14_cats = []
    Q14_vals = []

    for col in data.columns:
        if 'Q14' in col:
            Q14_cats.extend(data[col].value_counts().reset_index()['index'].to_list())
            Q14_vals.extend(data[col].value_counts().reset_index()[col].to_list())

    tmp_frameworks = pd.DataFrame({'Framework':Q14_cats,
                               'Values':Q14_vals,
                                'Profession': item
                              })
    tmp_frameworks['Values']= ((tmp_frameworks['Values']/tmp_frameworks['Values'].values.sum())*100).round(0)
    table = pd.concat([table, tmp_frameworks], axis=0)

In order to breakdown our viz with respect to each profession, we will set the value of the animation frame to the column 'Profession' of our temporary dataframe. The frames key will point to a list of figures, each of which will be cycled through when we move the slider. It will create a separate bar plot for individual profession that we selected.

When we set the animation frame parameter, we also need to specify two additional lines of code to update the layout
```
fig["layout"].pop("updatemenus")
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 130,)

```
The first open provides a slider along with the vizualization to allow us to slide through each frame and the other one is to padd the slider so it does not overlay on top of axis label.

fig = px.bar(table, x="Framework", y="Values",  
                animation_frame="Profession", 
                title='Relative percentage of Viz libraries used by different profession',
                labels={'Framework': 'Viz Libraries', 'Values':'Percentage of users'}) 

fig["layout"].pop("updatemenus") 
fig['layout']['sliders'][0]['pad']=dict(r= 10, t= 130,)
fig.show() 

Compared to the previous chart, using the animation frame allows us to see how usuage of different libraries change depending on the profession. One thing we can see is Ggplot is most popular with statisticians.

Although Plotly Express supports animation for many chart and map types, smooth inter-frame transitions (where we get a play button to cycle through each frame) are today only possible for scatter and bar. Lets plot another chart on geo coordinates and see if it works. We can plot geographical data quiet easily using

```
px.scatter_geo()
```

It contains the parameter for animation_frame as well, so let us create a basic chart to see the where all the respondents come from. Unsuprisingly, most of the respondents come from India or USA, with India having the largest size of student respondents.

groups = df[['Q3','Q5','measure']].groupby(['Q3','Q5']).sum().reset_index()

fig = px.scatter_geo(groups, locations='Q3', animation_frame='Q5',
                     locationmode='country names', size='measure', projection='natural earth')
fig["layout"].pop("updatemenus") 
fig

## Adding drop down menu to update our plot

Using a slider to update the frames in our plot is quiet useful, but what if we have lots of options in the frame? Then the slider may not be the most optimum method to update our plot. In that case we can use drop down menu to select the particular frame of data that we are interested to visualise. This can get a little complicated, but there are two componenets that we need to understand to be able to use it effectively. 

1. graph objects
2. fig.add_trace() and buttons

### Graph Objects:
At a low level, we can think of figures as represented by dictionary and displayed using the fig.show() function. This is what we have been doing so far, where we created dictionary values of figures and updated that dictionary with new values.

The[ plotly.graph_objects](https://plotly.com/python-api-reference/plotly.graph_objects.html) module lets us generate an automatically generated hierarchy of classes called 'Graph Objects'. They offer several benefits compared to plain python dictionaries, see ["When to use Graph Objects"](https://plotly.com/python/graph-objects/) to learn more about them.

### Adding traces:
New traces can be added to graph objects using the add_trace() method, which accepts a graph object trace 9an instance of go.Scatter, go.Bar, etc.) and adds it to the figure. This allows us to start with an empty figure and add traces to it sequentially. 


**To begin with we will group our data to explore just the questions we are interested in.**



age_groups = df[['Q6', 'Q3', 'measure']].groupby(['Q6','Q3']).sum().reset_index()
countries = []
fig=go.Figure()
buttons = []
default = 'United Kingdom of Great Britain and Northern Ireland'

for country in age_groups.Q3.value_counts().index:
    temp = age_groups[age_groups.Q3 == country]
    fig.add_trace(go.Bar(x=temp['Q6'], y=temp['measure'], visible=(country==default)))
    countries.extend([country])

for country in age_groups.Q3.value_counts().index:
    buttons.append(dict(method='update',
                        label=country,
                        args = [{'visible': [country==r for r in countries]}]))

We can see that the code that generates the following plot has two for loops.

```
for country in age_groups.Q3.value_counts().index:
    temp = age_groups[age_groups.Q3 == country]
    fig.add_trace(go.Bar(x=temp['Q6'], y=temp['measure'], visible=(country==default)))
    countries.extend([country])
```
The first loop will go through every options we want to set in our dropdown, essentially we are trying to filter our data for each option and add the trace to our graph object.

```
for country in age_groups.Q3.value_counts().index:
    buttons.append(dict(method='update',
                        label=country,
                        args = [{'visible': [country==r for r in countries]}]))
```
The second loop creates button values for each of the traces that we sequentially created in the previous loop. This will then be used to create our dropdown menu to update our data. While appending each of our buttons we also pass the argument to connect it each country so that the data can be updated depending on which country we selected.

After we have created our traces and buttons now all that's remaining is for us to update the layout of our plot to include a drop down menu and plot our figure.

fig.update_layout(showlegend=False, updatemenus=[{"buttons": buttons, "direction": "down",
                                                  "active": countries.index(default), "showactive": True,
                                                  "x": 0.7, "y": 1.20}])
fig.show()