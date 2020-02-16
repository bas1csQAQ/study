#include <stdio.h>
#include <string.h>
#include <math.h> 
// 输入3×4数组，用指针方法实现将每行中的最小数与第0列元素对调。
int main(){
	
	int a[3][4],i,j,*p=a[0];
	for(i=0;i<3;i++)
	for(j=0;j<4;j++) scanf("%d",p++);
	
	for(p=&a[0][0];p<a[0]+12;p+=4) // 每次把每一行放进去进行排序
	swap(p);
	p=a[0]; // 让指针指向第一个元素 下面使用指针输出数组
	for(i=0;i<3;i++){ 
		for(j=0;j<4;j++) 
			printf("%3d",*p++);
		printf("\n");
	}
}
swap(int  *p1){
	int min,i,*p2=p1,*p3;
	p3 = p1 ;
	for(i=0;i<4;i++)
	{
		if(*p2<*p3) 
			p3=p2;
			p2++;
	}
	min=*p1;
	*p1=*p3;
	*p3=min;
}

