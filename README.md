# Automated-with-python-part-2
flow control statement.
Flow control.The flow conrol statements can decides which python instructions to execute under which conditions.
in a flow chart, there is usually more than one way to go from a start of a program to the end, we see the exact same lines of code for the computer program.
before diving deep on flow control statements, there is need to first learn how to representhe yes and no options, we first need to understand how to write those branching points as python code. To that end, lets look at three important points under flow control statements which are: boolean values, comparison operators, and boolean operators.
BOOLEAN VALUES: the boolean values only has two values which are true and false. when you type a python code, the boolean values true and false lacks the quotes you place around strings, and they always start with capital T or F, with the rest of the word in lowercase. 
COMPARISON OPERATOR:it compares two values and evaluate down to a single booleam value.
Operator Meaning
== Equal to
!= Not equal to
< Less than
> Greater than
<= Less than or equal to
>= Greater than or equal to
These operators evaluate to True or False depending on the values you 
give them. Let’s try some operators now, starting with == and !=.
The Difference Between the == and = Ope r ators
You might have noticed that the == operator (equal to) has two equal signs, 
while the = operator (assignment) has just one equal sign. It’s easy to confuse 
these two operators with each other. Just remember these points:
•	 The == operator (equal to) asks whether two values are the same as each 
other.
•	 The = operator (assignment) puts the value on the right into the variable 
on the left.
To help remember which is which, notice that the == operator (equal to) 
consists of two characters, just like the != operator (not equal to) consists of 
two characters.Flow Control 35
You’ll often use comparison operators to compare a variable’s value to 
some other value, like in the eggCount <= 42 and myAge >= 10 examples. 
(After all, instead of typing 'dog' != 'cat' in your code, you could have just 
typed True.) You’ll see more examples of this later when you learn about 
flow control statements.
Boolean Operators
The three Boolean operators (and, or, and not) are used to compare boolean
values. Like comparison operators, they evaluate these expressions down 
to a Boolean value. Let’s explore these operators in detail, starting with the 
and operator. 
Binary Boolean Operators
The and and or operators always take two Boolean values (or expressions), 
so they’re considered binary operators. The and operator evaluates an expression to True if both Boolean values are True; otherwise, it evaluates to False.

A truth table shows every possible result of a Boolean operator. 
Expression Evaluates to…
True and True True
True and False False
False and True False
False and False False

The not Operator
Unlike and and or, the not operator operates on only one Boolean value (or 
expression). The not operator simply evaluates to the opposite Boolean value
The not Operator’s Truth Table
Expression Evaluates to…
not True False
not False True
MIXING BOOLEAN AND COMPARISON OPERATORS:
since the comparison operators forms the idea of boolean values, you can use them in expressions with the booleans operators.
Recall that the and, or, and not operators are called Boolean operators 
because they always operate on the Boolean values True and False. While 
expressions like 4 < 5 aren’t Boolean values, they are expressions that evaluate down to Boolean values.

Elements of Flow Control
Flow control statements often start with a part called the condition, and all 
are followed by a block of code called the clause. Before you learn about 
Python’s specific flow control statements, I’ll cover what a condition and a 
block are.
Conditions
The Boolean expressions you’ve seen so far could all be considered conditions, which are the same thing as expressions; condition is just a more 
specific name in the context of flow control statements. Conditions always 
evaluate down to a Boolean value, True or False. A flow control statement 
decides what to do based on whether its condition is True or False, and 
almost every flow control statement uses a condition.
Blocks of Code
Lines of Python code can be grouped together in blocks. You can tell when a 
block begins and ends from the indentation of the lines of code. There are 
three rules for blocks.
1. Blocks begin when the indentation increases.
2. Blocks can contain other blocks.
3. Blocks end when the indentation decreases to zero or to a containing 
block’s indentation

