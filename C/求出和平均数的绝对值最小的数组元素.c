#include <stdio.h>
#include <string.h>
#include <math.h>
// 输入一个数组 求出和平均数的绝对值最小的数组元素 

int	main()
{
	float a[20],pjz=0,s,t,n=5;
	int i,k;
	// 输入数组 
	for(i=0;i<n;i++){
		scanf("%f", &a[i]);
		pjz+=a[i];
	}
	// 求平均值 
	pjz=pjz/n;
	// 将数组第一个元素作为满足题目条件的元素 
	s=fabs(a[0]-pjz);
	t=a[0]; 
	// 如果有比a[0]更满足条件的 就将t改为更满足条件的 
	for(i=1;i<n;i++)
		if(fabs(a[i]-pjz)<s){
			s=fabs(a[i]-pjz);
			t=a[i];
		}
	printf("%f", t);
	return 0;
}

