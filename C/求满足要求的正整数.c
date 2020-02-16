#include <stdio.h>
/*
	给定不超过6的正整数 考虑从a 开始的连续四个数字 并输出由这四个数字组成的无重复数字的三位数 
	要求每行六个数字 
*/
int main(){
	
	int a ;
	scanf("%d",&a);
	
	int i,j,k;
	int cnt; 
	
	for(i=a;i<=a+3;i++){
		for(j=a;j<=a+3;j++){
			for(k=a;k<=a+3;k++){
				if(i!=j && i!=k && j!=k){
					cnt++;
					printf("%d%d%d",i,j,k);
					if(cnt==6){
						printf("\n");
						cnt=0;
					}else{
						printf(" ");
					}
				}
			}
		}
	} 
	return 0;
}