if Statements
The most common type of flow control statement is the if statement. An if
statement’s clause (that is, the block following the if statement) will execute 
if the statement’s condition is True. The clause is skipped if the condition is 
False.
In normal English, an if statement could be read as, “If this condition is 
true, execute the code in the clause.” In Python, an if statement consists of 
the following:
•	 The if keyword
•	 A condition (that is, an expression that evaluates to True or False)
•	 A colon
•	 Starting on the next line, an indented block of code (called the if clause 

For example, let’s say you have some code that checks to see whether 
someone’s name is Alice. (Pretend name was assigned some value earlier.)
if name == 'Alice':
 print('Hi, Alice.')

else Statements
An if clause can optionally be followed by an else statement. The else clause 
is executed only when the if statement’s condition is False. In plain English, 
an else statement could be read as, “If this condition is true, execute this 
code. Or else, execute that code.” An else statement doesn’t have a condition, and in code, an else statement always consists of the following:
•	 The else keyword
•	 A colon
•	 Starting on the next line, an indented block of code (called the else
clause)
Returning to the Alice example, let’s look at some code that uses an 
else statement to offer a different greeting if the person’s name isn’t Alice.
if name == 'Alice':
 print('Hi, Alice.')40 Chapter 2
else:
 print('Hello, stranger.')

elif Statements
While only one of the if or else clauses will execute, you may have a case 
where you want one of many possible clauses to execute. The elif statement
is an “else if” statement that always follows an if or another elif statement. 
It provides another condition that is checked only if any of the previous conditions were False. In code, an elif statement always consists of the following:
•	 The elif keyword
•	 A condition (that is, an expression that evaluates to True or False)
•	 A colon
•	 Starting on the next line, an indented block of code (called the elif
clause)
Let’s add an elif to the name checker to see this statement in action.
if name == 'Alice':
 print('Hi, Alice.')
elif age < 12:
 print('You are not Alice, kiddo.')

while Loop Statements
You can make a block of code execute over and over again with a while statement. The code in a while clause will be executed as long as the while statement’s condition is True. In code, a while statement always consists of the 
following:
•	 The while keyword
•	 A condition (that is, an expression that evaluates to True or False)
•	 A colon
•	 Starting on the next line, an indented block of code (called the while
clause)

An Annoying while Loop
Here’s a small example program that will keep asking you to type, literally, 
your name. Select File4New Window to open a new file editor window, enter 
the following code, and save the file as yourName.py: 
 name = ''
 while name != 'your name':
 print('Please type your name.')
 name = input()
 print('Thank you!')
First, the program sets the name variable to an empty string. This is so 
that the name != 'your name' condition will evaluate to True and the program 
execution will enter the while loop’s clause
The code inside this clause asks the user to type their name, which 
is assigned to the name variable . Since this is the last line of the block, 
the execution moves back to the start of the while loop and reevaluates the 
condition. If the value in name is not equal to the string 'your name', then 
the condition is True, and the execution enters the while clause again.
But once the user types your name, the condition of the while loop will 
be 'your name' != 'your name', which evaluates to False. The condition is now 
False, and instead of the program execution reentering the while loop’s 
clause, it skips past it and continues running the rest of the program .

break Statements
There is a shortcut to getting the program execution to break out of a while
loop’s clause early. If the execution reaches a break statement, it immediately exits the while loop’s clause. In code, a break statement simply contains 
the break keyword.
Pretty simple, right? Here’s a program that does the same thing as the 
previous program, but it uses a break statement to escape the loop. Enter the 
following code, and save the file as yourName2.py:
while True:
 print('Please type your name.')
name = input()
if name == 'your name':
break
print('Thank you!')
The first line creates an infinite loop; it is a while loop whose condition 
is always True. (The expression True, after all, always evaluates down to the 
value True.) The program execution will always enter the loop and will exit 
it only when a break statement is executed. (An infinite loop that never exits 
is a common programming bug.)
Just like before, this program asks the user to type your name . Now, 
however, while the execution is still inside the while loop, an if statement 
gets executed to check whether name is equal to your name. If this condition is True, the break statement is run , and the execution moves out of the 
loop to print('Thank you!') . Otherwise, the if statement’s clause with the 
break statement is skipped, which puts the execution at the end of the while
loop. At this point, the program execution jumps back to the start of the 
while statement u to recheck the condition. Since this condition is merely 
the True Boolean value, the execution enters the loop to ask the user to type 
your name again.

Importing Modules
All Python programs can call a basic set of functions called built-in functions, 
including the print(), input(), and len() functions you’ve seen before. Python 
also comes with a set of modules called the standard library. Each module 
is a Python program that contains a related group of functions that can be 
embedded in your programs. For example, the math module has mathematicsrelated functions, the random module has random number–related functions, 
and so on.
Before you can use the functions in a module, you must import the 
module with an import statement. In code, an import statement consists of 
the following:
•	 The import keyword
•	 The name of the module
•	 Optionally, more module names, as long as they are separated by 
commas
Once you import a module, you can use all the cool functions of that 
module. Let’s give it a try with the random module, which will give us access 
to the random.ranint() function.
Enter this code into the file editor, and save it as printRandom.py:
import random
for i in range(5):
 print(random.randint(1, 10))
When you run this program, the output will look something like this:
4
1
8
4
1
The random.randint() function call evaluates to a random integer value 
between the two integers that you pass it. Since randint() is in the random
module, you must first type random. in front of the function name to tell 
Python to look for this function inside the random module. 
Here’s an example of an import statement that imports four different 
modules:
import random, sys, os, math58 Chapter 2
Now we can use any of the functions in these four modules. We’ll learn 
more about them later in the book.
from import Statements
An alternative form of the import statement is composed of the from keyword, followed by the module name, the import keyword, and a star; for 
example, from random import *.
With this form of import statement, calls to functions in random will not 
need the random. prefix. However, using the full name makes for more readable code, so it is better to use the normal form of the import statement.
Ending a Program Early with sys.exit()
The last flow control concept to cover is how to terminate the program. 
This always happens if the program execution reaches the bottom of the 
instructions. However, you can cause the program to terminate, or exit, by 
calling the sys.exit() function. Since this function is in the sys module, you 
have to import sys before your program can use it.
Open a new file editor window and enter the following code, saving it as 
exitExample.py:
import sys
while True:
 print('Type exit to exit.')
 response = input()
 if response == 'exit':
 sys.exit()
 print('You typed ' + response + '.')
Run this program in IDLE. This program has an infinite loop with no 
break statement inside. The only way this program will end is if the user enters 
exit, causing sys.exit() to be called. When response is equal to exit, the program ends. Since the response variable is set by the input() function, the user 
must enter exit in order to stop the program.

Summary
By using expressions that evaluate to True or False (also called conditions), 
you can write programs that make decisions on what code to execute and 
what code to skip. You can also execute code over and over again in a loop 
while a certain condition evaluates to True. The break and continue statements 
are useful if you need to exit a loop or jump back to the start.
These flow control statements will let you write much more intelligent 
programs. There’s another type of flow control that you can achieve by writing your own functions, which is the topic of the next chapter.
