#include <stdio.h>
#include <string.h>
// ��д���� ���������ֵ����Լ������С������ 

int maxGongyueshu(int a, int b) {
	int num1 = a>b?b:a; // ����������С���Ǹ��ó��� 
	int num2 = a+b-num1; // ��ô������ǽϴ���Ǹ� 
	int i;
	if(num2%num1==0) // �������ܰ�С������ ��ô���С�ľ������Լ�� 
		return num1;
	for(i = num1-1;i>0;i--){
		if(num2%i == 0 && num1%i==0)
			return i;
	}
} 

int minGongbeishu(int a, int b) {
	int num1 = a>b?a:b; // ���������д���ó��� 
	int num2 = a+b-num1; // ��ô�������С���Ǹ�
	int i;
	if(num1%num2 == 0) // �����������Խ�С������ ��ô�����ľ�����С������ 
		return num1;
	for(i = num1+1; ;i++){
		if(i%num1==0 && i%num2==0) 
			return i;
	} 
}

int	main()
{
	int a,b;
	scanf("%d %d",&a,&b);
	int max = maxGongyueshu(a,b);
	int min = minGongbeishu(a,b);
	printf("max = %d,min = %d",max,min);
	return 0;
}

