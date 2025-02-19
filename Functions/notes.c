//Lisa Rehm, Functions notes
#include <stdio.h>

int add(void){ //we use {} in C, everything in the function must exist between the {}
    printf("%d", 6+8);
    return 6+8;
}

int main(void){
    printf("Hello World");
    add();
    return 0;
}
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



//Madness: don't return strings in C :)
//void add(int numOne,int numTwo){
//    printf("%d\n", numOne+numTwo);
//}

//const char* word(char type[10], int length){
//    char answer[10];
//    printf("Please give me a %s:\n", type);
//    getStr(answer, sizeof(answer)-1);
//    return answer;
//}

//int main(void){
//    word("name");
//    word("verb");
//    word("place");
//    printf("%s was %s until they somehow reached %s", word("name", 50), word("verb", 50), word("place", 50));
//    return 0;
//}
