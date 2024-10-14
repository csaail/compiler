#Design a program to convert the given Right Linear Grammar into Left Linear Grammar

def print_productions():
    print("Saail Chavan KFPMSCCS016")
    
    # Getting the number of productions
    n = int(input("\nEnter the number of productions you want to convert: "))
    
    prod = []  # To store productions
    for i in range(n):
        prod.append(input(f"\nEnter production number {i + 1} in the form of (X = bY): "))  # Example: A=cB, S=eF
    
    print("\n\nThe number of productions are as below:")
    for i in range(n):
        print(f"{i + 1}) {prod[i]}")
    
    print("\n\nLeft linear grammar is -->")
    for i in range(n):
        left, right = prod[i].split('=')  # Splitting production into non-terminal and production part
        print(f"{left.strip()} --> {right.strip()}")  # Output production


if __name__ == "__main__":
    print_productions()
