# Index 
 1. [Variables](#variables)
 2. [Data Types](#data-types)
 3. [A small introduction to classes](#classes)
    1. [Operators](#operators)
    2. [Methods](#methods)
 4. [Looking for help](#help)
 5. [Summary](#summary)

<a id='variables'></a>
# Variables


The most basic piece of code in any programming language is variables. Variables assign a piece of memory that will be accessible within the code. This information can be numbers, text, an image...


The basic way of declaring a variable is with the equal operator `=`, where we assign a data type to a symbol that we can call again in the rest of the program. 


```python
a = 1
b = 1.2
c = "Hi"
d = [1,2,3,4]
e = {"age":34,"heigt":50}
```

We have assigned an Integer, a Float, a String, a List and a Dictionary data types to the different variables. We will see Data Types in the next section. The information contained in the variables now can be accessed anytime.

Let's invocate a variable.


```python
c
```




    'Hi'



Alternatively, we can use the function `print()` to show the value of the variable.


```python
print(a)
print(b)
```

    1
    1.2


<a id='data-types'></a>
# Data Types

Data Types inform us of the kind of information a piece of memory contains and how it can be used in our code.

We can check what kind of type a variable contains using the function `type()`.


```python
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
```

    <class 'int'>
    <class 'float'>
    <class 'str'>
    <class 'list'>
    <class 'dict'>


In the following, we will go over the basic python types that are the base for more complex objects:

Basic Data Types

 - [Boolean](#Boolean)
 - [Integers and Floats](#integers-and-floats)
 - [Strings](#Strings)

Container Data Types

 - [Lists](#Lists)
 - [Dictionaries](#Dictionaries)

<a id='boolean'></a>
## Boolean

Boolean types are just `True` or `False`.


```python
a = True
b = False
```

<a id='integers-and-floats'></a>
## Integers and Floats

Among the most basic types, there are

 - Integer
 - Float

Let's declare one of each type,


```python
a = 2
b = 1.2
```

### Operating with numbers

We can perform different algebraic operations over these basic types.


```python
print(a-2)
print(a+2)
print(a/2)
print(a*2)
print(a**3) # Power to
print(a<0) # Less than
print(a<=0) # Less or equal than
print(a>0) # Greater than
print(a>=0) # Greater of equal than
```

    0
    4
    1.0
    4
    8
    False
    False
    True
    True


### Operate and assign basic types

A very common thing to do is to operate and assign after the operation to the same variable. There are operators that have been developed to perform that rule directly. Look at the following code.


```python
a = 1
a = a + 1
a
```




    2




```python
a = 1
a += 1
a
```




    2



<a id='strings'></a>
## Strings

Strings contain sets of characters.


```python
a = "String"
```

They can be concatenated by adding them.


```python
a += "s can be added"
a
```




    'Strings can be added'



We can check if there are other strings in them.


```python
"can" in a
```




    True



<a id='lists'></a>
## Lists

A coding language will be unuseful we had to keep a variable name for each number. most of the time we want to store big sets of data of the same feature. For that, we use lists. These are collections of data that can be used sequentially.

We declared them by using brackets and separating each object by commas.


```python
a = [1,2,3,4]
```

To take into account the elements of the array we use the brackets operator.


```python
a[1]
```




    2



We can access the elements from the end by writing negative positions. Is we would like to get the last number, we would write.


```python
a[-1]
```




    4



Notice that when calling `a[1]` we obtained the second element of the list! This is because **list enumeration **in arrays **starts** from 0**!**

For obtaining the first element we have to write the following:


```python
a[0]
```




    1



We can obtain several elements at the same time by slicing. Slices can be defined in the following ways:
 - `:final_not_included` will return from the first number
 - `initial:` will return until the last number
 - `initial:final_not_included`
 - `:` return all

Think about the following behaviors.


```python
print(a[:3])
print(a[1:])
print(a[1:3])
print(a[:])
```

    [1, 2, 3]
    [2, 3, 4]
    [2, 3]
    [1, 2, 3, 4]


The list doesn't need to contain all the elements of the same type.


```python
a = [1 ,"string", 1.2, False]
```

We can operate with the elements of a list in the usual way as with the types of its elements.


```python
a[0] += 3
a
```




    [4, 'string', 1.2, False]



We can also concatenate lists.



```python
a = []
a += [1,2,3,4]
a
```




    [1, 2, 3, 4]



Or add simple elements.


```python
a.append(5)
a
```




    [1, 2, 3, 4, 5]



<a id='dictionaries'></a>
## Dictionaries

Sometimes it is interesting to store complex data is to store the information with a key that is not a position, but with a name that is human readable. For that we use Dictionaries. These are declared in the form of `{key:feature, key:feature...}`.


```python
a = {"Height":12,"Length":1}
```

the keys can be obtained by calling the keys property.


```python
a.keys()
```




    dict_keys(['Height', 'Length'])



and each component can be accessed using the corresponding key.


```python
a["Height"]
```




    12



<a id='classes'></a>
# A small introduction to classes
All that we have mentioned above as Data Types are types of classes, also known as objects. Classes are constituted by:

 - **Variables**: That is the information contained in this class.
 - **Methods**: Functions (rules) that define how to manipulate that data.

As a very simple example, when we define in a variable an integer, what we are defining is a class integer. The variable is information in the memory stored (the integer) and the methods are the rules the computer knows to manipulate the integer (how to add it, subtract it, multiply it...).

Let's see this with the example of an integer.


```python
a = 3
print(type(a))
```

    <class 'int'>


There are two forms of interacting with classes:

<a id='operators'></a>
## Operators

Operators usually correspond to the most basic rules performed on the basic classes and correspond to arithmetic, comparison, identity operations. We have seen them above when performing sums (`+`), sum and addition (`+=`), or even checking if a number was in a list (`in`).

A very extensive list of operators can be found in the Cheatsheet.pdf that you will find along this tutorial. You do not have to learn them by memory, you will learn as you use them and you will see that they are very intuitive to work with most part of the time.


```python
a = 3
a + 3 #This uses an operator
```




    6



<a id='methods'></a>
## Methods

When dealing with more complex data types, certain rules do not have an operator. Recall for example when adding an element to a list that we called `list.append(add_variable)` or when we wanted to get the keys of the dictionary`.keys`()`. These are examples of methods, and rules that are defined for a specific class.

They are used calling with the structure `variable.method(arguments)`. The arguments will depend on the method. 

As with operators, it is not necessary at all that you learn all the methods for all the classes (I think it will be even impossible). You will learn the ones you use while programing. 



```python
a = [1,2,3]
a.append(4)
a
```




    [1, 2, 3, 4]



<a id='help'></a>
# Looking for help

Most of the programming is learning by doing. The more you code, the more easily you will deal with problems as you find them. 

There are a couple of things that will help you:

The function `help` will print you a description of the use of the chasses, methods, and functions that you call if documented.


```python
a = []
help(a.append)
```

    Help on built-in function append:
    
    append(object, /) method of builtins.list instance
        Append object to the end of the list.
    


Second, since Python is a great community, you will find almost all the doubts you can have while coding solved. Use Google when need it!

This is the first thing that appeared when searching: python add to list

[https://www.w3schools.com/python/python_lists_add.asp](https://www.w3schools.com/python/python_lists_add.asp)

<a id='summary'></a>
# Summary

By the end of this script, you should have understood the concepts of:

 - Variables: A symbol that is assigned to a piece of memory so it can be used in the rest of the code. 
 - Data types: The different information that can be used in a program. We saw Boolean, Integers, Floats, Strings, Lists and Dictionaries.
 - Classes: The abstract concept of data types that consists of the variables (information) and the rules of how to work with them (class).
 - Operators: One of the ways of operating with data types consists of the most basic operations.
 - Methods: Other rules to work with different data types.
 - Look for help when stuck!


