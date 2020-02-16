#include <stdio.h>
#include <string.h>
// 编写程序 随机输入两个整数请按从大到小顺序输出（请用两种不同的方法编程）。

void way1(int a, int b){
	if(a>b){
		printf("%-5d%-5d\n",a,b);
	}else{
		printf("%-5d%-5d\n",b,a);
	}
}
void way2(int a, int b){
	a>b?printf("%-5d%-5d\n",a,b):printf("%-5d%-5d\n",b,a);
}

int	main()
{
	int a, b;
	scanf("%d %d", &a, &b);
	way1(a, b);
	way2(a, b);

	
	return 0;
}

