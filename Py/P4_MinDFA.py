#Design a program to minimize the given DFA.

def state_no(cc, dfa):
    return next((i for i in range(5) if dfa[i][0] == cc), -1)

def main():
    dfa = [['A', 'B', 'C'], ['B', 'B', 'D'], ['C', 'B', 'C'], ['D', 'B', 'E'], ['E', 'B', 'C']]
    final_state, group = ['E'], [[""] * 4 for _ in range(4)]
    
    print("Saail Chavan KFPMSCCS016\n********* DFA *******\n\ta\tb")
    for row in dfa: print("\t".join(row))
    
    for i in range(5):  # Find final states
        if dfa[i][1] == final_state[0] or dfa[i][2] == final_state[0]: final_state.append(dfa[i][0])
    
    final_state.sort()  # Sort final states

    for a in range(5):  # Grouping equivalent states
        for b in range(a + 1, 5):
            if dfa[a][1:] == dfa[b][1:]: group[a][0], group[a][1] = dfa[a][0], dfa[b][0]

    print("\n\n********** MIN DFA ***********\n\ta\tb")
    for fs in final_state:
        ff = state_no(fs, dfa)
        if ff != -1:
            if dfa[ff][1] == group[0][1]: dfa[ff][1] = group[0][0]
            if dfa[ff][2] == group[0][1]: dfa[ff][2] = group[0][0]
            print(f"{fs}\t{dfa[ff][1]}\t{dfa[ff][2]}")

if __name__ == "__main__":
    main()
