# Q.21 What are oops concepts? Is multiple inheritance supported in java



""" Object-Oriented Programming (OOP) is a programming paradigm that revolves around the concept of "objects," which can contain data (attributes or properties) and code (methods or functions).
OOP is based on several fundamental concepts, often referred to as the four pillars of OOP:

1 Class: A class is a blueprint for creating objects. It defines the attributes (data fields) and methods (functions) that characterize objects of that class. Objects are instances of classes.

2 Object: An object is an instance of a class. It represents a real-world entity with its own state (attributes) and behavior (methods). Objects can interact with each other by invoking methods and accessing attributes.

3 Encapsulation: Encapsulation is the bundling of data (attributes) and methods (functions) that operate on that data into a single unit, i.e., a class. It hides the internal state of an object from the outside world and only exposes the necessary functionalities through public methods. Encapsulation helps in achieving data hiding and abstraction.

4 Inheritance: Inheritance is the mechanism by which a new class (subclass or derived class) inherits properties and behavior (methods) from an existing class (superclass or base class). It promotes code reusability and establishes a hierarchical relationship between classes. Inheritance allows subclasses to extend and specialize the functionality of their superclass.

5 Polymorphism: Polymorphism means "many forms." It allows objects of different classes to be treated as objects of a common superclass. Polymorphism enables methods to behave differently based on the object they are invoked upon. There are two types of polymorphism: compile-time polymorphism (method overloading) and runtime polymorphism (method overriding).

6 Abstraction: Abstraction refers to the process of hiding complex implementation details and showing only essential features of an object. It allows the creation of abstract classes and interfaces, which define a blueprint for other classes to follow. Abstract classes cannot be instantiated, while interfaces provide a contract for implementing classes


Regarding multiple inheritance in Java:

Java does not support multiple inheritance of classes, meaning a class cannot directly inherit from more than one class. This was a design decision made by the creators of Java to avoid certain complexities and ambiguities associated with multiple inheritance, such as the diamond problem.

However, Java does support multiple inheritance through interfaces.
A Java class can implement multiple interfaces, thereby inheriting method signatures from each interface. 
This allows Java to achieve the benefits of multiple inheritance in terms of code reuse and polymorphism, while avoiding the complexities of inheriting state (data members) from multiple classes.

"""