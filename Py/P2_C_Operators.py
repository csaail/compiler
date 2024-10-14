#Design a program to check given input is identifier, constants, reserved keywords, and operators.
#>=  &&
#Operators

def opr():
    operators = ["+", "-", "/", "*", "<=", ">=", "<", ">", "==", "!="]
    str_input = input("Enter the operator: ")

    if str_input in operators:
        print("Operator")
    else:
        print("Not an Operator")


if __name__ == "__main__":
    print("Saail Chavan KFPMSCCS016")
    opr()
