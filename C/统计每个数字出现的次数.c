#include <stdio.h>
/*
	����������ȷ����0-9������  ͳ��ÿ�����ֳ��ֵĴ��� ����-1���� 
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
		printf("%d������%d��",i,arr[i]);
	}
	
	return 0;
}
