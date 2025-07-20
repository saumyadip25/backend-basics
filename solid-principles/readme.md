# SOLID Principles

## 1. Single Responsibility Principle (SRP)
- **Definition:** A class should have one, and only one, reason to change.
- **Meaning:** A class must have only one responsibility or functionality.
- **Why Important:** 
  - A single-focused class is easier to maintain and test.
  - Reduces the risk of introducing bugs when changes are made.
  - Contains fewer methods and variables, making it more reusable.

---

## 2. Open/Closed Principle (OCP)
- **Definition:** Software entities (classes, modules, functions, etc.) should be **open for extension, but closed for modification.**
- **Meaning:** 
  - You should be able to add new features or behavior without modifying the existing code.
- **Why Important:**
  - Prevents breaking existing functionality.
  - Encourages using interfaces, abstract classes, and inheritance for extensibility.

---

## 3. Liskov Substitution Principle (LSP)
- **Definition:** Objects of a superclass should be replaceable with objects of its subclasses **without affecting the correctness of the program.**
- **Meaning:** 
  - Derived classes must honor the contracts defined by their base class.
  - A subclass should behave like its parent class when used in its place.
- **Why Important:**
  - Avoids unexpected behavior and ensures polymorphism works correctly.

---

## 4. Interface Segregation Principle (ISP)
- **Definition:** Clients should not be forced to depend on interfaces they do not use.
- **Meaning:** 
  - Prefer multiple small, specific interfaces over one large, general-purpose interface.
- **Why Important:**
  - Classes only implement methods they actually need.
  - Reduces unnecessary coupling and improves flexibility.

---

## 5. Dependency Inversion Principle (DIP)
- **Definition:** 
  - High-level modules should not depend on low-level modules.  
  - Both should depend on **abstractions.**  
  - Abstractions should not depend on details; **details should depend on abstractions.**
- **Meaning:** 
  - Rely on interfaces or abstract classes instead of concrete classes.
- **Why Important:**
  - Increases flexibility and testability (e.g., easier to swap implementations).
  - Reduces tight coupling between components.
