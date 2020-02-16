#include <stdio.h>
#include <string.h>
// 有一个排好序的数组 输入一个数将这个数字按照排序规则加入到数组中
// 先判断是不是大于最后一个 如果大于就不判断中间的 如果不大于再考虑中间的值的判断 

int	main()
{
	int a[11]={1,4,6,9,13,16,19,28,40,100};	
	int temp1,temp2,number,end,i,j;
	// 显示目前的数组 展示数组排序规则 
	printf("original array is:\n"); 
	for(i=0;i<10;i++) printf("%5d",a[i]);
	printf("\n");
	// 输入新的数 
	printf("insert a new number:");
	scanf("%d", &number );
	// 将最后一个数取出来 先行判断 
	end=a[9];
	// 如果新输入的数大于最后一个数 那么就把输入的数字放到数组最后 
	if(number>end) 
		a[10]=number ;
	else{
		// 否则的话 就开始判断中间的部分
		for(i=0;i<10;i++){
			// 如果输入的数字大于某一位的数字 
			if(a[i]>number){
				// 就将这个位置的数字保存出来 
				temp1=a[i]; 
				// 同时将这个数字保留在这个位置上 
				a[i]=number;
				// 通过循环将这个位置后面的所有数字 向后移动一位 
				for(j=i+1;j<11;j++){
					temp2=a[j]; 
					a[j]=temp1;
					temp1=temp2;
				}
				break;
			}
		}
	}
	// 输出加入新元素之后的数组 
	for(i=0;i<11;i++) printf("%6d",a[i]);
	return 0;
}

