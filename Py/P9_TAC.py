#Design a program to convert any expression into Three Address Code.

def generate_three_address_code(expr):
    sarr, code, j = [], [], 0
    print("Saail Chavan KFPMSCCS016")
    for c in expr:
        if c.isalnum():  # Operand
            sarr.append(c)
        elif c in '+-*/':  # Operator
            oprgt, oplft = sarr.pop(), sarr.pop()
            temp_var = f"T{j + 1}"
            print(f"{temp_var} = {oplft} {c} {oprgt}")
            sarr.append(temp_var)
            j += 1

if __name__ == "__main__":
    expr = input("Enter The Postfix Expression: ")
    generate_three_address_code(expr)
