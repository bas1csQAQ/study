#include <stdio.h>
/*
	求a的连续和  输入 2 3 => 输出 2+22+222 
*/
int main(){
	int a,n;
	scanf("%d %d",&a,&n);
	
	int  mask = 1;
	int sum =0;
	int t;
	int i ;
	for(i=0;i<n;i++){
		if(i==0){
			t=a;
		}else{
			t=a*mask+t;
		}
//		printf("%d\n",t);
		sum+=t;
		mask*=10;
	}
	printf("%d",sum);
	return 0;
}
