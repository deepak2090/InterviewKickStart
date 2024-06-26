

def outer_function(inner_function):
    def inner_call():
        print("wrapper function executed this before \n\"{}\" function".format(inner_function.__name__))
        return inner_function()
    return inner_call





#def display():
#    print("display function called")
#x = outer_function(display)
#x()


@outer_function
def display():
    print("display function only")

display()