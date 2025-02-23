// Lisa Rehm, Updata Hello World C
#include <stdio.h>


void greet(){
    char name[20];
    printf("What is your name?\n");
    scanf("%s", name);
    printf("Hello %s!\n", name);
}

int main(void){
    printf("Welcome to my program, please give me 5 names:\n");
    greet();
    greet();
    greet();
    greet();
    greet();
    return 0;
}
