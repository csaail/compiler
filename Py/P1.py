#Design a program to convert the given Right Linear Grammar into Left Linear Grammar
#A=cB, S=eF, A=cB

def print_productions():
    print("Saail Chavan KFPMSCCS016")
    
    n = int(input("Enter the number of productions you want to convert: "))
    
    prod = []
    for i in range(n):
        prod.append(input(f"\nEnter production number {i + 1} in the form of (X = bY): ")) 
    
    print("\n\nThe number of productions are as below:")
    for i in range(n):
        print(f"{i + 1}) {prod[i]}")
    
    print("\n\nLeft linear grammar is -->")
    for i in range(n):
        left, right = prod[i].split('=') 
        print(f"{left.strip()} --> {right.strip()}") 


if __name__ == "__main__":
    print_productions()
