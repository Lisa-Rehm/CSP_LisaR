//Lisa Rehm, Old Enough C
#include <stdio.h>

int age;

int main(void){
    printf("How old are you? (Please give me a number).\n");
    scanf("%d", &age);
    if(age >= 18){
        printf("You are old enough to vote!");
    }else{
        if(age >= 16){
            printf("You are old enough to drive!");
        }else{
            if(age >= 15){
                printf("You are old enough to get a learners permit!");
            }else{
                if(age >= 5){
                    printf("You are old enough to go to school!");
                }else{
                    printf("You are not old enough to do anything, sorry.");
                }
            }
        }
    }
    return 0;
}
