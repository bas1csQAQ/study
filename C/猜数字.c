#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(){
//	srand方法是 随机数发生器的初始化函数 配合 rand方法一起可以产生随机数数列 
	srand(time(0));
//	rand方法是C语言标准库中的方法  每次执行rand方法 都会产生一个随机数 
	const int a = rand() % 100 + 1 ;
	printf("%d\n",a);
	int num = 0;
	int count = 0;
	printf("请输入 您猜到的数字:\n");
	do{
		scanf("%d",&num);
		count++;
		if(a>num){
			printf("您猜的数小了,请重新猜一个数：\n");
		}else{
			printf("您猜的数大了,请重新猜一个数：\n");
		} 
	} while(num != a);
	printf("您猜对了 共用了 %d 次",count);
	return 0;
} 
