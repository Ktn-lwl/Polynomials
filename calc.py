from logicky_bits.Expression import Expression, Term, Variable, get_vars, superscript
from os import system
from string import ascii_lowercase, digits
from sys import exit

letters = set(ascii_lowercase)
nums = set(digits)
op_set = {"+", "-", "*", "^"}
parens = {")", "("} 

#edit zone
subs = {"@":"", "#":"", "$":"", "&":""}
#edit end

error_msg = "Invalid input. Please check your input and read the documentation for usage info."

def is_good_char(char):
    return char in letters or char in op_set or char in parens or char in nums #`or char in subs.keys()

def is_valid(problem):
    parenstack = 0
    index = 0
    clean = ""

    if problem[-1] in {"+","-","(","*","^"} or not is_good_char(problem[-1]):
        return (False, problem)

    while index < len(problem) - 1:
        char = problem[index]
        nxt = problem[index + 1]

        con1 = nxt in letters or nxt == "("
        con2 = nxt in nums
        con3 = nxt in {")","*","^"}

        if not is_good_char(char):
            return (False, problem)

        if char == ")" and parenstack == 0:
            return (False, problem)
        elif (char in letters or char == ")") and con2:
            return (False, problem)
        elif (char in {"+","-","("}) and con3:
            return (False, problem)
        elif char == "^" and nxt not in nums:
            return (False, problem)
        elif char == "^":
            clean += "**"
        elif (char in letters or char in nums or char == ")") and con1:
            clean += char + "*"
            parenstack -= char == ")"
        elif char == ")":
            clean += char
            parenstack -= 1
        elif char == "(":
            clean += char
            parenstack += 1
        else:
            clean += char
            
        index += 1

    if problem[-1] == ")" and parenstack != 1:
        return (False, problem)

    clean += problem[-1]
    return (True, clean)

#edit zone
def define_subs(sym):
    print("Enter Expression for substitution")
    expr = input(f"{sym} = ")
    if is_valid(expr)[0]:
        subs[sym] = expr[1]
    else:
        print(error_msg)
        clear = input("Press Enter to clear:\n")
        system("cls")
    
    main()
#edit end

def main():
    while True:
        variables = set()

        try:
            problem = input("Input a Polynomial to expand or press Enter to exit:\n")
        except EOFError:
            print(error_msg)
            continue

        problem = problem.replace(" ", "")

        if not problem:
            exit()

        #edit zone
        elif len(problem) == 2 and problem[0] == "~" and problem[1] in subs:
            define_subs(problem[1])
        #edit end

        system("cls")
        validated = is_valid(problem)

        if not validated[0]:
            print(error_msg)

        else:
            #create variables
            for char in validated[1]:
                if char in letters and char not in variables:
                    exec(f'{char} = Term(1, Variable("{char}"))')
                    variables.add(char)
            
            print(f"{problem} = ", end = "")
            exec(f"print({validated[1]})")

            for char in variables:
                exec(f"del {char}")
            
            del variables

        clear = input("Press Enter to clear:\n")
        system("cls")

        
if __name__ == "__main__":
    main()
