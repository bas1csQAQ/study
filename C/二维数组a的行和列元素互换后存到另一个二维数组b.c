#include <stdio.h>
#include <string.h>
// 编写程序 使用指针将输入的两个数按照从大到小输出 

int	main()
{
	int a,b,  *p1,*p2,*p ;
 	printf("input a,b:");
 	scanf("%d%d",&a,&b);
	p1=&a;
	p2=&b;
	if(a<b){
		p=p1;
		p1=p2; 
		p2=p;
	}
	printf("a=%d b=%d\n",a,b);
	printf("max=%d min=%d\n",  *p1,*p2);


	return 0;
}
