//Lisa Rehm, Expressions Notes C
#include <stdio.h>
#include <math.h> //this allows us to use exponents
// Integers int when we set the variable and %d when we print
// Floats float when we set the variable and %f when we print
// Strings (words) char when we set the variable and %s when we print, %c gives us the first character
// We set expressions as variables
// have division as float because you can get a decimal
int mynum;
float percent;
int add = 4+6;
int mul = 4*6;
int sub = 4-6;
float div = 6/4; //division gives a whole number in c like '//' in python
int mod = 6%4;
int ex = pow(5, 2);

int main(void){
    //printf("Type a number: \n");
    //scanf("%d", &mynum);
    //printf("You inputed %d\n", mynum);
    //printf("Give me a percent as a decimal: \n");
    //scanf("%f", &percent);
    //printf("Your percent is %f\n", percent);
    mul = 7*4; // reset variable, if you want to make the change before it's printed put it before, it has to be in the main
    printf("%d\n", add);
    printf("%d\n", mul);
    printf("%d\n", sub);
    printf("%.2f\n", div); //put the number of decimal places you want shown between % and f
    printf("%d\n", mod);
    printf("%d\n", ex);
    return 0;
}

//give it the data type then where to send it, the place you are sending it has to be premade
