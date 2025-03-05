//Lisa Rehm, Loopd Notes C
#include <stdio.h>

int main(void){
    // 1. What is a loop? 
        // A section of code that repeats
    // 2. What are the two types of loops?
        // For and while loops
    // 3. What is iteration
        // The act of repeating, or a specific repition or time through the loop
    // 4. What are lists? 
        // A bunch of values in one variable
    // 8. How do you make lists in C? In C they are called arrays
    int grades[] = {97, 95, 100, 70, 94, 98, 64};
    // brackets wamts # of items in list, if we set the list up here we don't need a number in the brackets
    // data should be the same as what's in the list
    // all list items must be the same data type and surrounded by {} with commas in between
    printf("%d\n", grades[3]); // to print one item we give the index number in the brackets
    grades[2] = 73; // you have to update one at a time
    printf("%d\n", grades[2]);

    // how to get the size of the array(list)
    // This is the number of bytes that the list takes
    printf("%lu\n", sizeof(grades));
    // to find the length
    int length = sizeof(grades)/sizeof(grades[0]);
    printf("%d\n", length);

    // 9. How do you make for loops in C?
        int x;
        for(x=0; x<10; x++){ // starting point (0), ending point (<5), increase by two (+=2)
            printf("Hello\n");
            x++;
        }
        int t;
        for(t=0; t<5; t+=2){
            printf("%d\n", t);
        }

        int l;
        for(l=0; l<length; l++){
            printf("%d\n", grades[l]);
        }
    // 10. How do you make while loops in C? // it's best to use x and i for random practice
        int i = 1;
        while(i<10){
        printf("%d\n", i);
        i++;
        }

        int iterator = 0;
        // while line sets the stop point/ how long it gets
        while(iterator <= 100){
            printf("%d\n", iterator);
            iterator += 10;
        }

        int iteratorl = 100;
        while(iteratorl <= 0){
            printf("%d\n", iteratorl);
            iteratorl -= 10;
        }

        char movies[][20] = {"Cinderella", "The Smurf Movie", "Transformers", "Cars", "Up", "1984"};
        int mlength = sizeof(movies)/sizeof(movies[0]);
        int m = 0;
        while(m<mlength){
            printf("%s\n", movies[m]);
            m++;
        }
    return 0;
}
