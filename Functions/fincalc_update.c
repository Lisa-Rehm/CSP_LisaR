//Lisa Rehm, Financial Calculator Update in C
#include <stdio.h>

float ask(char* category){
    float input;
    printf("How much do you spend on %s each month?\n", category);
    scanf("%f", &input);
    return input;
}

void tell_calc(float income, float amount, char* type){
    float pertype = (amount/income)*100;
    printf("You spend $%.2f on %s every month, which is %.2f%% of your income.\n", amount, type, pertype);
}

int main(void){
    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;
    float savings;
    float spending;
    float per_spending;
    printf("Welcome! This is a budget calculator!\n");
    printf("What is your monthly income?\n");
    scanf("%f", &income);
    rent = ask("rent or mortgage");
    utilities = ask("utilities");
    groceries = ask("groceries");
    transportation = ask("transportation");
    tell_calc(income, rent, "rent or mortgage");
    tell_calc(income, utilities, "utilities");
    tell_calc(income, groceries, "groceries");
    tell_calc(income, transportation, "transportation");
    savings = income * 0.1;
    spending = income - (rent + utilities + groceries + transportation + savings);
    per_spending = (spending/income)*100;
    printf("You have $%.2f dollars left to spend, which is %.2f%% of your income.\n", spending,per_spending);
    printf("We are going to put $%.2f in your savings.\n", savings);
    return 0;
}

