#include <stdio.h>
#include <string.h>
#include <math.h> 
// ����3��4���飬��ָ�뷽��ʵ�ֽ�ÿ���е���С�����0��Ԫ�ضԵ���
int main(){
	
	int a[3][4],i,j,*p=a[0];
	for(i=0;i<3;i++)
	for(j=0;j<4;j++) scanf("%d",p++);
	
	for(p=&a[0][0];p<a[0]+12;p+=4) // ÿ�ΰ�ÿһ�зŽ�ȥ��������
	swap(p);
	p=a[0]; // ��ָ��ָ���һ��Ԫ�� ����ʹ��ָ���������
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

