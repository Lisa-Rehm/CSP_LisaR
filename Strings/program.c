//Lisa Rehm, Silly Sentences C
#include <stdio.h>

char adj[20];
char gerund[20];
char noun[20];
char emotion[20];
char verb[20];

int main(void){
    printf("Welcome to my program! This is a MadLib! Please give me an adjective (one word please).\n");
    scanf("%s", adj);
    printf("Please give me a verb that ends in -ing (one word please).\n");
    scanf("%s", gerund);
    printf("Please give me an animal (one word please).\n");
    scanf("%s", noun);
    printf("Please give me an emotion (one word please).\n");
    scanf("%s", emotion);
    printf("Please give me a verb in past tense (one word please).\n");
    scanf("%s", verb);
    printf("Once there was a %s cow who was %s when he met a %s.\nThe cow was very %s and %s away, never to be seen again.\n", adj, gerund, noun, emotion, verb);
    return 0;
}
