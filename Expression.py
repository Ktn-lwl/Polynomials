from Variable import *

class Term:
    def __init__(self, coeff: int, *var_list: Variable):
        self.coeff = coeff
            
        if self.coeff == 0:
            self.variables = {}
        
        else:
            self.variables = {v.name:v.exp for v in var_list}
        
        #decompose 0 powers
        variable_keys = list(self.variables.keys())

        for variable in variable_keys:
            if self.variables[variable] == 0:
                del self.variables[variable]

        self.multivariacy = self.is_multivariate()

    #groundwork for division
    def is_multivariate(self):
        if self.is_int() or len(self.variables) < 2:
            return False
        
        return True

    def is_int(self):
        return self == self.coeff
    
    def __int__(self):
        return self.coeff

    def __str__(self, show_coeff = True):
        if self.coeff == 0:
            return "0"
        
        elif self.coeff == 1 and not self.variables:
            ret = "1"
        
        elif self.coeff == 1:
            ret = ""
        
        elif self.coeff == -1 and not self.variables:
            ret = "-1"

        elif self.coeff == -1:
            ret = "-"
        
        else:
            ret = f"{self.coeff}"*show_coeff

        for i in sorted(self.variables.keys()): 
            #arranges variables in the term in alphabetical order for a standard look
            ret += f"{i}{superscript(self.variables[i])}"

        return ret
    
    #helps create a dict when initializing an Expression
    def no_coeff_str(self):
        if self.is_int():
            return "0"
        
        if self.coeff == -1:
            return Term.__str__(self, show_coeff = False)[1:]
        
        return Term.__str__(self, show_coeff = False)

    def __add__(self, other):
        if type(other) == int and self.is_int():
            return Term(coeff = other + self.coeff)
        
        elif type(other) == int:
            return Expression(self, Term(other))

        elif type(other) == Expression:
            return Expression(self) + other
        
        elif type(other) == Term:
            pass
        
        else:
            raise TypeError(f"Can't add with '{type(other)}' object")

        if self.variables == other.variables:
            new_coeff = self.coeff + other.coeff
            return Term(new_coeff, *get_vars(self.variables))
        
        else:
            return Expression(self, other)
        
    def __sub__(self, other):
        return self + -1 * other
    
    def __rsub__(self, other):
        return other + -1 * self
    
    def __mul__(self, other):
        if other == 0:
            return 0
        
        elif type(other) == int:
            vars = get_vars(self.variables)
            new_coeff = self.coeff * other
            
            return Term(new_coeff, *vars)
        
        elif type(other) == Expression:
            return Expression(self) * other

        elif type(other) != Term:
            raise TypeError(f"Can't multiply Term object with '{type(other)}' object")

        new_coeff = self.coeff * other.coeff
        new_vars = self.variables.copy()
        
        for i in other.variables:
            if i in new_vars:
                new_vars[i] += other.variables[i]
            
            else:
                new_vars[i] = other.variables[i]
           
        new_vars = get_vars(new_vars)
        
        return Term(new_coeff, *new_vars)

    def __pow__(self, n):
        if n < 0:
            #polynomials have powers greater than or equal to 0
            return 0
        elif n == 0:
            return 1
        elif n == 1:
            return self
        elif n == 2:
            return self * self
        
        if n%2 == 0:
            return pow(self, n//2) ** 2
        else:
            return (pow(self, n//2) ** 2) * self
        
    def __eq__(self, other):
        if type(other) == Term:
            return self.variables == other.variables and self.coeff == other.coeff
        
        elif type(other) == int and not self.variables:
            return self.coeff == other
        
        elif type(other) == int and self.variables:
            return False
        
        else:
            return False
        
    #in place operations
    def __iadd__(self, other):
        return self + other
    
    def __isub__(self, other):
        return self - other
       
    def __imul__(self, other):
        return self * other

    def __ipow__(self, other):
        return self**other

    #ensure commutativity
    __rmul__ = __mul__ 
    __radd__ = __add__


class Expression:
    def __init__(self, *terms : Term):
        self.terms = dict([(terms[i].no_coeff_str(), terms[i]) for i in range(len(terms))])

        if "0" in self.terms and self.terms["0"] == 0:
            del self.terms["0"]

        self.multivariacy = self.is_multivariate()

    def is_multivariate(self):
        for term in self.terms:
            if self.terms[term].is_multivariate():
                return True
        
        if len(self.terms) > 2 or len(self.terms) == 2 and "0" not in self.terms:
            return True
            
        return False

    def __str__(self):
        if not self.terms:
            return "0"
        
        ret = ""
        for term in self.terms.values():
            if not ret:
                ret += f"{str(term)} "
            
            elif term.coeff < 0:
                ret += f"- {str(term)[1:]} "
            else:
                ret += f"+ {str(term)} "

        return ret[:-1] #remove the trailing space
    
    def __eq__(self, other):
        if type(other) == int:
            return Expression(Term(other)) == self
        
        elif type(other) == Term:
            return Expression(other) == self
        
        elif type(other) == Expression:
            return self.terms == other.terms

        else:
            return False
    
    def __add__(self, other):
        new_terms :dict = self.terms.copy()

        if type(other) == Expression:
            for term in  other.terms:
                if term in new_terms:
                    new_terms[term] = new_terms[term] + other.terms[term]

                else:
                    new_terms[term] = other.terms[term]
                
            return Expression(*new_terms.values())
        
        elif type(other) == int:
            return  self + Term(other)

        elif type(other) == Term:
            return self + Expression(other)
        
        else:
            raise TypeError(f"Can't perform addition between Expression and '{type(other)}' object.")
        
    def __sub__(self, other):
        return self + -1 * other
    
    def __rsub__(self, other):
        return other + -1 * self
        
    #I've hit a bit of a block here. My knee jerk reaction is to use an algorithm that
    #works on O(n²) time (Ignoring the underlying logic), and I have one ready to go. But
    #some googling (regarding polynomial expansion) tells me that it MIGHT be possible to
    #cut down on that time to somewhere between linear and loglinear time. I'm currently 
    #researching Fourier Transforms and Horner's method to this end.
    #Here's the O(n²) code in the mean time:
    
    
    def __mul__(self, other):
        res = Expression(*[])

        if type(other) == Term:
            other = Expression(other)
        elif type(other) == int:
            other = Expression(Term(other))
            
        for term in self.terms:
            for other_term in other.terms:
                res = res + (self.terms[term] * other.terms[other_term])
        
        if res == 0:
            return Expression(*[])
        
        return res

    def __pow__(self, n):
        if n < 0:
            #polynomials have powers greater than or equal to 0
            return 0
        elif n == 0:
            return 1
        elif n == 1:
            return self
        elif n == 2:
            return self * self
        
        if n%2 == 0:
            return pow(self, n//2) ** 2
        else:
            return (pow(self, n//2) ** 2) * self
    
    #in place operations
    def __iadd__(self, other):
        return self + other
    
    def __isub__(self, other):
        return self - other
       
    def __imul__(self, other):
        return self * other

    def __ipow__(self, other):
        return self**other

    #ensure commutativity
    __radd__ = __add__
    __rmul__ = __mul__