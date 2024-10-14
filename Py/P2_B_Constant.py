#Design a program to check given input is identifier, constants, reserved keywords, and operators.
#12345,  124asf
#Constants

def pcon():
    flag = True
    str_input = input("Enter the string: ")

    # Check if all characters are digits
    for char in str_input:
        if not ('0' <= char <= '9'):
            flag = False
            break

    # Print the result based on the flag
    if flag:
        print("Constant")
    else:
        print("Not a Constant")


if __name__ == "__main__":
    print("Saail Chavan KFPMSCCS016")
    pcon()
