
# Python program to
# demonstrate protected members
 




 
# Creating a base class
class Base:
    def __init__(self):
 
        # Protected member
        #here Declare the value in the object initialize constructor.
        self._a = 2
 






# Creating a derived class
class Derived(Base):
    def __init__(self):
 
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("Calling protected member of base class: ",
              self._a)
 
        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)



