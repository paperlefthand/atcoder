#include <stdio.h>
#include <math.h>

long int N;
long int i,j;
long int tmp;
long int sum=0;

int main(void){

    do{
    scanf("%ld", &N);
  }while(N > (long int)(pow(10,5))|| N < 1);

    long int total = (3*N+1);
    long int a[total];
    a[0] = 0;


    for(i=1;i<total;i++){
        do{
        scanf("%ld", &a[i]);
      }while(a[i]>(long int)(pow(10,9))|| a[i] < 1);
     }

    // sort
    for(i=1;i<total;i++){
      for(j=i+1;j<total;j++){
        if(a[j]>a[i]){
          tmp = a[j];
          a[j] = a[i];
          a[i] = tmp;
        }
      }
    }

    for(i=1;i<(N+1);i++){
      sum += a[2*i];
    }

    printf("%ld\n",sum);

    return(0);

}
