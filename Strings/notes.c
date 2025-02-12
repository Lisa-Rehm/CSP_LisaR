//Lisa Rehm, Strings Notes C
#include <stdio.h>
#include <string.h>

char name[20]; //have a number if you are not introducing the value rn

int main(void){
    //printf("Please tell me your full name.\n");
    //scanf("%s", name); 
    //scanf will only take input up to the first space, then it stops
    //fgets(name, 20, stdin); //fgets is also an input but gets everything, you need to tell it 3 things: variable, char # and stdin
    //printf("Hello %sWelcome to my program!", name);
    //char sentence[] = "The quick brown fox jumps over the lazy dog";
    //printf("%s\n", sentence);
    //printf("%lu\n", sizeof(sentence)); //index number (starting at 0)
    //printf("%lu\n", strlen(sentence)); //number of actual characters
    char one[] = "Hello ";
    char two[] = "World!";
    char three[] = "This is my program. ";
    //two[5] = '?';
    printf("%s\n", one);
    strcat(one, two);
    printf("%s\n", one);
    //strcat(three, one); //when cat, make sure to not run out of characters on the variable
    //printf("%s", three);
    strcat(one, three);
    printf("%s", one);
    return 0;
}
