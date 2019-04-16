# ask for name and store it in a variable
n = raw_input("What's your name? ")

# printing your name
print("Hello {}".format(n))

# creating a dictionary
dict1 = {'action 2': 'practice with SDx', 'action 3': 'sleep','action 1': 'read book'}

# printing the dictionary
print(dict1)

# asking users what action they want to perform
inpt = raw_input("Your choice? ")


# or doing it with built-in get function
get_val = dict1.get(inpt, "do something else")

#printing out the correct value for a dictionary key
#print("I'll {} later!".format(dict1[inpt]))
print("I'll {} later!".format(get_val))


