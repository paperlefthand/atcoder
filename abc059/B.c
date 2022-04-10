#include<stdio.h>
#include<string.h>

char a[101],b[101];

int len(char*);

int main(void){
    scanf("%s%s", a, b);
    if(a[0]=='0' || b[0]=='0'){
        printf("Error\n");
        return 0;
    }

    if(len(a)>len(b)){
        printf("GREATER\n");
    }else if(len(a)<len(b)){
        printf("LESS\n");
    }else{
        int i=0;
        while(a[i]!='\0'){
           if((int)a[i]>(int)b[i]){
               printf("GREATER\n");
               return 0;
           }else if((int)a[i]<(int)b[i]){
               printf("LESS\n");
               return 0;
           }else{
               i++;
           }
       }
       printf("EQUAL\n");
    }
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
