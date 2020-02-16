#include <stdio.h>
/*
	构建素数表 
*/
int main(void){
	const int MAXNUMBER = 100;
	int isPrime[MAXNUMBER];
	int i ,j;
	for(i=0;i<MAXNUMBER;i++){
		isPrime[i]=1;
//		printf("isPrime[i]=%d",isPrime[i]);
	}
	for(i = 2;i<MAXNUMBER;i++){
		if(isPrime[i]){
			for(j=2;i*j<MAXNUMBER;j++){
				isPrime[j*i]=0;
			}
		}
	}
	int count = 0;
	for(i=2;i<MAXNUMBER;i++){
		if(isPrime[i]){
			printf("%d\t",i);
			count++;
		}
		if(count%5==0){
			printf("\n");
		}
	}
	
	
	return 0;
}
