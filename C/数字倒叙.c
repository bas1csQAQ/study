#include <stdio.h>

int main(){
	int x ;
//	scanf("%d",&x);
	x=100;
	int digit;
	int ret = 0;
//	����һ��ԭ�ȵ� x ������������ 
	int t = x;
////	100 => 1
//	while(x>0){
//		digit = x%10;
////		��ÿ�εõ���β��+���ص���*10  ������Ҫ���ص��� 
//		ret = ret*10+digit;
//		printf("x=%d,digit = %d,ret=%d\n",x,digit,ret);
//		x /=10;
//	}
//	printf("ԭ���������� %d ��������֮�� Ϊ%d",t,ret); 
//
//	
//	100 => 001
	while(x>0){
		digit = x%10;
		printf("%d",digit);
//		��ÿ�εõ���β��+���ص���*10  ������Ҫ���ص��� 
		ret = ret*10+digit;
//		printf("x=%d,digit = %d,ret=%d\n",x,digit,ret);
		x /=10;
	}
//	printf("ԭ���������� %d ��������֮�� Ϊ%d",t,ret); 
	
}
