//Lisa Rehm, Time of Day C
#include <stdio.h>
#include <time.h>


int main(void){
    time_t now = time(NULL);
    struct tm * tm_struct = localtime(&now);
    int hour = tm_struct->tm_hour;
    printf("%d\n", hour);

    if (hour <= 7){
        printf("Good morning! Tis the best time of day!.\n");
    }else if(hour <= 11){
        printf("Good near end of waking period, you should start preparing for sleep now.\n");
    }else if(hour == 12){
        printf("Good day! You should probably fall asleep now before the sun gets too bright.\n");
    }else if(hour <= 16){
        printf("Good afternoon! Enjoy your sleep!\n");
    }else if(hour <= 19){
        printf("Good evening! I hope you are well rested!\n");
    }else if(hour <= 23){
        printf("Good night, Enjoy your day!\n");
    }else{
        printf("Go back to the non-24-hour planet from which you came. Or stay. I don't care.\n");
    }
    return 0;
}
