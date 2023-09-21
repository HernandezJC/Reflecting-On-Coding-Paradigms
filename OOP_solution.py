class Podracer:
  def __init__(self, max_speed, condition, price):
    self.max_speed = max_speed
    self.condition = condition
    self.price = price

  
  def repair(self):
    self.condition = "repaired"
    

class AnakinsPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def boost(self):
    self.max_speed *= 2
    

class SebulbasPod(Podracer):
  def __init__(self, max_speed, condition, price):
    super.init(max_speed, condition, price):
  
  def flame_jet(self,other):
    other.condition = "trashed"



# How does this solution demonstrate the four pillars of OOP? (It may not demonstrate all of them, describe only those that apply)
# - Encapsulation
# - Abstraction
# - Inheritance
# - Polymorphism

# This solution demonstrates several aspects of Object-Oriented Programming and adheres to some of the four pillars of OOP:
# Encapsulation:
# The Podracer class encapsulates the attributes max_speed, condition, and price.
# The AnakinsPod and SebulbasPod classes inherit these attributes and behavior and can also add their own specialized behavior such ads boost and flame_jet methods.

# Inheritance:
# Both AnakinsPod and SebulbasPod are subclasses of the Podracer class, which demonstrates the concept of inheritance. They inherit the attributes and methods of the parent class and can override or extend them as needed.

# Abstraction:
# The Podracer class abstracts the common properties and behavior of all podracer objects, allowing you to create specialized subclasses such as AnakinsPod and SebulbasPod with additional functionality.



# Would it have been easier to implement a solution to this problem using a different coding style? Why or why not?
# OOP is a suitable choice for this problem because it models real-world entities the podracers as objects with attributes and behaviors. It provides a clear way to structure the code by defining classes and their relationships. While it's possible to implement this without OOP, OOP simplifies the organization of code and makes it more intuitive to work with objects representing podracer entities.



# How did Object-Oriented Programming assist in solving this problem?
# OOP assists in solving this problem by allowing you to create a structured and modular codebase. It promotes code reuse through inheritance and allows you to model specialized behavior for different types of podracers. OOP makes it easier to manage and extend the project.