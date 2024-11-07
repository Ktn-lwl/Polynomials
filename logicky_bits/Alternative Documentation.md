Alternative Documentation
---

The easiest way to create an expression is to make the composing variables. For instance, to create an expression like x² + 2xy + y² we can do so by initializing all the present (x and y) as Terms. Terms are initialized with the syntax:

`Term(coefficient, Variable(representing_letter, exponent), ...)`

where the ellipsis indicates additional terms and the exponent in each `Variable()` call can be omitted if equal to 1.

To make a simple `x` and `y`, we can use the syntax:

```
x = Term(1, Variable("x"))
y = Term(1, Variable("y"))
```

And to get our final expression, we could just treat our 'code' variables x and y like we normally would on paper:

`result = x**2 + 2*x*y + y**2`

Or better yet, since this _is_ an expansion calculator, we could just use the factored form: (x+y)²

`result = (x + y)**2`

The calculator also supports equality comparison, so `(x + y)**2 == x**2 + 2*x*y + y**2` will return `True`.

---

Alternatively, we could use the full syntax method:

- x² can be initialized with the syntax: `Term(1, Variable("x", 2))`

- 2xy can be initialized by the syntax: `Term(2, Variable("x"), Variable("y"))`


and so to create our expression x² + 2xy + y², we wrap the terms we created in an `Expression()` statement. The full syntax is as follows:

`Expression(Term(1, Variable("x", 2)), Term(2, Variable("x"), Variable("y")), Term(1, Variable("y", 2)))`


NB: to get expression terms displayed in a particular order, they must be entered into the expression parenthenses in that order.