#include <stdio.h>

int main(){
	int n;
	scanf("%d",&n);
	
	int fact = 1;
	
	
//	ע�� ��forѭ��С������ д�����ĳ�ʼ�� ֻ��c99֧�� �������� ��Ҫ���༭���������� 
//	for( int i = n;i>1;i--){
//		fact *= i;
//	}
//	printf("%d! = %d",n,fact);
//

//	���� ����ֱ��ʹ�� n ������ ѭ����׳� �����ٶ������	
	int t = n;
	for(;n>1;n--){
		fact *= n;
	} 
	printf("%d! = %d",t,fact);
	
	return 0;
}
