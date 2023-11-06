1. Superclass, Baseclass, or Parentclass:
   - A superclass, baseclass, or parentclass is a class that serves as the blueprint for other classes. It contains common attributes and methods that can be inherited by its subclasses. Subclasses can extend and specialize the behavior of the superclass.

2. Subclass:
   - A subclass is a class that inherits attributes and methods from a superclass (or baseclass). It can add, modify, or extend the behavior of the superclass, creating a more specific or specialized class.

3. Listing Attributes and Methods of a Class or Instance:
   - To list all attributes and methods of a class, you can use the `dir(class_name)` function. To list the attributes and methods of an instance, you can use `dir(instance_name)`.

4. Instance with New Attributes:
   - Instances can have new attributes added at any time by simply assigning values to them. These new attributes are specific to the instance and don't affect the class or other instances.

5. Inheriting a Class from Another:
   - Inheritance is achieved in Python by defining a subclass that specifies the superclass it inherits from in its class definition, like this: `class Subclass(Superclass):`. The subclass will inherit the attributes and methods of the superclass.

6. Defining a Class with Multiple Base Classes:
   - Multiple inheritance allows a class to inherit from multiple base classes. You can specify multiple base classes in the class definition like this: `class Subclass(BaseClass1, BaseClass2):`.

7. Default Class for Inheritance:
   - Every class in Python implicitly inherits from the built-in `object` class. This means that even if you don't specify a superclass, your class is a subclass of `object`.

8. Overriding Inherited Methods or Attributes:
   - To override a method or attribute inherited from the base class, define a method or attribute with the same name in the subclass. This new implementation will be used in the subclass.

9. Attributes and Methods Available to Subclasses:
   - Subclasses inherit all public attributes and methods from their superclasses. Private attributes and methods (those with names starting with an underscore) are not inherited.

10. Purpose of Inheritance:
    - Inheritance promotes code reuse and allows you to create specialized classes based on existing ones. It helps in structuring code hierarchies and maintaining a clear and organized class hierarchy.

11. Using isinstance, issubclass, type, and super Built-in Functions:
    - `isinstance(object, class)` checks if an object is an instance of a specific class.
    - `issubclass(class, classinfo)` checks if a class is a subclass of another class.
    - `type(object)` returns the type of an object, and `super()` is used to call methods from a superclass within a subclass.
