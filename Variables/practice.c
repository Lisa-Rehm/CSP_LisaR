//Lisa Rehm, Variables Practice C
#include <stdio.h>

char name[] = "Lisa";

float sml_num = 8.6;

int lrg_num = 941;

char breakfast[] = "nothing";

char fav_color[] = "red";

char school[] = "UCAS";

int year = 2025;

char eye_color[] = "blue";

int age = 15;

char fav_subject[] = "chemistry";

int main(void){
    printf("My name is %s\n", name);
    printf("A number between 1 and 10 is %f\n", sml_num);
    printf("A number between 100 and 1000 is %d\n", lrg_num);
    printf("For breakfast I had %s\n", breakfast);
    printf("My favorite color is %s\n", fav_color);
    printf("For school I go to %s\n", school);
    printf("It is currently %d\n", year);
    printf("My eyes are %s\n", eye_color);
    printf("I am %d years old\n", age);
    printf("My favorite subject is %s\n", fav_subject);
    return 0;
}
