#include <stdio.h>
#include <string.h>
// ��д���� ����һ�����飬���д��10��������Ҫ���ҳ��������������±꣬�������������еĵ�һ��Ԫ�ضԻ�λ�á�
// ���� ��ͨ����  ֻ�ǻ��� ָ���� 


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
