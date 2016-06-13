# This program says hello and asks for my name.

print ("Hello World")


print ("What is your name?")  # This commands asks for the user's name.
myName = input()    # defines the name variable.
print ("It is good to meet you, " + myName) # Greeting phrase.
print ("The length of your name is:")
print (len(myName))

print("What is your age?")   # This block asks the user's age
myAge = input()
print ("You will be " + str(int(myAge) +1) + " in a year.")
