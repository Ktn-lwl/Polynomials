Polynomials!
---
I want to actually try using magic methods and operator overloading, so I've decided to make a useful tool for math classes: Code that makes working with polynomials easy(-ish) : )!

Functionality
---
I made this on a whim, so I'll probably add more functionality as I go along, but basically I want it to:

1. [ ] Perform operations on and between polynomials.

Updates
---
Well, this _is_ the first commit so there are no updates per se, so here's achieved funtionality so far:

- Implemented Variables[^1] and Terms[^2] as classes.
- Can multiply Variables and Terms commutatively.

To-Do
---
- Add functionality for addition and subtraction, and __maybe__ division. Addition and subtraction should be easy
- Add comments (I really need to work on my commenting culture)

[^1]: For the sake of this project, a Variable is a mathematical object of the form $x^n$ where "x" is a letter representing the mathematical variable, and n is its exponent .
[^2]: For the sake of this project, a Term is mathematical object cmoposed of at least one of such variables mentioned above, and a coefficient. All Variables can be changed into terms, but for simplicity, I've decided to make it so that Terms can't be changed back to Variables. so before any operation is carried out, all objects involved are changed to Terms.