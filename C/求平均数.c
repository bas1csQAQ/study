#include <stdio.h> 

int main(){
	int num ;
	int count = 0;
	int sum = 1;
	printf("������һЩ���֣�������� -1 ��Ϊ����");
	do{
	
	scanf("%d",&num);
		sum += num;
		count++;
	}while(num!=-1);
	printf("���� %d ���� ��Щ����ƽ����Ϊ %f",count-1,1.0*sum/(count-1));
//	printf("%f",19/3.0); 3 5 11 -1 
	
	
	return 0; 
}
