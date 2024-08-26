class Parent:
    def __init__(self):
        self._private = "I'm private"
        self.public = "I'm public"

    def __private_method(self):
        return "This is a private method"

    def public_method(self):
        return "This is a public method"

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.public = "I'm still public"

    def access_private(self):
        # This will not work
        #return self.__private  # AttributeError: 'Child' object has no attribute '__private'
        #return self.public
        
        # However, you can access the mangled name
        return self._private  # Returns "I'm private"

    def call_private_method(self):
        # This will not work
        # return self.__private_method()  # AttributeError: 'Child' object has no attribute '__private_method'
        
        # However, you can access the mangled name
        return self.__private_method()  # Returns "This is a private method"

x = Child()
breakpoint()
print(x.access_private() + x._Parent__private_method())