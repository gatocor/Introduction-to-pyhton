# Index

 1. [Functions](#functions)
 2. [Scope of variables](#scope)
 3. [Packages](#packages)
    1. [Installing packages](#installing)
    2. [Importing packages](#importing)
    3. [Importing your own code](#code)

<a id='functions'></a>
# Functions

In the previous sections, we have how to declare variables, how to work with different Data Types and how to direct our code with conditions and loops.

When programming, we are repeating many times the same operations all times so it would be a waste of time to have to write everything every time. It would be a good thing to have a way of reusing code. That is what functions are for.

We have seen many examples already. `type(X)`, `help(X)`, `enumerate(X)`, `range(X)` and methods like `list.append(X)` are examples of functions that already exist and you can use. Many already-made functions exist in packages as we will see later. However, sometimes you may need to program your functions.

The structure to define a function is,

```python
def name_of_function(arg1,arg2,arg3...,karg1=val1,karg2=val2...):
    #some code

    return any_variables_you_want_to_return
```

Some remarks: 
 - `arg1`, `arg2`, `arg3`... are variables that you will always have to pass to the function. They always go at the beginning of the function.
 - `karg1`, `karg2`... are variables that are already initialized. That means that you can give them a new value and if you don't they will take the `val1`, `val` values.
 - Code inside the function has to be indented (tabulated), as in conditionals and loops.
 - The `return` is followed by variables that you want to return outside the function. If you do not write it, the function will return nothing.
 - When calling a function, you will always have to put parentheses after the name of the function, with any of the arguments that you want to send to it.

Let's see some simple examples.

  -**A function without arguments and without return**


```python
def say_hi():
    print("Hi")
```


```python
say_hi()
```

    Hi


  -**A function with arguments and without return**


```python
def say_hi2(name):
    print("Hi",name)
```


```python
say_hi2("python student")
```

    Hi python student


You can see that if you call this function without giving any argument, it will return an error.


```python
say_hi2()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-5-1651309af83d> in <module>
    ----> 1 say_hi2()
    

    TypeError: say_hi2() missing 1 required positional argument: 'name'


Additionally, you can specify the name of the argument you are assigning. In this way, you can assign them in any order, if not, they will be interpreted in order.


```python
def say_hi3(name,age):
    print("Hi",name,", you are",age,"years old.")
```


```python
say_hi3("python",3)
```

    Hi python , you are 3 years old.



```python
say_hi3(age=3,name="python")
```

    Hi python , you are 3 years old.


  -**A function with keyword arguments and without return**


```python
def say_hi4(name="someone"):
    print("Hi",name)
```


```python
say_hi4()
```

    Hi someone



```python
say_hi4("Peter")
```

    Hi Peter



```python
say_hi4(name="Peter")
```

    Hi Peter


  -**A function with return**


```python
def add1(x):
    y = x+1
    return y
```


```python
add1(3)
```




    4



  -**A function with several returns**


```python
def add1substrac1(x):
    y = x+1
    z = x-1
    return y,z
```


```python
add1substrac1(2)
```




    (3, 1)



<a id='scope'></a>
# Scope of variables

Variables that are declared inside a function cannot be seen outside. Consider this example this case:


```python
def declare_x():
    x = 4
```


```python
x = 0

declare_x()

x
```




    0



As you can see, even if we have declared a variable called x inside the function, it doesn't mean that we are modifying the variable outside the scope of this function. The other way around is not true.

Consider the following case:


```python
def print_x():
    print(x)
```


```python
x = 0

print_x()
```

    0


Even if x was not declared inside the function `print_x()`, we have been able to read it! This is because, a function, in case of not finding a variable declared, will search for a declaration outside the scope. **You have to be extremely careful with this as not declaring all the variables used inside a function is not a good practice.** Consider for example this case:


```python
def sum_1():
    x[1] += 1
```


```python
x = [1,2,3]

sum_1()

x
```




    [1, 3, 3]



The function has changed the list outside the function. Maybe this is not what we wanted and can lead to unexpected errors! All the variables that we need from the outside inside our function, we should ask them as arguments or declared arguments.

<a id='packages'></a>
# Packages

One of the main motivations for using Python is that there is much code available around there that we can use for our purposes. This code is distributed in packages. In the following, we will see how to use this code in our code.

<a id='installing'></a>
## Installing packages

We installed packages during the Setting up of this tutorial (see README file in the main folder). We can install a package by opening a terminal and using `pip`.

```
$ pip install name_of_package
```

What pip will do is search in the [PiPy](https://pypi.org/), the official database where python most of the packages are stored and, if finds a package with this name, will try to install it on your computer.

<a id='importing'></a>
## Importing packages

Once we have the packages installed, we can use them by importing them. There are several ways to import code from a package:

```python
import name_of_package #Imports full package. Anything in the package is used writing name_of_package.name_of_function
import name_of_package as abreviation #Imports full package. Anything in the package is used writing abreviation.name_of_function
from name_of_package import things_you_want_to_import 
```

Let's see how to use them in an example. We are going to import the package `numpy` which contains mathematical functions.


```python
import numpy
```

In numpuy there is the function cosinus. Now we can use it as,


```python
numpy.cos(3)
```




    -0.9899924966004454



This is very verbose if all the time we have to write `numpy.something`. A way more compact is to give a nickname to the package. Let's do this.


```python
import numpy as np
```


```python
np.cos(3)
```




    -0.9899924966004454



A lot better! 

In this way, we have uploaded everything that the package python has in it. However, we may be interested sometimes in using just a single or a few functions. We can upload single functions using the `from import` form.


```python
from numpy import cos
```


```python
cos(3)
```




    -0.9899924966004454



<a id='code'></a>
## Importing your code

When you start working a lot with your programs, it is possible that you start generating the code that you would like to reuse between analysis, and work. At this time you can consider two things:

 - Have a python file where your store your custom functions.
 - Make your package and distribute it.

The second option is something that is outside the scope of a beginner and even for people that is not dedicated to developing code. However, we can go for a more basic thing which is keeping code in a file apart from our analysis notebook and we can always take it to other analysis.

Have a look at the python file `my_custom_functions.py` inside this subfolder. Inside it you will see the following function:

```python
#Inside my_custom_functions.py

def my_custom_hi():
    """
    Function that says hi!
    """
    print("Hi from my_custom_functions_file!")
```

We would like to use this function here! We by using `from import` style without including the `.py` ending.


```python
from my_custom_functions import * #The asterisc means to import all that is inside the file
```


```python
my_custom_hi()
```

    Hi from my_custom_functions.py file!


Now you can have an external file where to keep the custom functions that you can use in all your analysis without having to copy-paste in other places!

A couple of final remarks:

 - If you have already imported a custom package and then you modify the content in it, you will have to restart the kernel (the jupyter or the interactive shell) and import it before you can see the messages.
 - The commented lines within triplet commas just below the `def` are comments that appear when you call the `help` function. For sanity, you should comment on your functions. Maybe in the moment, you write a function is clear in your head how it works, but who knows in a couple of weeks...


```python
help(my_custom_hi)
```

    Help on function my_custom_hi in module my_custom_functions:
    
    my_custom_hi()
        Function that says hi!
    



```python

```
