from  superscript import superscript

class Variable:
    def __init__(self, name:str, exp: int = 1):
        self.name = name[0] #ensure that names are single characters only
        self.exp = exp
    
    def __str__(self):
        return f"{self.name}{superscript(self.exp)}"
    
def get_vars(var_list: dict = None):
    return [Variable(v, var_list[v])  for v in var_list.keys()]