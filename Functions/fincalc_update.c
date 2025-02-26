//Lisa Rehm, Financial Calculator Update in C
#include <stdio.h>

float ask(char* category){
    float input;
    printf("How much do you spend on %s each month?\n", category);
    scanf("%f", &input);
}

void tell_calc(float income, float amount, char* type){
    float pertype = (amount/income)*100;
    printf("You spend %f on %s every month, which is %f of your income.\n", amount, type, pertype);
}

int main(void){
    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;
    printf("Welcome! This is a budget calculator!\n");
    printf("What is your monthly income?\n");
    scanf("%f", &income);
    ask("rent or mortgage");
    ask("utilities");
    ask("groceries");
    ask("transportation");

    tell_calc(income, rent, "rent or mortgage");
    return 0;
}

//float rent;
//float utilities;
//float groceries;
//float transportation;

// float savings;
// float spending;
// float per_rent;
// float per_utilities;
// float per_groceries;
// float per_transportation;
// float per_spending;

//calculation function + this is how much you spend

// calculate spending and savings in or out of the main?

 //etc.
    // call function for after calculations
    // spending amount
    // savings


//Lisa Rehm, Fincancial Calculator C
//#include <stdio.h>



//int main(void){
//    printf("Welcome! This is a budget calculator.\n");
//    printf("What is your monthly income?\n");
//    scanf("%f", &income);
//    printf("How much do you spend on rent or a mortgage each month?\n");
//    scanf("%f", &rent);
//    printf("How much do you spend on utilities each month?\n");
//    scanf("%f", &utilities);
//    printf("How much do you spend on groceries each month??\n");
//    scanf("%f", &groceries);
//    printf("How much do you spend on transportation each month?\n");
//    scanf("%f", &transportation);
//    savings = income * 0.1;
//    spending = income - (rent + utilities + groceries + transportation + savings);
//    per_rent = (rent / income) * 100;
//    per_utilities = (utilities / income) * 100;
//    per_groceries = (groceries / income) * 100;
//    per_transportation = (transportation / income) * 100;
//    per_spending = (spending / income) * 100;
//    printf("You spend $%.2f on rent which is %.2f%% of your income.\n", rent, per_rent);
//    printf("You spend $%.2f on utilities which is %.2f%% of your income.\n", utilities, per_utilities);
//    printf("You spend $%.2f on groceries which is %.2f%% of your income.\n", groceries, per_groceries);
//    printf("You spend $%.2f on transportation which is %.2f%% of your inome.\n", transportation, per_transportation);
//    printf("You have $%.2f dollars left to spend, which is %.2f%% of your income.\n", spending, per_spending);
//    printf("We are going to put $%.2f in your savings.\n", savings);
//    return 0;
//}

