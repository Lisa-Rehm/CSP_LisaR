//Lisa Rehm, Expressions practice C
#include <stdio.h>
#include <math.h>

float eqn1 = 7-24/8*4+6;
float eqn2 = 18/3-7+2*5;
float eqn3= 6*4/12+72/8-9;
float eqn4 = (17-6/2)+4*3;
float eqn5 = (-2*(1*4-2/2))+(6+2-3);
float eqn6 = (-1*((3-4*7)/5)-2*24/6);
float eqn7 = (3*pow(5, 2)/15)-(5-pow(2, 2));
float eqn8 = (pow(1, 4)*pow(2, 2)+pow(3, 3))-pow(2, 5)/4;
float eqn9 = pow((22/2-2*5), 2)+pow((4-6/6), 2);

int main(void){
    printf(("%.1f\n"), eqn1);
    printf(("%.1f\n"), eqn2);
    printf(("%.1f\n"), eqn3);
    printf(("%.1f\n"), eqn4);
    printf(("%.1f\n"), eqn5);
    printf(("%.1f\n"), eqn6);
    printf(("%.1f\n"), eqn7);
    printf(("%.1f\n"), eqn8);
    printf(("%.1f\n"), eqn9);
    return 0;
}

