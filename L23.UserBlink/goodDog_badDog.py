''' Good Dog - Bad Dog
Example code to demonstrate variables, input function, 
and if/elif/else decisions
Keith E. Kelly
10/4/20
'''
dog_name = input("What is your dog's name?")
print("Hello " + dog_name + "!")
#in Python 3 you can also use f-strings
print(f"{dog_name} says woof!")

sit = False
stay = False

if sit == False:
    print("Bad dod!")
if sit == True:
    print("Good dog")
if stay == True:
    print("Very good dog!")

# if not sit:
#     print("Bad dod!")
# if sit:
#     print("Good dog")
# if sit and stay:
#     print("Very good dog!")
# if not sit and stay:
#     print("Confused dog!")

# if sit == True and stay == True:
#     print("Very good dog")
# elif sit == True:
#     print("Good dog")
# else:
#     print("Bad dog")