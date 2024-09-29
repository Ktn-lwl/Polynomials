class Variable:
    def __init__(self, name:str, exp: int):
        self.name = name[0]
        self.exp = exp

    def __mul__(self, other):
        if type(other) == Variable:
            return Term(variable=self) * Term(variable=other)
        elif type(other) == Term:
            return Term(variable=self) * other
            
    def __eq__(self, other):
        return self.name == other.name and self.exp == other.exp
    
    def __str__(self):
        return f"{self.name}^{self.exp}"
    
    __rmul__ = __mul__
         
class Term:
    def __init__(self, variables: list[Variable] = None, coeff: int = 1, variable: Variable = None):
        if variable:
            self.variables = {variable.name:variable.exp}
            self.coeff = coeff

        else:
            self.variables = {v.name:v.exp for v in variables}
            self.coeff = coeff
    
    def __mul__(self, other):#under implementation
        if type(other) == Variable:
            other = Term(variable=other)

        new_coeff = self.coeff*other.coeff
        new_vars = self.variables.copy()
        
        for i in other.variables.keys():
            try:
                new_vars[i] += other.variables[i]

            except KeyError:
                new_vars[i] = other.variables[i]
        
        new_vars = [Variable(k, new_vars[k]) for k in new_vars.keys()]
        
        return Term(coeff=new_coeff, variables=new_vars)
    
    def __str__(self):
        if self.coeff == 0:
            return "0"
        elif self.coeff == 1:
            ret = ""
        else:
            ret = f"{self.coeff}"
        for i in sorted(self.variables.keys()):
            ret += f"{i}^{self.variables[i]}"

        return ret

    __rmul__ = __mul__

a, b, c = Variable("x", 3), Variable("y", 2), Variable("x", 2)
e = Term([Variable("a", 3), Variable("y", 3)], coeff=7)
d = a * b * c * e

print(f"{a} * {b} * {c} * {e} = {d}")
print(Term(variable=a))
