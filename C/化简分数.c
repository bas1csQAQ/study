#include <stdio.h>
/*
	����һ������ ���仯��Ϊ������ ���� ���� 60/120  => 1/2 
*/
int main(){
	int fenzi,fenmu;
	scanf("%d/%d",&fenzi,&fenmu);
	
	int a = fenzi;
	int b = fenmu;
	int t;
//	��b = 0 �� a�������Լ��  
//	��b������0  ����a��bȡ��  ��a=b b=���� 
	while(b!=0){
		t=a%b;
		a=b;
		b=t;
	}
	printf("%d/%d�����Ϊ:%d/%d",fenzi,fenmu,fenzi/a,fenmu/a);

	return 0;
}
