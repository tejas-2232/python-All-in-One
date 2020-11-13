# python-All-in-One 

# Tagline- _Do not copy paste while Learning_

## structure


* In this repo we will cover all codes and revision needed for quick brush up for concepts.
* so that when we need to visit the concepts,its available for us.

_The Structure is like_
1. Conditional statements
  1.1 If loop
  1.2 for loop
  1.3 while loop

2. Functions and variables  
 
3. Classes
4. Reading files
5. Strings
6. functions and files
7. memorizing logic
 


__1. Conditional statements<br>__

_1.1 If else Loop:_ 
       
       ```  
       password = raw_input("Enter the password")
       if password =="MI6":
          print("welcome Mr.bond")
       else: 
          print("access denied")    
       ```
Let's check what is if...else loop.
  ```py
  if condition-1:
        sequence of statements-1
  elif condition-n:
        sequence of statements-n
  else:
        default sequence of statements
  ```

The conditionals can also be represented by following code snippet.<br>

```py
if cake == "delicious":
   return "Yes please"
elif cake == "Okay":
   return "I will have a small piece"
else:
   return "No,Thank You"
```

Now, let's try to put college grades into use and understand how we can put the grades
through programming:

| Grdaes | Score |
|--------|-------|
|   A    |All grades above 4|
|   B    |All grades above 3 and below 3.5 |
|   C    |All grades above 2.5 and below3  |
|   D    | All Grades below 2.5 |

<br>

```py
 num = float(input("Enter the number:"))

 if num > 4:
     letter = "A"
 elif num > 3:
    letter = "B"
 elif num > 2:
    letter = "C"
 else: 
    letter = "D"   
 print("The grade is",letter)       
```

_1.2 For Loop:_

The simple example of for loop can be given as:

```py
for item in list:
   print item
```

It prints all the items in list

suppose, list=[1,2,3,4,5,6], "item" is new variable created at runtime. Then it is referenced to array(list) index and printed using {print item} line.<br>

The output is=> [1,2,3,4,5,6] 

_1.3 While Loop:_

While loop is run until the condition is true. When it becomes FALSE the loop terminates. <br>

for example:

```py
while (total < max_val):
   total += values[i]
   i+=2  # i is incremented by two. Due to this condition becomes false & loop terminates. 
      
```

__2. Functions__

Let's try to understand functions in new way.

```py
def divide(dividend, divisor):
      quotient = dividend/divisor
      remainder = divident % divisor
      return quotient, remainder
```

__This is the generalised code for division. Here,the primary goal is to understand how functions work.__  _Functions are nothing but blocks of code which when called run the block with provided parameters and returns data as a result._

__How to call function__: Function can be called using their name and parenthesis.
For example:

```py
divide(25,5)
# here it takes two params hence we passed 25 and 5
```

__3. Classes:__

Class is something that it's like a home to functions and objects.
Class bundles data and functionality together.

For Ex:

```py
   def __init__(self,name,age):
      self.name = name
      self.age = age

   def birthday(self):
      self.age +=1   
```
