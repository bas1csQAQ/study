#include <stdio.h>
/*
	����һ���� �����ӡ1*1��n*n�ĳ˷��� 
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
