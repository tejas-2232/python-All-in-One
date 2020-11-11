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
 

3. Reading files
4. Strings
5. functions and files
6. memorizing logic
7. 


1. Conditional statements<br>

1.1 If else Loop: 
       
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

1.2 For Loop:

The simple example of for loop can be given as:

```py
for item in list:
   print item
```

It prints all the items in list

suppose, list=[1,2,3,4,5,6], "item" is new variable created at runtime. Then it is referenced to array(list) index and printed using {print item} line.<br>

The output is=> [1,2,3,4,5,6] 

1.3 While Loop:

While loop is run until the condition is true. When it becomes FALSE the loop terminates. <br>

for example:

```py
while (total < max_val):
   total += values[i]
   i+=2  # i is incremented by two. Due to this condition becomes false & loop terminates. 
      
```

2. Functions

Let's try to understand functions in ne way.