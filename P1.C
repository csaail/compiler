#include <stdio.h>
#include <string.h>
char Nt[10];
char ts[10];
char prod[50][10];
int n;
void print() {
    printf("Saail Chavan KFPMSCCS016\n");
    printf("\nEnter the number of productions you want to convert: ");
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("\nEnter production number %d in the form of (X = bY): ", i + 1);
        scanf("%s", prod[i]);  // Example: A=cB, S=eF
    }
    printf("\n\nThe number of productions are as below:\n");
    for (int i = 0; i < n; i++) {
        printf("%d) %s\n", i + 1, prod[i]);
    }
    printf("\n\nLeft linear grammar is -->\n");
    for (int i = 0; i < n; i++) {
        char *p = strtok(prod[i], "=");
        if (p != NULL) {
            char left = *p;  // First character (Non-terminal)
            p = strtok(NULL, "=");
            if (p != NULL) {
                printf("%c --> %s\n", left, p);  // Output production
            }
        }
    }
}
int main() {
    print();
    return 0;
}