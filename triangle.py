# #Write a class Triangle with three instance double variables, namely sideA, sideB, and sideC. The class must have the following methods: 
# A default constructor that creates a triangle with all sides being equal to 1.0.
# A one-parameter constructor that accepts a double and creates an equilateral triangle with all sides equal to the passed parameter.
# -A two-parameter constructor that accepts two doubles x and y, and creates an isosceles triangle with sides x, x, and y. 
# -A three-parameter constructor that accepts three doubles x, y, and z, and creates a triangle with sides respectively equal to x, y, and z. 
# -A constructor that accepts a reference to an existing triangle and creates a corresponding clone; it should also return a reference to the cloned triangle.



# In the Python version, make use of single constructor that do all the jobs demanded by multiple constructors and
# @property decorator for exposing and validating side values. This problem is designed to give you hands-on practice
#  in object-oriented concepts such as constructor overloading, object cloning, static members, encapsulation, and basic geometric logic. 


class Triangle:
    def __init__(self, x=None, y=None, z=None):
        # 0 arguments: default triangle
        if x is None:
            self.sideA = self.sideB = self.sideC = 1.0

        # 1 argument: equilateral or clone 
        elif y is None and z is None:
            if isinstance(x, Triangle):  # clone: copy sides from existing triangle
                self.sideA, self.sideB, self.sideC = x.sideA, x.sideB, x.sideC
            else:                       # equilateral: all sides equal to x
                self.sideA = self.sideB = self.sideC = x

        # 2 arguments: isosceles
        elif z is None:
            self.sideB = self.sideA = x  # two equal sides
            self.sideC = y                # third side

        # 3 arguments: scalene
        else:
            self.sideA, self.sideB, self.sideC = x, y, z

        # Optional: You could validate triangle inequality here if desired
        # self._validate_triangle()

    # Internal variables start with '_' to prevent recursion inside setters/getters

    @property
    def sideA(self):
        #Getter for sideA
        return self._sideA
    
    @sideA.setter
    def sideA(self, val):
        #setter for sideC
        if val < 0:
            raise ValueError("The side can't be less than 0")  # prevent negative side
        else:
            self._sideA = val  # store the value internally

    @property
    def sideB(self):
        #getter for sideB
        return self._sideB 
    
    @sideB.setter
    def sideB(self, val):
        #setter for sideB
        if val < 0:
            raise ValueError("The side can't be less than 0")
        else:
            self._sideB = val 

    @property
    def sideC(self):
        #Getter for sideC
        return self._sideC
    
    @sideC.setter
    def sideC(self, val):
        #setter for sideC
        if val < 0:
            raise ValueError("The side can't be less than 0")
        else:
            self._sideC = val 

    def __str__(self):
        return f"Triangle({self.sideA}, {self.sideB}, {self.sideC})"

  
