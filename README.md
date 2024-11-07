Polynomials!
---
I want to actually try using magic methods and operator overloading, so I've decided to make a useful tool for math classes: A polynomial expansion calculator!

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
Simply run calc.py, type the polynomial you'd like to expand into the terminal (with some caveats, see below), and hit Enter!


#### _Currently supported syntax_
| Operation | Syntax|
| --- | --- |
| Addition | `+` |
| Subtraction | `-` |
| Multiplication | `*` |
| Exponentiation | `^` |

__Warnings__: 
- Variables must be lowercase Latin letters e.g. a, b, c, ...
- __Quirks with exponentiation__: If you want proper results with exponentiation, you __must__ follow the exponentiation symbol immediately with a non-negative integer that is either delimited by a `+`, `-`, `*` or EOL. In other words, that part of your input needs to be of the form: (expression)<sup>n</sup> and where n is a non-negative integer and is followed immediately by a plus, minus, or multiplication sign, or nothing at all. I'll try to improve the regex to allow for parentheses, please bear with me.

- I don't reccommend making exponents too big (for obvious reasons). It works for most part, but for (expression)<sup>n</sup>, as n gets huge, it takes more runtime and you might get truncated output because of the insanely huge numbers generated.

For a surface-level breakdown on how it works behind the scenes, check out the <a href="logicky_bits/Alternative Documentation.md">Alternative Documentation</a>.

Updates
---
### Finally! A _proper_ interface!
- I made a new file: calc.py that allows for an interactive session to expand polynomials provided user input is syntactically correct.

### Reorganization
- Oops! You might've noticed it looks awfully empty in the home directory. Don't worry, I just did some reorganizing; there's a new subdirectory where I keep the logic.

### Refactoring
- Fixed some weird variable names and rephrased some things.


To-Do
---
- Fix exponentiation regex.
- Add functionality for Division.
- Build a prettier UI: I'm learning JavaScript and Flask to help with this (might be a while).
