''' This hello example demonstrates the use of 
user defined functions in Python.
'''

# Define two new functions. 
# You can "call" these as many times as you wish
def welcome():
    print("Welcome the the demonstration of functions.")
    print("Remember, you must alway define a function")
    print("before you can use it.")


def hello(name):
    print("Hello " + name + "!")
    #print(f"Hello {name}!")    #Note f-strings don't work on the Pi!
    #print("Hello {}!".format(name))
    print()


# Here is the main code. Call some functions!
# Be sure to use the debugger (both F10 and F11) to see this work
welcome()
hello("Keith")
hello("Pete")

