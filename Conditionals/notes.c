//Lisa Rehm, Conditionals notes C
#include <stdio.h>
#include <string.h>

char name[] = "Vienna";
int num = 7;

int main(void){
    if(strcmp(name, "Vienna") == 0){
        printf("Hello, Ms. LaRose. Welcome to class.\n");
    }else{
        printf("Hello %s, welcome to class!\n", name);
    }

//&& = and, or = ||, not = !=
    if(num > 5 && num < 10){
        if(num == 7){
            printf("%d is an unlucky number.\n", num);
        }else{
        printf("%d is a large single digit number.\n", num);
        }
    }else if (num >= 10){
        printf("%d is not a single digit number.\n", num);
    }else{
        printf("%d is a small single digit number.\n", num);
    }

    return 0;
}


#include <time.h>

int main(void){
    // {time_t seconds;
    // seconds = time(NULL);
    // printf("Seconds since January 1, 1970 = %d\n", seconds);}


    time_t rawtime;
    struct tm * timeinfo;

    time(&rawtime);
    timeinfo = localtime(&rawtime);
    printf("Current time and date is %s\n", asctime(timeinfo));

    //current hour
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d\n", hour);
    return 0;
}
