#include <stdio.h>
#include <string.h>
// ��д���� ����������������밴�Ӵ�С˳��������������ֲ�ͬ�ķ�����̣���

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

