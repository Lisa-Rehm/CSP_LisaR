//Lisa Rehm, Expressions Notes C
#include <stdio.h>
// Integers int when we set the variable and %d when we print
// Floats float when we set the variable and %f when we print
// Strings (words) char when we set the variable and %s when we print, %c gives us the first character
int mynum;

int main(void){
    printf("Type a number: \n");
    scanf("%d", &mynum);
    printf("You inputed %d", mynum);
    return 0;
}
