#include <stdio.h> 

int main(){
	int num ;
	int count = 0;
	int sum = 1;
	printf("请输入一些数字，最后输入 -1 视为结束");
	do{
	
	scanf("%d",&num);
		sum += num;
		count++;
	}while(num!=-1);
	printf("共有 %d 个数 这些数的平均数为 %f",count-1,1.0*sum/(count-1));
//	printf("%f",19/3.0); 3 5 11 -1 
	
	
	return 0; 
}
