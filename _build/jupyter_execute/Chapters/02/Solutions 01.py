# 📃 Solution for Exercise 01
<hr style="height:0.6px;border:none;color:#666;background-color:#666;" />

## 

What is 5 to the power of 5?

5 ** 5

## 

What is the remainder from dividing 73 by 6?

73 % 6

## 

How many times does the whole number 3 go into 123? What is the remainder of dividing 123 by 3?

print(1234 // 3)
print(1234 % 3)

## 

Split this string on the space character into a list:

```
s = "MDS is going virtual!"
```

s = "MDS is going virtual!"
s.split()

## 

Given the following variables:

```
thing = "light"
speed = 299792458  # m/s
```

Use f-strings to print:

```
The speed of light is 2.997925e+08 m/s.
```

thing = "light"
speed = 299792458  # m/s
print(f"The speed of {thing} is {speed:2e} m/s.")

## 

Given this nested list, use indexing to grab the word "MDS":

l = [10,[3,4],[5,[100,200,['MDS']],23,11],1,7]

l[2][1][2]

## 

Given this nest dictionary grab the word "MDS":

d = {
    "outer": [
        1,
        2,
        3,
        {"inner": ["this", "is", "inception", {"inner_inner": [1, 2, 3, "MDS"]}]},
    ]
}

d['outer'][3]['inner'][3]['inner_inner'][3]

## 

Why does the following cell return an error?

t = (1, 2, 3, 4, 5)
t[-1] = 6

Because tuples are immutable!

## 

Use string methods to extract the website domain from an email, e.g., from the string `"bruce.wayne@fakemail.com"`, you should extract `"fakemail"`.

email = "bruce.wayne@fakemail.com"
email.split("@")[-1].split(".com")[0]

## 

Given the variable `language` which contains a string, use `if/elif/else` to write a program that:
- return "I love snakes!" if `language` is `"python"` (any kind of capitalization)
- return "Are you a pirate?" if `language` is `"R"` (any kind of capitalization)
- else return "What is `language`?" if `language` is anything else.

language = "python"
if language.lower() == "python":
    print("I love snakes!")
elif language.lower() == "r":
    print("Are you a pirate?")
else:
    print(f"What is {language}?")