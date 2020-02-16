#include <stdio.h>

int main(){
	int x ;
//	scanf("%d",&x);
	x=100;
	int digit;
	int ret = 0;
//	保存一份原先的 x 用以最后输出用 
	int t = x;
////	100 => 1
//	while(x>0){
//		digit = x%10;
////		让每次得到的尾数+返回的数*10  就是需要返回的数 
//		ret = ret*10+digit;
//		printf("x=%d,digit = %d,ret=%d\n",x,digit,ret);
//		x /=10;
//	}
//	printf("原来的数字是 %d 数字逆序之后 为%d",t,ret); 
//
//	
//	100 => 001
	while(x>0){
		digit = x%10;
		printf("%d",digit);
//		让每次得到的尾数+返回的数*10  就是需要返回的数 
		ret = ret*10+digit;
//		printf("x=%d,digit = %d,ret=%d\n",x,digit,ret);
		x /=10;
	}
//	printf("原来的数字是 %d 数字逆序之后 为%d",t,ret); 
	
}
