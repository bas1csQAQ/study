#include <stdio.h>
/*
	ָ��ʹ�ó��� 
*/
//	1.��������������ֵ 
void swap(int *pa,int *pb);
//	�������ض��ֵ ����ĳЩֵͨ��ָ�뽫ֵ����  ��ʱ�����д����ָ�����ʵ���Ͼ�����Ҫ��������ؽ���ı���
void minAndMax(int arr[],int len,int *min,int* max);
// �������������״̬�� ���ͨ��ָ�뷵��
int divide(int m,int n,int *result);
int main(void){
//	1.��������������ֵ 
	int a=5,b=6;
	swap(&a,&b);
	printf("a=%d,b=%d\n",a,b);
//	�������ض��ֵ ����ĳЩֵͨ��ָ�뽫ֵ����  ��ʱ�����д����ָ�����ʵ���Ͼ�����Ҫ��������ؽ���ı���
	int arr[]={1,55,3,25,100,90};
	int max,min;
	minAndMax(arr,sizeof(arr)/sizeof(arr[0]),&min,&max);
	printf("max=%d,min=%d\n",max,min);
//	�������������״̬�� ���ͨ��ָ�뷵�� 
	int m=5,n=2;
	int result;
	
	if(divide(m,n,&result))
		printf("result=%d\n",result);
	
	return 0;
}

void swap(int *pa,int *pb){
	int t = *pa;
	*pa=*pb;
	*pb = t; 
}

void minAndMax(int arr[],int len,int *min,int* max){
	int i ;
	*min = *max = 0;
	for(i=0;i<len;i++){
		if(arr[i]>*max){
			*max=arr[i];
		}
		if(arr[i]<*min){
			*min=arr[i];
		}
	}
}

int divide(int m,int n,int *result){
//	��������Ϊ0 ����Ҫ�ж��Ƿ�Ҫִ�� ���Ƿ�������״̬ 
	int ret = 1;
	if(n==0) 
		ret = 0;
	else
		*result = m/n;
	return ret;
}

