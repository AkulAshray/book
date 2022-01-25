# Visualizing Branching Programs
<hr style="height:1px;border:none;color:#666;background-color:#666;" />

In the preceding section we saw how conditional statements (`if..elif...else statements`) help us control the flow of our code. We can have as many conditional statements as we like, but only the condition that evaluates as True will get executed. We can see how the computer performs the execution of code in the visulization below. You can click on next to see the changes that take place inside the machine's memory while executing the code. 

!pip install metakernel
from metakernel import register_ipython_magics
register_ipython_magics()

%%tutor
x, y, z = 10, 42, 84

x = y if y > z else z

if x%y == 0:
    if x == y:
        print('x is same as y')
    else:
        print('x is divisible by y')
else:
    print('x is not divisible by y')
print(float(x))
x = float(x)
print('Done with code')

```{note} 
We haven't spoken about frames in Python, but we will encounter them when we talk about functions, we will use this visualization in future as we encounter more sophisticated programming concepts and objects in later chapters.
```

We can see that even though there are 12 lines of code the computer performs the execution of code in 8 steps. In the first step it assigns the values to the variables we specified, and then changes the value of $x$ based on the condition we specified in the second line of code. We can see how the computer jumps straight to the else code block when it encounters that the `if` condition is found to be false. It then prints the output and comes out of the entire `if...else` code block and moves on to line 12.

Another point to note is that when the code at `print(float(x))` is executed, it changes the value of $x$ to a floating point number and prints its output, but there is no change in the actual value of variable $x$ in computer's memory. The only time the actual value of the variable changes is when we specify them explicity (which we do in code line 13).

Conditionals allow us to write programs that are more interesting than straight-line programs, but this class of branching programs is still quite limited. There is very little we can do with conditions and numeric data type, in order to construct more complex programs we will look at `sequence type` objects. They open up the option to construct another important programming language concept, **iteration**.



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