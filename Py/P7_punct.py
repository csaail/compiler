#Design a program to find FIRST and FOLLOW of all productions.

def check_punctuator():
    punctuators = [".", ",", ";", "(", ")", "{", "}", "[", "]"]
    flag = False

    print("Enter the punctuator: ")
    user_input = input().strip()

    for punct in punctuators:
        if user_input == punct:
            flag = True
            break

    if flag:
        print("Punctuator")
    else:
        print("Not a Punctuator")

if __name__ == "__main__":
    print("Saail Chavan KFPMSCCS016")
    check_punctuator()

