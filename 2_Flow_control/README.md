# Index

 1. [Conditional](#conditional)
    1. [Careful note on variable declaration](#declaration)
 2. [Loops](#loops)
    1. [For](#for)
       1. [range](#range)
       2. [enumerate](#enumerate)
       3. [comprehension lists (optional)](#comprehension)
    2. [While](#while)
    3. [Break](#break)
    4. [Careful with infinite loops](#infinite)
 3. [Summary](#summary)

<a id='conditional'></a>
# Conditional

We do not necessarily need to want all the code to go over the same steps in the code. For that, we use conditionals. The basic structure of a condition is:

```python
if some_boolean_condition:
    #some code
elif some_other_boolean_comparison:
    #some other code
else:
    #some code any of the other conditions were fullfilled
```

A few remarks have to be made:
 1. The `if` and `elseif` conditions must be completed with a condition, that is, an expression that is `True` or `False`. It would be good if you have a look at the Comparison, Logical and Membership operators in Cheatsheet.
 2. After each condition, we finish with two dots `:`.
 3. The `elif` and the `else` are not necessary. You can put them or not in the condition depending on if you need them or not.
 4. You can put as many `elif`s as you want, but only one `else`.
 5. The code inside the conditions must be spaced with a tab. This will happen every time that you put the `:` in any of the codes. This is compulsory for the code to work correctly. It was a programmatic decision made for the code to be clear.

Let's see some examples.

 - **With only if**


```python
age = 10

price = 10
if age < 10:
    price = 0 #Change price to zero

price
```




    10



 - **With if and else**


```python
age = 10

if age < 10:
    price = 0
else:
    price = 20

price
```




    20



 - **With if and elif**


```python
age = 10

if age < 10:
    price = 0
elif age >= 10:
    price = 20

price
```




    20



 - **With everything**


```python
age = 7

if age < 10:
    price = 5
elif age < 15:
    price = 10
elif age < 18:
    price = 15
else:
    price = 20

price
```




    5



<a id='declaration'></a>
## Careful note on  variable declaration

When declaring variables inside conditions, you have to be careful that the variable is defined if you use it outside the conditional statement.

Consider the following two cases:


```python
age = 7
price = 0

del price #Delete the variable everywhere

if age < 10:
    price = 0

price
```




    0




```python
age = 10
price = 0

del price #Delete the variable everywhere

if age < 10:
    price = 0

price
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-6-6e172172e418> in <module>
          7     price = 0
          8 
    ----> 9 price
    

    NameError: name 'price' is not defined


After eliminating the variable price, the conditional only creates this variable if `age < 10`. If this is the case, everything works correctly. However, in the second example, the variable does not exist since we did not enter the condition of the if statement and the variable were not created giving rise to an error.

A good practise for avoiding this is to make sure that the variable is always declared in the scope that you are going to use it. See the first example we showed before.


```python
age = 10

#Since I am going to use it outside the conditions, I declare the variable before the conditions to make sure it always exists.
price = 10 
if age < 10:
    price = 0 #Change price to zero

price
```




    10



In this way, I will always make sure I have the variable `price` declared.

<a id='loops'></a>
# Loops

Most of the power of a computer is that it can perform repetitive operations many times and a lot faster than humans.

Sometimes we want the code to be run iteratively, for example when checking all the elements of a list or a dictionary, or repeat something until some criterion is met. For that, we use loop operations.

<a id='for'></a>
## for loop

For loops useful when you want to perform the same operation a fixed maximum of times. The structure it follows is,

```python 
for iterator_variable in iterable_class:
    # Do some code
```

The `iterator_variable` is a variable that we define to go over the iterable elements. The `iterable_class` is any class that can be iterated. For example, Strings, Lists and Dictionaries are iterables, but not Floats. An easy way to check if a class is iterable is to call the function `iter(X)` and check if it gives an error.

Consider the following examples:

 - **Iterating over strings**


```python
l = "Hola"

for i in l:
    print(i)
```

    H
    o
    l
    a


 - **Iterating over lists**


```python
l = [1,2,3]

for i in l:
    print(i)
```

    1
    2
    3


 - **Iterating over dictionaries**

Notice in the example that iterating over a dictionary gives to the iterator variables the keys. Then, we can call the values of each element by calling the dictionary with each key.


```python
l = {"a":1,"b":2,"c":3}

for i in l:
    print(i, ":", l[i])
```

    a : 1
    b : 2
    c : 3


 - **Checking a class is not iterable**


```python
iter(1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-90bfa304bd69> in <module>
    ----> 1 iter(1)
    

    TypeError: 'int' object is not iterable


<a id='range'></a>
### function range

Sometimes you do not want to specifically over a created class but to make a specific iterable. In those cases, the function `range` generates an iterable for you.

See the following examples:


```python
for i in range(3): #Defining max (not included)
    print(i)
```

    0
    1
    2



```python
for i in range(1,3): #Defining min and max (max not included)
    print(i)
```

    1
    2



```python
for i in range(1,10,2): #Defining min, max and step (max not included)
    print(i)
```

    1
    3
    5
    7
    9


- **Sum a number to a all the elements of a list**


```python
l = [1,2,3]
for i in range(3): #Defining min, max and step (max not included)
    l[i] += 1

l
```




    [2, 3, 4]



<a id='enumerate'></a>
### function enumerate

When going over a list, the iterator returns the elements of the list. But imagine what you want to make is to modify the elements in the list.

If you perform the naive option you can see that nothing changes.


```python
l = [1,2,3]

for i in l:
    i += 1

l
```




    [1, 2, 3]



This is because the information stored in `i` is a copy of each element.

An alternative would be to go over the positions of the list with `range` as in one of the examples we saw before. However, you need to know or obtain the information on the length of the list to tell it to range.

An alternative is to call the function `enumerate` which returns the positions and the elements of the iterable.

See the following example noticing that we are defining two iterator variables, one for positions and the other for the elements.


```python
l = [1,2,3]

for i,j in enumerate(l):
    l[i] += 1
    print("Position",i," Value",j)

l
```

    Position 0  Value 1
    Position 1  Value 2
    Position 2  Value 3





    [2, 3, 4]



<a id='comprehension'></a>
### List comprehension (optional)

A `list` is one of the basic containers. Sometimes if interesting to create automatic lists. 

Imagine that we want to create a new list with only the pair numbers of a list.

We can do it now that we know with our loop function:


```python
l = [1,2,4,3,5,6,7,8,2,0]
newl = []

for i,j in enumerate(l):
    if (j % 2) == 0: #Check if the residual of the division by two is zero
        newl.append(j)

newl
```




    [2, 4, 6, 8, 2, 0]



Great. However, this is very verbose. Usually, we do this thing many times in a code as lists are very basic objects.

We can do the same with comprehension lists. They are written with the following structure,

```python
newlist = [expression for item in iterable if condition == True]
```

Where the `if` condition is not necessary to be written if there is no condition to be met.

The above example will look like this:


```python
l = [1,2,4,3,5,6,7,8,2,0]

lnew = [j for i,j in enumerate(l) if (j % 2) == 0]

lnew
```




    [2, 4, 6, 8, 2, 0]



That as you can see is very close to what we did above but in a more concise manner.

<a id='while'></a>
# while loop 

When we do not know the number of repetitions needed in a process, we make a while loop. It has the following structure,

```python
while condition == True:
    #Do something
```

Let's see some examples.


```python
n = 0

while n < 10:
    n += 1
    print("Repetition ", n)
```

    Repetition  1
    Repetition  2
    Repetition  3
    Repetition  4
    Repetition  5
    Repetition  6
    Repetition  7
    Repetition  8
    Repetition  9
    Repetition  10


<a id='break'></a>
## Break

Sometimes, we want to stop loops before the for has finished or the while has met the condition. We can use `break` for this purpose, both in `for` and `while` loops.

See the following analog examples:


```python
l = [1,2,3,4,5,6,7,8]

for i,j in enumerate(l):
    if j > 3.5:
        print("I found a value above 3.5 in iteration ",i)
        break 
    
    print("Iteration ",i)

```

    Iteration  0
    Iteration  1
    Iteration  2
    I found a value above 3.5 in iteration  3



```python
l = [1,2,3,4,5,6,7,8]

count = 0
while count < len(l):
    if l[count] > 3.5:
        print("I found a value above 3.5 in iteration ",count)
        break 
    
    print("Iteration ",count)
    count += 1
```

    Iteration  0
    Iteration  1
    Iteration  2
    I found a value above 3.5 in iteration  3


<a id='infinite'></a>
# Careful with infinite loops

While `for` loops are more as there are supposed to have a maximum number of steps, `while` loops do not have that closure. This means that if the condition to stop is never met, they may run forever.

See the following code:

```python
n = 0

while n < 10:
    n -= 1
```

we can see that `n` will never be bigger than 10 and the loop will run forever. For this reason, it is advisable to use `for` loops always that is possible. In this sense, in the examples in the [break section](#break) where both codes do the same, it will prefer to use the loop with `for`.


<a id='summary'></a>
# Summary

By the end of this script, you should have learned how to control the workflow of your code by:

 - Writing conditional statements and being aware of problems when defining variables inside conditional statements.
 - Making for and while loops and using several handy functions to make iterations. Be aware of potential problems with infinite loops.



