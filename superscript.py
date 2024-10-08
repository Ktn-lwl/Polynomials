exponents = "⁰¹²³⁴⁵⁶⁷⁸⁹"

def superscript(exp: int):
    if exp < 0:
        ret = "⁻"
        for i in str(exp)[1:]:
            ret += exponents[int(i)]
    else:
        ret = ""
        for i in str(exp):
            ret += exponents[int(i)]
    
    return ret
