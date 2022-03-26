#include<stdio.h>

int main(void){
    int a,b;
    scanf("%d %d",&a,&b);
    int h;
    h = (a + b) % 24;
    printf("%d\n",h);
    return 0;
}
