//Lisa Rehm, Name Decorator C
#include <stdio.h>
#include <string.h>

char name[20];
char decor_one[] = ">(^";
char decor_two[] = "^)<";

int main(void){
    printf("What is your first name?\n");
    scanf("%s", &name);
    strcat(name, decor_two);
    strcat(decor_one, name);
    printf("Your name is %s\n", decor_one);
    return 0;
}
