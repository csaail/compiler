#include <stdio.h>
#include <string.h>

struct prod {
    char lhs[50];
    char rhs[50];
} p[30];
int first[20][20], firstp[20][20], firsts[20][20], last[20][20], lastp[20][20], lasts[20][20], equals[20][20], lt[20][20], gt[20][20];
char opm[20][20];
int tot, i, j, k, cnt = 0, flag = 0, sum = 0;
char sym[30], ans = 'y', ch = '\0';

void display(int mat[20][20]) {
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
        printf("\n\n Enter production (LHS RHS) : ");
        scanf("%s %s", p[tot].lhs, p[tot].rhs);
        tot++;
        printf("\n continue? (y/n) : ");
        ans = getchar();
        // Clear the buffer
        while (getchar() != '\n');
    }

    printf("\n\n Productions are : ");
    for (i = 0; i < tot; i++)
        printf("\n\n %s -> %s", p[i].lhs, p[i].rhs);

    cnt = 0;
    sym[cnt++] = p[0].lhs[0];

    for (i = 0; i < tot; i++) {
        flag = 0;
        for (j = 0; j < strlen(sym); j++) {
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
            for (j = 0; j < strlen(sym); j++) {
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
    printf("\n\n sym final : \n");
    for (i = 0; i < strlen(sym); i++) {
        printf("\t%c", sym[i]);
    }
    // Initialize matrices
    for (i = 0; i < 20; i++) {
        for (j = 0; j < 20; j++) {
            first[i][j] = firstp[i][j] = firsts[i][j] = last[i][j] = lastp[i][j] = lasts[i][j] = equals[i][j] = lt[i][j] = gt[i][j] = 0;
            opm[i][j] = '0';  // Initialize operator matrix
        }
    }
    return 0;
}
