#include <stdio.h>

int main(){
	int n;
	scanf("%d",&n);
	
	int fact = 1;
	
	
//	注意 在for循环小括号中 写变量的初始化 只有c99支持 这样定义 需要给编辑器进行设置 
//	for( int i = n;i>1;i--){
//		fact *= i;
//	}
//	printf("%d! = %d",n,fact);
//

//	或者 可以直接使用 n 来进行 循环求阶乘 可以少定义变量	
	int t = n;
	for(;n>1;n--){
		fact *= n;
	} 
	printf("%d! = %d",t,fact);
	
	return 0;
}
