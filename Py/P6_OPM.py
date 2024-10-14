#Design a program to develop Operator Precedence Matrix (OPM).
#abc def

def display(matrix, symbols):
    # Print header row
    print("  ", " ".join(symbols))
    
    # Print matrix with corresponding symbol rows
    for i, sym in enumerate(symbols):
        print(f"{sym} ", " ".join(map(str, matrix[i])))

def main():
    productions = []
    first = [[0] * 20 for _ in range(20)]
    firstp = [[0] * 20 for _ in range(20)]
    firsts = [[0] * 20 for _ in range(20)]
    last = [[0] * 20 for _ in range(20)]
    lastp = [[0] * 20 for _ in range(20)]
    lasts = [[0] * 20 for _ in range(20)]
    equals = [[0] * 20 for _ in range(20)]
    lt = [[0] * 20 for _ in range(20)]
    gt = [[0] * 20 for _ in range(20)]
    opm = [['0'] * 20 for _ in range(20)]  # Operator precedence matrix
    symbols = []
    tot = 0
    
    ans = 'n'
    
    # Input productions
    while ans == 'n':
        print("Saail Chavan KFPMSCCS016")
        lhs = input("Enter LHS: ")
        rhs = input("Enter RHS: ")
        productions.append((lhs, rhs))
        tot += 1
        ans = input("\nContinue? (y/n): ").lower()

    # Display productions
    print("\nProductions are:")
    for lhs, rhs in productions:
        print(f"\n{lhs} -> {rhs}")

    # Extract unique symbols
    symbols.append(productions[0][0][0])
    
    for lhs, rhs in productions:
        if lhs[0] not in symbols:
            symbols.append(lhs[0])
        for char in rhs:
            if char not in symbols:
                symbols.append(char)

    # Display final symbols
    print("\n\nsym final:")
    print("\t", "\t".join(symbols))

    # Initialize matrices
    for i in range(20):
        for j in range(20):
            first[i][j] = firstp[i][j] = firsts[i][j] = last[i][j] = lastp[i][j] = lasts[i][j] = equals[i][j] = lt[i][j] = gt[i][j] = 0
            opm[i][j] = '0'  # Initialize operator precedence matrix

if __name__ == "__main__":
    main()