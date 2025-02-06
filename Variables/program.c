// Lisa Rehm, Variables program C
#include <stdio.h>

char user_name[10];

int main(void){
    printf("What is your name? \n");
    scanf("%s", &user_name);
    printf("Nice to meet you %s", user_name);
}
