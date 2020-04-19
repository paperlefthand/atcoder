#include<stdio.h>
#include<math.h>

unsigned long int n;


signed long long int sum(signed long int*, unsigned long int);
_Bool prop0(signed long int arr[], unsigned long int i);
_Bool prop1(signed long int arr[], unsigned long int i);

int main(void){
    scanf("%ld", &n);
    if(n<2||n>pow(10,5)){printf("Error\n");return 0;}

    signed long int arr[n];
    for(int i=0;i<n;i++){
        scanf("%ld", &arr[i]);
        if(arr[i]<-pow(10,9)||arr[i]>pow(10,9)){printf("Error\n");return 0;}
    }

    unsigned long int i=0;

    // while(!prop0(arr,i)||!prop1(arr,i)){
    printf("%d\n", prop0(arr,n));
    return 0;
    }







signed long long int sum(signed long int arr[], unsigned long int i){
    signed long long int sum = 0;
    for(unsigned long int j=0;j<i;j++){
        sum += arr[j];
    }
    return sum;
}

_Bool prop0(signed long int arr[], unsigned long int i){
    for(unsigned long int j=0;j<i;j++){
        if(sum(arr, j)==0){return 0;}
    }
    return 1;
}

_Bool prop1(signed long int arr[], unsigned long int i){
    if(!prop0(arr,i)){return 0;}
    for(unsigned long int j=0;j<(i-1);j++){
        if(sum(arr, j)*sum(arr, j+1)>=0){return 0;}
    }
    return 1;
}
