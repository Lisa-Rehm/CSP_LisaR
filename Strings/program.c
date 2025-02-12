//Lisa Rehm, Silly Sentences C
#include <stdio.h>

char noun[20];
char adj[20];
char adv[20];

int main(void){
    printf("Welcome to my program! Please give me a noun (one word please).\n");
    scanf("%s", noun);
    printf("Please give me an adjective (one word please).\n");
    scanf("%s", adj);
    printf("Please give me an adverb (one word please).\n");
    scanf("%s", adv);
    printf("%s and %s and %s.\n", noun, adj, adv);
    return 0;
}
