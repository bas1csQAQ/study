#include <stdio.h>
#include <stdlib.h>
/*
	��̬�����ڴ� 
*/

void maxRAM();
int main(void){
	
	int number;
	int* a;
	int i;
	printf("������������"); 
	scanf("%d",&number);
	a=(int*)malloc(number*sizeof(int));
	
	for(i = 0;i<number;i++){ 
		scanf("%d",&a[i]);
	}
	for(i=number-1;i>=0;i--){
		printf("%d  ",a[i]);
	}
	free(a);
	maxRAM();
	
	return 0;
}

void maxRAM(){
	void *p;
	int cnt = 0;
	while((p=malloc(100*1024*1024))){
		cnt++;
	}
	printf("������%d00MB���ڴ�ռ�\n",cnt);
}

