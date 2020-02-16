#include <stdio.h>
/*
	给定一个数字 输出打印数字的拼音 例如 输入 123 => yi er san  // -123 => fu yi er san 
*/
int main(){
	int n ;
	scanf("%d",&n);
	
//	判断是否是负数 
	if(n<0){
		printf("fu ");
		n=-n;
	}
	
//	判断位数 
	int mask = 1;
	int t = n;
	while(t>9){
		t /= 10;
		mask *= 10;
	}
//	正序分解数字 并根据数字输出对应拼音 
	do{
		int d = n/mask;
		switch(d){
			case 0:printf("ling");break;
			case 1:printf("yi");break;
			case 2:printf("er");break;
			case 3:printf("san");break;
			case 4:printf("si");break;
			case 5:printf("wu");break;
			case 6:printf("liu");break;
			case 7:printf("qi");break;
			case 8:printf("ba");break;
			case 9:printf("jiu");break;
		}
		if(mask>9){
			printf(" ");
		}
		n %= mask;
		mask/=10;
	}while(mask>0);
	printf("\n");
	return 0;
}
