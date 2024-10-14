#Design a program to check given input is identifier, constants, reserved keywords, and operators.
#Identifier

def is_valid_identifier(s):
    # Check if the first character is a letter
    if not (('a' <= s[0] <= 'z') or ('A' <= s[0] <= 'Z')):
        return False

    # Traverse the string for the rest of the characters
    for i in range(1, len(s)):
        if not (('a' <= s[i] <= 'z') or ('A' <= s[i] <= 'Z') or ('0' <= s[i] <= '9') or s[i] == '_'):
            return False

    # String is a valid identifier
    return True


if __name__ == "__main__":
    print("Saail Chavan KFPMSCCS016")
    str_input = input("Enter a string: ")

    if is_valid_identifier(str_input):
        print("Identifier")
    else:
        print("Not an Identifier")
