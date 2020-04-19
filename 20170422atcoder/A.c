#include<stdio.h>
#include<string.h>
#include<ctype.h>

char str[3][10];

int len(char*);

int main(void){
    for(int i=0;i<3;i++){
        scanf("%s", str[i]);
        if(len(str[i])<1 || len(str[i])>10){
            printf("Error\n");
            return 0;
        }
        printf("%c", toupper(str[i][0]));

    }
    printf("\n");
    return 0;


}



int len(char arr[]){
    char* p = arr;
    int count=0;
    char end = '\0';
    while(strcmp(p,&end)){
        count++;
        p++;
    }
    return count;
}
