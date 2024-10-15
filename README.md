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
I plan on giving this program the ability to:
1. [-] Add polynomials
2. [-] Subtract polynomials
3. [-] Multiply polynomials
4. [-] Raise polynomials to the nth power (exponentiation)
5. [ ] Perform polynomial division

Updates
---
##### New Features: Subtraction and Exponentiation
- Subtraction and Exponentiation can now be performed on Terms and Expressions. Exponentiation only works on non-negative integer powers
##### Bug Fixes
- __Issue__: Various program failures due to faulty logic in class initializers, particularly with respect to objects that could be said to equal 0 and with coefficients of -1.
- __Fix__: Faulty initalizer logic updated.

To-Do
---
- Add functionality for Division.
- I'm considering building a UI for this, because it's essentially a really dumb programming language in its current state.
