#include <stdio.h>

int main(){
//	����ʹ 1�� 2�� 5�ǵĴչ� 10�� ���µ�Ǯ��

	int x ;// ��Ǯ��
	int one,two,five;// ÿһ��Ǯ������ 
	
//	scanf("%d",x);
	x=3;
	int exit = 0;
	for(one = 0;one<x*10;one++){
		for(two = 0;two <x*10/2;two++){// ��Ǯ��(��)*10 �õ� �ܹ���Ǯ��(��) / ÿ��Ǯ�� ��ֵ = û��Ǯ������ 
			for(five = 0;five<x*10/5;five++){
				if(one*1+two*2+five*5 == x*10){
					printf("%d��1�ǵĺ�%d��2�ǵĺ�%d��5�ǵĿ������ %d ��Ǯ\n",one,two,five,x);
//					goto out; 
					exit =1;
					break;
				}
				if(exit)break;
			}
			if(exit)break;
		}
	}
	
//	һ�㲻����ʹ�� goto ��Ϊ̫������ �������goto ��Ѵ���ṹŪ�ú���  ��������ѭ��һ��ʹ�� ���� break��
//out :
	return 0; 
	 
} 
