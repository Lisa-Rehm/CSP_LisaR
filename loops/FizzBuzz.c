//Lisa Rehm, FizzBuzz C
#include <stdio.h>

int num = 1;

int main(void){
    while(num <= 50){
        if (num%3 == 0 && num%5 == 0){
            printf("fizzbuzz\n");
        }else if (num %3 == 0){
            printf("fizz\n");
        }else if (num%5 == 0){
            printf("buzz\n");
        }else{
            printf("%d\n", num);
        }
        num+=1;
    }
    return 0;
}
