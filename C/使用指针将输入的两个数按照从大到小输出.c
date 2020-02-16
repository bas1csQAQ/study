#include <stdio.h>
#include <string.h>
// 编写程序 设有一个数组，其中存放10个整数，要求找出最大的数和它的下标，并把它和数组中的第一个元素对换位置。
// 就是 普通交换  只是换成 指针了 


int	main()
{
	int arr[10],i,maxIndex,max,first,firstIndex;
	for(i=0;i<10;i++) 
		scanf("%d", &arr[i]);
	first = max = arr[0];
	firstIndex = maxIndex = 0;
	
	for(i=1;i<10;i++){
		if(arr[i]>arr[maxIndex]){
			maxIndex = i;
			max = arr[i];
		}
	}
	for(i=0;i<10;i++){
		printf("%-5d",arr[i]);
	}
	printf("\n");
	arr[maxIndex] = first;
	arr[firstIndex] = max;
	
	for(i=0;i<10;i++){
		printf("%-5d",arr[i]);
	}
	return 0;
}
