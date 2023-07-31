# Explain Exception handling? What is an Error in Python?
--> """An exception is an event, which occurs during the execution of a program that disrupts
    the normal flow of the program's instructions. In general, when a Python script encounters
    a situation that it cannot cope with, it raises an exception. An exception is a Python obj
    that represents an error.
    try: when the code inside try block will run successfully
    except: if try block does'nt run the except block will be executed
    else: if try block will run successfully then else will be defaultly executed
    finally: this block will run in every situation(wather the condition gets
	run or not)"""

#  How many except statements can a try-except block have? Name Some built-in exception classes:
--> """there is at least one except statement.
    there are four except statements : try , except, else, finally
    there are many types of built in exception class like systemerror, taberror, typeerror etc."""

# When will the else part of try-except-else be executed?
-->"""if try block will run successfully then else will be defaultly executed.."""

# Can one block of except statements handle multiple exception?
--> yes try except block can handle one or more exception.

# When is the finally block executed?
"""this block will run in every situation(wather the condition gets run or not)..."""


# What happens when „1‟== 1 is executed? 
--> """ It simply evaluates to False and does not raise any exception."""


# How Do You Handle Exceptions With Try/Except/Finally In Python? Explain with coding snippets.
--> A:7 """therer are four types of exception in exception handling:-
    try: when the code inside try block will run successfully
    except: if try block does'nt run the except block will be executed
    else: if try block will run successfully then else will be defaultly executed
    finally: this block will run in every situation(wather the condition gets
	run or not)"""
   # --> code :-
try:
    print("Value = ",u)
except Exception as e:
    print("Error:",e)

# Write python program that user to enter only odd numbers, else will raise an exception.
def get_odd_number():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            if num % 2 != 1:
                raise ValueError("You must enter an odd number.")
            return num
        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    try:
        odd_number = get_odd_number()
        print(f"You entered an odd number: {odd_number}")
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user.")
    except Exception as e:
        print(f"An error occurred: {e}")


