//Lisa Rehm, Family Loop C
#include <stdio.h>

int main(void){
    char chickens[][20] = {"Dragon", "Macadamia", "Pecan", "Parmesan", "Pistachio", "Harley", "Phoenix", "Sphinx", "Aussie"};
    int length = sizeof(chickens)/sizeof(chickens[0]);
    int x;
    for(x=0; x<length; x++){
        printf("Hello %s the chicken!\n", chickens[x]);
    }
    return 0;
}
