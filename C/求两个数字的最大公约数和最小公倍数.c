#include <stdio.h>
#include <string.h>
// 编写程序 求两个数字的最大公约数和最小公倍数 

int maxGongyueshu(int a, int b) {
	int num1 = a>b?b:a; // 把两个数中小的那个拿出来 
	int num2 = a+b-num1; // 那么这个就是较大的那个 
	int i;
	if(num2%num1==0) // 如果大的能把小的整除 那么这个小的就是最大公约数 
		return num1;
	for(i = num1-1;i>0;i--){
		if(num2%i == 0 && num1%i==0)
			return i;
	}
} 

int minGongbeishu(int a, int b) {
	int num1 = a>b?a:b; // 把两个数中大的拿出来 
	int num2 = a+b-num1; // 那么这个就是小的那个
	int i;
	if(num1%num2 == 0) // 如果大的数可以将小的整除 那么这个大的就是最小公倍数 
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

