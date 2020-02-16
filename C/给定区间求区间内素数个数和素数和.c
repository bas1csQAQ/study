#include <stdio.h>
/*
	给定一个区间 求这个区间中的 素数个数和素数和 
*/
int main(){
	int m,n;
	scanf("%d %d",&m,&n);
	
	int i = m,j;
	int isPrime = 0;// 是否为素数 
	int count = 0;// 素数数量 
	int sum = 0;// 素数和 
	while(i<n){
		printf("i = %d",i);
//		判断当前循环体是否为素数 
		for(j=2;j<i;j++){
			if(i%j == 0){
				isPrime = 1;
				break;
			}
		}
//		若 isPrime == 1 则 此时的i 是素数 将数量+1 并将此时的i进行累加操作 放到sum中 
		if(isPrime){
			count ++;
			sum += i;
		}
//		在下次循环开始前 进行数据重新初始化 
		isPrime = 0;
		i++;
	}
	printf("在 %d - %d 范围内素数有 %d个 总和为%d",m,n,count,sum);
	return 0;
}
