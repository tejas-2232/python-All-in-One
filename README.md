# python-All-in-One 
# Tagline- _Do not copy paste while Learning_

## structure


* In this repo we will cover all codes and revision needed for quick brush up for concepts.
* so that when we need to visit the concepts,its available for us.

_The Structure is like_

1. Data Types
2. Conditional statements
  2.1 If loop
  2.2 for loop
  2.3 while loop

3. Functions and variables  
 
4. Classes
5. Reading files
6. Strings
7. functions and files
8. memorizing logic
 

__1.Data Types__

There are seven data types in python. Let's have a look at them with direct examaple for better understanding.<br>

boolean = True

number = 1.1

string = "Strings can be declared with single or double quotes."



__2. Conditional statements<br>__

_2.1 If else Loop:_ 
       
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

_2.2 For Loop:_

The simple example of for loop can be given as:

```py
for item in list:
   print item
```

It prints all the items in list

suppose, list=[1,2,3,4,5,6], "item" is new variable created at runtime. Then it is referenced to array(list) index and printed using {print item} line.<br>

The output is=> [1,2,3,4,5,6] 

_2.3 While Loop:_

While loop is run until the condition is true. When it becomes FALSE the loop terminates. <br>

for example:

```py
while (total < max_val):
   total += values[i]
   i+=2  # i is incremented by two. Due to this condition becomes false & loop terminates. 
      
```

__3. Functions__

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

divide(45,5)
# here also it takes 2 parameters
```

__4. Classes:__

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

# Sorry for inconvenience 
# shifting the course for while | change of Resources 


#### The next sections for the course are:

1. List based collections

   1.1 Lists/Arrays<br>
   1.2 Linked Lists<br>
   1.3 Stacks<br>
   1.4 Queues<br>

2. Searching and Sorting

   2.1 Binary Search<br>
   2.2 Recursion<br>
   2.3 Bubble Sort<br>
   2.4 Merge Sort<br>
   2.5 Quick Sort<br>

3. Maps and Hashing
4. Trees
5. Graphs
6. Case Studies in Algorithms
7. Technical Interview Tips


<br>

## 1. List based collections: <br>
 __1.1 Lists:__ <p> Python has an interesting data stucture called a "list" that is much more than a mere list. Behind the scenes a Python list is built as an array. Even though you can do many operations on a Python list with just one line of code, there's a lot of code built in to the Python language running to make that operation possible. <br>
   For example, inserting into a list is easy (happens in constant time). However, inserting into an array is O(n), since you may need to shift elements to make space for the one you're inserting, or even copy everything to a new array if you run out of space. Thus, inserting into a Python list is actually O(n), while operations that search for an element at a particular spot are O(1).
   <br> Python is a "higher level" programming language, so you can accomplish a task with little code. However, there's a lot of code built into the infrastructure in this way that causes your code to actually run much more slowly than you'd think. Keep this in the back of your mind when using Python. <br>
   You likely won't need to know the details of how Python works behind the scenes in a programming interview, but you'll seem very impressive if you do!

   </p>

__1.2 Linked Lists:__ <p>
* Linked List is extension of list but it's definitely not an array. A Linked List is characterised by it's links. 
* Each elements has some notion of what the next element is since it's connected to it, but not necessarily how long the list is or where it is in the list. </p> 
<p>

* Linked list has a memory location of next block for traversing purpose and that block has memory location of next block and so on.<br>
* The blocks in linked list should be connected and if any link is missing then traversing becomes difficult.
 </p>
 There isn't a built-in data structure in Python that looks like a linked list. Thankfully, it's easy to make classes that represent data structures in Python!

 Single unit linked list examaple

 ```py
 class Element(object):
   def __init__(self, value):
      self.value = value
      self.next = None
```
Before moving on lets understand it. We use ``` __init__``` to initialize a new ``` Element ```. An Element has some value associated with it (which could be anything—a number, a string, a character, et cetera), and it has a variable that points to the next element in the linked list. 

**Let's see how to setup ```LinkedList``` class**

```py
class LinkedList(object):
      def __init__(self,head=None):
         self.head = head
```

* This code is very similar— we're just establishing that a __LinkedList__ is something that has a __head__ Element, which is the first element in the list. If we establish a __new LinkedList without a head__, it will default to __None__. 

**Let's build one method to append new elements at end of LinkedList**

```py
class append(self,new_element):
      current = self.head

      if self.head:
         while current.next:
            current = current.next
         current.next = new_element
      else:
         self.head = new_element

```
* If LinkedList already has a ```head```, we iterate through the ```next``` reference in every ```Element ```until we reach the end of the list.

* Set ```next``` for the end of the list to the ```new_element```. Alternatively, if there is no head already, you should just assign new_element to it and do nothing else.


**1.3 Stacks:** <p>Stack is a data structure in python which is based on LIFO( Last In First Out). 
It has two methods <br>
* push()
* pop()

**_push()_** is used when we need to add element in stack.

Similarly, when we need to remove an element from stack we use **_pop()_** method.

 </p>

**1.4 Queues:** <p> Unlike stack queue is a linear data structure that stores elements is FIFO order i.e First In First Out. The recently added item in Queue is removed last.
A quick example to visualize is queue of person at ticket box. The person who comes first is served first and the last one is served last.


__Operations in Queue:__

1. Enqueue: <p> In this operation we add elements to queue. If the queue is full then it's called as overflow.

</p>

2. Dequeue: <p> The operation of removing elements from queue is called Dequeue. The items are removed in same fashion as they have entered in queue. </p>

</p> 

__Priority Queue :__ Priority queue is also type of queue in which less popular elements are placed in front and more popular elements are place at the back.



## 2. Searching and Sorting

<p> 

* In order to implement algorithms in programming languages, you will need to understand an algorithm in detailed.

* Human may know how algorithm works but we need the computers to know how algorithms work as computers are going to execute it.
</p>
__2.1 Binary Search:<br>__ <p> 

* Binary search is the efficient algorithm for finding an item from sorted or unsorted array. The most common ways to use binary search is to find an item in array. 
* Basically an algorithm is just high level description of a trick of solving a problem.  

* If all the names in the world are written down together in order and you want to search for the position of a specific name, binary search will accomplish this in a maximum of 35  iterations. 
* It works on only sorted set of elements.
* while performing opearion on binary search, the total number of iterations may vary depending upon the number to be searched.

<img src="https://he-s3.s3.amazonaws.com/media/uploads/d90e6d2.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 10px;" />

</p>
