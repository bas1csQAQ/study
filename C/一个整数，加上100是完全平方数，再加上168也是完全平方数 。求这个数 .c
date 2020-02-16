#include "stdio.h"
#include "string.h"
#include "math.h"

// 一个整数，加上100是完全平方数，再加上168也是完全平方数 。求这个数 
int main()
{ 
	int i = 1;
	double a,b;
	while(1){
		a = sqrt(i+100);
		b = sqrt(i+100+168);
		if(a == (int)a && b == (int)b){
			printf("%d\n",i);
		}
		
		if(i>10000) break;
		i++;
	}
	
return 0;

}


