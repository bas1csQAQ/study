#include "stdio.h"
#include "string.h"
#include "math.h"

// һ������������100����ȫƽ�������ټ���168Ҳ����ȫƽ���� ��������� 
int main()
{ 
	int i = 1;
	double a,b;
	while(1){
		a = sqrt(i+100);
		b = sqrt(i+100+168);
		if(a == (int)a && b == (int)b){
			printf("%d\n",i);
		}
		
		if(i>10000) break;
		i++;
	}
	
return 0;

}


