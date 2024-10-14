#include <stdio.h>
#include <ctype.h>
#include <string.h>
char sarr[50][50];  // Stack to hold operands
char arr[50];       // Input expression
char code[10][10];  // Three-address code
int top = 0;        // Stack pointer
void push(char a[10]) {
    strcpy(sarr[top], a);
    top++;
}
void pop(char b[10]) {
    top--;
    strcpy(b, sarr[top]);
}
int main() {
    int i, j = 0;
    char oprgt[20], oplft[20], exp[50], temp[10];
    printf("Saail Chavan KFPMSCCS016\n");
    printf("Enter The Postfix Expression: ");
    scanf("%s", arr);
    printf("\nThree Address Code For Given Expression:\n\n");

    for (i = 0; i < strlen(arr); i++) {
        if (isalpha(arr[i]) || isdigit(arr[i])) {
            temp[0] = arr[i];
            temp[1] = '\0';
            push(temp);
        } else {
            if (arr[i] == '+' || arr[i] == '-' || arr[i] == '*' || arr[i] == '/') {
                temp[0] = arr[i];
                temp[1] = '\0';
                pop(oprgt);      // Right operand
                pop(oplft);      // Left operand
                sprintf(exp, "%s %s %s", oplft, temp, oprgt); // Create expression
                sprintf(code[j], "T%d", j + 1);  // Generate temporary variable name
                printf("%s = %s\n", code[j], exp); // Output the three-address code
                push(code[j]);   // Push the result back to the stack
                j++;
            }
        }
    }
    return 0;
}
