#include <stdio.h>

int main(){
//	f(x)=1-1/2+1/3+...+1/n
	int n;
	scanf("%d",&n);
	int i ;
	double sum=0.0;
	double sign = 1;
	for(i=1;i<=n;i++){
			sum += sign/i;	
			sign = -sign;
	}
	printf("f(%d) = %f\n",n,sum);
	
	return 0;
}
