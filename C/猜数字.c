#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
//	srand������ ������������ĳ�ʼ������ ��� rand����һ����Բ������������ 
	srand(time(0));
//	rand������C���Ա�׼���еķ���  ÿ��ִ��rand���� �������һ������� 
	const int a = rand() % 100 + 1 ;
	printf("%d\n",a);
	int num = 0;
	int count = 0;
	printf("������ ���µ�������:\n");
	do{
		scanf("%d",&num);
		count++;
		if(a>num){
			printf("���µ���С��,�����²�һ������\n");
		}else{
			printf("���µ�������,�����²�һ������\n");
		} 
	} while(num != a);
	printf("���¶��� ������ %d ��",count);
	return 0;
} 
