#include <stdio.h>
/*
	����һ������ ����������е� ���������������� 
*/
int main(){
	int m,n;
	scanf("%d %d",&m,&n);
	
	int i = m,j;
	int isPrime = 0;// �Ƿ�Ϊ���� 
	int count = 0;// �������� 
	int sum = 0;// ������ 
	while(i<n){
		printf("i = %d",i);
//		�жϵ�ǰѭ�����Ƿ�Ϊ���� 
		for(j=2;j<i;j++){
			if(i%j == 0){
				isPrime = 1;
				break;
			}
		}
//		�� isPrime == 1 �� ��ʱ��i ������ ������+1 ������ʱ��i�����ۼӲ��� �ŵ�sum�� 
		if(isPrime){
			count ++;
			sum += i;
		}
//		���´�ѭ����ʼǰ �����������³�ʼ�� 
		isPrime = 0;
		i++;
	}
	printf("�� %d - %d ��Χ�������� %d�� �ܺ�Ϊ%d",m,n,count,sum);
	return 0;
}
