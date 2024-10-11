Polynomials!
---
I want to actually try using magic methods and operator overloading, so I've decided to make a useful tool for math classes: Code that makes working with polynomials easy(-ish) : )!

Definitions _(For the sake of this project...)_
---
- Variable: A mathematical object of the form x^n where "x" is a letter representing the mathematical variable, and n is its exponent.
- Term: A mathematical object composed of at least one Variable (the exception being when they decompose into just coefficients) and a numerical coefficient.
- Expression: A sum of Terms

Functionality
---
I made this on a whim, so I'll probably add more functionality as I go along, but basically I want it to:

1. [ ] Perform operations on and between polynomials.

Updates
---
##### Bug Fix
- __Issue__: exponents equal to 1 still got displayed. It's not wrong, just odd to look at because math isn't usually written that way.
- __Fix__: Variables to the 1th power now hide their exponent.
##### Modularity
- The cyclic dependency that existed between Terms and Variables has been removed at the expense of Variable's operability i.e Variables' ability to independently function in operations has been removed. 
- The Variable class has been moved to its own file, Variable.py . Terms and objects are still somewhat cyclically dependent in the case of addition and so they exist together in Expression.py.
##### New Class: Expressions
- Expressions should be the highest level object I create. They are an aggregation of Terms, which are an aggregation of Variables.
- Expressions currently support distributive multiplication, addition, and equality comparison with ints, Terms, and other Expressions.

To-Do
---
- Add functionality for subtraction and __maybe__ division.
