#include <stdio.h>
/*
	指针使用场景 
*/
//	1.交换两个变量的值 
void swap(int *pa,int *pb);
//	函数返回多个值 所以某些值通过指针将值返回  此时函数中传入的指针参数实际上就是需要被保存带回结果的变量
void minAndMax(int arr[],int len,int *min,int* max);
// 函数返回运算的状态， 结果通过指针返回
int divide(int m,int n,int *result);
int main(void){
//	1.交换两个变量的值 
	int a=5,b=6;
	swap(&a,&b);
	printf("a=%d,b=%d\n",a,b);
//	函数返回多个值 所以某些值通过指针将值返回  此时函数中传入的指针参数实际上就是需要被保存带回结果的变量
	int arr[]={1,55,3,25,100,90};
	int max,min;
	minAndMax(arr,sizeof(arr)/sizeof(arr[0]),&min,&max);
	printf("max=%d,min=%d\n",max,min);
//	函数返回运算的状态， 结果通过指针返回 
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
//	除数不能为0 所以要判断是否要执行 就是返回运算状态 
	int ret = 1;
	if(n==0) 
		ret = 0;
	else
		*result = m/n;
	return ret;
}

