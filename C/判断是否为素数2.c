#include <stdio.h>
#include <math.h>
int isPrime(int x);
// 一个合数必然能拆成一大一小因数的积，算到平方根相当于找那个小的因数
int main(void)
{
	
    int x;
	scanf("%d",&x); 
	if(isPrime(x))
	    printf("%d是素数。\n",x);
	else
	    printf("%d不是素数。\n",x);
	return 0;
}
int isPrime(int x){
	int ret = 1;
	int i;
	if(x==1 || (x%2 ==0 && x!=2))
		ret = 0;
	for(i=3;i<sqrt(x);i+=2){
		if(x%i==0){
			ret = 0;
			break;
		}
	}
	
	return ret;
}


