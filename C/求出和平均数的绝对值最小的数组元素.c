#include <stdio.h>
#include <string.h>
#include <math.h>
// ����һ������ �����ƽ�����ľ���ֵ��С������Ԫ�� 

int	main()
{
	float a[20],pjz=0,s,t,n=5;
	int i,k;
	// �������� 
	for(i=0;i<n;i++){
		scanf("%f", &a[i]);
		pjz+=a[i];
	}
	// ��ƽ��ֵ 
	pjz=pjz/n;
	// �������һ��Ԫ����Ϊ������Ŀ������Ԫ�� 
	s=fabs(a[0]-pjz);
	t=a[0]; 
	// ����б�a[0]������������ �ͽ�t��Ϊ������������ 
	for(i=1;i<n;i++)
		if(fabs(a[i]-pjz)<s){
			s=fabs(a[i]-pjz);
			t=a[i];
		}
	printf("%f", t);
	return 0;
}

