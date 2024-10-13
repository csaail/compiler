#include <iostream>
#include <string.h>
using namespace std;

int state_no(char);
char dfa[5][4] = { "ABC", "BBD", "CBC", "DBE", "EBC" };

int main() {
    int i, j, k, l, a, b, c, d, e;
    char final_state[5];
    final_state[0] = 'E';
    final_state[1] = '\0';  // Null-terminated string
    char group[4][4] = {0}; // Initialize the group array to avoid garbage values
    char new_group[5][4] = {0}; // Similar initialization
    cout << "Saail Chavan KFPMSCCS016" << endl;
    cout << "********* DFA *******" << endl;
    cout << "" << "\t" << "a" << "\t" << "b" << endl;
    for (i = 0; i < 5; i++) {
        for (j = 0; j <= 2; j++) {
            cout << dfa[i][j] << "\t";
        }
        cout << endl;
    }
    cout << "Give Final State= " << final_state << endl;
    // This part is finding the minimal DFA
    k = 0;
    l = 0;
    for (i = 0; i <= 4; i++) {
        for (j = 1; j < 3; j++) {
            if (dfa[i][j] == final_state[k]) {
                k++;
                final_state[k] = dfa[i][0];
                l++;
                break;  // break loop and continue
            }
        }
    }
    c = 1; d = 0; e = 0;
    for (a = 0; a <= 4; a++) {
        for (b = 0; b <= 4; b++) {
            if (b == a) continue;
            if ((dfa[a][c] == dfa[b][c]) && (dfa[a][c + 1] == dfa[b][c + 1])) {
                group[d][e] = dfa[a][0];
                e++;
                group[d][e] = dfa[b][0];
                d++;
                break;
            }
        }
    }
    // Sorting the final states
    for (int q = 0; q < 4; q++) {
        for (int m = 0; m < 4; m++) {
            if (final_state[q] < final_state[m]) {
                char temp = final_state[q];
                final_state[q] = final_state[m];
                final_state[m] = temp;
            }
        }
    }
    cout << endl << endl << "********** MIN DFA ***********" << endl;
    cout << " " << "\ta\tb" << endl;
    // Printing the minimized DFA
    for (int o = 0; o <= 3; o++) {
        int ff = state_no(final_state[o]);
        if (dfa[ff][1] == group[0][1])
            dfa[ff][1] = group[0][0];
        if (dfa[ff][2] == group[0][1])
            dfa[ff][2] = group[0][0];
        cout << final_state[o] << "\t" << dfa[ff][1] << "\t" << dfa[ff][2] << endl;
    }
    return 0;
}
int state_no(char cc) {
    for (int aa = 0; aa <= 4; aa++) {
        if (dfa[aa][0] == cc) {
            return aa;
        }
    }
    return -1;  // Return -1 if state is not found
}