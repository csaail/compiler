#Practical 5: Design a program to develop Simple Precedence Matrix (SPM).
# S->aS, X->aX, B->!*

class Production:
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

def display(matrix, symbols):
    print("Display Matrix:")
    print(" ", " ".join(symbols))
    for i, row in enumerate(matrix):
        print(symbols[i], " ".join(map(str, row)))

def main():
    productions = []
    symbols = set()

    while True:
        lhs, rhs = input("\nEnter production (LHS RHS): ").split()
        productions.append(Production(lhs, rhs))
        symbols.add(lhs)
        symbols.update(rhs)
        ans = input("Continue? (y/n): ")
        if ans.lower() != 'y':
            break

    print("\nProductions are:")
    for prod in productions:
        print(f"{prod.lhs} -> {prod.rhs}")

    symbols = list(symbols)
    cnt = len(symbols)
    first = [[0] * cnt for _ in range(cnt)]
    last = [[0] * cnt for _ in range(cnt)]
    equals = [[0] * cnt for _ in range(cnt)]
    lt = [[0] * cnt for _ in range(cnt)]
    gt = [[0] * cnt for _ in range(cnt)]
    spm = [['0'] * cnt for _ in range(cnt)]

    # Compute FIRST matrix
    for prod in productions:
        lhs_index = symbols.index(prod.lhs)
        rhs_index = symbols.index(prod.rhs[0]) if prod.rhs else -1
        if rhs_index != -1:
            first[lhs_index][rhs_index] = 1

    print("\n\nFIRST MATRIX:")
    display(first, symbols)

    # Compute LAST matrix
    for prod in productions:
        lhs_index = symbols.index(prod.lhs)
        rhs_index = symbols.index(prod.rhs[-1]) if prod.rhs else -1
        if rhs_index != -1:
            last[lhs_index][rhs_index] = 1

    print("\n\nLAST MATRIX:")
    display(last, symbols)

    # Compute EQUALS matrix
    for prod in productions:
        for i in range(len(prod.rhs) - 1):
            lhs_index = symbols.index(prod.rhs[i])
            rhs_index = symbols.index(prod.rhs[i + 1])
            equals[lhs_index][rhs_index] = 1

    print("\n\nEQUALS MATRIX:")
    display(equals, symbols)

    # Compute LESS THAN matrix
    for i in range(cnt):
        for j in range(cnt):
            lt[i][j] = sum(equals[i][k] * first[k][j] for k in range(cnt))

    print("\n\nLESS THAN MATRIX:")
    display(lt, symbols)

    # Compute GREATER THAN matrix
    for i in range(cnt):
        for j in range(cnt):
            gt[i][j] = sum(last[k][i] * equals[k][j] for k in range(cnt))

    print("\n\nGREATER THAN MATRIX:")
    display(gt, symbols)

    # Build SPM matrix
    for i in range(cnt):
        for j in range(cnt):
            if lt[i][j] == 1:
                spm[i][j] = '<'
            elif gt[i][j] == 1:
                spm[i][j] = '>'
            elif equals[i][j] == 1:
                spm[i][j] = '='
            else:
                spm[i][j] = '0'  # No relation

    print("\n\nSPM MATRIX:")
    for row in spm:
        print(" ".join(row))

if __name__ == "__main__":
    main()