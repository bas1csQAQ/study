#include <stdio.h>
/*
	输入数量不确定的0-9的整数  统计每个数字出现的次数 输入-1结束 
*/
int main(void){
	const int NUMBER = 10;
	int arr[NUMBER];
	int i ;
	for(i=0;i<NUMBER;i++){
		arr[i]=0;
	}
	int n ;
	scanf("%d",&n);
	while(n!=-1){
		if(n>=0 && n<=9){
			arr[n]++;
		}
		scanf("%d",&n);
	}
	for(i=0;i<NUMBER;i++){
		printf("%d出现了%d次",i,arr[i]);
	}
	
	return 0;
}
