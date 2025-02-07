//Lisa Rehm, Fincancial Calculator C
#include <stdio.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;
float spending;
float per_rent;
float per_utilities;
float per_groceries;
float per_transportation;
float per_spending;


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
    spending = income - (rent + utilities + groceries + transportation + savings);
    per_rent = (rent / income) * 100;
    per_utilities = (utilities / income) * 100;
    per_groceries = (groceries / income) * 100;
    per_transportation = (transportation / income) * 100;
    per_spending = (spending / income) * 100;
    printf("You spend %f percent on rent.\n", per_rent);
    printf("You spend %f percent on utilities.\n", per_utilities);
    printf("You spend %f percent on groceries.\n", per_groceries);
    printf("You spend %f percent on transportation.\n", per_transportation);
    printf("You have $%f dollars left to spend.\n", per_spending);
    printf("%f\n", savings);
    return 0;
}

// run and see if there is a way to have % in final print statements
