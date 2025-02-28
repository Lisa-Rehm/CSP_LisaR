//Lisa Rehm, Old Enough C
#include <stdio.h>

int age;

int main(void){
    printf("How old are you? (Please give me a number).\n");
    scanf("%d", &age);
    if(age >= 18){
        printf("You are old enough to vote!\n");
    }else if(age >= 16){
        printf("You are old enough to drive!\n");
    }else if (age >= 15){
        printf("You are old enough to get a learners permit!\n");
    }else if(age >= 5){
        printf("You are old enough to go to school!\n");
    }else{
        printf("You are not old enough to do anything, sorry.\n");
    }
    return 0;
    }
