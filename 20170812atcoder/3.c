#include <stdio.h>

int lcm(int, int);

int main (void){
    int n,i;
    scanf ("%d", &n);
    int t[n];

    for(i=0;i<n;i++){
        scanf("%d", &t[i]);
    }

    for(i=1;i<n;i++){
        t[i] = lcm(t[i-1],t[i]);
    }

    printf("%d\n",t[n-1]);
    return 0;

}

int lcm (int a, int b){

    int l = a*b;

    if(a<b){
        int tmp = a;
        a = b;
        b = tmp;
    }

    int r = a % b;
     while(r!=0){
       a = b;
       b = r;
       r = a % b;
     }


    return l/b;
}
