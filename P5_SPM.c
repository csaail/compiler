#include <stdio.h>
#include <string.h>

struct prod {
    char lhs[50];
    char rhs[50];
} p[30];

int first[20][20], firstp[20][20], firsts[20][20], last[20][20], lastp[20][20], lasts[20][20], equals[20][20], lt[20][20], gt[20][20], temp[20][20];
char spm[20][20];
int tot = 0, i, j, k, cnt = 0, flag = 0, sum = 0;
char sym[30], ans = 'y';

void display(int mat[20][20]) {
    printf("Display Matrix:\n");
    for (i = 0; i < strlen(sym); i++) {
        printf(" %c", sym[i]);
    }
    printf("\n");
    for (i = 0; i < strlen(sym); i++) {
        printf("%c ", sym[i]);
        for (j = 0; j < strlen(sym); j++) {
            printf("%d ", mat[i][j]);
        }
        printf("\n");
    }
}

int main() {
    tot = 0;

    while (ans == 'y') {        
        printf("Saail Chavan KFPMSCCS016");
        printf("\nEnter production (LHS RHS): ");
        scanf("%s %s", p[tot].lhs, p[tot].rhs);
        tot++;
        printf("Continue? (y/n): ");
        ans = getchar(); // Use getchar() to get the character input
        while (getchar() != '\n'); // Clear buffer
    }

    printf("\nProductions are:\n");
    for (i = 0; i < tot; i++) {
        printf("%s -> %s\n", p[i].lhs, p[i].rhs);
    }

    cnt = 0;
    sym[cnt++] = p[0].lhs[0];

    for (i = 0; i < tot; i++) {
        flag = 0;
        for (j = 0; j < cnt; j++) {
            if (sym[j] == p[i].lhs[0]) {
                flag = 1;
                break;
            }
        }
        if (!flag) {
            sym[cnt++] = p[i].lhs[0];
        }

        for (k = 0; k < strlen(p[i].rhs); k++) {
            flag = 0;
            for (j = 0; j < cnt; j++) {
                if (sym[j] == p[i].rhs[k]) {
                    flag = 1;
                    break;
                }
            }
            if (!flag) {
                sym[cnt++] = p[i].rhs[k];
            }
        }
    }

    printf("\nsym final:\n");
    for (i = 0; i < cnt; i++) {
        printf("\t%c", sym[i]);
    }

    for (i = 0; i < 20; i++) {
        for (j = 0; j < 20; j++) {
            first[i][j] = firstp[i][j] = firsts[i][j] = 0;
            last[i][j] = lastp[i][j] = lasts[i][j] = 0;
            equals[i][j] = lt[i][j] = gt[i][j] = 0;
            spm[i][j] = '0'; // Initialize to '0'
        }
    }

    // Compute FIRST matrix
    for (k = 0; k < tot; k++) {
        for (i = 0; i < cnt; i++) {
            for (j = 0; j < cnt; j++) {
                if (p[k].lhs[0] == sym[i] && p[k].rhs[0] == sym[j]) {
                    first[i][j] = 1;
                }
            }
        }
    }

    printf("\n\nFIRST MATRIX:\n");
    display(first);

    // Copy FIRST to FIRSTP
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            firstp[i][j] = first[i][j];
        }
    }

    // Compute FIRST PLUS matrix
    for (i = 1; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            if (firstp[j][i] == 1) {
                for (k = 0; k < cnt; k++) {
                    firstp[j][k] |= firstp[i][k];
                }
            }
        }
    }

    printf("\n\nFIRST PLUS MATRIX:\n");
    display(firstp);

    // Compute FIRST STAR matrix
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            firsts[i][j] = firstp[i][j];
            if (i == j) {
                firsts[i][j] = 1;
            }
        }
    }

    printf("\n\nFIRST STAR MATRIX:\n");
    display(firsts);

    // Compute LAST matrix
    k = 0;
    while (k < tot) {
        for (i = 0; i < cnt; i++) {
            for (j = 0; j < cnt; j++) {
                if (p[k].lhs[0] == sym[i] && p[k].rhs[strlen(p[k].rhs) - 1] == sym[j]) {
                    last[i][j] = 1;
                    k++;
                }
            }
        }
    }

    printf("\n\nLAST MATRIX:\n");
    display(last);

    // Copy LAST to LASTP
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            lastp[i][j] = last[i][j];
        }
    }

    // Compute LAST PLUS matrix
    for (i = 1; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            if (lastp[j][i] == 1) {
                for (k = 0; k < cnt; k++) {
                    lastp[j][k] |= lastp[i][k];
                }
            }
        }
    }

    printf("\n\nLAST PLUS MATRIX:\n");
    display(lastp);

    // Compute LAST STAR matrix
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            lasts[i][j] = lastp[i][j];
            if (i == j) {
                lasts[i][j] = 1;
            }
        }
    }

    printf("\n\nLAST STAR MATRIX:\n");
    display(lasts);

    // Compute EQUALS matrix
    for (cnt = 0; cnt < tot; cnt++) {
        k = 0;
        if (strlen(p[cnt].rhs) > 1) {
            for (i = 0; i < cnt; i++) {
                for (j = 0; j < cnt; j++) {
                    if (p[cnt].rhs[k] == sym[i] && p[cnt].rhs[k + 1] == sym[j]) {
                        equals[i][j] = 1;
                        k++;
                    }
                }
            }
        }
    }

    printf("\n\nEQUALS MATRIX:\n");
    display(equals);

    // Compute LESS THAN matrix
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            sum = 0;
            for (k = 0; k < cnt; k++) {
                sum += equals[i][k] * firstp[k][j];
            }
            lt[i][j] = sum;
        }
    }

    printf("\n\nLESS THAN MATRIX:\n");
    display(lt);

    // Compute GREATER THAN matrix
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            sum = 0;
            for (k = 0; k < cnt; k++) {
                sum += lastp[k][i] * equals[k][j];
            }
            temp[i][j] = sum;
        }
    }

    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            sum = 0;
            for (k = 0; k < cnt; k++) {
                sum += temp[i][k] * firsts[k][j];
            }
            gt[i][j] = sum;
        }
    }

    printf("\n\nGREATER THAN MATRIX:\n");
    display(gt);

    // Build SPM matrix
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            if (lt[i][j] == 1) spm[i][j] = '<';
            else if (gt[i][j] == 1) spm[i][j] = '>';
            else if (equals[i][j] == 1) spm[i][j] = '=';
            else spm[i][j] = '0'; // No relation
        }
    }

    printf("\n\nSPM MATRIX:\n");
    for (i = 0; i < cnt; i++) {
        for (j = 0; j < cnt; j++) {
            printf("%c ", spm[i][j]);
        }
        printf("\n");
    }

    return 0;
}
