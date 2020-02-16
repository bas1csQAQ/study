/*
	辗转相除法求最大公约数：
	1.若b=0 那么a就是这两个数的最大公约数
	2.将 a%b 然后让a=b b=余数	然后回到第一步 进行判断
	
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
	printf("最大公约数为%d",a);
	
	
	
	return 0;
}
