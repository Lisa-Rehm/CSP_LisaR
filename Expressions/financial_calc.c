//Lisa Rehm, Fincancial Calculator C
#include <stdio.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;


int main(void){
    printf("Welcome! This is a budget calculator.\n");
    printf("What is your monthly income?\n");
    scanf("%f", &income);
    printf("How much do you spend on rent or a mortgage each month?\n");
    scanf("%f", &rent);
    printf("How much do you spend on utilities each month?\n");
    scanf("%f", &utilities);
    printf("How much do you spend on groceries each month??\n");
    scanf("%f", &groceries);
    printf("How much do you spend on transportation each month?\n");
    scanf("%f", &transportation);
    savings = income * 0.1;
    printf("%f\n", savings);
    return 0;
}






// Calculate savings as 10% of income (variable) (tell user it is 10%)


// Calculate spending money income - (rent+utilities+groceries+transportation+savings) (variable)


// Calculate percent of rent (rent/income) (variabe)


// Calculate percent of utilities (utilities/income) (variabe)


// Calculate percent of groceries (groceries/income) (variabe)


// Calculate percent of transportation (transportation/income) (variabe)


// Calculate percent of spending money (spending/total) (variable)


// tell user rent spending amount and percent ("You spend $xx.xx on rent and that is xx% of your income")


// tell user utilities spending amount and percent ("You spend $xx.xx on utilities and that is xx% of your income")


// tell user groceries spending amount and percent ("You spend $xx.xx on groceries and that is xx% of your income")


// tell user transportation spending amount and percent ("You spend $xx.xx on transportation and that is xx% of your income")


// tell user spending amount and percent ("You spend $xx.xx on spending and that is xx% of your income")


// tell user savings spending amount and percent ("You spend $xx.xx on savings and that is 10% of your income")
