#include <stdio.h>

int main(){
	int x ;
	scanf("%d",&x);
	
	int isPrime = 1;
	int i;
	for(i =2 ;i<x;i++){
		if(x%i ==0){
			isPrime = 0;
			break; 
		}
	}
	if(isPrime == 1){
		printf("%d������",x);
	}else{
		printf("%d��������",x);
	}
	return 0;
}
