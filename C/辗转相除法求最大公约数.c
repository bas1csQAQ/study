/*
	շת����������Լ����
	1.��b=0 ��ôa�����������������Լ��
	2.�� a%b Ȼ����a=b b=����	Ȼ��ص���һ�� �����ж�
	
	a	b	t
	12	18	12
	18	12	6
	12	6	0
	6	0
	
	=>6 
*/

#include <stdio.h>

int main(){
	int a,b,t ;
	scanf("%d %d",&a,&b);
	
	while( b!=0 ){
		t = a%b;
		a = b;
		b = t;
		printf("a=%d,b=%d,t=%d\n",a,b,t);
	}
	printf("���Լ��Ϊ%d",a);
	
	
	
	return 0;
}
