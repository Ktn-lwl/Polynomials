from superscript import superscript

class Variable:
    """
    In this project, a Variable is defined as a mathematical object of the form:
    X^n, where "X" is the letter representing it, and n is the exponent, a 
    natural number. For simplicity, all mathematical operations on Variable objects
    return Term objects.
    """
    def __init__(self, name:str, exp: int = 0):
        self.name = name[0] #ensure that names are single characters only
        self.exp = exp

    def is_int(self):
        return self == 1
    
    def __str__(self):
        return f"{self.name}{superscript(self.exp)}"
    
    """
    The functions below hand work over to the Term class because Variables exist
    in a subdomain of Terms' domain
    """

    def __add__(self, other):
        return Term(variable = self) + other
        
    def __mul__(self, other):
        return Term(variable = self) * other

    def __eq__(self, other):
        return Term(variable = self) == other
    
    #ensure commutativity
    __rmul__ = __mul__ 
    __radd__ = __add__

class Term:
    """
    In this project, a Term is a mathematical object that can be represented as the
    product of one or more Variable objects with a numerical coefficient. 
    """
    def __init__(self, var_list: list[Variable] = [], coeff: int = 1, variable: Variable = None):
        #Param list functions in place of a function overload.
        #Can either create from scratch with a list of variables or convert a single variable.
        if variable:
            self.variables = {variable.name:variable.exp}
            self.coeff = coeff

        else:
            self.variables = {v.name:v.exp for v in var_list}
            self.coeff = coeff

    def is_int(self):
        return self == self.coeff
    
    def __str__(self):
        if self.coeff == 0:
            return "0"
        
        elif self.coeff == 1 and not self.variables:
            ret = "1"
        
        elif self.coeff == 1:
            ret = ""
        
        else:
            ret = f"{self.coeff}"

        for i in sorted(self.variables.keys()): 
            #arranges variables in the term in alphabetical order for a standard look
            ret += f"{i}{superscript(self.variables[i])}"

        return ret

    def __add__(self, other):
        if type(other) == int and self.is_int():
            return Term(coeff = other + self.coeff)
        
        elif type(other) == Variable:
            other = Term(variable = other)

        elif type(other) != Term:
            #There's a chance I might implement expressions as a class, but that might be overkill
            #For now, do nothing in this case ¯\_(ツ)_/¯ 
            pass

        if self.variables == other.variables:
            new_coeff = self.coeff + other.coeff
            return Term(coeff = new_coeff, var_list = get_vars(self.variables))
    
    def __mul__(self, other):
        if other == 0:
            return 0
        
        elif type(other) == int:
            vars = get_vars(self.variables)
            new_coeff = self.coeff * other
            
            return Term(var_list = vars, coeff = new_coeff)

        elif type(other) == Variable:
            other = Term(variable = other)

        elif type(other) != Term:
            raise TypeError(f"Can't multiply Term object with '{type(other)}' object")

        new_coeff = self.coeff * other.coeff
        new_vars = self.variables.copy()
        
        for i in other.variables.keys():
            try:
                new_vars[i] += other.variables[i]

            except KeyError:
                new_vars[i] = other.variables[i]
        
        new_vars = get_vars(new_vars)
        
        return Term(coeff = new_coeff, var_list = new_vars)
    
    def __eq__(self, other):
        if type(other) == Variable:
            return Term(variable = other) == self
        
        elif type(other) == Term:
            return self.variables == other.variables and self.coeff == other.coeff
        
        elif type(other) == int and other == 0:
            return self.coeff == 0
        
        elif type(other) == int:
            for vars in self.variables.keys():
                if self.variables[vars] != 0:
                    return False

            return self.coeff == other
        
        else:
            return False
        
    #ensure commutativity
    __rmul__ = __mul__ 
    __radd__ = __add__


def get_vars(var_list: dict = None):
    return [Variable(v, var_list[v])  for v in var_list.keys()]

