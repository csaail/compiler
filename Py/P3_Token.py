#Design a lexical analyzer to recognize the token defined by the given program.
#Saail Chavan, Saail007

def is_valid_identifier(s):
    # Check if the first character is a letter
    if not (('a' <= s[0] <= 'z') or ('A' <= s[0] <= 'Z')):
        return False

    # Traverse the string for the rest of the characters
    for char in s[1:]:
        if not (('a' <= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9') or char == '_'):
            return False

    # String is a valid identifier
    return True

def is_operator(s):
    operators = ["+", "-", "/", "*", "<=", ">=", "<", ">", "==", "!="]
    return s in operators

def is_punctuation(s):
    punctuations = [".", ",", ";", "(", ")", "{", "}", "[", "]"]
    return s in punctuations

def is_reserved_keyword(s):
    reserved_keywords = ["printf", "scanf", "if", "else", "break"]
    return s in reserved_keywords

def is_constant(s):
    # Check if all characters are digits
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return True

def main():
    str_input = input("Enter a string: ")
    # Check if the string is a valid identifier, reserved keyword, operator, punctuation, or constant
    if (is_valid_identifier(str_input) or is_reserved_keyword(str_input) or
            is_punctuation(str_input) or is_operator(str_input) or is_constant(str_input)):
        print(f"{str_input} is a Token")
    else:
        print(f"{str_input} is Not a Token")

if __name__ == "__main__":
    main()
