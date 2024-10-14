#Design a program to check given input is identifier, constants, reserved keywords, and operators.
#compiler, break
#Reserved keywords

def res():
    reserved_keywords = ["printf", "scanf", "if", "else", "break"]
    str_input = input("Enter the string: ")

    if str_input in reserved_keywords:
        print("Reserved Keyword")
    else:
        print("Not a Reserved Keyword")


if __name__ == "__main__":
    print("Saail Chavan KFPMSCCS016\n")
    res()
