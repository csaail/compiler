def display(matrix, symbols):
    print("Display Matrix:")
    print("  ", " ".join(symbols))
    for i, sym in enumerate(symbols):
        print(f"{sym} ", " ".join(map(str, matrix[i][:len(symbols)])))

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
    spm = [['0'] * 20 for _ in range(20)]
    symbols = []
    
    # Input productions
    while True:
        lhs = input("Enter LHS: ")
        rhs = input("Enter RHS: ")
        productions.append((lhs, rhs))
        ans = input("Continue? (y/n): ")
        if ans.lower() == 'y':
            break
    
    # Extract unique symbols
    symbols.append(productions[0][0][0])
    for lhs, rhs in productions:
        if lhs[0] not in symbols:
            symbols.append(lhs[0])
        for char in rhs:
            if char not in symbols:
                symbols.append(char)

    # Compute FIRST matrix
    for lhs, rhs in productions:
        i = symbols.index(lhs[0])
        j = symbols.index(rhs[0])
        first[i][j] = 1
    
    print("\nFIRST MATRIX:")
    display(first, symbols)

    # Copy FIRST to FIRSTP
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            firstp[i][j] = first[i][j]

    # Compute FIRST PLUS matrix
    for i in range(1, len(symbols)):
        for j in range(len(symbols)):
            if firstp[j][i] == 1:
                for k in range(len(symbols)):
                    firstp[j][k] |= firstp[i][k]
    
    print("\nFIRST PLUS MATRIX:")
    display(firstp, symbols)

    # Compute FIRST STAR matrix
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            firsts[i][j] = firstp[i][j]
            if i == j:
                firsts[i][j] = 1
    
    print("\nFIRST STAR MATRIX:")
    display(firsts, symbols)

    # Compute LAST matrix
    for lhs, rhs in productions:
        i = symbols.index(lhs[0])
        j = symbols.index(rhs[-1])
        last[i][j] = 1
    
    print("\nLAST MATRIX:")
    display(last, symbols)

    # Copy LAST to LASTP
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            lastp[i][j] = last[i][j]

    # Compute LAST PLUS matrix
    for i in range(1, len(symbols)):
        for j in range(len(symbols)):
            if lastp[j][i] == 1:
                for k in range(len(symbols)):
                    lastp[j][k] |= lastp[i][k]
    
    print("\nLAST PLUS MATRIX:")
    display(lastp, symbols)

    # Compute LAST STAR matrix
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            lasts[i][j] = lastp[i][j]
            if i == j:
                lasts[i][j] = 1
    
    print("\nLAST STAR MATRIX:")
    display(lasts, symbols)

    # Compute EQUALS matrix
    for lhs, rhs in productions:
        if len(rhs) > 1:
            i = symbols.index(rhs[0])
            j = symbols.index(rhs[1])
            equals[i][j] = 1
    
    print("\nEQUALS MATRIX:")
    display(equals, symbols)

    # Compute LESS THAN matrix
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            lt[i][j] = sum(equals[i][k] * firstp[k][j] for k in range(len(symbols)))
    
    print("\nLESS THAN MATRIX:")
    display(lt, symbols)

    # Compute GREATER THAN matrix
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            temp = sum(lastp[k][i] * equals[k][j] for k in range(len(symbols)))
            gt[i][j] = sum(temp * firsts[k][j] for k in range(len(symbols)))
    
    print("\nGREATER THAN MATRIX:")
    display(gt, symbols)

    # Build SPM matrix
    for i in range(len(symbols)):
        for j in range(len(symbols)):
            if lt[i][j] == 1:
                spm[i][j] = '<'
            elif gt[i][j] == 1:
                spm[i][j] = '>'
            elif equals[i][j] == 1:
                spm[i][j] = '='
            else:
                spm[i][j] = '0'
    
    print("\nSPM MATRIX:")
    for row in spm[:len(symbols)]:
        print(" ".join(row[:len(symbols)]))

if __name__ == "__main__":
    main()
