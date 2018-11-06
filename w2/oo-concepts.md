# Object-oriented programming

---

# What is an _object?_

An object combines **state**, **behavior**, and **identity**.

- State is data, known as attributes or properties.
- Behaviors are known as methods.
- Identity is the object's _class_.

---

# Exercise: object-oriented programming with phones

- What properties does your phone have?
- What actions can your phone do?
- Could you organize phones into a hierarchy?

---

# What is a _class_?

A _class_ is a blueprint for an object.

```js
var students = new Set() // js
```

```rb
students = Set.new       # ruby
```

`Set` is a class[^1]; `students` is an object.

[^1]: not really a class, but close enough; will discuss with JS people later

---

# Inheritance

Vehicle → Four-Wheeled Vehicle → Car → Sedan
A sedan _is a_ car, which _is a_ four-wheeled vehicle, which _is a_ vehicle.

Animal → Mammal → Primate → Orangutan

---

# Exercise: inheritance is tricky

- What's the inheritance chain for a ukulele?
- What's the inheritance chain for a diet root beer?
- What's the inheritance chain for a person in the classroom?

---

# Composition

A person _has a_ job, has family members, has communities.

```
Person
  Job
  Person[] (family)
  Community[]
```

Building objects out of other objects is composition.

---

# Is this better?

- Claimed benefits
  - Code reuse
  - Improved software maintainability
  - Better design: OOP forces programmers to spend more time in design
  - Encapsulation: once an object is created, knowledge of its implementation is not necessary to use it
