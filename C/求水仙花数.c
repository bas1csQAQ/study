#include <stdio.h>
/*
	ˮ�ɻ��� 
*/
int main(){
	 int n;
	 scanf("%d",&n);
	 int i;
	 int first = 1;
	 i =1;
//	 ȷ���������λ��
	 while(i<n){
	 	first *= 10;
	 	i++;
	 }
	 i=first;
//	 �����Ӧ��λ����ˮ�ɻ��� 
	 while(i<first*10){
	 	int t = i;
		 int sum = 0; 
	 	do{
//	 		�������������� ���зָ� 
	 		int d = t%10;
	 		t/=10;
	 		// ��ֽ�����֮��ÿһλ��n�η� 
	 		int p = d;
//	 		����ѭ������  �η��� 
	 		int j = 1;
	 		while(j<n){
	 			p*=d;
	 			j++;
			}
			sum+=p;
//	 		printf("%d\n",d);
		}while(t>0);
		
		if(i==sum){
			printf("%d\n",i);
		}
		i++;
	 } 
//	 printf("first = %d",first);
	return 0;
}
