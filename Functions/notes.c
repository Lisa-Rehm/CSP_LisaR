//Lisa Rehm, Functions notes
#include <stdio.h>

//int add(void){ //we use {} in C, everything in the function must exist between the {}
//    printf("%d", 6+8)
//    return 6+8;
//}

//int main(void){
//    printf("Hello World");
//    add();
//    return 0;
//}
// whatever data type set at beginning (int) has to match the data type in the return (0)
// we have to define things above the main function


// C requires a function in order to run
//int main(void){
//    printf("Hello World");
//    return 0;
//}

//void add(){ this is for no return
//    etc
//}

//void add(int, numOne,int numTwo){
//    printf("%d\n", numOne + numTwo)
//}

//int main (void)
//    printf("Hello World\n");
//    add();
//    return 0;
//}


char input(char type[20]){
    char answer[50];
    printf("Please give me a %s:\n", 
    type);
    scanf("%s", answer);
    return answer;
}

int main(void){
    input("name");
    input("verb");
    input("verb");
    printf("%s was %s until they somehow reached %s", input("name"), input("verb"), input("verb"));
}
