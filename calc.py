from logicky_bits.Expression import Expression, Term, Variable, get_vars, superscript
from os import system
from string import ascii_lowercase, digits
from sys import exit

letters = set(ascii_lowercase)
nums = set(digits)
op_set = {"+", "-", "*", "^"}
parens = {")", "("}

def is_good_char(char):
    return char in letters or char in op_set or char in parens or char in nums

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
        print(parenstack)
        return (False, problem)

    clean += problem[-1]
    return (True, clean)


def main():
    while True:
        variables = set()
        problem = input("Input a Polynomial to expand or press Enter to exit:\n")

        if not problem:
            exit()

        system("cls")
        validated = is_valid(problem)

        if not validated[0]:
            print("Invalid input. Please check your input and read the documentation for usage info.")

        else:
            #create variables
            for char in validated[1]:
                if char in letters and char not in variables:
                    exec(f'{char} = Term(1, Variable("{char}"))')
                    variables.add(char)
            
            exec(f"print({validated[1]})")

            for char in variables:
                exec(f"del {char}")
            
            del variables

        clear = input("Press Enter to clear:\n")
        system("cls")

        
if __name__ == "__main__":
    main()
