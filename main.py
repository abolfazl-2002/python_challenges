# get the user's first and last name and give them in reverse order

firstName=input("enter first name:\n") # first name
lastName=input("enter last name:\n") # last name

# reverse func
def reverse(firstname,lastname):
    fullName = lastname+ " " + firstname

    return fullName

print(reverse(firstName,lastName))