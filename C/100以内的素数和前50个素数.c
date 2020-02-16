#include <stdio.h>

int main(){
	int i;
	int j;
//	100以内素数 
	for(i = 2;i<100;i++){
		int isPrime = 1; 
		for(j=2;j<i;j++){
			if(i%j == 0){
				isPrime = 0;
				break;
			}
		}
		if(isPrime == 1){
			printf("%d	",i);
		}
	}
	
	printf("\n\n");
//	前50素数 
	int cnt = 0;
	for(i = 2;cnt<50;i++){
		int isPrime = 1; 
		for(j=2;j<i;j++){
			if(i%j == 0){
				isPrime = 0;
				break;
			}
		}
		if(isPrime == 1){
			cnt++;
			printf("%d	",i);
			if(cnt %5==0){
				printf("\n");
			}
		}
	}
	
}
