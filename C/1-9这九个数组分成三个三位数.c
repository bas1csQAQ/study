#include <stdio.h>
#include <string.h>
// 编写程序要让1-9这九个数组分成三个三位数 
// 要求第二个三位数是第一个的两倍 第三个三位数是第一个的三倍 

int a[9];
int OK(int t, int *s){
	int *p, *q;
	for(p = s; p < s + 3; p ++){
		// 将传递进来的三位数进行拆分 放到数组a中 
		*p = t%10;
		t=t/10;
		// 把每次执行函数放进来的数字和数组a中所有的数字进行逐一判断  
		// 不满足题目条件的就返回0 就会导致main函数中的if条件不满足 就不会继续执行
		// 条件： 不能是0 而且每次传递进来的值不能和数组中已经有的值重复 
		for(q=a; q < p; q++){
			if(*q == 0 || *q == *p){
				return (0);
			}
		}
	}
} 
int main() {
	int m, count = 0;
	// 将条件设定为 333 是因为 333 的三倍已经是三位数中最大的范畴了 
	for(m = 123; m <= 333; m++)
		if(OK(m, a) && OK(m * 2, a+3) && OK(m * 3, a+6))
			printf("第%d组数字：%d,%d,%d\n",++count,m,m * 2, m * 3);
	
	return 0;

	return 0; 
	
}
