#include <stdio.h>
/*
	水仙花数 
*/
int main(){
	 int n;
	 scanf("%d",&n);
	 int i;
	 int first = 1;
	 i =1;
//	 确定是输出几位数
	 while(i<n){
	 	first *= 10;
	 	i++;
	 }
	 i=first;
//	 输出对应几位数的水仙花数 
	 while(i<first*10){
	 	int t = i;
		 int sum = 0; 
	 	do{
//	 		将满足条件的数 进行分割 
	 		int d = t%10;
	 		t/=10;
	 		// 求分解数字之后每一位的n次方 
	 		int p = d;
//	 		定义循环次数  次方数 
	 		int j = 1;
	 		while(j<n){
	 			p*=d;
	 			j++;
			}
			sum+=p;
//	 		printf("%d\n",d);
		}while(t>0);
		
		if(i==sum){
			printf("%d\n",i);
		}
		i++;
	 } 
//	 printf("first = %d",first);
	return 0;
}
