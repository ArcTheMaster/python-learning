# functions with outputs
def my_function():
    result = 3 * 2
    return result

print(my_function())

def format_name(firstname, lastname):
    if firstname == '' or lastname == '':
        # return # option 1 to leave the function early
        # raise Exception('empty value') # option 2 to leaver the function early but flagged as an exception
        exit('empty value') # option 3 similar to option 1 but with a message added to the output
    else:
        # full_name = firstname.lower().capitalize() + ' ' + lastname.lower().capitalize() # option 1
        full_name = f"{firstname} {lastname}" # option 2
        return full_name.title()

firstname = str(input('enter firstname: \n'))
lastname = str(input('enter lastname: \n'))
print(format_name(firstname, lastname))

