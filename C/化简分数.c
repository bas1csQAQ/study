#include <stdio.h>
/*
	给定一个分数 将其化简为最简分数 例如 输入 60/120  => 1/2 
*/
int main(){
	int fenzi,fenmu;
	scanf("%d/%d",&fenzi,&fenmu);
	
	int a = fenzi;
	int b = fenmu;
	int t;
//	若b = 0 则 a就是最大公约数  
//	若b不等于0  则让a对b取余  让a=b b=余数 
	while(b!=0){
		t=a%b;
		a=b;
		b=t;
	}
	printf("%d/%d化简后为:%d/%d",fenzi,fenmu,fenzi/a,fenmu/a);

	return 0;
}
