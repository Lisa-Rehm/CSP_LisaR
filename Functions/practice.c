// Lisa Rehm, Updata Hello World C
#include <stdio.h>

char name[30];

void greet(char name[]){
    printf("Hello %s!\n", name);
}

int main(void){
    printf("Welcome to my program, please welcome these five individuals:\n");
    greet("Sally");
    greet("Meri");
    greet("Ruby");
    greet("Tina");
    greet("Teri");
    return 0;
}
