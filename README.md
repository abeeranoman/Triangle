# Triangle Class in Python  

## Overview  
This project implements a `Triangle` class in Python that supports creating different types of triangles:  
- Default triangle (all sides = 1.0)  
- Equilateral triangle (all sides equal)  
- Isosceles triangle (two sides equal)  
- Scalene triangle (all sides different)  
- Clone of another triangle  

The class uses property decorators to safely handle side values and prevents invalid inputs such as negative lengths.  

---

## Features  
- Multiple constructors based on the number and type of arguments.  
- Safe getters and setters for each side using `@property`.  
- Validation to prevent negative side lengths.  
- String representation for easy output.  
- Ability to clone from another triangle instance.  

---

## Example Usage  

```python
from triangle import Triangle  

# Default triangle (all sides = 1.0)
t1 = Triangle()  
print(t1)   # Triangle(1.0, 1.0, 1.0)  

# Equilateral triangle
t2 = Triangle(5)  
print(t2)   # Triangle(5, 5, 5)  

# Isosceles triangle
t3 = Triangle(4, 6)  
print(t3)   # Triangle(4, 4, 6)  

# Scalene triangle
t4 = Triangle(3, 4, 5)  
print(t4)   # Triangle(3, 4, 5)  

# Clone of another triangle
t5 = Triangle(t4)  
print(t5)   # Triangle(3, 4, 5)
