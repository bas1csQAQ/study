#include <stdio.h>
/*
	输入一个数 输出打印1*1到n*n的乘法表 
*/
int main(){
	int n;
	scanf("%d",&n);
	int i,j;
	for(i=1;i<=n;i++){
		for(j=1;j<=i;j++){
			printf("%d * %d = %d",j,i,i*j);
			if(j!=i){
				printf("\t");
			}
		}
		printf("\n");
	}
	return 0;
}
