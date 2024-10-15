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

1. [x] Add polynomials
2. [x] Subtract polynomials
3. [x] Multiply polynomials
4. [x] Raise polynomials to the nth power (exponentiation)
5. [ ] Perform polynomial division

Usage
---
To create an expression like x² + 2xy + y² we first need to create the terms present, and to do that, for each term we use the syntax:

`Term(_coefficient_, Variable(_representing letter_, _exponent_), ...)`

where the ellipsis indicates additional terms and the exponent in each `Variable()` call can be omitted if equal to 1.


- x² can be initialized with the syntax: `Term(1, Variable("x", 2))`

- 2xy can be initialized by the syntax: `Term(2, Variable("x"), Variable("y"))`


and so to create our expression x² + 2xy + y², we wrap the terms we created in an `Expression()` statement. The full syntax is as follows:

`Expression(Term(1, Variable("x", 2)), Term(2, Variable("x"), Variable("y")), Term(1, Variable("y", 2)))`


NB: to get expression terms displayed in a particular order, they must be entered into the expression parenthenses in that order.

Updates
---
##### New Features: Subtraction and Exponentiation
- Subtraction and Exponentiation can now be performed on Terms and Expressions. Exponentiation only works on non-negative integer powers
##### Bug Fixes
- __Issue__: Various program failures due to faulty logic in class initializers, particularly with respect to objects that could be said to equal 0 and with coefficients of -1.
- __Fix__: Faulty initalizer logic updated.
##### Refactored code for pythonicness

To-Do
---
- Add functionality for Division.
- I'm considering building a UI for this, because it's essentially a really dumb programming language in its current state.
