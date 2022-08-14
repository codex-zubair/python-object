# creating an object class.
class objectStuff:

    # THIS IS THE PROPERTIES OF THE OBJECT
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print("working");
        if self.name == "hello":
            print("yes Hello")

# THIS IS THE FUNCTION FOR CALLING THE SYSTEM.
    def do_work(self):

        print(self.name)
        print(self.age)
